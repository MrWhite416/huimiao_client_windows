# development time: 2024-08-14  1:51

import asyncio
import threading
import time
import queue
import websockets
import json
import datetime


# 定义发送消息的数据
msg = {
    "sender": "cwb",
    "type": "message",
    "content": "你好 灰喵",
    "time": str(datetime.time),
}


class ProcessMsg:
    """
    加工处理消息
    """
    pass


class RunClient(object):

    def __init__(self, win, ip, port, key):
        super().__init__()
        self.user_input = None
        self.q = queue.Queue()
        self.condition_c = threading.Condition()
        self.condition_b = asyncio.Condition()
        self.ready_c = False
        self.ready_send = False
        self.win = win
        self.ip = ip
        self.port = port
        self.key = key
        self.loop = None
        self.connect_result = None
        self.websocket = None
        self.run()

    def gain_user_input(self):
        """获取前端用户发送的消息"""
        try:
            content = self.q.get(timeout=1)
            return content
        except queue.Empty:
            print('The queue is empty!')
            return None

    async def receive_messages(self, websocket):
        """接收并处理服务器消息"""
        while True:
            try:
                if websocket == 'fail':
                    print('连接失败')
                    return
                print("连接还在")
                response = await websocket.recv()
                print('接收到消息')
                response = json.loads(response)

                # 发送者的用户名
                name = response['sender']
                # 消息内容
                msg = response['content']

                print(f"\n{name}:{msg}")
                yield {'name': name, 'msg': msg}

            except websockets.ConnectionClosed:
                print("Connection with server closed")
                break

    async def send_messages(self):
        """处理用户输入并发送消息到服务器"""
        print('发送函数开始执行',datetime.datetime.now())
        while True:
            async with self.condition_b:
                await self.condition_b.wait()

            content = self.gain_user_input()
            if not content:
                continue
            print(content)
            message = {
                "sender": "lsy",
                "type": "message",
                "content": content,
                "time": "2024-8-5-17-17",  # 可以根据需要动态生成时间
            }
            await self.websocket.send(json.dumps(message))

    async def connect(self):
        p_ad = f"ws://{self.ip}:{self.port}"
        uri = p_ad
        headers = {
            "X-Auth-Key": self.key  # 连接密钥
        }
        try:
            websocket = await websockets.connect(uri, extra_headers=headers)
            print('连接成功')
            self.connect_result = 'success'
            self.event.set()
            return websocket
        except:
            print('连接失败')
            self.connect_result='fail'
            # 发出事件信号
            self.event.set()
            return 'fail'

    async def recv_t(self,):
        print('接收函数开始执行',datetime.datetime.now())
        recv_ui = None  # 接收消息前端展示函数
        refresh_canvas = None  # 更新画布的函数
        canvas = None  # 画布
        # 启动接收消息的任务
        recv = self.receive_messages(self.websocket)
        print('已经创建接收函数的生成器')
        print('马上遍历生成器', )
        async for recv_result in recv:
            print('从生成器中取出：',recv_result)
            if recv_result['name'] == 'server':
                # 当客户端第一次接收消息时，需要等待UI执行到某步骤才能继续执行
                with self.condition_c:
                    while not self.ready_c:
                        self.condition_c.wait()  # 等待被通知执行
                self.ready_c = False  # 将准备值修改回去
                recv_ui = self.q.get()
                refresh_canvas = self.q.get()
                canvas = self.q.get()

            recv_ui(recv_result)
            refresh_canvas(None,canvas)  # 刷新
            print('调用了receive_msg')

    async def run_tasks(self,):
        self.websocket = await self.connect()  # 连接
        print('已经创建连接')

        # 创建发送消息的任务
        recv_task = asyncio.create_task(self.recv_t())
        send_task = asyncio.create_task(self.send_messages())


        # 等待任务完成
        # results = await send_task
        result = await asyncio.gather(recv_task,send_task)
        print(result[0], result[1])


    def get_loop(self,):
        asyncio.set_event_loop(self.loop)
        self.loop.run_forever()


    def run(self):
        coroutine = self.run_tasks()

        self.loop = asyncio.new_event_loop()

        self.event = threading.Event()
        t = threading.Thread(target=self.get_loop, )
        t.start()

        asyncio.run_coroutine_threadsafe(coroutine,self.loop)

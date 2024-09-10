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
        self.q = queue.Queue()
        self.condition_c = threading.Condition()
        self.ready_c = False
        self.win = win
        self.ip = ip
        self.port = port
        self.key = key
        self.loop = None
        self.connect_result = None
        self.run()

    async def receive_messages(self, websocket):
        """接收并处理服务器消息"""
        while True:
            try:
                if websocket == 'fail':
                    print('连接失败')
                    return
                print("连接还在")
                response = await websocket.recv()
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

    async def send_messages(self, websocket):
        print('发送消息')

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

            self.connect_result='fail'
            # 发出事件信号
            self.event.set()
            return 'fail'

    async def run_tasks(self):
        websocket = await self.connect()
        # 启动接收消息的任务
        recv_task = self.receive_messages(websocket)
        async for recv_result in recv_task:
            print(recv_result)

            with self.condition_c:
                while not self.ready_c:
                    self.condition_c.wait()  # 等待被通知执行
            self.ready_c = False  # 将准备值修改回去

            recv_ui = self.q.get()
            recv_ui(recv_result)
            print('调用了receive_msg')

        # 启动发送消息的任务
        send_task = asyncio.create_task(self.send_messages(websocket))
        # recv_task = asyncio.create_task(self.receive_messages(websocket))

        # 等待任务完成
        results = await send_task
        # await asyncio.gather(send_task,recv_task)



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

async def receive_messages(websocket):
    """接收并处理服务器消息"""
    while True:
        try:
            response = await websocket.recv()
            response = json.loads(response)

            print(f"\n{response['sender']}:{response['content']}")

        except websockets.ConnectionClosed:
            print("Connection with server closed")
            break


async def send_messages(websocket):
    """处理用户输入并发送消息到服务器"""
    while True:
        user_input = await asyncio.to_thread(input, "You: ")
        message = {
            "sender": "lsy",
            "type": "message",
            "content": user_input,
            "time": "2024-8-5-17-17",  # 可以根据需要动态生成时间
        }
        await websocket.send(json.dumps(message))


async def client(ip, port, key):
    p_ad = f"ws://{ip}:{port}"
    uri = p_ad
    headers = {
        "X-Auth-Key": key  # 连接密钥
    }

    async with websockets.connect(uri, extra_headers=headers) as websocket:
        # 启动接收消息的任务
        receive_task = asyncio.create_task(receive_messages(websocket))
        # 启动发送消息的任务
        send_task = asyncio.create_task(send_messages(websocket))

        # 等待任务完成
        await asyncio.gather(receive_task, send_task)

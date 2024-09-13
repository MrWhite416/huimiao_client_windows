"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import time
import tkinter

# 示例下载 https://www.pytk.net/blog/1702564569.html
from miaow_ui import Win
import threading
import asyncio
from client_app.client import *
import threading
import queue


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win

    def __init__(self):
        self.server_ip = "106.53.104.224"
        self.server_port = "2048"
        self.key = ''
        self.remark = ''
        self.canvas = None
        self.client_me = None

    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

    def show_add_server(self, event):
        for widget in self.ui.tk_frame_lzvno8t5.winfo_children():
            widget.place_forget()

        tk_input_serverip_ = self.ui.tk_input_serverip(self.ui.tk_frame_lzvno8t5)
        tk_input_serverport_ = self.ui.tk_input_serverport(self.ui.tk_frame_lzvno8t5)
        tk_input_key_ = self.ui.tk_input_key(self.ui.tk_frame_lzvno8t5)
        tk_input_remark_ = self.ui.tk_input_remark(self.ui.tk_frame_lzvno8t5)
        connect_btn = self.ui.tk_button_join(self.ui.tk_frame_lzvno8t5)

        def click_connect(e, p):
            is_empty = self.connect_verify_empty(tk_input_serverip_, tk_input_serverport_, tk_input_key_,tk_input_remark_)
            if is_empty:
                wait_w = self.ui.wait_content(p, '连接中.. .. ..')

                # 连接实例
                self.client_me = RunClient(self.ui,self.server_ip,self.server_port,self.key)

                def return_result():
                    # 等待事件信号
                    self.client_me.event.wait()
                    # 将event设置回去
                    self.client_me.event.clear()

                    # 连接结果
                    if self.client_me.connect_result == 'fail':
                        # 连接失败
                        self.ui.connect_fail()

                    elif self.client_me.connect_result == 'success':
                        # 提示 连接成功
                        self.ui.connect_success()

                        def close_w(e):

                            if e.widget == wait_w:
                                print('触发了关闭事件')
                                """只有当触发销毁事件的组件是wait_w时"""
                                """
                                由于tkinter中的事件传播机制，子组件的destory事件会向上传播到父组件（别的事件不会）
                                ，从而导致父组件上绑定的<Destroy>事件被触发，因此，
                                此处要做一个if判断，只有满足要求的组件被销毁才触发事件函数
                                """


                                # 开一个新线程等待画布组件出现，接收消息操作才能继续执行
                                def wait_canvas():
                                    flag = True
                                    while flag:
                                        if self.canvas:
                                            flag = False
                                            self.client_me.q.put(self.receive_msg)  # 接收消息
                                            self.client_me.q.put(self.ui.on_canvas_configure)  # 更新画布
                                            self.client_me.q.put(self.canvas)
                                            with self.client_me.condition_c:
                                                self.client_me.ready_c = True
                                                self.client_me.condition_c.notify()  # 通知后端线程可以继续执行
                                                print('已经通知接收后端继续执行')

                                t_1 = threading.Thread(target=wait_canvas)
                                t_1.start()

                                # 当提示窗口关闭时才开始接收消息
                                btn = self.add_server_to_msglist(remark=self.remark)
                                btn.config(command=self.show_chat,)
                                self.show_chat(e)

                        wait_w.bind('<Destroy>', close_w)

                # 新开一个线程，避免gui假死
                t = threading.Thread(target=return_result)
                t.start()

        connect_btn.bind('<Button-1>', lambda e: click_connect(e, self.ui.tk_frame_lzvno8t5))

    def connect_verify_empty(self, ip_border, port_border, key_border, remark_border):
        """连接时验证所有值是否为空"""
        if not ip_border.get():
            self.ui.error('ip不能为空！')
            return None
        if not port_border.get():
            self.ui.error('端口不能为空！')
            return None
        if not key_border.get():
            self.ui.error('密钥不能为空！')
            return None
        if not remark_border.get():
            self.ui.error('备注不能为空！')
            return None

        self.server_ip = ip_border.get().strip()
        self.server_port = port_border.get().strip()
        self.key = key_border.get().strip()
        self.remark = remark_border.get().strip()

        return True

    def show_chat(self, e=None):
        # 清空之前的页面
        for widget in self.ui.tk_frame_lzvno8t5.winfo_children():

            """有bug暂时为解决--当提示窗口被关闭时执行此函数，但是此函数会将提示窗口也算入"""
            # 暂时使用if判断  虽然有点不优雅
            if e:
                if isinstance(e.widget,tkinter.Toplevel):
                    continue
            widget.place_forget()

        #  头
        head = self.ui.tk_frame_chat_head(self.ui.tk_frame_lzvno8t5)
        self.name = self.ui.tk_label_chat_name(head)

        # 身体
        body = self.ui.tk_frame_chat_body(self.ui.tk_frame_lzvno8t5)
        self.canvas = self.ui.tk_canvas_chat_body(body)

        self.ui.bind_event(self.canvas)  # 绑定滚动滑轮事件

        # 脚
        foot = self.ui.tk_frame_chat_foot(self.ui.tk_frame_lzvno8t5)
        text_box = self.ui.tk_text_chat_content(foot)
        send_button = self.ui.tk_button_chat_send(foot)

        # 左键按下，发送一条消息
        send_button.bind('<Button-1>', lambda e: self.send_msg(e, text_box))
        # 左键松开，刷新滚动区域以匹配当前画布所有组件
        send_button.bind('<ButtonRelease-1>', lambda e: self.ui.on_canvas_configure(e, self.canvas))

    def msg_frame_y(self):

        # 聊天框中一条消息容器高度为60
        # 根据画布中子项目数计算
        y = (60 * len(self.canvas.children.values())) + 10 * (len(self.canvas.children.values()) + 1)

        return y

    def add_msgui(self, e, content):
        # 消息的y坐标
        y = self.msg_frame_y()

        self.ui.send_msg(self.canvas, content, y=y)

    def send_msg(self, e, text_box):

        # 获取多行文本框的内容
        content = text_box.get("1.0", "end-1c")
        self.add_msgui(e, content)

        # 通过队列传入后端
        self.client_me.q.put(content)

        loop = asyncio.new_event_loop()  # 创建一个事件循环

        notify_ex = self.notify_thread()  # 通知协程对象可以继续执行的协程任务
        t = threading.Thread(target=self.new_loop,args=(loop,))  # 将事件循环跑起来
        t.start()

        asyncio.run_coroutine_threadsafe(notify_ex,loop=loop)  # 将协程任务添加到事件循环


        print('将内容存入了q')

        # 清空多行文本框
        text_box.delete("1.0", "end")

    def add_server_to_msglist(self,remark):
        y = len(self.ui.tk_canvas_left.children.values()) * 50 + ((len(self.ui.tk_canvas_left.children.values())) + 1) * 10

        btn = self.ui.add_server_list(self.ui.tk_canvas_left,remark,y)

        return btn

    def receive_msg(self,content):
        """
        接收消息
        :return:
        """

        '''接收消息后端逻辑'''
        print(content)
        try:
            name = content['name']
            msg = content['msg']
            y = self.msg_frame_y()
            print(name, msg, y)
        except Exception as e:
            print(e)



        '''前端展示'''
        self.ui.recv_msg(self.canvas, msg, y)
        print('发送了消息到前端')

    def new_loop(self,loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
        return loop

    async def notify_thread(self):
        async with self.client_me.condition_b:
            self.client_me.condition_b.notify()

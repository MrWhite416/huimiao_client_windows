"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
import random
import threading
import time
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter.ttk import *
from PIL import Image, ImageTk


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.prompt_win = None  # 提示信息的弹窗
        self.__win()
        self.tk_frame_lzvnfv9g = self.__tk_frame_lzvnfv9g(self)
        self.tk_label_lzvnghd3 = self.__tk_label_lzvnghd3(self.tk_frame_lzvnfv9g)
        self.tk_select_box_lzvni53a = self.__tk_select_box_lzvni53a(self.tk_frame_lzvnfv9g)
        self.tk_button_lzwyjg1f = self.__tk_button_lzwyjg1f(self.tk_frame_lzvnfv9g)
        self.tk_frame_lzvnltk3 = self.__tk_frame_lzvnltk3(self)
        self.tk_canvas_left = self.__tk_canvas_left(self.tk_frame_lzvnltk3)
        # self.tk_button_lzvny8vc = self.__tk_button_lzvny8vc(self.tk_frame_lzvnltk3)
        # self.tk_button_lzvnyaf2 = self.__tk_button_lzvnyaf2(self.tk_frame_lzvnltk3)
        self.tk_frame_lzvno8t5 = self.__tk_frame_lzvno8t5(self)


    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 800
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_frame_lzvnfv9g(self, parent):

        # 设置frame样式
        style = Style()
        style.configure("head_bg.TFrame", background="lightgray")

        frame = Frame(parent, style="head_bg.TFrame")
        frame.place(x=0, y=0, width=300, height=64)
        return frame

    def __tk_label_lzvnghd3(self, parent):
        label = Label(parent, text="头像", anchor="center", )
        label.place(x=0, y=0, width=64, height=64)
        return label

    def __tk_select_box_lzvni53a(self, parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("设置", "Python", "Tkinter Helper")
        cb.place(x=236, y=0, width=64, height=64)
        return cb

    def __tk_button_lzwyjg1f(self, parent):
        btn = Button(parent, text="添加服务器", takefocus=False, )
        btn.place(x=116, y=0, width=64, height=64)
        return btn

    def __tk_frame_lzvnltk3(self, parent):
        style = Style()
        style.configure("left.TFrame", background="#2d8a5e")

        frame = Frame(parent, style="left.TFrame")
        frame.place(x=0, y=64, width=300, height=436)
        return frame

    def __tk_canvas_left(self, parent):
        canvas = Canvas(parent, width=300, height=436, background="#ffffff", scrollregion=(0, 0, 300, 436))
        scrollbar = Scrollbar(parent, command=canvas.yview)

        canvas.config(yscrollcommand=scrollbar.set)

        canvas.place(x=0, y=0)
        scrollbar.place(relx=1.0, rely=0.0, relheight=1.0, anchor='ne')

        return canvas


    def __tk_button_lzvny8vc(self, parent):
        btn = Button(parent, text="好友1", takefocus=False, )
        btn.place(x=0, y=27, width=283, height=50)
        return btn

    def __tk_button_lzvnyaf2(self, parent):
        btn = Button(parent, text="好友2", takefocus=False, )
        btn.place(x=0, y=110, width=283, height=50)
        return btn

    def __tk_frame_lzvno8t5(self, parent):
        frame = Frame(parent, )
        frame.place(x=301, y=0, width=500, height=500)
        return frame

    def tk_input_serverip(self, parent):

        ipt = Entry(parent, )
        ipt.place(x=81, y=63, width=150, height=30)

        label = Label(parent, text="ip", anchor="center", )
        label.place(x=240, y=63, width=40, height=30)
        return ipt

    def tk_input_serverport(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=81, y=100, width=150, height=30)

        label = Label(parent, text="端口号", anchor="center", )
        label.place(x=240, y=100, width=40, height=30)
        return ipt

    def tk_input_key(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=81, y=140, width=150, height=30)

        label = Label(parent, text="秘钥", anchor="center", )
        label.place(x=240, y=140, width=40, height=30)
        return ipt

    def tk_input_remark(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=81, y=180, width=150, height=30)

        label = Label(parent, text="备注", anchor="center", )
        label.place(x=240, y=180, width=40, height=30)
        return ipt

    def tk_button_join(self, parent):
        btn = Button(parent, text="连接", takefocus=False, )
        btn.place(x=130, y=240, width=60, height=30)
        return btn

    def tk_frame_chat_head(self, parent):
        style = Style()
        style.configure("head.TFrame", background="#000000")

        frame = Frame(parent, style="head.TFrame")
        frame.place(x=0, y=0, width=500, height=64)
        return frame

    def tk_frame_chat_body(self, parent):
        frame = Frame(parent, width=500, height=335)
        frame.place(x=0, y=65)

        return frame

    def tk_frame_chat_foot(self, parent):
        style = Style()
        style.configure("foot.TFrame", background="#21CF5D")

        frame = Frame(parent, style="foot.TFrame")
        frame.place(x=0, y=401, width=500, height=100)
        return frame

    def tk_label_chat_name(self, parent):
        label = Label(parent, text="密友昵称", anchor="w", )
        label.place(x=0, y=0, width=200, height=64)
        return label

    def tk_text_chat_content(self, parent):
        text = Text(parent, )
        text.place(x=0, y=0, width=400, height=100)
        return text

    def tk_button_chat_send(self, parent):
        style = Style()
        style.configure('1.TButton', background='#000000', foreground='#000000')

        btn = Button(parent, text='发送', takefocus=False, style='1.TButton')
        btn.place(x=401, y=0, width=99, height=100)
        return btn

    def tk_scrollbar_chat(self, parent,c):
        scrollbar = Scrollbar(parent,command=c.yview)
        c.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 500, 335))
        scrollbar.place(relx=1.0, rely=0.0, relheight=1.0, anchor='ne')

        return scrollbar

    def tk_canvas_chat_body(self, parent):
        canvas = Canvas(parent, width=500, height=335, background="#ffffff",scrollregion=(0, 0, 500, 335))
        scrollbar = Scrollbar(parent, command=canvas.yview)

        # vsb = self.tk_scrollbar_chat(parent, canvas)

        canvas.config(yscrollcommand=scrollbar.set)

        canvas.place(x=0, y=0)
        scrollbar.place(relx=1.0, rely=0.0, relheight=1.0, anchor='ne')

        return canvas

    def on_mousewheel(self, event, canvas):
        # 根据鼠标滚轮的方向更新canvas的滚动位置
        if event.delta > 0:
            # 向上滚动
            canvas.yview_scroll(-1, "units")
        else:
            # 向下滚动
            canvas.yview_scroll(1, "units")

    def on_canvas_configure(self, event, canvas):
        '''重置滚动区域以包含当前画布大小'''
        canvas.config(scrollregion=canvas.bbox("all"))

    def bind_event(self, canvas):
        # 为Canvas绑定鼠标滚轮事件
        canvas.bind("<MouseWheel>", lambda e: self.on_mousewheel(e, canvas))
        canvas.bind('<Configure>', lambda e: self.on_canvas_configure(e, canvas))

    def recv_msg(self,parent,msg,y):
        Style().configure('f.TFrame', background='#ffffff')
        frame = Frame(parent, width=360, height=60, style="f.TFrame")
        i = parent.create_window((190, y), window=frame, anchor='n')

        img = Image.open('D:\\灰喵\\img\\虞书欣2.jpg')
        new_img = img.resize((50, 50))
        photo = ImageTk.PhotoImage(new_img)

        # 宽高50
        img_label = Label(frame, image=photo)
        img_label.place(x=0, y=5, width=50, height=50)
        img_label.image = photo

        # 用于装消息的子容器
        # 左边距 10
        s = Style().configure('msg.TFrame', background='#B418C9')
        msg_frame = Frame(frame, style='msg.TFrame')
        msg_frame.place(x=55, y=5, width=305, height=50)

        # 消息
        # 靠左排列
        msg_label = Label(msg_frame, text=msg, background="#7092BE", font=font.Font(size=8), foreground='red')
        msg_label.place(x=4, y=0, width=296, height=50)

    def send_msg(self,parent,msg,y):
        Style().configure('f.TFrame', background='#ffffff')
        frame = Frame(parent, width=360, height=60, style="f.TFrame")
        i = parent.create_window((290, y), window=frame, anchor='n')

        img = Image.open('D:\\灰喵\\img\\虞书欣2.jpg')
        new_img = img.resize((50, 50))
        photo = ImageTk.PhotoImage(new_img)

        # 宽高50
        img_label = Label(frame, image=photo)
        img_label.place(x=310, y=5, width=50, height=50)
        img_label.image = photo

        # 用于装消息的子容器
        # 左边距 10
        s = Style().configure('msg.TFrame', background='#B418C9')
        msg_frame = Frame(frame, style='msg.TFrame')
        msg_frame.place(x=0, y=5, width=305, height=50)

        # 消息
        # 靠左排列
        msg_label = Label(msg_frame, text=msg, background="#7092BE", font=font.Font(size=8), foreground='red')
        msg_label.place(x=4, y=0, width=296, height=50)

    def add_server_list(self,parent,remark,y):
        btn = Button(parent, text=remark, takefocus=False, )
        btn.place(x=0, y=y, width=283, height=50)
        return btn

    def error(self,content):
        error_box = messagebox.showerror('操作有误',content)

    def wait_content(self,parent,content):
        self.prompt_win = Toplevel(parent,)
        self.prompt_win.title('请等待')
        self.prompt_win.protocol("WM_DELETE_WINDOW", lambda: None)  # 禁用关闭窗口的按钮
        x = self.winfo_x()+self.winfo_width()/2-100
        y = self.winfo_y()+self.winfo_height()/2-50
        self.prompt_win.geometry(f'200x100+{int(x)}+{int(y)}')
        self.prompt_win.resizable(False,False)

        s = Style().configure('l.TLabel',background='#7999f0'
                              , anchor='center',font=('', 20))
        label = Label(self.prompt_win, text=content,
                      style='l.TLabel')
        label.place(width=200,height=100)

        self.attributes("-disabled", True)  # 禁用主窗口交互
        return self.prompt_win

    def connect_fail(self):
        self.prompt_win.title = '连接结果'
        for label in self.prompt_win.winfo_children():
            # 连接失败 时的样式
            Style().configure('l.TLabel',background='#FCC8E6',anchor='center',font=('', 20))
            label.config(text='连接失败！！！',style='l.TLabel')

            self.attributes("-disabled", False)  # 启用主窗口交互
            self.prompt_win.protocol("WM_DELETE_WINDOW", self.prompt_win.destroy)  # 启用关闭窗口的按钮

    def connect_success(self):
        self.prompt_win.title = '连接结果'
        for label in self.prompt_win.winfo_children():
            # 连接成功 时的样式
            Style().configure('l.TLabel',background='#FF0000',anchor='center',font=('', 20))
            label.config(text='连接成功！！！',style='l.TLabel')

            self.attributes("-disabled", False)  # 启用主窗口交互
            self.prompt_win.protocol("WM_DELETE_WINDOW", self.prompt_win.destroy)  # 启用关闭窗口的按钮


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)


    def __event_bind(self):
        self.tk_button_lzwyjg1f.bind('<Button-1>', self.ctl.show_add_server)
        # self.tk_button_lzvny8vc.bind('<Button-1>', self.ctl.show_chat)


    def __style_config(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()

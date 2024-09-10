# development time: 2024-08-15  3:05
# developer: 元英

import random
from tkinter import *
from tkinter.ttk import *


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_lzu9sif4 = self.__tk_label_lzu9sif4(self)
        self.tk_label_lzu9sk3m = self.__tk_label_lzu9sk3m(self)
        self.tk_button_lzu9smck = self.__tk_button_lzu9smck(self)
        self.tk_button_lzu9snex = self.__tk_button_lzu9snex(self)
        self.tk_input_lzu9sop8 = self.__tk_input_lzu9sop8(self)
        self.tk_input_lzu9spzp = self.__tk_input_lzu9spzp(self)

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 638
        height = 416
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

    def __tk_label_lzu9sif4(self, parent):
        label = Label(parent, text="账号", anchor="center", )
        label.place(x=142, y=60, width=100, height=60)
        return label

    def __tk_label_lzu9sk3m(self, parent):
        label = Label(parent, text="密码", anchor="center", )
        label.place(x=137, y=150, width=100, height=64)
        return label

    def __tk_button_lzu9smck(self, parent):
        btn = Button(parent, text="登录", takefocus=False, )
        btn.place(x=150, y=280, width=95, height=50)
        return btn

    def __tk_button_lzu9snex(self, parent):
        btn = Button(parent, text="注册", takefocus=False, )
        btn.place(x=370, y=280, width=100, height=50)
        return btn

    def __tk_input_lzu9sop8(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=300, y=63, width=200, height=60)
        return ipt

    def __tk_input_lzu9spzp(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=300, y=149, width=200, height=60)
        return ipt


class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.__style_config()
        self.ctl.init(self)

    def __event_bind(self):
        pass

    def __style_config(self):
        pass


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
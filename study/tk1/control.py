"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
# 示例下载 https://www.pytk.net/blog/1702564569.html
from ui import Win
from tkinter import messagebox


class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui: Win
    def __init__(self):
        pass
    def init(self, ui):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui = ui
        # TODO 组件初始化 赋值操作

        # 是密码框加密而非显示明文
        self.ui.tk_input_password.configure(show='*')

    def login(self,evt):
        username = self.ui.tk_input_username.get()
        pwd= self.ui.tk_input_password.get()

        if username=='' or pwd=='':
            messagebox.showerror('notice','账号或密码不能为空')

        print(username,pwd)
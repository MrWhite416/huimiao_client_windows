# development time: 2024-08-15  3:05
# developer: 元英
# 导入布局文件
from miaow_ui import Win as MainWin

# 导入窗口控制器
from miaow_control import Controller as MainUIController
# 将窗口控制器 传递给UI
app = MainWin(MainUIController())
if __name__ == "__main__":
    # 启动
    app.mainloop()
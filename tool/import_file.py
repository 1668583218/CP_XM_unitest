from time import sleep
import pywinauto
from pywinauto.keyboard import send_keys


def import_file(file_name_path):
    # 使用pywinauto来选择文件
    app = pywinauto.Desktop()
    # 选择文件上传的窗口
    dlg = app["打开"]

    # # 选择文件地址输入框，点击激活
    # dlg["Toolbar3"].click()
    # sleep(3)
    # # 键盘输入上传文件的路径
    # send_keys("桌面")
    # sleep(1)
    # # 键盘输入回车，打开该路径
    # send_keys("{VK_RETURN}")
    # sleep(1)
    # 选中文件名输入框，输入文件名
    dlg["文件名(&N):Edit"].type_keys(file_name_path)
    sleep(1)
    # 点击打开
    dlg["打开(&O)"].click()
    try:
        dlg["打开(&O)"].click()
    except:
        pass


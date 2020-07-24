"""
    PyAutoGUI——做职场高手,让所有GUI自动化,击败无聊的办公室重复性操作
        GUI:图形用户界面(Graphical User Interface)
            例如 办公软件,音乐播放器...
        盘点工作中的机械化重复性操作：
            打开各种软件、各种办公软件、发邮件....
        作用：自动控制鼠标和键盘。
        文档：https://pyautogui.readthedocs.io/en/latest/install.html
        安装：
            1. 打开运行窗口 win + r
            2. 输入cmd，回车确认。
            2. 输入pip install pyautogui
"""
# 准备一个工具
import pyautogui

# pyautogui.moveTo(x轴，y轴)
# pyautogui.moveTo(x轴，y轴,持续时间)
pyautogui.moveTo(329, 411, 3)  # 移动到酷狗位置
pyautogui.doubleClick()  # 双击打开

pyautogui.sleep(5)  # 等待2秒(给酷狗打开的时间)
# 定位图片位置
# pyautogui.locateOnScreen(需要定位的图片名称)
playlocation = pyautogui.locateOnScreen("play.png")
# # 找到中心点
playpoint = pyautogui.center(playlocation)

pyautogui.moveTo(playpoint.x, playpoint.y, 3)  # 移动到播放按钮
pyautogui.click()  # 单击播放

# 查看说明文档的快捷键：ctrl + Q
# 显示鼠标位置
#      1. 在命令行中输入python
#      2. 粘贴代码
# import pyautogui
# pyautogui.displayMousePosition()

# 截图
# im = pyautogui.screenshot(region=(592, 814, 75, 75))
# im.save("play.png")

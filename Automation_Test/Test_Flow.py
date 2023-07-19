from Library.Web_Page.web_control import WebControl
from Driver.create_driver import WebDriver
import time
 
fileName = f'./Automation_Test/Pictures/{time.strftime("%Y%m%d-%H%M%S", time.localtime())}.png'
webControl = WebControl(WebDriver().Create_Driver())
webControl.set_window_size(600, 800)
webControl.enter_target_page("https://www.cathaybk.com.tw/cathaybk/")
webControl.screen_shot(filePath = fileName)
time.sleep(20)
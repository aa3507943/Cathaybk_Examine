from Library.Web_Page.web_control import WebControl
from Driver.create_driver import WebDriver

class Chrome:
    def __init__(self):
        self.web_control = WebControl(WebDriver().Create_Driver())
        self.web_control.set_window_size(600, 800)
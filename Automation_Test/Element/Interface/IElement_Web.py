from abc import ABC, abstractproperty
from Library.Web_Page.web_control import WebControl

class IElement_HomePage(ABC):
    def __init__(self, driver: WebControl):
        self.Driver = driver
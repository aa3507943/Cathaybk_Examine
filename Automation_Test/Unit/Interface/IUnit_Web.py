from abc import ABC, abstractmethod, abstractproperty
from Library.Web_Page.web_control import WebControl
from Element.Interface.IElement_Web import *

class IUnitHomePage(ABC):
    def __init__(self, driver: WebControl, element: IHomePage):
        self.driver = driver
        self.element = element
    @abstractmethod
    def Goto_Cathaybk_Page(self):
        "進到國泰世華銀行首頁"

    @abstractmethod
    def Screen_Shot_Home_Page(self, filePath: str):
        "針對畫面做截圖，並存入指定位址"
        
    @abstractmethod
    def Click_Side_Menu_Btn(self):
        "點擊側邊菜單展開圖示"
        
    """其他的題目中用不到，先不列入，但可在此擴充"""
    
class IUnitSideMenu(ABC):
    def __init__(self, driver: WebControl, element: ISideMenu):
        self.driver = driver
        self.element = element
    @abstractmethod
    def Close_Side_Menu(self):
        "關閉側邊菜單"
        
    @abstractmethod
    def Click_Personal_Finance(self):
        "點擊個人金融選項"
        
    @abstractmethod
    def Click_Product_Introdcue(self):
        "點擊產品介紹選項"
        
    @abstractmethod
    def Click_Digital_Service(self):
        "點擊數位服務選項"
        
    @abstractmethod
    def Click_About_Cathaybk(self):
        "點擊關於國泰選項"
        
    @abstractmethod
    def Click_Support_Service(self):
        "點擊支援服務選項"
        
    @abstractmethod
    def Click_Service_Base(self):
        "點擊支援據點選項"
        
    """多寫的僅以示例，其他暫且用不到，但可在此擴充"""
        
class IUnitProductIntroduce(ABC):
    def __init__(self, driver: WebControl, element: IProductIntroduce):
        self.driver = driver
        self.element = element
    @abstractmethod
    def Click_Credit_Card(self):
        "點擊信用卡選項"
    
    @abstractmethod
    def Get_Credit_Card_Option_Amounts(self):
        "獲取信用卡選項數量"
    
    @abstractmethod
    def Screen_Shot_Credit_Card_Option_List(self):
        "截圖信用卡選項列表"

    @abstractmethod
    def Click_Card_Introduce(self):
        "點擊卡片介紹選項"
        
    @abstractmethod
    def Click_Credit_Card_Offers(self):
        "點擊刷卡優惠選項"
        
    @abstractmethod
    def Click_Bank_Deposit(self):
        "點擊存款選項"
        
    """多寫的僅以示例，其他暫且用不到，但可在此擴充"""

class IUnitCardIntroduce(ABC):
    def __init__(self, driver: WebControl, element: ICardIntroduce):
        self.driver = driver
        self.element = element
    @abstractmethod
    def Scroll_To_Target_Area(self):
        "滾動至目標元素區域"
    @abstractmethod
    def Screen_Shot_Card_Block(self, filePath):
        "截圖卡片區域"
    @abstractmethod
    def Change_Display_Card(self):
        "更換展示的卡片"
    @abstractmethod
    def Get_Stop_Issue_Card_Amounts(self):
        "獲取停用卡片數量"
    
    """其他的題目中用不到，先不列入，但可在此擴充"""
    
class IUnit(ABC):
    @abstractproperty
    def unit_home_page(self)-> IUnitHomePage: pass
    @abstractproperty
    def unit_side_menu(self)-> IUnitSideMenu: pass
    @abstractproperty
    def unit_product_introduce(self)-> IUnitProductIntroduce: pass
    @abstractproperty
    def unit_card_introduce(self)-> IUnitCardIntroduce: pass

    def __init__(self, driver: WebControl): 
        self.driver = driver
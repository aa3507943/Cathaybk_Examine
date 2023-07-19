from Automation_Test.Element.Interface.IElement_Web import IHomePage, IProductIntroduce, ISideMenu, WebControl
from Automation_Test.Library.Web_Page.web_control import WebControl
from Automation_Test.Unit.Interface.IUnit_Web import *

class UnitHomePage(IUnitHomePage):
    def __init__(self, driver: WebControl, element: IHomePage):
        super().__init__(driver, element)
    def Screen_Shot(self, filePath: str):
        super().Screen_Shot(filePath)
        self.driver.screen_shot(filePath)
    def Click_Side_Menu_Btn(self):
        super().Click_Side_Menu_Btn()
        self.driver.element_click(self.element.menu_burger_icon)

class UnitSideMenu(IUnitSideMenu):
    def __init__(self, driver: WebControl, element: ISideMenu):
        super().__init__(driver, element)
    def Close_Side_Menu(self):
        super().Close_Side_Menu()
        self.driver.element_click(self.element.close_btn)
    def Click_Personal_Finance(self):
        super().Click_Personal_Finance()
        self.driver.element_click(self.element.personal_finance_btn)
    def Click_Product_Introdcue(self):
        super().Click_Product_Introdcue()
        self.driver.element_click(self.element.product_intro_btn)
    def Click_Digital_Service(self):
        super().Click_Digital_Service()
        self.driver.element_click(self.element.digital_service_btn)
    def Click_About_Cathaybk(self):
        super().Click_About_Cathaybk()
        self.driver.element_click(self.element.about_cathaybk_btn)
    def Click_Support_Service(self):
        super().Click_Support_Service()
        self.driver.element_click(self.element.support_service_btn)
    def Click_Service_Base(self):
        super().Click_Service_Base()
        self.driver.element_click(self.element.service_base_btn)

class UnitProductIntroduce(IUnitProductIntroduce):
    def __init__(self, driver: WebControl, element: IProductIntroduce):
        super().__init__(driver, element)
    def Click_Credit_Card(self):
        super().Click_Credit_Card()
        self.driver.element_click(self.element.credit_card_btn)
    def Click_Card_Introduce(self):
        super().Click_Card_Introduce()
        self.driver.element_click(self.element.card_intro_btn)
    def Click_Credit_Card_Offers(self):
        super().Click_Credit_Card_Offers()
        self.driver.element_click(self.element.credit_card_offers_btn)
    def Click_Bank_Deposit(self):
        super().Click_Bank_Deposit()
        self.driver.element_click(self.element.bank_deposit_btn)    

class UnitCardIntroduce(IUnitCardIntroduce):
    def __init__(self, driver: WebControl, element: ICardIntroduce):
        self.driver = driver
        self.element = element
    @abstractmethod
    def Screen_Shot_Card_Block(self, filePath):
        from selenium.webdriver.common.action_chains import ActionChains
        action_chains = ActionChains(self.driver.driver)
        action_chains.scroll_to_element(self.element.stop_issue_card_block)
        self.driver.screen_shot(filePath)
    @abstractmethod
    def Get_Stop_Issue_Card_Amounts(self):
        return len(self.element.turn_card_btn)
    

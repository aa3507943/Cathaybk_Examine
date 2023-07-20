from Element.Interface.IElement_Web import IHomePage, IProductIntroduce, ISideMenu, WebControl
from Library.Web_Page.web_control import WebControl
from Unit.Interface.IUnit_Web import *
from Unit.Interface.IUnit_Web import IUnitCardIntroduce, IUnitHomePage, IUnitProductIntroduce, IUnitSideMenu
from Element.Interface.IElement_Web import *
import time
import os

class UnitHomePage(IUnitHomePage):
    def __init__(self, driver: WebControl, element: IHomePage):
        super().__init__(driver, element)
    def Goto_Cathaybk_Page(self, url):
        super().Goto_Cathaybk_Page()
        self.driver.enter_target_page(url)
    def Screen_Shot_Home_Page(self, filePath: str):
        super().Screen_Shot_Home_Page(filePath)
        self.driver.screen_shot(filePath)
        if os.path.isfile(filePath) == False:
            raise "找不到檔案"
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
        time.sleep(3)
    def Get_Credit_Card_Option_Amounts(self):
        super().Get_Credit_Card_Option_Amounts()
        return len(self.element.credit_card_option_list)
    def Screen_Shot_Credit_Card_Option_List(self, filePath):
        self.driver.screen_shot(filePath)
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
    def Scroll_To_Target_Area(self):
        from selenium.webdriver.common.action_chains import ActionChains
        action_chains = ActionChains(self.driver.driver)
        action_chains.scroll_to_element(self.element.stop_issue_card_block).pause(1).release().perform()
    def Screen_Shot_Card_Block(self, filePath):
        self.driver.screen_shot(filePath)
    def Change_Display_Card(self, index):
        self.driver.element_click(self.element.turn_card_btn[index])
        time.sleep(2)
    def Get_Stop_Issue_Card_Amounts(self):
        # print("停發卡片有:", len(self.element.turn_card_btn), "張")
        return len(self.element.turn_card_btn)
    
class Unit(IUnit):
    @property
    def unit_home_page(self) -> IUnitHomePage:
        return self._unit_home_page
    @property
    def unit_side_menu(self) -> IUnitSideMenu:
        return self._unit_side_menu
    @property
    def unit_product_introduce(self) -> IUnitProductIntroduce:
        return self._unit_product_introduce
    @property
    def unit_card_introduce(self) -> IUnitCardIntroduce:
        return self._unit_card_introduce
    
    def __init__(self, driver: WebControl, element: IElement):
        super().__init__(driver)
        self._unit_home_page: IUnitHomePage = UnitHomePage(driver, element.home_page)
        self._unit_side_menu: IUnitSideMenu = UnitSideMenu(driver, element.side_menu)
        self._unit_product_introduce: IUnitProductIntroduce = UnitProductIntroduce(driver, element.product_introduce)
        self._unit_card_introduce: IUnitCardIntroduce = UnitCardIntroduce(driver, element.card_introduce)
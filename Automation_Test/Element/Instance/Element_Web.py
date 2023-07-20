from Element.Interface.IElement_Web import *
from Library.Web_Page.web_control import WebControl

class HomePage(IHomePage):
    def __init__(self, driver: WebControl):
        super().__init__(driver)
    @property
    def signin_btn(self): return self.driver.get_element("//a[@class='cubre-m-button -login']")
    @property
    def signout_btn(self): return self.driver.get_element("//a[@class='cubre-m-button -logout']")
    @property
    def menu_burger_icon(self): return self.driver.get_element("//a[@class='cubre-a-burger']")
    @property
    def search_bar(self): return self.driver.get_element("//input[@class='cubre-m-searchBox__box']")
    @property
    def search_btn(self): return self.driver.get_element("//a[@class='cubre-m-searchBox__tool -send']")
    @property
    def create_account_btn(self): return self.driver.get_element("//div[@class='cubre-o-quickLink__item']//a[@href='/cathaybk/personal/product/deposit/open-account']")
    @property
    def choose_credit_card_btn(self): return self.driver.get_element("//div[@class='cubre-o-quickLink__item']//a[@href='/cathaybk/personal/product/credit-card/cards']")
    @property
    def online_apply_btn(self): return self.driver.get_element("//div[@class='cubre-o-quickLink__item']//a[@href='/cathaybk/personal/digital-service/intro/online']")
    @property
    def exchange_rate_search_btn(self): return self.driver.get_element("//div[@class='cubre-o-quickLink__item']//a[@href='/cathaybk/personal/product/deposit/currency-billboard']")
    @property
    def reserve_service_btn(self): return self.driver.get_element("//div[@class='cubre-o-quickLink__item']//a[@href='https://www.cathaybk.com.tw/eservice/Appointment/IntroS0']")
    @property
    def activities_area_btn(self): return self.driver.get_element("//div[@class='cubre-o-quickLink__item']//a[@href='/cathaybk/personal/event/overview']")
    @property
    def AI_customer_service_btn(self): return self.driver.get_element("//div[@class='smart_icon']")
    
class SideMenu(ISideMenu):
    def __init__(self, driver: WebControl):
        super().__init__(driver)
    @property
    def close_btn(self): return self.driver.get_element("//div//img[@class='cubre-a-burger__img -close']")
    @property
    def search_bar(self): return self.driver.get_element("//div[@class='cubre-m-searchBox -header']//input[@class='cubre-m-searchBox__box']")
    @property
    def search_btn(self): return self.driver.get_element("//div[@class='cubre-m-searchBox -header']//a[@class='cubre-m-searchBox__tool -send']")
    @property
    def personal_finance_btn(self): return self.driver.get_element("//a[@href='/cathaybk/personal']")
    @property
    def product_intro_btn(self): return self.driver.get_elements("//div[@class='cubre-o-menu']//div[@class='cubre-o-menu__item']")[0]
    @property
    def digital_service_btn(self): return self.driver.get_elements("//div[@class='cubre-o-menu']//div[@class='cubre-o-menu__item']")[1]
    @property
    def about_cathaybk_btn(self): return self.driver.get_elements("//div[@class='cubre-o-menu']//div[@class='cubre-o-menu__item']")[2]
    @property
    def support_service_btn(self): return self.driver.get_elements("//div[@class='cubre-o-menu']//div[@class='cubre-o-menu__item']")[3]
    @property
    def service_base_btn(self): return self.driver.get_element("//a[@href='/cathaybk/locations']")
    @property
    def change_to_english_btn(self): return self.driver.get_element("//a[@href='/cathaybk/english/about-us/about-us/company-history?sc_lang=en-us']")
    @property
    def enterprise_finance_btn(self): return self.driver.get_element("//a[@href='https://www.cathaybk.com.tw/cathaybk/corp/']")
    @property
    def private_bank_btn(self): return self.driver.get_element("//a[@href='https://www.cathaybk.com.tw/cathaybk/promo/private-bank/index.html']")
    @property
    def overseas_base_btn(self): return self.driver.get_element("//a[@href='https://www.cathaybk.com.tw/overseas']")
    
class ProductIntroduce(IProductIntroduce):
    def __init__(self, driver: WebControl):
        super().__init__(driver)
    @property
    def credit_card_btn(self): return self.driver.get_elements("//div[@class='cubre-o-menu__item is-L1open']//div[@class='cubre-o-menu__content']//div[@class='cubre-o-menuLinkList__btn']")[0]
    @property
    def credit_card_option_list(self): return self.driver.get_elements("//div[@class='cubre-o-menuLinkList__item is-L2open']//div[@class='cubre-o-menuLinkList__content']//a")
    @property
    def card_intro_btn(self): return self.driver.get_element("//div[@class='cubre-o-menuLinkList__content']//a[@href='/cathaybk/personal/product/credit-card/cards']")
    @property
    def credit_card_offers_btn(self): return self.driver.get_element("//div[@class='cubre-o-menuLinkList__content']//a[@href='/cathaybk/personal/event/overview']")
    @property
    def bank_deposit_btn(self): return self.driver.get_elements("//div[@class='cubre-o-menu__content']//div[@class='cubre-o-menuLinkList__btn']")[1]
    @property
    def loan_btn(self): return self.driver.get_elements("//div[@class='cubre-o-menu__content']//div[@class='cubre-o-menuLinkList__btn']")[2]

class CardIntroduce(ICardIntroduce):
    def __init__(self, driver: WebControl):
        super().__init__(driver)
    @property
    def stop_issue_card_block(self): return self.driver.get_element("//section[@data-anchor-block='blockname06']")
    @property
    def turn_card_btn(self): return self.driver.get_elements("//section[@data-anchor-block='blockname06']//div[@class='cubre-o-slide__page swiper-pagination-clickable swiper-pagination-bullets']//span")
    
class Element(IElement):
    def __init__(self, driver: WebControl):
        self.driver = driver
        self.home_page:IHomePage = HomePage(driver)
        self.side_menu:ISideMenu = SideMenu(driver)
        self.product_introduce: IProductIntroduce = ProductIntroduce(driver)
        self.card_introduce: ICardIntroduce = CardIntroduce(driver)
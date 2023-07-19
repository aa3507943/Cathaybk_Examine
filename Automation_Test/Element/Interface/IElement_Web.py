from abc import ABC, abstractproperty
from Library.Web_Page.web_control import WebControl

class IHomePage(ABC):
    def __init__(self, driver: WebControl):
        self.driver = driver
    @abstractproperty
    def signin_btn(self): "登入鍵"
    @abstractproperty
    def menu_burger_icon(self): "左上角選單鍵"
    @abstractproperty
    def search_bar(self): "搜尋欄位"
    @abstractproperty
    def search_btn(self): "搜尋鍵"
    @abstractproperty
    def create_account_btn(self): "開戶鍵"
    @abstractproperty
    def choose_credit_card_btn(self): "挑選信用卡鍵"
    @abstractproperty
    def online_apply_btn(self): "線上申辦鍵"
    @abstractproperty
    def exchange_rate_search_btn(self): "匯率查詢鍵"
    @abstractproperty
    def reserve_service_btn(self): "預約服務鍵"
    @abstractproperty
    def activities_area_btn(self): "活動區域鍵"
    @abstractproperty
    def AI_customer_service_btn(self): "智能客服鍵"
    """多寫的僅以示例，其他暫且用不到，但可在此擴充"""

class ISideMenu(ABC):
    def __init__(self, driver: WebControl):
        self.driver = driver
    @abstractproperty
    def close_btn(self): "關閉選單鍵"
    @abstractproperty
    def signin_btn(self): "登入鍵"
    @abstractproperty
    def search_bar(self): "搜尋欄位"
    @abstractproperty
    def search_btn(self): "搜尋鍵"
    @abstractproperty
    def personal_finance_btn(self): "個人金融鍵"
    @abstractproperty
    def product_intro_btn(self): "產品介紹鍵"
    @abstractproperty
    def digital_service_btn(self): "數位服務鍵"
    @abstractproperty
    def about_cathaybk_btn(self): "關於國泰鍵"
    @abstractproperty
    def support_service_btn(self): "支援服務鍵"
    @abstractproperty
    def service_base_btn(self): "支援據點鍵"
    @abstractproperty
    def change_to_english_btn(self): "切換至英文介面鍵"
    @abstractproperty
    def enterprise_finance_btn(self): "企業金融鍵"
    @abstractproperty
    def private_bank_btn(self): "私人銀行鍵"
    @abstractproperty
    def overseas_base_btn(self): "海外據點鍵"
    """多寫的僅以示例，其他暫且用不到，但可在此擴充"""

class ProductIntroduce(ABC):
    def __init__(self, driver: WebControl):
        self.driver = driver
    @abstractproperty
    def credit_card_btn(self): "信用卡鍵"
    @abstractproperty
    def credit_card_list(self): "信用卡列表"
    @abstractproperty
    def card_intro_btn(self): "卡片介紹鍵"
    @abstractproperty
    def credit_card_offers_btn(self): "刷卡優惠鍵"
    @abstractproperty
    def bank_deposit_btn(self): "存款鍵"
    @abstractproperty
    def loan_btn(self): "貸款鍵"
    """多寫的僅以示例，其他暫且用不到，但可在此擴充"""

class CardIntroduce(ABC):
    def __init__(self, driver: WebControl):
        self.driver = driver
    @abstractproperty
    def stop_issue_card_list(self): "停發卡列表"
    @abstractproperty
    def stop_issue_card_block(self): "停發卡區塊"
    """其他暫且用不到，但可在此擴充"""

class IElement:
    home_page: IHomePage
    side_menu: ISideMenu
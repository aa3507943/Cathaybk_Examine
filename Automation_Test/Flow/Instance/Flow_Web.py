from Flow.Interface.IFlow_Web import *
from Unit.Interface.IUnit_Web import IUnit
import traceback
from Event_Record.exception_handler import ExceptionHandler


class FlowCase1(IFlowCase1):
    def __init__(self, unit: IUnit):
        self.log = ExceptionHandler
        try:
            super().__init__(unit)
            self.unit.unit_home_page.Goto_Cathaybk_Page("https://www.cathaybk.com.tw/cathaybk/")
            self.unit.unit_home_page.Screen_Shot_Home_Page('./Automation_Test/Pictures/Case1.png')
        except: #若例外發生時，記錄錯誤，強制結束此測項
            self.log(msg= traceback.format_exc(), exceptionLevel= "critical")
        finally: #不論項目成功與否，皆重整測項回首頁
            self.unit.unit_home_page.Goto_Cathaybk_Page("https://www.cathaybk.com.tw/cathaybk/")

class FlowCase2(IFlowCase2):
    def __init__(self, unit: IUnit):
        self.log = ExceptionHandler
        try:
            super().__init__(unit)
            self.unit.unit_home_page.Goto_Cathaybk_Page("https://www.cathaybk.com.tw/cathaybk/")
            self.unit.unit_home_page.Click_Side_Menu_Btn()
            self.unit.unit_side_menu.Click_Product_Introdcue()
            self.unit.unit_product_introduce.Click_Credit_Card()
            options = self.unit.unit_product_introduce.Get_Credit_Card_Option_Amounts()
            print("信用卡選項有", options, "項功能")
            self.unit.unit_product_introduce.Screen_Shot_Credit_Card_Option_List("./Automation_Test/Pictures/Case2.png")
        except: #若例外發生時，記錄錯誤，強制結束此測項
            self.log(msg= traceback.format_exc(), exceptionLevel= "critical")
        finally: #不論項目成功與否，皆重整測項回首頁
            self.unit.unit_home_page.Goto_Cathaybk_Page("https://www.cathaybk.com.tw/cathaybk/")

class FlowCase3(IFlowCase3):
    def __init__(self, unit: IUnit):
        self.log = ExceptionHandler
        try:
            super().__init__(unit)
            self.unit.unit_home_page.Goto_Cathaybk_Page("https://www.cathaybk.com.tw/cathaybk/")
            self.unit.unit_home_page.Click_Side_Menu_Btn()
            self.unit.unit_side_menu.Click_Product_Introdcue()
            self.unit.unit_product_introduce.Click_Credit_Card()
            self.unit.unit_product_introduce.Get_Credit_Card_Option_Amounts()
            self.unit.unit_product_introduce.Click_Card_Introduce()
            self.all_stop_issue_card = self.unit.unit_card_introduce.Get_Stop_Issue_Card_Amounts()
            print("停發信用卡有", self.all_stop_issue_card, "張")
            self.unit.unit_card_introduce.Scroll_To_Target_Area()
            self.Change_Card_And_Screen_shot()
            self.Photo_Check()
        except: #若例外發生時，記錄錯誤，強制結束此測項
            self.log(msg= traceback.format_exc(), exceptionLevel= "critical")
        finally: #動作結束，關閉網頁
            self.unit.driver.close_webpage()
    
    def Change_Card_And_Screen_shot(self):
        count = 0
        while count < self.all_stop_issue_card:
            self.unit.unit_card_introduce.Screen_Shot_Card_Block(f'./Automation_Test/Pictures/Case3-{str(count+1)}.png')
            self.unit.unit_card_introduce.Change_Display_Card(count)
            count += 1
        
    def Photo_Check(self):
        import os
        pic_count = 0
        all_photo_list = os.listdir("./Automation_Test/Pictures/")
        for i in range(len(all_photo_list)): #檢查存圖片資料夾中共有幾張屬於Case3的圖片
            if "Case3" in all_photo_list[i]:
                pic_count += 1
        if pic_count == self.all_stop_issue_card: #比較圖片實際張數與停發信用卡張數是否一致
            print("停發卡片截圖數量與停發卡片數量一致")
        else:
            print("停發卡片截圖數量與停發卡片數量不一致")

class Flow(IFlow):
    @property
    def Case1(self)-> IFlowCase1: FlowCase1(self.unit)
    @property
    def Case2(self)-> IFlowCase2: FlowCase2(self.unit)
    @property
    def Case3(self)-> IFlowCase3: FlowCase3(self.unit)
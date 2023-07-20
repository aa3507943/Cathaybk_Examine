from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Event_Record.exception_handler import ExceptionHandler
from Driver.create_driver import WebDriver
import time

class WebControl(): #python v3.11.x selenium 4.8.x 網頁控制
    def __init__(self, driver:webdriver.Chrome):
        self.driver:webdriver.Chrome = driver
        self.log = ExceptionHandler
        
    """呼叫此函式需可最大化當前控制的瀏覽器"""
    def maximize_window(self):
        "最大化視窗"
        self.log(msg= "將視窗最大化\n")
        self.driver.maximize_window()
        
    """呼叫此函式需可最小化當前控制的瀏覽器"""
    def minimize_window(self):
        "最小化視窗"
        self.log(msg= "將視窗最小化\n")
        self.driver.minimize_window()
    
    def set_window_size(self, width, height):
        "調整瀏覽器大小"
        self.log(msg= f"將視窗大小設置為{width}x{height}\n")
        self.driver.set_window_size(width, height)       

    """呼叫此函式可以將視窗移到所需的位置"""
    def move_window(self, x, y):
        "移動視窗到x, y上"
        self.log(msg= f"將視窗移動至螢幕座標 ({x}, {y})\n")
        self.driver.set_window_position(x, y)

    """呼叫此函式並於參數位置放入URL，連結至目標網頁"""
    def enter_target_page(self, url):
        "進入目標網頁"
        self.log(msg= f"進入 {url} 網頁\n")
        self.driver.get(url)
        self.all_page_wait()
    
    """呼叫此函式可以關閉當前控制的瀏覽器"""
    def close_webpage(self):
        "關閉網頁"
        self.log(msg= "關閉瀏覽器\n")
        self.driver.quit()
    
    """呼叫此函式需可重整當前控制的瀏覽器"""
    def reload_webpage(self):
        "重載網頁"
        self.log(msg= "重整瀏覽器\n")
        self.driver.refresh()
        self.all_page_wait()
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件"""
    def get_element(self, element):
        "取得元素"
        self.log(msg= f"取元素 {element}")
        self.element_wait(element, 5)
        return self.driver.find_element(By.XPATH, element)
    
    """呼叫此函式並從參數代入元件的Path，可在當前瀏覽器
    頁面上定位到相對應的元件列表，並給定另一參數指定要從
    列表中取第幾個index的元件"""
    def get_elements(self, element):
        "取得元素列"
        self.log(msg= f"取元素 {element} 列表")
        self.elements_wait(element, 5)
        return self.driver.find_elements(By.XPATH, element)
    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件做點擊的動作"""
    def element_click(self, getElement: get_element or get_elements):
        "點擊元素"
        self.log(msg= f"點擊元素 {getElement}")
        getElement.click()
    
    """呼叫此函式並從參數代入定位到的元件，可以對該元件    做輸入的動作，並給定另一參數指定可以輸入什麼"""
    def element_send_keys(self, getElement: get_element or get_elements, content):
        "傳遞值給元素"
        self.log(msg= f"傳值給元素 {getElement}")
        getElement.send_keys(content)
 
    def check_browser_alive(self):
        "確認瀏覽器是否存在"
        self.log(msg= "確認瀏覽器是否存活")
        try:
            self.driver.session_id
            return True
        except:
            return False
        
    """呼叫此函式並從參數代入欲定位的元件要等待多久時間載入"""
    def element_wait(self, element, time: int):
        "等待元素"
        try:
            WebDriverWait(self.driver, time).until(EC.element_to_be_clickable((By.XPATH, element))) 
        except:
            # logging.error(msg= "Time Out! Cannot locate the eleement. 時間到！無法定位到該元件。\n", exc_info= True)
            self.log(msg= "超時！無法定位到該元件。\n", exceptionLevel= "critical")
            raise
    
    """呼叫此函式並從參數代入欲定位的元件列表要等待多久時間載入"""
    def elements_wait(self, elements, time: int):
        "等待元素列"
        try:
            WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located((By.XPATH, elements))) 
        except:
            self.log(msg= "超時！無法定位到該元件。\n", exceptionLevel= "critical")
            raise
        
    """等待整個頁面載入完畢"""
    def all_page_wait(self):
        "整個頁面載入"
        self.driver.implicitly_wait(30)

    """切換視窗"""
    def switch_window(self, index):
        self.log(msg = f"切換分頁index為 {index}")
        self.driver.switch_to.window(self.driver.window_handles[index])

    """控制警告視窗"""
    def switch_alert(self):
        try:
            self.log(msg="進行網頁警示對話框控制")
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except:
            self.log(msg= "網頁警示對話框控制項目出現異常", exceptionLevel= "error")
            raise

    "特例"
    def subElement_get(self, subDriver: webdriver.Chrome, element): #使用父元素以獲取子元素
        try:
            self.log(msg= f"透過父元素{subDriver}協助定位子元素{element}")
            self.all_page_wait()
            return subDriver.find_elements(By.XPATH, element)
        except:
            self.log(msg= "定位失敗，出現異常", exceptionLevel= "critical")
            raise
    
    """截圖"""
    def screen_shot(self, filePath):
        self.log(msg= f"進行截圖動作並將圖片存至{filePath}")
        self.driver.save_screenshot(filePath)
        # self.driver.save_screenshot(f'./Pictures/{time.strftime("%Y%m%d-%H%M%S", time.localtime())}.png')
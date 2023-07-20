import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from Automation_Test.Event_Record.exception_handler import ExceptionHandler
driver = webdriver.Chrome(ChromeDriverManager().install())

class Test:
    def __init__(self):
        a = 15
        a /= 3
        a = str(a)
        a = a + 15

class Test2:
    def __init__(self):
        try:
            driver.get("https://youtube.com")
            # driver.implicitly_wait(10)
            driver.find_element(By.XPATH, "//button[@aria-label='使用語音']").click()
            # Test()
        except Exception:
            ExceptionHandler(msg = traceback.format_exc(), exceptionLevel= "critical")
            print(traceback.format_exc())

Test2()
import os
from Event_Record.exception_handler import ExceptionHandler

class FileAmountChecker:
    def __init__(self):
        self.folder_checker()

    def folder_checker(self):
        logFolder = "Event_Record/Log/"
        try:
            if len(os.listdir(logFolder)) <= 10:
                ExceptionHandler(msg = "Log記錄檔無須進行刪除", exceptionLevel= "info")
            else:
                ExceptionHandler(msg = "Log記錄檔多於10個，進行刪除動作", exceptionLevel= "warning")
                while len(os.listdir(logFolder)) > 10:
                    os.remove(logFolder + os.listdir(logFolder)[0])
                ExceptionHandler(msg = "Log記錄檔已刪除剩至近10個", exceptionLevel= "info")
        except:
            ExceptionHandler(msg = "刪除Log記錄檔動作出現未知異常，需進行排除", exceptionLevel= "critical")
            raise
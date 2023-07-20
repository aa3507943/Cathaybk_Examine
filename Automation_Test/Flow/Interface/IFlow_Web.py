from abc import ABC, abstractproperty
from Unit.Interface.IUnit_Web import IUnit

class IFlowCase1(ABC):
    "進到國泰世華銀行首頁並截圖"
    def __init__(self, unit: IUnit):
        self.unit = unit
        "將Unit拼裝成測試流程置於此處"
class IFlowCase2(ABC):
    "點選左上角選單，進入 個人金融 > 產品介紹 > 信用卡列表，需計算有幾個項目並將畫面截圖。"
    def __init__(self, unit: IUnit):
        "將Unit拼裝成測試流程置於此處"
        self.unit = unit
class IFlowCase3(ABC):
    "個人金融 > 產品介紹 > 信用卡 > 卡片介紹 > 計算頁面上所有(停發)信用卡數量並截圖"
    def __init__(self, unit: IUnit):
        "將Unit拼裝成測試流程置於此處"
        self.unit = unit
class IFlow(ABC):
    def __init__(self, unit:IUnit): 
        self.unit = unit
    @abstractproperty
    def Case1(self)-> IFlowCase1: "呼叫並執行測項1"
    @abstractproperty
    def Case2(self)-> IFlowCase2: "呼叫並執行測項2"
    @abstractproperty
    def Case3(self)-> IFlowCase3: "呼叫並執行測項3"

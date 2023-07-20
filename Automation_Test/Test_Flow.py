from Flow.Instance.Flow_Web import Flow
from Unit.Instance.Unit_Web import Unit
from System.Web_Chrome import Chrome
from Element.Instance.Element_Web import Element

class AutoTest:
    def __init__(self, enviroment: str):
        match enviroment: #此處可以測試要跑的環境，因時間關係沒有把Mobile App的操作寫入
            case "Chrome": 
                self.source = Chrome()
                self.Run_Chrome_Cases()
                
    def Run_Android_App_Cases(self):
        pass
    def Run_Chrome_Cases(self): 
        flow = Flow(Unit(self.source.web_control, Element(self.source.web_control)))
        flow.Case1
        flow.Case2
        flow.Case3


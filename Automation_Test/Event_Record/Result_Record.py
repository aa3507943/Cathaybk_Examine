import time, os

class ResultRecord:
    def __init__(self, resource, Time):
        self.Resource = resource
        self.today = time.strftime("%Y%m%d", time.localtime())
        self.recordPath = f"./Event_Record/Html/{self.today}.html"
        self.Time = Time
        self.Hour = 0
        self.Minute = 0
        self.Second = 0

    def time_calculate(self):
        while self.Time >= 60:
            if self.Time >= 3600:
                self.Hour = round(self.Time // 3600)
                self.Time -= self.Hour*3600
            elif self.Time >= 60 and self.Time < 3600:
                self.Minute = round(self.Time // 60)
                self.Time -= self.Minute*60
        else:
            self.Second = round(self.Time)
    
    def create_file(self):
        if os.path.isfile(self.recordPath) == False:
            with open(self.recordPath, mode= 'a+', encoding= "utf-8") as f:
                pass

    def record_result(self):
        self.time_calculate()
        self.create_file()
        with open(self.recordPath, mode = "a+",encoding="utf-8") as f:
            content = f.read()
            f.seek(0, 0)
            f.write("<html>")
            f.write("<head><title>"+ "The File Conversion Result \n" + "</title></head>")
            f.write("<body>\n")
            f.write("<h1>"+ time.strftime("%Y%m%d ", time.localtime()) + "The File Conversion Result: \n" + "</h1>")
            f.write(f"<h2>🆕所有檔案共: {self.Resource.step.totalFiles} 個</h2>\n")
            f.write(f"<h2>✔️轉換成功檔案共: {self.Resource.step.successFiles} 個</h2>\n")
            f.write(f"<h2>❌轉換失敗檔案共: {self.Resource.step.unsuccessFiles} 個</h2>\n")
            f.write(f"<h2>⏱️ 本次花費時間共 {self.Hour} 時 {self.Minute} 分 {self.Second} 秒</h2>\n")
            f.write("</body></html>")
            f.write(content)
           

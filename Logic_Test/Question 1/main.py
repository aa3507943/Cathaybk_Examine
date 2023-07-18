"""簡易版： 函式直接帶入題目給的數列即可轉換"""

def reverse_tool(gradeList):
    for i in range(len(gradeList)):
        opsiteGrade = "".join(reversed(str(gradeList[i]))) #將參數傳入之整數值轉為字串形式後，用reversed函式反轉(此動作會將字串拆成字元組列表)再拼回字串
        gradeList[i] = eval(opsiteGrade) #將字串轉為可做計算之值
    print(gradeList)

reverse_tool([35, 46, 57, 91, 29])

"""複雜版: 因題目敘述為輸入 [35, 46, 57, 91, 29]，，以此為規則會用下列邏輯針對輸入先做一次處理，再做成績反轉"""
import re
def reverse_tool(string: str):
    splits = re.split(',| ', string[1:-1]) #用正規表達式，將代入的無頭尾引號「串列」字串做字串切分
    result = [] #建立空串列接處理完的值
    for i in range(0, len(splits), 2):
        opsiteGrade = "".join(reversed(str(splits[i]))) #將參數傳入之整數值轉為字串形式後，用reversed函式反轉(此動作會將字串拆成字元組列表)再拼回字串
        result.append(eval(opsiteGrade)) #將字串轉為可做計算之值
    print(result)
    
grades = input()
#grades = "[35, 46, 57, 91, 29]" 可直接解除註解用此行測試
reverse_tool(grades)
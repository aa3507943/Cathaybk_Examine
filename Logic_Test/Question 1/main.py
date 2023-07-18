def reverse_tool(gradeList):
    for i in range(len(gradeList)):
        opsiteGrade = "".join(reversed(str(gradeList[i]))) #將參數傳入之整數值轉為字串形式後，用reversed函式反轉(此動作會將字串拆成字元組列表)再拼回字串
        gradeList[i] = eval(opsiteGrade) #將字串轉為可做計算之值
    print(gradeList)


# reverse_tool(wrong_grades)
CelebrateText = "Hello welcome to Cathay 60th year anniversary"
calculateDict = {}
textList = sorted(CelebrateText.upper()) 
#因題目輸出有經過字元排序，故先處理原字串；又因不論大小寫，故先將其先轉為大寫，再讓其排序後存成List

for i in textList:
    if i.upper() == " ": #題目為計算"字母"，故遇到空格就跳過
        continue
    else:
        if i.upper() not in calculateDict.keys(): #當字母不在字典中時，將其設為字典的Key值，並把預設Value值設為1
            calculateDict.setdefault(i.upper(), 1)
        else: #反之，當字母在字典中時，取出該字母Key的值做+1
            calculateDict[i.upper()] += 1

for i in range(len(calculateDict.keys())):
    print(list(calculateDict.keys())[i], list(calculateDict.values())[i]) #將字串的Key和Value印出
    
"""PS. 經測試，題目Excel中A的數量有誤，應為5個"""
    
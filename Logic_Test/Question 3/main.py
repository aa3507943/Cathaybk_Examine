number = eval(input("請輸入QA部門人數: ")) #輸入數值並將其轉換為可運算量
memberList = [x for x in range(1, number + 1 )] #依上變數值，用生成式作出1~number的串列
print(memberList)
index = 0 #因後面會以while迴圈做運算，故在迴圈外先建立計算串列跑到第幾個元素的變數宣告
tmp = 1 #此變數用以計算現在報數到多少，從1開始
while len(memberList) > 1:
    if tmp == 3: #若報到3
        memberList.remove(memberList[index]) #移除對應的串列元素
        tmp = 1 #將報數初始化到1 
        index -= 1 #因下一次會從原串列的下一個元素開始，且又因有元素被刪除，故抓元素的index要退一位，才不會抓錯
    else:        
        tmp += 1 #報數加一
    if index == len(memberList) - 1: #當index做完串列最後一位時，為使其從頭開始連續做，將index + 1改為index = 0
        index = 0
    else:
        index += 1 
print(memberList[0])

    
        
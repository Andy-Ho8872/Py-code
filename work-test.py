#請撰寫一程式，讓使用者輸入十個成績，列出由小至大的值,
#接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。

numberList = []
n = int(input("請輸入列表長度(例如: 10) : "))
for i in range(1, n+1):
    print("輸入第", i,"個數", ":")
    item = int(input())
    numberList.append(item)
print("輸出後列表 ", numberList)
sorted_numberList =numberList
print("排序後列表",sorted(sorted_numberList))
print("最大值為: ", max(sorted_numberList))
print("最小值為: ", min(sorted_numberList))
print("總和為: ", sum(sorted_numberList))
print("=================================================================")

set_numberlist = set(sorted_numberList)
sorted_set_numberList = sorted(set_numberlist)

print("剔除重複之數值後: ", set_numberlist)
print("重新排序", sorted_set_numberList)



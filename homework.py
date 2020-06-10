#使用者輸入十個成績，列出由小至大的值，接下來將十個成績中最小和最大值（最小、最大值不重複）以外的成績作加總及平均，並輸出結果。

numberList = []
n = int(input("請輸入列表長度(例如: 10) : "))
for i in range(1, n+1):
    print("輸入第", i,"個數", ":")
    item = int(input())
    numberList.append(item)
    print("=================================================================")
print("輸出後列表 ", numberList)

sorted_numberList = sorted(numberList)  # 將輸出後列表由小至大排序

print("排序後列表",  (sorted_numberList))
print("最小值為: ", min(sorted_numberList))
print("最大值為: ", max(sorted_numberList))
print("總和為: ", sum(sorted_numberList))

#計算平均值
total = sum(sorted_numberList) 
i = i

print("平均為:" ,total/i)
print("=================================================================")

#剔除重複的值，並重新排序
set_numberlist = set(sorted_numberList)
sorted_set_numberList = sorted(set_numberlist)

print("剔除重複之數值後: ", set_numberlist)
print("重新排序", sorted_set_numberList)

x = len(sorted_set_numberList)
print("剔除最大最小值後: ", sorted_set_numberList[1:x-1])

#計算剔除後總和與平均
excluded = sum(sorted_set_numberList[1:x-1])
print("剔除後總和: ", excluded )

y = len(sorted_set_numberList[1:x-1])
excluded_sum = excluded/y
print("剔除後平均: ", excluded_sum)



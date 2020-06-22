import pandas as pd
# 讀取資料
data = pd.read_csv("googleplaystore.csv")  # 把 CSV 格式的檔案讀取成一個 DaraFrame

# 觀察資料
print("資料數量", data.shape)
print("資料欄位", data.columns)
print("==================================================================================")

# 分析資料:評分的各種統計數據
condition = data["Rating"]<=5  # 只取評分 <=5
data = data[condition]
print("評分平均數", data["Rating"].mean())
print("評分中位數", data["Rating"].median())
print("取得前 1000 個應用程式的平均值",data["Rating"].nlargest(1000).mean())
print("==================================================================================")

# 分析資料:安裝數量的各種統計數據
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "").replace("Free", "")) # 將原始資料轉換為數字，並把原本的"逗號"與"+號"替代為空字串(將無法使用的資料剃除)
print("安裝平均數", data["Installs"].mean())
condition = data["Installs"]>100000
print("安裝數量大於 100000 的應用程式", data[condition].shape[0])
print("==================================================================================")

#基於資料的應用: 透過關鍵字搜尋應用程式的名稱
keyword = input("請輸入關鍵字: ")
condition = data["App"].str.contains(keyword, case=False) # 判斷應用程式的字串是否包含使用者輸入的關鍵字, case為是否判定大小寫(False為忽略)
print("關鍵字包含", ">", keyword, "<", "的應用程式數量: ", data[condition].shape[0])
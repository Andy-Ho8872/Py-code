import tkinter as tk

#處理隨機數生成
import random 

#處理複製功能
import pyperclip

#建立主視窗
win = tk.Tk() 

#設定視窗名稱(標題)
win.title("練習用_隨機座標產生器")  

#設定視窗大小
win.geometry("400x200+800+400")  #(寬x高 +X +Y) (用字串表示,後面的 + 前者數字為X軸，後者為Y)---(設定開啟視窗大小預設值及位置)
win.minsize(width=400, height=200) #設定視窗最小值
win.maxsize(width=1024, height=768) #設定視窗最大值
#win.resizable(0, 0)  #使視窗無法被縮放

#設定視窗icon
win.iconbitmap("E:\\python-training\\icon\\tomato.ico") #圖檔的副檔名建議用.ico

#設定背景顏色
win.config(background="pink")

#設定透明度
win.attributes("-alpha",0.95) #透明度設定值為 0 ~ 1   0為完全透明，1為不透明
#置頂視窗
win.attributes("-topmost",True)

#建立按鈕功能
def generate_XY():
    min_value = int(min_entry.get())
    max_value = int(max_entry.get())
    X = str(random.randint(min_value, max_value)) #產生隨機亂數(最小值, 最大值)
    Y = str(random.randint(min_value, max_value))
    lb_show_X_result.config(text="X座標為:"+X)
    lb_show_Y_result.config(text="Y座標為:"+Y)

def copy_XY():
    cop_x = lb_show_X_result.cget("text")  #cget() 函數為抓取特定內容 例如: text, background, foreground
    cop_y = lb_show_Y_result.cget("text")
    pyperclip.copy(cop_x +"\n" + cop_y)
     
#建立與設定按鈕(Button)。
generate = tk.Button(text="產生")  #產生座標按鈕
generate.config(background="skyblue") #設定按鈕背景顏色
generate.config(command=generate_XY ) #設定按鈕功能
generate.place(relx=0.4, rely=0.9, anchor="center")  #放置(封裝、包裝)按鈕，按鈕才會出現。  放置方法:  1 .pack()   2 .place   3 .grid()

copy = tk.Button(text="複製") #複製座標按鈕
copy.config(background="skyblue")
copy.config(command=copy_XY )
copy.place(relx=0.6, rely=0.9, anchor="center")

#建立與設定輸入物件(Entry)
min_entry = tk.Entry()
min_entry.config(width=8)
min_entry.place(relx=0.3, rely=0.45, anchor="center")

max_entry = tk.Entry()
max_entry.config(width=8)
max_entry.place(relx=0.7, rely=0.45, anchor="center")

#設定與建立標籤(Label)
lb01 = tk.Label(text="隨機產生X, Y座標 (需輸入整數)", font=14)
lb01.config(foreground="red")
lb01.config(background="white")
lb01.place(relx=0.5, rely=0.1, anchor="center") #此為相對定位 rel值在 0~1之間，anchor為錨點

lb02 = tk.Label(text="最小值")
lb02.config(background="light yellow")
lb02.place(relx=0.3, rely=0.3, anchor="center")

lb03 = tk.Label(text="最大值")
lb03.config(background="light yellow")
lb03.place(relx=0.7, rely=0.3, anchor="center")

lb_show_result = tk.Label(text="成果")
lb_show_result.config(background="light yellow")
lb_show_result.place(relx=0.5, rely=0.55, anchor="center")

lb_show_X_result = tk.Label(text="")
lb_show_X_result.config(foreground="red")
lb_show_X_result.config(background="pink")
lb_show_X_result.place(relx=0.5, rely=0.65, anchor="center")

lb_show_Y_result =tk.Label(text="")
lb_show_Y_result.config(foreground="red")
lb_show_Y_result.config(background="pink")
lb_show_Y_result.place(relx=0.5, rely=0.75, anchor="center")

#常駐主視窗
win.mainloop() 

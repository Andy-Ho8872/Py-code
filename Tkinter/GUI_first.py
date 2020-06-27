import tkinter as tk
from PIL import Image, ImageTk 
#建立主視窗
win = tk.Tk() 

#設定視窗名稱(標題)
win.title("視窗名稱測試")  

#設定視窗大小
win.geometry("400x300+800+400")  #(寬x高 +X +Y) (用字串表示,後面的 + 前者數字為X軸，後者為Y)---(設定開啟視窗大小預設值及位置)
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

#建立按鈕圖片
img = Image.open("E:\\python-training\\icon\\0.png") #圖片位置
load_image = ImageTk.PhotoImage(img)  #需先將圖片轉換成 Photoimage

show_tomato = Image.open("E:\\python-training\\icon\\tomato.png") 
load_tomato_img = ImageTk.PhotoImage(show_tomato)

#建立按鈕功能
def click_open():
    show_tomato.show()  

#建立與設定按鈕(Button)。
btn01 = tk.Button(text="按鈕1") 
btn01.config(image=load_image) #修改按鈕樣式
btn01.config(command=click_open) #設定按鈕功能

btn01.place(relx=0.5, rely=0.5, anchor="center")  #放置(封裝、包裝)按鈕，按鈕才會出現。  放置方法:  1 .pack()   2 .place   3 .grid()

#建立與設定輸入物件(Entry)
en01 = tk.Entry()
en01.pack()

#設定與建立標籤(Label)
lb01 = tk.Label(text="這是標籤")
lb01.config(background="white")
lb01.place(relx=0.5, rely=0.8, anchor="center") #此為相對定位 rel值在 0~1之間，anchor為錨點


#常駐主視窗
win.mainloop() 

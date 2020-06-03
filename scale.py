import tkinter as tk

#建立主視窗
win = tk.Tk() 

#設定視窗名稱(標題)
win.title("視窗名稱測試")  

#設定視窗大小
win.geometry("400x300+800+400")  #(寬x高 +X +Y) (用字串表示,後面的 + 前者數字為X軸，後者為Y)---(設定開啟視窗大小預設值及位置)
win.minsize(width=400, height=200) #設定視窗最小值
win.maxsize(width=1024, height=768) #設定視窗最大值


#設定視窗背景顏色
win.config(background="skyblue")

#建立拉桿功能
def get_val(self):
    s_value = s.get()
    win.attributes("-alpha", s_value/100)
    print(s_value)

#建立拉桿元件
s = tk.Scale(orient="horizontal") #把拉桿改成水平
s.config(width=30)    #更改拉桿寬度
s.config(length=300)   #更改拉桿長度
s.config(from_=0, to=100)
s.config(showvalue=0, tickinterval= 10, resolution= 10) #顯示拉桿數字  0為關閉  1為開啟, 也可以指定數值、間隔區間(tickinterval) 、解析度(resolution)
s.config(label="TK slider") #標籤位置無法更動
s.config(command= get_val) #連結功能
s.set(50) #設定拉桿預設值
s.place(relx=0.5, rely=0.5 , anchor="center")




win.mainloop() 
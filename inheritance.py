class Mamml:
    def walk(self):
        print("walk")
        
        
class Dog(Mamml):  # Dog 會繼承 Mamml 的 屬性( walk() )，且方法(Method)必須存在,或 pass
    def bark(self): 
        print("bark")

class Cat(Mamml):  # Cat 也會繼承 Mamml 的屬性
    pass  # pass = 無， 直接跳過，且方法內最少要"空兩行"在進行下一個分類的創建
        

dog1 = Dog()
dog1.walk()
dog1.bark()




class Cat():
    def __init__(self, name, age, gender):  # 因為self是class本身 所以第一個不用更動
        self.name = name  # 在這邊self.的設定 就代表你之後可以用的class屬性
        self.age = age
        self.gender = gender       
Cat_info = Cat("來福", 7 ,"male")
print("姓名:",Cat_info.name,"\n" "年齡:",Cat_info.age,"\n" "性別:",Cat_info.gender)


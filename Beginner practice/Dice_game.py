import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        third = random.randint(1, 6)
        fotrh = random.randint(1, 6)
        return(first, second, third, fotrh)

# 建立新的 Dice 實體
dice = Dice()

# 執行 5次 roll 方法並印出
for i in range(5):
    print("--------------")
    print(dice.roll()) # 使用 roll 方法

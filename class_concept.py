class Point:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        
    def move(self):
        print("move")
        
    def draw(self):
        print("draw")
        
p1 = Point(22, 30)
print(p1.x)


class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print("Hello I am", self.name)
        
per1 = Person("Will Smith")
per1.talk()

per2 = Person("Bob Smith")
per2.talk()
class Person:
    def __init__(self, name): #생성자. 
        self.name = name

    def say_hello(self):
        print("Hi!", self.name)

he = Person("smith")
he.say_hello()

#파이썬 클래스 상속: class클래스명(부모클래스):
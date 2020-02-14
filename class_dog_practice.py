# 嘗試自定義一個表示狗的類(dog)
# 類是現實中的抽象！
# 屬性: name, age, gender, hight.....
# 方法：叫、咬、跑

class Dog():
    """
    表示狗的類
    """
    
    def __init__(self,**kwargs):
        self.name = kwargs["name"]
        self.age = kwargs["age"]
        self.gender = kwargs["gender"]
        self.height = kwargs["height"]
        pass
 
    def bark(self):
        print("狗叫～～～～")

    def bite(self):
        print("咬人～～～～")

    def run(self):
        print("{} is running~~~~~~".format(self.name))



dog = Dog(name="dog", age=10, gender='male', height=30)

print(dog.name)
# 目前我們可以直接通過 object.property的方式來修改屬性的值，這種方式導致對象中的屬性可以隨意修改，非常不安全！！！因為值可以被任意修改不論對錯
dog.name = "cat"
dog.bark()
dog.run()

# 現在我們需要一種方式來增加數據的安全性
#  1.屬性不能任意修改（我讓你改你才能改，不讓你改你就不能改）
#  2.屬性不能修改為任意的值（年齡不能是負數）
#

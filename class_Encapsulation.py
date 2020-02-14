# 現在我們需要一種方式來增加數據的安全性
#  1.屬性不能任意修改（我讓你改你才能改，不讓你改你就不能改）
#  2.屬性不能修改為任意的值（年齡不能是負數）


# 封裝是OOP的三大特性之一
# 封裝指的是隱藏對象中一些不希望被外部所訪問的屬性或方法
# 好處 => 增加數據安全性
# 使用封裝，確實增加了類的定義的複雜度，但是它也確保了數據的安全性
#  1.隱藏了屬性名，使調用者無法隨意修改對象
#  2.增加getter & setter方法，很好控制屬性是否是只能讀取的
#    如果希望屬性只是只讀的，則可以直接去掉setter方法
#    如果希望屬性不能被外部訪問，則可以直接去掉getter方法
#  3.使用setter方法設置屬性，可以增加數據的驗證，確保數據的值是正確的
#  4.使用getter方法獲取屬性，使用setter方法設置屬性
#      可以在讀取屬性和修改屬性的同時做一些其他的處理
#

class Dog():

    def __init__(self, name):
        #self.name = name
        self.hidden_name = name

    def say_hello(self):
        print("Hello~~~~{}".format(self.hidden_name))

d = Dog("Tim")
d.name = "Tommy"

d.say_hello()

# 如何隱藏一個對象中的屬性？
#  - 將對象中的屬性名，修改為一個外部不知道的名字（防君子不防小人）


# 如何獲取（修改）對象中的屬性？
# 需要提供一個getter和setter方法使外部可以訪問到屬性
#  - getter 獲取對象中的指定屬性（get_屬性名）
#  = setter 用來設定對象的指定屬性(set_屬性名)

class Dog2():

    def __init__(self, name):
        self.hidden_name = name
   
    def say_hello(self):
        print("Hello~~~{}".format(self.hidden_name))

    def get_name(self):
        """
            get_name()用來獲取對象的name屬性
        """
        #在現實生活中，這是很方便的功能，例如電商的話可以在這邊記錄這個商品被查詢過幾次之類的
        print("用戶讀取了屬性")
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name



d2 = Dog2("旺財")

d2.say_hello()

d2.get_name()

# 調用setter來修改name屬性
d2.set_name("小黑")
d2.say_hello()


class Dog3():

    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age
   
    def say_hello(self):
        print("Hello~~~{}".format(self.hidden_name))

    def get_name(self):
        """
            get_name()用來獲取對象的name屬性
        """
        return self.hidden_name

    def set_name(self, name):
        self.hidden_name = name

    def get_age(self):
        return self.hidden_age

    def set_age(self,age):
        if age > 0:
            self.hidden_age = age

d3 = Dog3("旺財", 8)
d3.set_age(-10)



print(d3.get_age())

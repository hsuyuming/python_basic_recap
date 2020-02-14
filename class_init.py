# 類中包含了數據（屬性）以及行為（方法），但是每一個類的屬性可能都有不同的value，所以我們基本上不會在class中定義屬性

class Person:

    def say_hello(self):
        print("Hello~~~{}".format(self.name))

#如果不在類中定義屬性的話，直覺的想法可能是創建後給予屬性

p1 = Person()
p1.name = "Abe"
p1.say_hello()

p2 = Person()
p2.name = 'John'
p2.say_hello()

#p3 = Person()
#p3.say_hello()
#Traceback (most recent call last):
#  File "class_init.py", line 19, in <module>
#    p3.say_hello()
#  File "class_init.py", line 6, in say_hello
#    print("Hello~~~{}".format(self.name))
#AttributeError: 'Person' object has no attribute 'name'


# 需求：對於Person class，name是必須的，但是每一個對象中的name屬性基本上都是不同的
# 我們希望在創建對象的時候，必須設置name屬性，如果不設置對象將無法創建，並且屬性的創建應該是自動完成的，而不是在創建對象後手動添加


# 所以我們可以在類中定義一些特殊方法(magic method)
# 特殊方法都以__開頭，以__結尾
# 特殊方法不需要我們自己調用，一般不要嘗試去調用特殊方法
# 特殊方法在特定的時候會特定調用
# 如何學習特殊方法：
#  - 特殊方法在什麼時候調用
#  - 特殊方法有什麼作用
# 創建對象的流程
# p1 = Person()的運行流程
#  1. 創建一個變量
#  2. 在記憶體中創建一個新對象
#  3. __init__(self)z; 方法執行
#  4. 將對象的id assign給變數
#
#  init 會在對象創建後執行
#  init 可以用來向新創建的對象中初始化屬性

class Person2:

    print("Person2區塊的程式碼")
    def __init__(self):
        #print("init 方法執行了")
        self.name = "abehsu"

    def say_hello(self):
        print("Hello~~~~{}".format(self.name))

p4 = Person2()
#p4.__init__()
#init 方法執行了
#init 方法執行了

p5 = Person2()
p6 = Person2()
p7 = Person2()



class Person3:

    print("Person2區塊的程式碼")
    def __init__(self, name):
        #print("init 方法執行了")
        self.name = name

    def say_hello(self):
        print("Hello~~~~{}".format(self.name))

#p7 = Person3()
#Traceback (most recent call last):
#  File "class_init.py", line 80, in <module>
#    p7 = Person3()
#TypeError: __init__() missing 1 required positional argument: 'name'


p7 = Person3("abehsu")
p8 = Person3("May")
p9 = Person3("Kelley")

p7.say_hello()
p8.say_hello()

# 類的基本結構
#  class 類型（父類）:
#    公共的屬性....
#    
#    # 對象的初始化方法
#    def __init__(self):
#        ........
#    
#    # 其他方法
#    def method1(self):
#        ........
#








































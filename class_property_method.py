# 所有事物都由兩部分構成
#  - 數據（屬性）
#  - 行為（方法）

# 類中所定義的屬性跟方法都是公共的
# 屬性和方法查找流程
#    -  當我們調用一個對象的屬性時，解析器會在當前對象中尋找是否含有該屬性，如果有，則直接返回當前對象的屬性值，如果沒有的話，則去當前對象的類對象中尋找，如果有則返回類對象的屬性值，如果又沒有，那就會報錯


class Person():
    name = "abehsu"
    
    def say_hello(self):
        # 方法每次被調用時，解析器都會自動傳遞第一個實參
        # 注意！在方法中不能直接調用類別的屬性

        # 第一個參數，就是調用方法的對象本身
        # 如果是p1調用的，則第一個參數就是p1 object
        # 如果是p2調用的，則第一個參數就是p2 object
        # 一班我們都將這個參數命名為self

#        print("Hello~~~~~~{}".format(name))
#        Traceback (most recent call last):
#         File "class_property_method.py", line 44, in <module>
#           p1.say_hello()
#        File "class_property_method.py", line 15, in say_hello
#          print("Hello~~~~~~{}".format(name))
        #print(self)
        print("Hello~~~~~~{}".format(self.name))

p1 = Person()
p2 = Person()
print(p1.name)

# 修改p1的name屬性，這時候會加name這個屬性存到p1 object的value中
p1.name = "aaa"

print(p1.name)

# 類對象與實例對象都可以保存屬性和方法
#  - 如果這個屬性（方法），是所有的實例共享的，則應該將其保存在類對象中#  - 如果這個屬性（方法），是某個實例特有的，那就應該寶文在實例對象中ㄇ# 例如人有名字，每個人的名字都不一樣，這就不適合放在類對象的屬性中

# 一般情況下，屬性保存在實例對象中，方法保存在類對象中

p1.name = "Tom"
p2.name = "May"

print(p1.name)
print(p2.name)

del p2.name

print(p1.name)
print(p2.name)



# 這邊可以發現，下面兩次對象的位置都相同，可以了解到類型方法中的第一個參數，實際上就是調用方法對象的本身
p1.say_hello() #<__main__.Person object at 0x107703d68>
print(p1) #<__main__.Person object at 0x10d21fd68>

p2.say_hello()












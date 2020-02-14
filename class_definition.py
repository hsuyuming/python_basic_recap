# 類的定義
#   - 類和對象都是對現實生活中或程序中的內容的抽象
#   - 想想事物共有得特點
#   - 實際上所有事物都由兩個部分構成：
#     1. 數據（屬性）
#     2. 行為（方法）


class Person():
    # 在class的空間中，我們可以定義變量和函數
    # 在類中我們所定義的變數，將會變成所有實例的公共屬性
    # 所有實例都可以訪問這些變數
    name = 'abehsu' # 公共屬性，所有實例都可以訪問

    # 在類中也可以定義函數，類中定義的函數，我們稱為方法
    # 這些方法也可以透過類的實例來執行
    def say_hello(a):
        print(a)
        print("Hello~~~~")

# 創建Person的instance
p1 = Person()
p2 = Person()

print(p1.name)
print(p2.name)



# 調用方法,對象.方法名()
# 方法調用和函數的調用有區別
# 如果是函數調用，則調用時傳幾個參數，就會有幾個實參
# 但是如果是方法調用，默認會傳遞一個參數,所以方法中至少要定義一個形參，第一個參數由解析器自動傳遞，所以定義方法時，至少要定義一個形參


#print(p1.say_hello())
#Traceback (most recent call last):
#  File "class_intro2.py", line 27, in <module>
#    print(p1.say_hello())
#TypeError: say_hello() takes 0 positional arguments but 1 was given

print(p1.say_hello())










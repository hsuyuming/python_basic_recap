
def add(a, b):
    """
    求任意兩個數字的和
    """
#    print("計算開始.......")
    result =  a + b
#    print("計算結束.......")
    return result

def mul(a, b):
    """
    求任意兩個數字的積
    """
#    print("計算開始.......")
    result = a * b
#    print("計算結束.......")
    return result 

# 需求：可以函數計算前印開始計算，在開始計算後印計算完畢
# 方法ㄧ：直接修改函數來實現需求，但會產生一些問題
#     - 如果要改的函數很多，修改起來很麻煩
#     - 不方便後期維護
#     - 假如函數不是我們自己定義，是別人定義我們拿來使用，拿來修改會違反OCP原則
#     - OCP -> 開放對程式的擴展，關閉對程式的修改

# 新需求：我們希望在不修改原函數的狀況下，來對函數進行擴展

def fn():
    print("我是fn函數")

# 我們只需要根據現有的函數，來創建一個新函數
def extend_fn():
    print("函數開始執行......")
    fn()
    print("函數執行結束......")

extend_fn()



#def new_add():
#    print("函數開始執行......")
#    add()
#    print("函數執行結束......")

#new_add()
#Traceback (most recent call last):
#  File "decorator_function.py", line 47, in <module>
#    new_add()
#  File "decorator_function.py", line 44, in new_add
#    add()
#TypeError: add() missing 2 required positional arguments: 'a' and 'b'


def new_add2(a, b):
    print("函數開始執行......")
    result = add(a, b)
    print("函數執行結束......")
    return result 

r = new_add2(123, 456)
print(r)


# 需求三：如果讓這種擴展方式更通用？
# 解決方法：創建一個函數，讓這個函數可以自動地幫我們生成函數

def begin_end(old):
    """
    用來對其他函數進行擴展，使其他函數可以在執行前打印開始執行，結束後印出執行結束
    參數：
        old 要擴展的函數對象 
    """

    #創建一個新函數
    def new_function():
        print("開始執行......")
        old()
        print("執行結束......")
    
    #返回新函數   
    return new_function

#f = begin_end()
#f2 = begin_end()

#print(f) <function begin_end.<locals>.new_function at 0x10dbd11e0>
#print(f2) <function begin_end.<locals>.new_function at 0x10dbd1268>


f = begin_end(fn)
f()


def begin_end2(old):
    """
    用來對其他函數進行擴展，使其他函數可以在執行前打印開始執行，結束後印出執行結束
    參數：
        old 要擴展的函數對象 
    """

    #創建一個新函數
    def new_function(*args, **kwargs):
        print("開始執行......")
        result = old(*args, **kwargs)
        print("執行結束......")
        return result
    
    #返回新函數   
    return new_function

f = begin_end2(fn)
f2 = begin_end2(add)

r = f()
print(r)
r2 = f2(123,456)
print(r2)



# begin_end2() 這種函數我們就稱它為裝飾器，通過裝飾器可以在不修改原來函數的狀況下，進行擴展，在開發中，我們都是通過裝飾器來擴展函數的功能


@begin_end2
def hello_world():
    print("hello world~~~~~")


print(hello_world) #<function begin_end2.<locals>.new_function at 0x10d86f400>

hello_world()


def extend_function(old):
    
    def new_function(*args, **kwargs):
        print("decorator2-開始執行~~~~")
        result = old(*args, **kwargs)
        print("decorator2-執行結束~~~")
        return result
    return new_function




# 可以為一個函數指定多個裝飾器decorator，從內向外
@begin_end2
@extend_function
def hello_world2():
    print("hello_workld~~~")

hello_world2()

#開始執行......
#decorator2-開始執行~~~~
#hello_workld~~~
#decorator2-執行結束~~~
#執行結束......








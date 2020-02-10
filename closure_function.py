# 將函數當作返回值返回，也是一種高階函數
# 這個高階函數我們也稱為closure function, 通過閉包我們可以創建一些只有當前函數能訪問的變量
# 可以將一些私有的數據藏在closure中


# 形成 closure function的要件
# 1.函數嵌套
# 2.將內部函數作為返回值返回
# 3.內部函數必須要用到外部函數的變量




def fn():

    a = 10
    
    # 在函數內在定義一個函數
    def inner():
        print("I am fn2", a)
    
    return inner


print(fn())


# r是一個函數，是調用fn()後返回的函數
# 這個函數是在fn()內部定義的,並不是全局函數
# 所以這個函數總是能訪問到fn()函數內的變量


r = fn()
r()

#print(a)
#Traceback (most recent call last):
#  File "closure_obj.py", line 27, in <module>
#    print(a)
#NameError: name 'a' is not defined


# 求多個數的平均值

nums = [50,30,20,10,77]

print(sum(nums) / len(nums))


#創建list保存數值
nums = []

def avg(n):
    # 將n加到list中
    nums.append(n)
    # 求平均值
    return sum(nums) / len(nums)

print(avg(10))
print(avg(10))

# 注意在這時候，nums是個全局的變數，再任意位置可以被訪問修改，這樣很危險
#nums.append('hello')
#Traceback (most recent call last):
#  File "closure_obj.py", line 60, in <module>
#    print(avg(30))
#  File "closure_obj.py", line 51, in avg
#    return sum(nums) / len(nums)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'



print(avg(30))
print(avg(30))
    

def make_avg():
    nums = []
    
    def avg(n):
        nums.append(n)
        return sum(nums) / len(nums)

    return avg


avg2 = make_avg()

print(avg2(10))
print(avg2(20))
nums = []
print(avg2(30))








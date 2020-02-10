
#如果想要function的型參是可變動的話，可以加＊
def fn(a,b,*c):
    print("a=",a)
    print("b=",b)
    print("c=",c, type(c))


fn(1,2,3,4,5,6,7,8)


# 帶星號的型參只能有一個
# 帶星號的參數，可以跟其他類別的型參搭配使用
# 如果帶星號的型參不在最後一個參數位置，那麼在帶星號型參後面的參數都需要是屬於關鍵字參數類型
def fn2(a, *b, c):
    print("a=",a)
    print("b=",b)
    print("c=",c, type(c))

fn2(1,4,5,7,8,c=9)


#如果在型參的開頭直接寫一個*，則要求我們所有的參數都必須以關鍵字參數的形式傳遞
def fn3(*,a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c, type(c))

#fn3(1,2,3) -> Error

fn3(a=1, b=2, c=3)


# *型參只能接收位置參數，而不能接受關鍵字參數
def fn4(*a):
    print("a=",a)
#fn4(b=1,d=2,c=3)

#Traceback (most recent call last):
#  File "variable_param_function.py", line 37, in <module>
#    fn4(b=1,d=2,c=3)
#TypeError: fn4() got an unexpected keyword argument 'b'

# **(兩個星)型參可以接受其他的關鍵字參數，他會將這些參數統一保存到一個字典中
# 型參只能有一個，並且必須寫在所有參數的最後面
def fn5(**a):
    print("a=",a)

fn5(b=1,d=2,c=3)


def fn6(b,**a):
    print("a=",a)
    print("b=",b)

fn6(b=1,d=2,c=3)

def fn7(a,b,c,*d,**e):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)
    print("e=",e)

fn7(1,2,3,4,5,6,7,8,e=100)



# 參數的解包（拆包）
def fn8(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)


t=(10,20,30)
t1=[10,20,30]

fn8(*t)
fn8(*t)

def fn9(a,b,*c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

t=(10,20,30,40)
t1=[10,20,30,40]

fn9(*t)
fn9(*t1)




def fn10(**kwgs):
    print(kwgs['a'])

d = {"a":1,"b":2,"c":3}
fn10(**d)

# 命名空間  namespace
# 命名空間指的是變數存儲的空間，每一個變數都需要儲存到一個指定的命名空間當中
# 每一個作用域都有它對應的命名空間
# 全局命名空間，用來保存全局變量，函數命名空間用來保存函數中的變量
# 命名空間實際上就是一個字典，是一個專門用來存變數的dictionary


# locals()用來獲取當前作用域的命名空間

a = 10
b = 20

def fn(a:int, b:int) -> int:
    internal_scope = locals()
    print("區域內的命名空間:",locals())
    
    global_scope = globals()
    print("全局命名空間:",global_scope)
   
    return a + b

scope = locals()
print(scope, type(scope))

print(scope["a"])

# 利用在字典內添加key-value相當於在全局中創建了一個變數（不建議這麼做）
scope["c"]=100

print(c)

fn(1,2)

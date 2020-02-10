# 高階函數
# 接收函數作為參數，或者將函數作為返回值的函數就是高階函數

# 創建一個列表
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 定義一個函數：可以將找到指定列表中的所有偶數，保存到一個新的列表中返回
# 當我們使用一個函數作為參數的時候，實際上是將指定的代碼傳遞進了目標函數 

def fn2(i):
    if i % 2 == 0:
        return True
    return False

def fn3(i):
    if i % 2 != 0:
        return True 
    return False

def fn4(i):
    if i % 3 ==0:
        return True
    return False


def fn(func, lst:list):
    """
        fn()函數可以將指定列表中的所有偶數獲取出來，並保留一個新列表返回
        參數：
            lst : 要進行篩選的夜表
    """

    new_list = []

    for n in lst:
        if func(n):
            new_list.append(n)
        #if n % 2 == 0 :
        #    new_list.append(n)

    return new_list


#print(help(fn))

print( fn(fn2, l) )
print( fn(fn3, l) )
print( fn(fn4, l) )










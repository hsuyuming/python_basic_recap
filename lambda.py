# filter()
# filter() 可以從序列中過濾出符合條件的元素，將結果保存到一個新的序列中
# 參數:
# 1. 函數，根據該函數來過濾序列（可迭代的結構）
# 2. 需要過濾的序列（可迭代的結構）
#返回值：
# 過濾後的新序列（可迭代的結構）


l = [1,2,3,4,5,6,7,8,9,10]


def fn4(i):
    if i % 3 == 0 :
        return True
    return False



r = filter(fn4, l)
print(r)
print(list(r))


print(lambda x,y : x + y)
print(type(lambda x,y : x + y))
print( (lambda x,y : x + y)(10,20) )


print( filter(lambda i : i % 3 == 0 , l) )
print( list (filter(lambda i : i % 3 == 0 , l) ))



r = map( lambda x : x+1, l)
print(list(r))









# == / != / is / is not 差別

# == / != 比較的是Object的值是否相等
# is / is not 比較的是Object的id是否相等

a = [1, 2, 3]
b = [1, 2, 3]
print(a,b)
print("a id:",id(a), "b id:", id(b))

print( a == b ) # a和b的值相等，會返回True
print( a is b)  # a和b不是同個對象,記憶體儲存的位置不同，會返回False

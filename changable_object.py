
# 可變Object
# List 就是一個可變Object
# a = [123]
# a[0] = 10 (改變Object裡面的值)
# 這個操作是透過變數去修改Object的值
# 當我們去修改對象的時候，如果有其他變數也指向這個對象，修改結果也會反映在其他變數上

# a = [4, 5, 6] (改變量)
# 這個操作是在給變數重新賦值，這個操作會改變變數指定的Object，但不會影響其他變數



a = [1, 2, 3]
b = a

print("a","id:",id(a),"type:",type(a), "value:", a)
print("b","id:",id(b),"type:",type(b), "value:", b)

a[0] = 10
print("a","id:",id(a),"type:",type(a), "value:", a)
print("b","id:",id(b),"type:",type(b), "value:", b)

a = [2, 6, 9]
print("a","id:",id(a),"type:",type(a), "value:", a)
print("b","id:",id(b),"type:",type(b), "value:", b)

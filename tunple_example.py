
# Tuple的解構
# 解構就是將Tuple當中的每一個元素都asign給一個變量


my_tuple = (10, 20, 30, 40)
a, b, c, d = my_tuple
print(a)
print(b)
print(c)
print(d)


# 應用場境：可以拿來交換變數的值

a = 100
b = 200
print(a)
print(b)
print("開始交換")
a, b = (b,a)
print(a)
print(b)

# 在對一個Tuple進行解構的時候，變數的數量必須和Tuple內裡面的元素數量一致
# 如果變數數量不一致的時候，可以添加一個*，這樣變量將會獲取Tuple中剩下的元素
print("===============Example:如果變數數量與Tuple元素不一致=================")
my_tuple = (10,20,30,40,50)
a, b, *c = my_tuple
print(a)
print(b)
print(c)
print("===============Example2:如果變數數量與Tuple元素不一致=================")
my_tuple = (10,20,30,40,50)
a, *b, c = my_tuple
print(a)
print(b)
print(c)


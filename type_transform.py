#類型轉換不會更改Object本身的類型，而是根據當前Object的值創建一個新的Object

a = 'hello'
b = 123

#print( a + b ) 不同類型不同運算


#類型轉換4函數 int() float() str() bool()

# int() 可以將其他Object轉換成int
# 不會對原來的變數產生影響，只會將Object轉換為指定的類型並將其作為返回值返回
# 如果需要修改原本的變數，則需要重新asign

a = True
print(id(a))
print("a = ", a)
print("type(a) = ",type(a))

int(a)
a = int(a)
print(id(a))
print("type(a) = ", type(a) )

a = '123'
print("a = ", a)
print("type(a) = ",type(a) )

a = int(a)
print("a = ", a)
print("type(a) = ",type(a))



# bool()

a = '0'
print("a = ", a)
print("type(a) = ",type(a))
a = bool(a)
print("a = ", a)
print("type(a) = ",type(a))


a = ''
print("a = ", a)
print("type(a) = ",type(a))
a = bool(a)
print("a = ", a)
print("type(a) = ",type(a))


a = None
print("a = ", a)
print("type(a) = ",type(a))
a = bool(a)
print("a = ", a)
print("type(a) = ",type(a))

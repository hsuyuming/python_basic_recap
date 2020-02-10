#通過類型檢查，只能檢查變數的型別類型

a = 123
b = '123'

print("a = ",a)
print("b = ",b)

#type()用來檢查值的類型
type(123)
c = type(123)
print(c)

print(type(b))


print("--------------------")
print(type(1))
print(type(1.5))
print(type(True))
print(type("Hello"))
print(type(None))

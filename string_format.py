#格式化字符串
a = "hello"

a = "hello" + "abc"
print(a)
print("a = " + a) #這種寫法不常見

# 字串不能跟其他型別進行加法運算，會遇到TypeError: must be str, not int


print('a =',a)

# %f (小數)
# %d (整數)

print('%f'%1.234)
print('%.2f'%1.234)

print('%d'%123.4534636)

#格式化字符串
c = f'hello'
print(c)

c = f" hello {a}"
print(c)

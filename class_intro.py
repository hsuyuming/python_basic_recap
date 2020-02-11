a = int(10) #創建一個class的instance
b = str('hello')

print(a, type(a))
print(b, type(b))



# 使用class關鍵字來定義類型
# class 類名（開頭大寫）([父類])
class MyClass():
    pass

print(MyClass) #<class '__main__.MyClass'>

#使用類創建對象，就像調用函數一樣
mc = MyClass()
print(mc, type(mc)) #<__main__.MyClass object at 0x104269e48> <class '__main__.MyClass'>


mc2 = MyClass()
mc3 = MyClass()
mc4 = MyClass()
print(mc2, type(mc2))
print(mc3, type(mc3))
print(mc4, type(mc4))


# isinstance() 用來檢查一個對象是不是一個類的實例
result = isinstance(mc,MyClass)
print(result)

result2 = isinstance(mc,str)
print(result2)



# class 也是一個對象(object)
# class 是一個用來創建對象的對象
# class是一個type類型的對象，定義類其實實際上就是定義了一個type類型的對象
print(id(MyClass)) #140493896054712
print(type(MyClass)) #<class 'type'> 


mc5 = MyClass()
# 在記憶體中創建一個變數mc5
# 在記憶體中建立一個object (id=xxx type=MyClass value= )
# 將object的id指定給變數

# 現在我們通過MyClass這個類創建的對象是一個空對象
# 也就是對象中實際上什麼都沒有，就相當於是一個空盒子
# 我們可以向對象中添加變量，對象中的變量稱為屬性
# 語法：對象.屬性名=屬性值

mc5.name = "abehsu"

print(mc5.name)









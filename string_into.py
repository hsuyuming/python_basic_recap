

s = 'hello'
print(s)
s1 = "hello"
print(s1)
#相同引號之間，不能再加入相同引號
#單引號以及雙引號都不能跨行使用(可以使用反斜線或是用"""""")
# """"""(代表長字符串),並且會保留字串格式
#s3 = "Abe said:"Hello world""
s3 = 'Abe said:"Hello world"'
print(s3)

s4='123,\
456, \
789'
print(s4)


s5="""23,
456, 
789"""
print(s5)

# \uxxxx 表示unicode編碼
unicode_str = "\u16a1"
print(unicode_str)

#Object會儲存三種屬性在記憶體中，分別是id,type,value

a = 123

#我們可以用id()來查看Object的id,id是由interpreter產生,在Cpython中,id就是Object的memory location
#Object一但創建，id就永遠不能更改
print(id(a))
#4474875696


#類型決定了Object有哪些功能
print(type(a))
#<class 'int'>

#值就是Object實際儲存的數據
#可以分為 可改變Object以及不可改變Object


#變量以及對象
#Object並沒有直接儲存在變量中，比較像是給Object取了個別名
#變量中儲存的不是Object的值而是Object的id(memory location)
#變量和變量之間是相互獨立的，修改一個變量不會影響另一個變量

a = 10
print('a', a,'id:',id(a))
b = a
print('b', b,'id:',id(b))

a = 20
print('a', a,'id:',id(a))
print('b', b,'id:',id(b))




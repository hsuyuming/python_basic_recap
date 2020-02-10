

# sort()可以接受一個關鍵字參數:key
# key需要一個函數作為參數，當設置了函數當作參數
# 每次都會以列表中的一個元素作為參數來調用函數，並且使用函數的返回值來比較元素的大小


l = ['bb', 'aaaa', 'c', 'ddddddddd', 'fff']

l.sort()
print(l)

l.sort(key=len)
print(l)


# sorted()
# 這個函數和sort()的用法基本一致，但是sorted()可以對任意的序列進行排序，並且使用sorted()不會影響原來的對象，而是返回一個新對象

l2 = [2, 5, '1', 3, '6', '4']

print("排序前：",l2)
print(sorted(l2,key=int))
print("排序前：",l2)


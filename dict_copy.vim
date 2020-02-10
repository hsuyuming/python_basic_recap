

a = {"name":"abe","age":27}
b = a
print("a id:", id(a), "a value:",a)
print("b id:", id(b), "b value:",b)

print("-------Change dict value -----------")

a["name"] = "yyy"
print("a id:", id(a), "a value:",a)
print("b id:", id(b), "b value:",b)

print("\n")

# copy()
# copy會對於dict進行淺複製
# 複製以後的對象，和元對象是獨立的，修改一個並不會影響另一個
# 但是注意！！！！淺複製會複製對象內部的值，但如果值也是一個可變對象，這個可變對象不會被複製


a = {"name":"abe","age":27}
b = a.copy()
print("a id:", id(a), "a value:",a)
print("b id:", id(b), "b value:",b)

print("-------Change dict value -----------")

a["name"] = "yyy"
print("a id:", id(a), "a value:",a)
print("b id:", id(b), "b value:",b)

print("\n")

a = {"test":{"name":"abe","age":27},"b":2,"c":3}
b = a.copy()
print("a id:", id(a), "a value:",a)
print("b id:", id(b), "b value:",b)

print("-------Change dict value -----------")
a["b"] = 10
a["test"]["name"] = "abehsu2"
print("a id:", id(a), "a value:",a)
print("b id:", id(b), "b value:",b)



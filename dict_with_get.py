
d = {
"name":"abe",
"age":27
}


# 我們可以給定特定的Key來獲得dict裡面的值，但是透過這種方式的時候，如果Key不存在就會報錯
print(d["name"])

try:
  print(d["test"])
except Exception as e:
  print("Error happen")



# 另一種取得Value的方式，我們可以用get，用get的時候如果key不存在，不會報錯，而是會返回None,我們也可以給預設值

print(d.get("name"))
print(d.get("test"))
print(d.get("test","default_value"))

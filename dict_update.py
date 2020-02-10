
# update([other])
# 可以將其他的dict內的key-value加入到當前的dict中，如果key有重複的話，key裡面的值會被更新

d = { "a":1, "b":2, "c":3 }
d2 = { "d":4, "e":5, "f":6, "a":7 }
d.update(d2)
print(d)

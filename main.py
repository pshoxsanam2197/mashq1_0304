# 6-m
sonlar = [1, 6, 3, 8, 2, 10]
print(sonlar)
a = list(filter(lambda x : x > 5,  sonlar))
print(a)

# 7-m
m = [12, 5, 7, 20, 3, 15]
print(m)
a = list(filter(lambda x : x < 10, m))
print(a)

# 8-m
roy = [3, 5, 9, 10, 12, 14]
print(roy)
roy2 = list(filter(lambda el: el % 3 == 0, roy))
print(roy2)

# 9-m
roy =  [6, 8, 12, 15, 18, 20]
print(roy)
roy2 = list(filter(lambda el: el % 2 == 0 and el % 3 == 0, roy))
print(roy2)

# 10-m
roy = [6, 8, 12, 15, 18, 20]
print(roy)
roy2 = list(filter(lambda el: el != 0 ,roy))
print(roy2)

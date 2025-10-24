a = 12
b = 5
print(b - a)
print(b - abs(2 * b - a) * 3) # (11)
print("{0:05b}".format(b)) # (12)
c = [2, 7, 15, 12, 9] # (13)
c.sort() # (14)
print(c) # (15)
print(c[2:3]) # (16)インデックス2から4の手前までのスライスをリストで返す
print(f'{(a - b) / c[3]:->8.3f}') # (17)


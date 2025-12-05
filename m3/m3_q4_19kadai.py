list_a = []
for x in range(1, 31):
	if x % 2 == 0:
		continue # 偶数の時に繰り返す
	list_a.append(x)
print(list_a)

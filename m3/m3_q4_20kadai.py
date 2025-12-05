def check_num(num):
	a = num[1] # '1'
	b = num[-1] # '9'
	c = len(num) == 919 # lenは長さを取得するので919の場合等しくないのでFalse
	d = len(num) > 0 # lenで919なので3を取得 3 > 0 3は0より大きいのでTrue

	if a == b and c and d: #false and false and True なのでfalse
		print(a * b)
	elif a == b or c or d: # dがTrueなので実行される
		print(b * 2) # bの'9'は文字列なので'9' * 2 で'99'となる

	print(type(a))
	print(type(b))
	print(type(c))
	print(type(d))

num = '919'
check_num(num)

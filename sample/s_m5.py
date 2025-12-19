list_a = [214, 54, 178, 3, 200]
list_b = ['','','','','']

i = 0
for x in list_a: # list_aの各要素をxへ
	if x <= 80: # xが80以下
		list_b[i] = 'low' # lowを代入
	elif x <= 200: # xが200以下
		list_b[i] = 'middle' # middleを代入
	else: # それ以外(x > 200)
		list_b[i] = 'high'
	i += 1 # 次の代入用にインデックスを１増やす
print(list_b) # ['high', 'low', 'middle', 'low', 'middle']

list_c = [4, 2, 6, 2]
list_a += list_c # list_aにlist_cを結合
print(list_a) # [214, 54, 178, 3, 200, 4, 2, 6, 2]

list_d = list_c.copy() # list_dは[4, 2, 6, 2]をコピー
for x in list_d[-2:]: # 末尾２要素(6, 2)を順にxに代入
	list_d.insert(2, x) # インデックス２へxを代入(以降は右へずれる)
print(list_d) # [4, 2, 2, 6, 6, 2]

list_e = list_c # list_eはlist_cの参照
list_e.remove(2) # 最初に出現する２を一つ削除
print(list_c) # [4, 6, 2]

list_f = []
for x in range(0, 10, 3): # 0, 3, 6, 9 を順にxに代入
	if 10 <= x ** 2 and x ** 2 < 30: # x²が１０以上３０未満
		list_f.append(2 * x) # xの２倍を追加
	elif 30 <= x ** 2: # x²が３０以上
		list_f.append(x ** 2) # z²を追加
	else: # それ以外(x² < １０)
		list_f.append(x) # x を追加
print(list_f) # [0, 3, 36, 81]

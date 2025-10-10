phrase = 'PythonProgrraming'
list_p = [] # 空のリストを作成
for p in phrase: # 繰り返して1文字ずつ検査
	if p not in list_p: # pがlist_pにまだ含まれていなければ、list_p.append(p) list_pにpを追加(append)する。
		list_p.append(p)
print(len(phrase) - len(list_p)) # 17-11=6 6は重複した文字の数
for p in list_p: # 重複のない文字が格納されたlist_pから、文字1つずつ順番にpとして取り出す。
	print(p, end="") # end=""で文字の自動で改行が入らないようにして、隣に続けて出力
print()

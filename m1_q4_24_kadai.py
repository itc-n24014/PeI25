animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
	print("totalの値は", total)
	form_D = animal.startswith('D') # animalが'D'で始まる場合True,そうでない場合falseを返す
	is_long = len(animal) > 5 # animalの文字数が5文字以上ならTrue
	if form_D and is_long:
		break	# どちらもTrueならbreak
	elif not form_D and is_long:
		total += animal.find('b') # 最初に'bが現れるインデックスを返し、見つからなければ-1を返す
	else:
		total += len(animal)
print(total)

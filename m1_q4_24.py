animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
	form_D = animal.startswith('D') # animalが'D'で始まり場合True,そうでない場合falseヲァエス
	is_long = len(animal) > 5 # animalの文字数が5文字以上ならTrue
	if form_D and is_long:
		break	# どちらもTrueならbreak
	elif not form_D and is_long:
		total += animal.find('b') # 最初に'bが現れるインデックスを返し、見つからなければ-1を返す
	else:
		total += len(animal)
print(total)

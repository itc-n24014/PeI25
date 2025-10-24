fruits = ['マンゴー', 'パイナップル', 'バンシルー']

d = 2
while d < 4:
    favorite = fruits.pop(11 % d)  # さっぱりで好き
    d += 2

print("取り出した果物:", favorite)
print("残りの果物リスト:", fruits)


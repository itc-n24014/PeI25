import random # shuffleやrandintで利用
import sys # sys.exit()で利用

words = [('apple', 'りんご'), ('banana', 'ばなな'), ('coconut', 'ココナッツ'),
        ('donut', 'ドーナツ'), ('effort', '努力'), ('future', '未来'),
        ('gorilla', 'ゴリラ'), ('house', '家'), ('information', '情報'),
        ('journey', '旅')]

questions = int(input('出題数を入力'))

length = len(words) # wordsの長さ(数)をlengthに代入
if length < questions: # questions が登録されている単語数より多い場合は終了
    print('登録された単語数以下の数値を入力してください')
    sys.exit()

count = 0 # 出題済み問題数をカウントする変数
correct = 0 # 正解数

while count < questions:
    random.shuffle(words) # wordsの中身をシャッフル
    ans_index = random.randint(0, 3)  # words の最初の4要素の中から正解をランダムに選び、ans_indexに格納
    print(f'問題{count + 1}:{words[ans_index][0]}の意味は？') # 問題文の出力

    for i in range(2): # # words の最初の4要素を2回に分けて選択肢として表示
        print(f'{i * 2 + 1}:{words[i * 2][1]}, {i * 2 + 2}:{words[i * 2 + 1][1]}') # 選択肢の出力を2回のループで行う

    answer = input('1から4の数字で解答(終了するには"x"を入力):')
    if answer == 'x': # xが入力されたらループ終了
        break

    print(f'あなたの解答:{answer}')
    if answer == str(ans_index + 1): # input()で入力された数字はstrなのでstr()を使って変換し比較
        print('正解！')
        correct += 1
    else:
        print(f'不正解！正解は{ans_index + 1}の{words[ans_index][1]}でした！')

    count += 1 # 次の問題のためカウントを進める

print(f'成績:正解{correct}問 (全{count}問)') # 成績の表示

import random  # shuffleやrandintを使うために読み込む
import sys     # プログラムを途中で終了させるために使う

# 英単語と日本語の意味をセットで登録したリスト
words = [('apple', 'りんご'), ('banana', 'ばなな'), ('coconut', 'ココナッツ'),
        ('donut', 'ドーナツ'), ('effort', '努力'), ('future', '未来'),
        ('gorilla', 'ゴリラ'), ('house', '家'), ('information', '情報'),
        ('journey', '旅')]

# 出題する問題数を入力してもらう
questions = int(input('出題数を入力'))

length = len(words)  # 登録されている単語の数をlengthに入れる
if length < questions:  # 出題数が単語数より多い場合はエラー
    print('登録された単語数以下の数値を入力してください')
    sys.exit()  # プログラムを終了

count = 0    # 何問出題したかを数えるための変数
correct = 0  # 正解した問題数を数えるための変数

while count < questions:  # 指定された問題数になるまで繰り返す
    random.shuffle(words)  # 単語の順番をランダムに並び替える
    ans_index = random.randint(0, 3)  # 最初の4つの中から正解の位置を決める
    print(f'問題{count + 1}:{words[ans_index][0]}の意味は？')  # 問題文を表示

    for i in range(2):  # 選択肢を2回に分けて表示する
        print(f'{i * 2 + 1}:{words[i * 2][1]}, {i * 2 + 2}:{words[i * 2 + 1][1]}')
        # 1〜4番までの日本語の意味を表示

    answer = input('1から4の数字で解答(終了するには"x"を入力):')  # 解答を入力
    if answer == 'x':  # xが入力されたら途中で終了
        break

    print(f'あなたの解答:{answer}')  # 入力された解答を表示
    if answer == str(ans_index + 1):  # 正解の番号と比較
        print('正解！')
        correct += 1  # 正解数を増やす
    else:
        print(f'不正解！正解は{ans_index + 1}の{words[ans_index][1]}でした！')

    count += 1  # 出題数を1つ増やす

print(f'成績:正解{correct}問 (全{count}問)')  # 最終結果を表示


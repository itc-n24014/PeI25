def func(a, b):
    # a ** b が 64 以下なら 1（True相当）を返し、それ以外は 0（False相当）を返す
    return 1 if a ** b <= 64 else 0

# bool関数について：
# ・bool(値) は、その値を True か False に変換する関数
# ・0、空文字、空リスト、None などは False
# ・それ以外の値は True として扱われる

x = func(4, 3)
y = func(3, 4)
a = func(5, 6)  # 追加：変数aに func(5,6) の戻り値を代入

z = [bool(x), bool(y), bool(a)]  # a も含めてリストに格納
print(z)


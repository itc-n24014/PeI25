a = [2.02, 2.03, 2.04]
b = [2.05, 2.06, -2.07]
c = a + b

print(max(c))
print(min(c[2:5]))
print(round(c[2], 1))
print(round(c[5], 1))
print(round(c[3], 1))  # 2.0になるのは2.05が内部的に2.049999...と表現されるため


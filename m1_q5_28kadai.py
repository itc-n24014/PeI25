day = ['月', '月', '火', '水', '木', '金', '金']

for d in ['月', '火', '水', '木', '金']:
    if d in day[day.index(d)+1:]:
        day.remove(d)  # 重複を削除

day.insert(len(day), '土')  # '土'を追加
day.insert(len(day), '日')  # '日'を追加

print(day)

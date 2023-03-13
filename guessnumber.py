# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話印出"終於猜對了
# 猜錯的話提示比答案大/小

import random
ans = random.randint(1, 100)
n = 0
while True:
    guess = int(input('請輸入答案'))
    n += 1
    if guess == ans:
        print('終於猜對了')
        break
    elif guess < ans:
        print('比答案小，猜大點')
    elif guess > ans:
        print('比答案大，猜小點')
print('你猜了', n, '次')
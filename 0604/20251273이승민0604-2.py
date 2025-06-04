#산점도 그래프 그리기

import matplotlib.pyplot as plt
import random as r

x = []; y = []; input_clr = []; size = []

for i in range(100):
    x.append(r.randint(1, 100))
    y.append(r.randint(1, 100))
    input_clr.append(r.randint(1, 100))
    size.append(r.randint(1, 500))

# print(x)
# print(y)
#그래프 그리기

# input_clr = input("그래프 색깔을 입력하세요 : ")
# size = input("그래프 크기를 입력하세요 : ")

plt.scatter(x, y, color = input_clr, s = size, alpha=0.3)
plt.show()
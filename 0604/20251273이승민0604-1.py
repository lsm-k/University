import matplotlib.pyplot as plt

data = [102, 140, 160, 300, 80, 90, 250, 130]

x = range(len(data))        #len()함수는 리스트의 길이를 리턴하는 함수
plt.bar(x, data)            #x축은 리스트 길이로, y축은 data값으로 bor를 그리겠다
plt.show()

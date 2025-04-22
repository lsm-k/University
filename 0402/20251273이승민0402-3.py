import random as r

""" n_1 = r.randint(1,45)
n_2 = r.randint(1,45)
n_3 = r.randint(1,45)
n_4 = r.randint(1,45)
n_5 = r.randint(1,45)
n_6 = r.randint(1,45)

print("이번주 행운의 로또번호입니다")
print(n_1, end=' ')
print(n_2, end=' ')
print(n_3, end=' ')
print(n_4, end=' ')
print(n_5, end=' ')
print(n_6) """

#주제2-숫자맞추기게임(컴퓨터가 갖고있는 숫자를 맞춰라)

com = r.randint(1,100)
try_num = 0
player = 0

while True:
    player = int(input("컴퓨터가 갖고있는 숫자는 뭘까요?"))
    try_num += 1
    if com == player:
        print("정답입니다")
        break
    elif com > player:
        print("힌트 : 더 큰값 입력해보세요")
    elif com < player:
        print("힌트 : 더 작은값 입력해보세요")

print("당신은 총", try_num, "만에 성공했습니다")
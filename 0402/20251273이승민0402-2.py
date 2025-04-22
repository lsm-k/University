#주제-1 이름을 여러번 입력하기

for i in range(0, 5, 1):
    print("홍길동",end=' ')

print()

a = 0

while  a < 5:
    print("아이유", end=' ')
    a += 1
print()

#주제-2 1~100까지 값을 출력하기

""" print('1', end=' ')
print('2', end=' ')
print('3', end=' ')
print('4', end=' ')
print('5')
"""

for num in range(1, 101, 1):
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=' ')

print()

#주제3-50~100사이의 7의 배수값 출력
num_7 = 0
while True:
    if num_7 % 7 == 0 and num_7 >= 50 and num_7 <= 100:
        print(num_7)
    elif num_7 > 100:
        break
    num_7 = num_7 + 1
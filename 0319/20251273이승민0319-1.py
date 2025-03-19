#주제 - 인터뷰 프로그램

'''

name = input("당신의 이름을 알려주세요~")
age = input("나이는 어떻게 되세요?")

print("--------------------")
print("오늘 ", name, "님 인터뷰ㅔ 응해주셔서 감사합니다")
print("나이는는 ", age, "이시군요 감사합니다")
'''

#주제 - 간단한 계산 프로그램
n1 = int(input("값1 입력?"))
n2 = int(input("값2 입력?"))
#n1 = 10
#n2 = 3.3
res1 = n1 + n2
res2 = n1 - n2
res3 = n1 > n2
res4 = n1 / n2

print(n1, '+', n2, '=',res1)
print(n1, '-', n2, '=',res2)
print(n1, '>', n2, '=',res3)
print(n1, '*', n2, '=',n1 * n2)
print(n1, '/', n2, '=%.2f'%res4)
print(n1, '//', n2, '=',n1 // n2)
print(n1, '%', n2, '=',n1 % n2)

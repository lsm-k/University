'''
#문제1-두개의 값을 입력받아 사각형과 삼각형 넓이 출력

w = int(input("밑변 길이 입력?"))
h = int(input("높이 길이 입력?"))

square_area = w * h
triangle_area = w * h / 2

print("사각형의 넓이 : ", square_area)
print("삼각형의 넓이 : ", triangle_area)

#문제2-원의 넓이 출력

pi = 3.14
radius = float(input("반지름 입력?"))
circle_area = pi * radius * radius
print("반지름이 ", radius, "인 원의 넓이 : %.3f"%circle_area)
'''

#점수 3개를 입력받아 총점과 평균 구해주세요

score_1 = float(input("국어점수 입력 : "))
score_2 = float(input("수학점수 입력 : "))
score_3 = float(input("영어점수 입력 : "))

total = score_1 + score_2 + score_3
average = total / 3

print("총점 : %.2f"%total)
print("평균 : %.2f"%average)
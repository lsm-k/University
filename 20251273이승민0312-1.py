#터틀을 이용한프로그램 제작

import turtle as t

t.Screen()
t.title("제작-20251273이승민")
t.shape("turtle")


#100크기의 사각형
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(90)

#좌표이동
t.penup()
t.goto(-50,0)
t.pendown()

#50크기의 사각형
t.forward(50)
t.left(-90)
t.forward(50)
t.left(-90)
t.forward(50)
t.left(-90)
t.forward(50)

#좌표이동
t.penup()
t.goto(-50,-100)
t.pendown()

#삼각형 그리기(사이즈 100)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

#리본모양 만들기
t.forward(80)
t.left(-120)
t.forward(80)
t.left(-120)
t.forward(80)

#좌표 이동
t.penup()
t.goto(50,200)
t.pendown()

#6각형 그리기
t.pencolor("#A9F5F2")
t.left(52)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)
t.left(60)
t.forward(60)

#오각형 별 그리기
#조건1.변길이 100
#조건2.72도로 두번회전한 144도를 회전
#별의 다음 꼭짓점을 그릴때는 72도를 회전한다


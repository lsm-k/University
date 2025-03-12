#오각형 별 그리기
#조건1.변길이 100
#조건2.72도로 두번회전한 144도를 회전
#별의 다음 꼭짓점을 그릴때는 72도를 회전한다

import turtle as t

t.Screen()
t.title("제작-20251273이승민")
t.shape("turtle")

t.right(72)
t.forward(100)
t.left(72)

for i in range(4):
    t.forward(100)
    t.right(144)
    t.forward(100)
    t.left(72)
    
t.forward(100)

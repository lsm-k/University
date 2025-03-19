import turtle as t
t.Screen()
t.title("제작-20251273이승민")
t.shape("turtle")

def mv(i,j):
    t.penup()
    t.goto(i,j)
    t.pendown()

#이름쓰기
t.penup()
t.goto(-300,100)
t.pendown()

t.circle(30)

mv(-250,180)

t.right(90)
t.forward(100)

mv(-180,180)

t.left(30)
t.forward(50)

mv(-180,180)

t.right(60)
t.forward(50)
t.left(120)

mv(-220,120)

t.forward(90)

mv(-180,50)

t.circle(30)

mv(-100,180)

for i in range(4):
    t.forward(40)
    t.right(90)

mv(-50,200)

t.right(90)
t.forward(60)

mv(-80,100)

t.forward(30)
t.left(90)
t.forward(70)

import turtle

win = turtle.Screen()
ball = turtle.Turtle('circle')
ball.penup()

xvel = 3
yvel = 3
start_x = -300
start_y = 200
floor = -300
overall_time = 200
restitution_coefficient = 0.8

ball.goto(start_x, start_y)
ball.down()

time = 0
while time < overall_time:
    if ball.ycor() < floor and yvel < 0:
        yvel = yvel * -restitution_coefficient
    ball.setx(ball.xcor() + xvel)
    ball.sety(ball.ycor() + yvel)
    yvel = yvel - 1
    time = time + 1
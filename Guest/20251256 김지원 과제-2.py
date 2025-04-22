import turtle 
import random

win=turtle.Screen()
dice_Computer = turtle. Turtle()
dice_Player = turtle. Turtle()

win. setup (800, 400) 
win.title
def toss_dice():        #주사위 던저기 
    num = random.randint (1,6)
    return num


for i in range(1,7):
    turtle.addshape('d:/대학/University/Guest/주사위/주사위' +str(i)+ '.gif')

dice_Computer.penup()
dice_Player.penup()

dice_Computer. goto(-200, 0) 
dice_Player. goto (200, 0)

win_Computer=0
win_Player=0
player = 0
com = 0


while True:
    player = toss_dice()
    com = toss_dice()
    dice_Computer.shape('d:/대학/University/Guest/주사위/주사위' +str(com)+ '.gif')
    dice_Player.shape('d:/대학/University/Guest/주사위/주사위' +str(player)+ '.gif')
    if player > com:
        print("이겼습니다")
        win_Player += 1
    elif player < com:
        print("졌습니다")
        win_Computer += 1
    elif player == com:
        print("비겼습니다")
    reTry = input("게임을 다시 시작할래요, 예(y), 아니요(n)")
    if reTry != 'r':
        print(win_Player, "승", win_Computer,"패")
        break
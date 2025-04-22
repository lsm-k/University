#주제1-자동차면허 1종 필기 합격여부

score_1 = int(input("점수를 입력하시오 : "))
if score_1 >= 70:
    print("합격! 기능 시험 준비하세요")
else:
    print("불합격! 다시 시험보세요")

#주제2-성적평가(A,B,C,D,F)

score_2 = int(input("점수를 입력하시오 : "))
if score_2 >= 90 and score_2 <= 00:
    hakjum = 'A'
elif score_2 >= 80 and score_2 <= 89:
    hakjum = 'B'
elif score_2 >= 70 and score_2 <= 79:
    hakjum = 'C'
elif score_2 >= 60 and score_2 <= 69:
    hakjum = 'D'
else:
    hakjum = "F 또는 100점보다 큰 값 입력 불가"

print("당신의 학점은", hakjum)

#주제3-메뉴선택(1.학식 2.집밥 3.돈까스 4.짬뽕)

menu = int(input("점심메뉴를 선택하세요 : "))

if menu == 1:
    res = "학식"
if menu == 2:
    res = "집밥"
if menu == 3:
    res = "돈까스"
if menu == 4:
    res = "짬뽕"

print("오늘 점심은", res, "이군요 맛나게 드세요")

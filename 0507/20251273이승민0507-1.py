class question:
    #문제분해 예제1
    def Q1():
        a=2;b=5;c=10;d=20;
        x=(c+d)/(b+1)-a
        print('처음에 들판에서 놀고 있던 참새의 수 : %d'%x,'마리')


    #문제 2 - 수련의 개수는?
    def Q2():
        a, b, c, d = 1/3, 1/5, 1/6, 1/4
        t = 6
        x=round(t/(1-(a-b-c-d)))
        print(x)

    #문제 3 - 몇마리 파리가 잡아먹혔을까까
    def Q3():
        x = int(input('두꺼비가 잡아먹은 파리 수 입력 : '))
        a=x
        f=x//2 #정수형 결과 나오도록 계산 - 개구리
        b=f//5 #잠자리
        c=b*5 #암닭
        r = x+f+b+c
        print('잡아먹힌 파리의 수는? : ', r)



question_input = input('실행시킬 문제를 입력하세요 : ')
try:
    method = getattr(question, f"Q{question_input}")
    method()
except AttributeError:
    print("잘못된 입력입니다")

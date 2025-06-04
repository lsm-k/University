#모듈이란? 기능별로 여러 함수를 모아놓은 파일을 의미한다.

#절댓값 구하는 함수

class my_Math():
    def abs(x):
        if x > 0:
            return x
        else:
            return -x
    
    #재귀함수중 대표 팩토리얼 함수
    def fact(n):
        if n == 0:
            return 1
        else:
            return n*my_Math.fact(n-1)
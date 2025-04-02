#자동판매기 프로그램

object_price = int(input("물건값을 입력하시오 : "))

#지폐, 동전 개수 입력
won_1000 = int(input("1000원짜리의 개수 : "))
won_500 = int(input("500원짜리의 개수 : "))
won_100 = int(input("100원짜리의 개수 : "))

#받은 돈 계산
print("받은 돈 : ", won_1000*1000 + won_500*500 + won_100*100)
object_price = won_1000*1000 + won_500*500 + won_100*100 - object_price

#단위 계산
won_1000 = object_price//1000
won_500 = (object_price - won_1000*1000)//500
won_100 = (object_price - won_1000*1000 - won_500*500)//100
won_10 = (object_price - won_1000*1000 - won_500*500 - won_100*100)//10
won_1 = object_price - won_1000*1000 - won_500*500 - won_100*100 - won_10*10

#거스름돈 출력
print("거스름돈 : ", object_price)
print("1000원 : ", won_1000)
print("500원 : ",won_500)
print("100원 : ",won_100)
print("10원 : ",won_10)
print("1원 : ",won_1)

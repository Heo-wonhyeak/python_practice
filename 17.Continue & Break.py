# continue : 명령문을 실행시키지 않고 다음으로 반복함 
# break : 해당 반복문은 무조건 탈출!(종료)
# absent = [2, 5] # 결석
# no_book = [7, 9] # 책을 안가져옴
# for student in range(1, 11): #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     if student in absent: # 결석했다면
#         continue # 패스하고(뛰어넘고) 반복
#     elif student in no_book:
#         print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(student))
#         break # 종료!
#     print("{0}, 책을 읽어봐".format(student))

'''
    Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
    50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

    조건1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해집니다.
    조건2 : 당신은 소요 시간 5~ 15분 사이의 승객만 매칭해야 합니다.

    (출력문 예제)
    [O] 1번째 손님 (소요시간 : 15분)
    [ ] 2번째 손님 (소요시간 : 50분)
    [O] 3번째 손님 (소요시간 : 5분)
    ...
    [O] 50번째 손님 (소요시간 : 16분)

    총 탑승 승객 : 5 분
'''
from random import * 

total_customer = 0 # 총 탑승 승객 수

for customer in range(1, 51): # 1~50명의 승객 
   time = int(random()*46+5) # time = randrange(5, 51) << 강사님 방식 
   if time >= 5 and time <= 15:
      print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
      total_customer += 1
   elif time >15 and time <= 50:
      print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer,time))
   else:
      print("시간 설정 오류")

print("\n총 탑승 승객 : {0} 분".format(total_customer))
print(abs(-5)) # 5 절대값을 반환해줌 
print(pow(4, 3)) # 64 '승'의 의미 4^3 = 64
print(max(5, 12)) # 12 최댓값
print(min(5, 12)) # 5 최솟값
print(round(3.14)) # 3 반올림
print(round(4.56)) # 5 

# math 라이브러리 안에 있는 모든 것을 이용하겠다는 의미
from math import * 
print(floor(4.99)) # 4 내림
print(ceil(3.01)) # 4 올림
print(sqrt(16)) # 4 제곱근 출력

# Random 라이브러리
from random import *
print(random()) # 0.0이상 1.0 미만의 임의의 값 생성
print(random()*10) # 0.0이상 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 0.0이상 10.0 미만의 임의의 정수 생성
print(int(random()*10) + 1) # 1이상 10 이하의 임의의 정수 생성
# 로또 값 출력
print(int(random()*45) + 1) # 1이상 45 이하의 임의의 정수 생성
print(int(random()*45) + 1) # 1이상 45 이하의 임의의 정수 생성
print(int(random()*45) + 1) # 1이상 45 이하의 임의의 정수 생성
print(int(random()*45) + 1) # 1이상 45 이하의 임의의 정수 생성
print(int(random()*45) + 1) # 1이상 45 이하의 임의의 정수 생성
print(int(random()*45) + 1) # 1이상 45 이하의 임의의 정수 생성

print(randrange(1,46)) # 1이상 46 미만의 임의의 정수 생성
print(randint(1,45)) # 1이상 45 이하의 임의의 정수 생성

'''
    Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
    월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
    아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

    조건 1: 랜덤으로 날짜를 뽑아야 함
    조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
    조건 3: 매월 1~3일은 스터디를 준비를 해야 하므로 제외

    (출력문 예제)
    오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''
from random import *

online_day1 = int(random()*25)+4
online_day2 = randrange(4,29)
online_day3 = randint(4,28)
offline_day = randint(4,28)

print("온라인 스터디 모임 첫째 날짜는 매월 "+str(online_day1)+" 일로 선정되었습니다.")
print("온라인 스터디 모임 둘쨰 날짜는 매월 "+str(online_day2)+" 일로 선정되었습니다.")
print("온라인 스터디 모임 셋째 날짜는 매월 "+str(online_day3)+" 일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월 "+str(offline_day)+" 일로 선정되었습니다.")
# 자료구조의 변경

# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # {'커피', '우유', '주스'} <class 'set'>

# menu = list(menu)
# print(menu, type(menu)) # ['주스', '커피', '우유'] <class 'list'>

# menu = tuple(menu)
# print(menu, type(menu)) # ('커피', '우유', '주스') <class 'tuple'>

# menu = set(menu)
# print(menu, type(menu)) # {'주스', '커피', '우유'} <class 'set'>

'''
    Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
    참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
    댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
    추첨 프로그램을 작성하시오.

    조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
    조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되, 중복 불가
    조건3 : random 모듈의 shuffle과 sample을 활용

    (출력 예제)
    -- 당첨자 발표 --
    치킨 당첨자 : 1
    커피 당첨자 : [2, 3, 4]
    -- 축하합니다 --

'''

from random import *

# case 1
# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(id)
# print(id)
# chicken = id[0]
# print(chicken)
# coffee = id[1:4]
# print(coffee)

# print("-- 당첨자 발표 --\n치킨 당첨자 : {0}\n커피 당첨자 : {1}\n-- 축하합니다 --".format(chicken,coffee))

# case 2
# id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
id = range(1, 21) # 1~20 까지의 숫자를 생성
id = list(id) # 레인지를 리스트로 변경 
shuffle(id)
print(id)

chicken = sample(id,1)
print(chicken)
int_chicken = chicken[0]
print(int_chicken)
id.remove(int_chicken)
print(id)
coffee = sample(id,3)
print("coffee :: " ,coffee)

print("-- 당첨자 발표 --\n치킨 당첨자 : {0}\n커피 당첨자 : {1}\n-- 축하합니다 --".format(int_chicken,coffee))
# 지역변수 : 함수 내에서만 호출 가능
# 전역변수 : 프로그램내에서 어디서든 호출 가능 

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     # gun = 20 # 지역 변수 
#     global gun # 전역 공간에 있는 gun 사용하겠다는 의미 
#     # 하지만 일반적으로는 변수로 받아서 사용함 
#     gun = gun - soldiers # 경계 근무 나간 군인의 숫자
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers # 여기서 는 함수내 지역 변수임
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun # 이렇게 바깥쪽으로 return 해줘야 바깥에서 사용가능 

# print("[전역]전체 총 : {0}".format(gun))
# checkpoint(2)
# print("[전역]남은 총 : {0}".format(gun))

# gun = checkpoint_ret(gun,4)
# print("[전역]남은 총 : {0}".format(gun))

'''
    Quiz) 표준 체중을 구하는 프로그램을 작성하시오

    * 표준 체중 : 각 개인의 키에 적당한 체중

    (성별에 따른 공식)
    남자 : 키(m) * 키(m) * 22
    여자 : 키(m) * 키(m) * 21

    조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수 명 : std_weight
        * 전달 값 : 키(height), 성별(gender)
    조건 2 : 표준 체중은 소수점 둘째자리까지 표시

    (출력 예제)
    키 175cm 남자의 표준 체중은 67.38kg 입니다.
'''

def std_weight(height, gender):
    if gender == 1:
        weight = height/100 * height/100 * 22
        gender = "남자"
        return height, round(weight, 2) , gender
    elif gender == 2:
        weight = height/100 * height/100 * 21
        gender = "여자"
        return height, round(weight, 2) , gender
    
height = 175
gender = 1
weight = 0

height, weight, gender = std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

height = 160
gender = 2
weight = 0
height, weight, gender = std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
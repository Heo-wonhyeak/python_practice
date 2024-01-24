# 애완동물을 소개해 주세요~
# print("우리집 강아지의 이름은 연탄이")
# print("연탄이는 4살이며, 산책을 아주 좋아해요")
# print("연탄이는 어른일까요? True")

# # 연탄이 -> 해피로 이름 변경
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = (age >= 3)

# print("우리집 "+animal+"의 이름은 "+name)
# # 정수형을 문자와 결합할 경우 str() 으로 감싸준다
# print(name+"는 "+str(age)+"살이며, "+hobby+"을 아주 좋아해요")
# # boolean형을 문자와 결합할 경우 str() 으로 감싸준다
# print(name+"는 어른일까요? "+str(is_adult))

# # 정수형이나 boolean을 결합할 경우,를 입력하면 str()로 감싸지 않아도 되지만, 마지막에 빈칸이 하나 추가된다
# print(name,"는 ",age,"살이며, "+hobby+"을 아주 좋아하는데 어른인가요?",is_adult)

''' 
    여러 문장 주석 
    처리 방법 = 앞,뒤로 작은따옴표 3개씩
'''

# Quiz) 변수를 이용하여 다음 문장을 출력하시오

# 변수명 : station
# 변수값 : 사당,신도림,인천공항 순서대로 입력

# 출력 문장 : XX 행 열차가 들어오고 있습니다.

station = "사당"

print(station+" 행 열차가 들어오고 있습니다.")

station = "신도림"

print(station,"행 열차가 들어오고 있습니다.")

station = "인천공항"

print(station,"행 열차가 들어오고 있습니다.")
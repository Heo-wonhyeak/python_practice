# 분기(if)

weather = "비"
'''
     if 조건문:
        실행 명령문
        elif 다음 조건문:
            실행 명령문
        ... elif 다수 가능
        else:
            모든 조건이 다를때 실행 명령문
'''

if weather == "비" :
    print("우산을 챙기세요") # 우산을 챙기세요

if weather == "맑음" :
    print("화창한 날씨입니다.") # 조건이 일치하지 않으므로 아무것도 출력되지 않음


weather = "미세먼지"

if weather == "비" :
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비할 필요가 없어요")
# 미세먼지 조건에 맞으므로 :: 마스크를 챙기세요
    
weather = "맑음"

if weather == "비" :
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비할 필요가 없어요")
# 모든 조건이 다르므로 :: 준비할 필요가 없어요
    
# input으로 입력 받아서 변수 넣기
weather = input("오늘 날씨는 어때요?")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비할 필요가 없어요")
#    입력하는 내용에 따라 print 내용이 달라짐 

# input case2
temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 10<= temp and 30 > temp:
    print("좋은 기온이네요")
elif 0 <= temp and 10 > temp:
    print("약간 쌀쌀하네요")
else:
    print("너무 추우니 나가지마세요~")
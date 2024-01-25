# 탈출 문자

# \n : 줄바꿈
print("백문의 불여일견 \n백견이 불여일타")

# \" : 큰 따옴표 넣기 위해
# \' : 작은 따옴표 넣기 위해
print("저는 \"허원혁\"입니다.")
print('저는 \'허원혁\'입니다.')

# \\ : 역 슬래시를 넣기 위해 ==> 하나의 역 슬래시만 나옴
# 경로 출력에 많이 사용됨
print("C:\\Users\\USER\\Desktop\\phython_project\\phython_workspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple => Red Apple 에서 커서가 앞으로가서 한문자씩 없애면서 타이핑이 추가됨

# \d : 백스페이스 (한 글자 삭제)
print("Redd\b Apple") # Red Apple

# \t : 탭
print("Red\tApple") # Red   Apple

'''
    Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

    ex) http://naver.com
    규칙1 : http:// 부분은 제외 --> naver.com
    규칙2 : 처음만나는 점(.) 이후 부분은 제외 => naver
    규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 개수 + "!"로 구성

    ex) 생성된 비밀번호 : nav51!
'''

url = "http://naver.com"
url_rule1 = url.replace("http://","")
# print("url_rule1 :: "+url_rule1)
url_rule2 = url_rule1[:(url_rule1.find("."))]
# print("url_rule2 :: "+url_rule2)
password = url_rule2[:3] + str(len(url_rule2)) + str(url_rule2.count("e")) + "!"

print("{1}의 비밀번호 :: {0}".format(password,url))

url = "http://google.com"
url_rule1 = url.replace("http://","")
# print("url_rule1 :: "+url_rule1)
url_rule2 = url_rule1[:(url_rule1.index("."))]
# print("url_rule2 :: "+url_rule2)
password = url_rule2[:3] + str(len(url_rule2)) + str(url_rule2.count("e")) + "!"

print("{1}의 비밀번호 :: {0}".format(password,url))

url = "http://daum.net"
url_rule1 = url.replace("http://","")
# print("url_rule1 :: "+url_rule1)
url_rule2 = url_rule1[:(url_rule1.find("."))]
# print("url_rule2 :: "+url_rule2)
password = url_rule2[:3] + str(len(url_rule2)) + str(url_rule2.count("e")) + "!"

print("{1}의 비밀번호 :: {0}".format(password,url))
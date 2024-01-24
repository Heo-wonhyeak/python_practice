# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 출력
print(python.upper()) # 모두 대문자로 출력
print(python[0].isupper()) # 첫번째 문자가 대문자인가?
print(len(python)) # 문자열의 길이 반환
print(python.replace("Python","Java")) # Python을 Java로 변경

index = python.index("n") # n은 어딨는지 위치 찾기
print(index)
index = python.index("n", index + 1) # 뒤에 표기한 자리 이후로 잇는 n의 위치 찾기
print(index)

print(python.find("n")) # 5
print(python.find("Java")) # -1
# print(python.index("Java")) # error 후 종료

print(python.count("n")) # 2
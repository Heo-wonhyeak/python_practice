# 표준 출력
# print("Python", "Java") # Python Java
# print("Python"+ "Java") # PythonJava
# print("Python","Java", sep=",") # Python,Java
# print("Python", "Java", "JavaScript", sep=" vs ") # Python vs Java vs JavaScript

# print("Python","Java", sep=",", end="?") # end 를 지정함으로써 줄 바꿈이 일어나지 않음 default 값이 \n
# print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요?

# import sys
# print("Python", "Java", file=sys.stdout) # Python Java 
# print("Python", "Java", file=sys.stderr) # Python Java
# 동일한 값처럼 보이지만 stdout == 표준 출력 / stderr == 표준 에러

# 시험 성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # items : key/value가 페어로(튜플로) 나옴 
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) 8공간을 만들고 좌측 정렬 # rjust 4공간을 확보후 우측 정렬

# # 은행 대기 순번표
# # 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : "+ str(num).zfill(3)) # zfill : 값이 없는 빈 공간은 0으로 채워라!

# 표준입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자 입력을 받게 된다면 숫자를 입력해도 str로 나옴(string)
print("입력하신 값은 : "+answer+" 입니다.")
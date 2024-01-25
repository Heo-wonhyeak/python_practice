# 반복문 

# for
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")

for wating_no in [0, 1, 2, 3]:
    print("대기번호 : {0}".format(wating_no+1))

# random - randrange 와 유사하게 range 함수를 사용 
for wating_no in range(4):
    print("대기번호 : {0}".format(wating_no+1))

for wating_no in range(1, 5):
    print("대기번호 : {0}".format(wating_no))    

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("{0}님, 커피는 폐기 처분 되었습니다".format(customer))

customer = "아이언맨"
index = 1
while True:
    print("{0}님, 커피가 준비되었습니다.{1}".format(customer,index))
    index += 1
    ### 무한루프 종료시 ctrl + c

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("성함이 어떻게 되시나요? : ")

# 한줄 for 문
# 출석 번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)
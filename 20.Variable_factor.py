# 가변인자를 이용한 함수 호출

# def profile(name, age, lang1, lang2="N/A", lang3="N/A", lang4="N/A", lang5="N/A"):
#     print("이름 : {0}\t나이 : {1}".format(name,age), end=" ") # end=" " 줄 바꿈을 하지 않고 한칸 띄워진 상태로 다음 print문 실행
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("허원혁", 30, "Phython", "Java") # 이름 : 허원혁   나이 : 30 Phython Java N/A N/A N/A
# profile("박지은", 25, "Phython", "Java", "Kotlin", "Swift", "C") # 이름 : 박지은   나이 : 25 Phython Java Kotlin Swift C


def profile(name, age, *language): # *language == 넣고싶은 만큼 계속 추가 가능 
    print("이름 : {0}\t나이 : {1}".format(name,age), end=" ") # end=" " 줄 바꿈을 하지 않고 한칸 띄워진 상태로 다음 print문 실행
    for lang in language:
        print(lang, end=" ")
    print()

profile("허원혁", 30, "Phython", "Java") # 이름 : 허원혁   나이 : 30 Phython Java
profile("박지은", 25, "Phython", "Java", "Kotlin", "Swift", "C", "JavaScript") # 이름 : 박지은   나이 : 25 Phython Java Kotlin Swift C JavaScript
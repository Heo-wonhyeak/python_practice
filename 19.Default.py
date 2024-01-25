# 함수에서 기본값

def profile(name, age, main_lang): 
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))
    
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업 듣는 경우

def profile(name, age=17, main_lang="Python"): 
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석") # 이름 : 유재석   나이 : 17       주 사용 언어 : Python
profile("김태호") # 이름 : 김태호   나이 : 17       주 사용 언어 : Python
profile("박지은", 18, "자바") # 이름 : 박지은   나이 : 18       주 사용 언어 : 자바

def profile(name, age, main_lang): 
     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile(name="유재석", main_lang="파이썬", age=20) # 이름 : 유재석   나이 : 20       주 사용 언어 : 파이썬
profile(main_lang="자바", age=21, name="이지우") # 이름 : 이지우   나이 : 21       주 사용 언어 : 자바
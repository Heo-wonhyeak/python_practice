# 튜플 : 리스트완 달리 내용 변경이나 추가는 불가능함 단, 속도가 빠름
#   -> 변경되지 않는 값의 경우 사용함

menu = ("돈까스","치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# menu.add("생선까스") -- 에러 발생 : 튜플은 추가 불가 

name = "김종국"
age = 40
hobby = "쇠질"
print(name,age,hobby) # 김종국 40 쇠질

(name, age, hobby) = ("김연아", 30, "피겨")
print(name,age,hobby) # 김연아 30 피겨
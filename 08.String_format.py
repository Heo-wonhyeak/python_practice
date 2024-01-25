#문자열 포맷
print("a" + "b")
print("a","b")

# case 1
print("나는 %d살입니다." % 20) # %d 는 % 이후의 값을 넣어주는데 정수형으로만 가능
print("나는 %s를 좋아해요." %"python") # %s :: 문자열
print("Apple은 %c로 시작해요." %"A") # %c :: 캐릭터(문자 한개)
# 단, %s로 하면 모든것이 그냥 가능..
print("나는 %s살입니다." % 20)
print("Apple은 %s로 시작해요." %"A")
print("나는 %s를 %s개 먹을거에요" %("사과",2))

# case 2
print("나는 {}살입니다." .format(20))
print("나는 {}를 {}개 먹을거에요" .format("사과",2))
print("나는 {1}를 {0}개 먹을거에요" .format(2,"사과"))

# case 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age=20))

# case 4 (v3.6 이상)
age = 20
color = "파란"
print(f"나는 {age}살이며, {color}색을 좋아해요")

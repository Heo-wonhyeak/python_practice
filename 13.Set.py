# 집합(set) : 중복이 안됨, 순서가 없음

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"허원혁", "윤희노", "이정환"}
python = set(["허원혁","박지은"])

# 교집합 (java와 python을 모두 할줄 아는 개발자)
print(java&python) # {'허원혁'}
print(java.intersection(python)) # {'허원혁'}

# 합집합 (java 혹은 python을 할 수 있는 개발자)
print(java|python) # {'이정환', '박지은', '윤희노', '허원혁'}
print(java.union(python)) # {'윤희노', '허원혁', '박지은', '이정환'}

# 차집합 (java는 할줄 알지만 python은 모르는 개발자)
print(java-python) # {'윤희노', '이정환'}
print(java.difference(python)) # {'윤희노', '이정환'}

# python을 할 줄 아는 사람이 늘어남
python.add("윤희노")
print(python) # {'윤희노', '박지은', '허원혁'}

# java를 까먹음
java.remove("윤희노")
print(java) # {'이정환', '허원혁'}
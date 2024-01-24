# 사전 : key - value 형태
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # 유재석
print(cabinet[100]) # 김태호

print(cabinet.get(3)) # 유재석
# print(cabinet[5]) # 키가 없으면 오류 띄우고 종료
print(cabinet.get(5)) # None
print("hi")
print(cabinet.get(5, "값 없음")) # 값 없음

print(3 in cabinet) # 3번이라는 키가 있어서 True
print(5 in cabinet) # 5번이라는 키가 없어서 False

container = {"A-3":"허원혁", "B-100":"박지은"}
print(container["A-3"]) # 허원혁
print(container["B-100"]) # 박지은

# 새 손님 
container["C-20"] = "김나현" # C-20의 키 값으로 내용 추가
print(container) # {'A-3': '허원혁', 'B-100': '박지은', 'C-20': '김나현'}

# 손님 변경
container["C-20"] = "김한" # 이미 키 값이 있는경우 내용 업데이트
print(container) # {'A-3': '허원혁', 'B-100': '박지은', 'C-20': '김한'}

# 손님 떠남
del container["C-20"]
print(container) # {'A-3': '허원혁', 'B-100': '박지은'}

# key들만 출력
print(container.keys()) # dict_keys(['A-3', 'B-100'])

# value들만 출력
print(container.values()) # dict_values(['허원혁', '박지은'])

# key, value 쌍으로 출력
print(container.items()) # dict_items([('A-3', '허원혁'), ('B-100', '박지은')])

# 폐장
container.clear()
print(container) # {}
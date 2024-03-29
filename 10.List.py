# 리스트 [] : 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명 
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway) # [10, 20, 30]

subway = ["유재석", "조세호", "박명수"]
print(subway) # ['유재석', '조세호', '박명수']

# 조세호가 몇번째 칸에 있는가?
print(subway.index("조세호")) # 1

# 하하가 다음 정류장에서 다음 칸에 탐
subway.append("하하") # append는 항상 맨 뒤에 입력됨
print(subway) # ['유재석', '조세호', '박명수', '하하']

# 정형돈을 유재석과 조세호 사이에 태움
subway.insert(1,"정형돈") # 해당 위치에 넣고 뒤는 한칸씩 밀림
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '하하']

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop()) # 하하
print(subway) # ['유재석', '정형돈', '조세호', '박명수']

print(subway.pop()) # 박명수
print(subway) # ['유재석', '정형돈', '조세호']

print(subway.pop()) # 조세호
print(subway) # ['유재석', '정형돈']

subway.append("유재석")
print(subway) # ['유재석', '정형돈', '조세호', '박명수', '유재석']
print(subway.count("유재석")) # 2

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]
num_list.reverse()
print(num_list) # [1, 2, 3, 4, 5]

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
print(mix_list) # ['조세호', 20, True]

# 리스트 확장
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]
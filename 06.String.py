# sentence = '나는 소년입니다.'
# print(sentence)

# sentence2 = "python은 쉬워요"
# print(sentence2)

# sentence3 = """
# 난 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# 슬라이싱(substring)
jumin = "940219-1234567"

print("성별 : " + jumin[7]) # 성별 : 1
# 0번째 부터 2번 직전이 1번까지 가져온다! 
print("연 : " + jumin[0:2]) # 연 : 94 
print("월 : " + jumin[2:4]) # 월 : 02
print("일 : " + jumin[4:6]) # 일 : 19
print("생년월일 : " + jumin[0:6]) # 생년월일 : 940219
# 처음부터 값을 가져올 경우 생략 가능
print("생년월일 : " + jumin[:6]) # 생년월일 : 940219
# 주민등록 뒤 7자리 가져오기
print("뒤 7자리 : " + jumin[7:]) # 뒤 7자리 : 1234567

# 뒤에서부터 짤라오기 (뒤 7번째부터 끝까지 ==> 뒤의 첫자리가 -1[0부터 시작이 아님])
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 뒤 7자리 (뒤에서부터) : 1234567

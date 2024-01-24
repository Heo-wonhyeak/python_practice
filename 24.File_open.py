
# score_file = open("score.txt", "w", encoding="utf8") # pen(파일이름, 덮어쓰기(write), 인코딩 정보)
# print("수학 : 0", file=score_file) # 파일에 내용 입력
# print("영어 : 50", file=score_file) # 파일에 내용 입력
# score_file.close() # 파일은 반드시 종료를 해줘야함 
# '''
#     terminal에 출력되는 값은 없이 해당 폴더에 텍스트 파일이 생성됨 
# '''

# score_file = open("score.txt", "a", encoding="utf8") # pen(파일이름, 추가해서 쓰기(append), 인코딩 정보)
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100\n")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # pen(파일이름, 읽기(read), 인코딩 정보)
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8") # pen(파일이름, 읽기(read), 인코딩 정보)
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 반복문을 통해 한줄씩 읽기
# score_file = open("score.txt", "r", encoding="utf8") # pen(파일이름, 읽기(read), 인코딩 정보)
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 리스트로 모든 줄 가져오기 
score_file = open("score.txt", "r", encoding="utf8") # pen(파일이름, 읽기(read), 인코딩 정보)
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
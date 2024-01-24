# With 

# import pickle

# with open("profile.pickle", "rb") as profile_file: # profile_file이란 변수에 profile.pickle 을 불러오고
#     print(pickle.load(profile_file)) # 출력함 
# with를 사용할 경우 close()를 해주지 않아도 됨
    
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("Python을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())

'''
    Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
    보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

    - X 주차 주간 보고 -
    부서 :
    이름 :
    업무 요약 :

    1주차부터 50주차까지의 보고서 만드는 프로그램을 작성하시오.

    조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''
import os

for weekly in range(1, 51):
    directory = "weekly_folder"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, "{0}주차.txt".format(weekly)), "w", encoding="utf8") as weekly_file:
        weekly_file.write("- {0} 주차 주간 보고 -\n".format(weekly))
        weekly_file.write("부서 : \n")
        weekly_file.write("이름 : \n")
        weekly_file.write("업무 요약 : \n")

## 강사 방법
# for i in range(1, 51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간 보고 -\n".format(i))
#         report_file.write("부서 : \n")
#         report_file.write("이름 : \n")
#         report_file.write("업무 요약 : \n")
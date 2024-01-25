# 피클 : 프로그램 상에서 사용하는 데이터를 파일 형태로 저장 

import pickle

profile_file = open("profile.pickle", "wb") 
    # open(파일 이름, 쓰기(write binary)) 피클을 사용하기 위해선 binary 를 꼭 설정해야하며, encoding 정보는 넣지 않아도 됨
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "게임"]}
print(profile)
pickle.dump(profile, profile_file) # profile에있는 정보를 profile_file에 피클로 저장 
profile_file.close()

profile_file = open("profile.pickle", "rb") # open(파일 이름, 읽기(read binary))
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

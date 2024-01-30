# 모듈
'''
    import theater_module # .py 를 제외한 만들어둔 모듈 파일 명을 적어서 가져온다 

    theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격 
    theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
    theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을때 
'''

# Alias
## 별명으로 호출 가능 
'''
    import theater_module as mv

    mv.price(3)
    mv.price_morning(4)
    mv.price_soldier(5)
'''

# from import
## 별명도 입력하지 않아도 호출 가능
'''
    from theater_module import *

    price(3)
    price_morning(4)
    price_soldier(5)
'''

## 필요한 함수만 가져다가 사용 하는 방법 
'''
    from theater_module import price, price_morning
    price(3)
    price_morning(4)
'''

## 필요 함수를 별명을 지정해서 가져옴 (이 전에 만든 price와는 다름)
from theater_module import price_soldier as price
price(5) 
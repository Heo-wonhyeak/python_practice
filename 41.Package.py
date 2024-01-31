# 패키지 :: 모듈들의 집합 이라고 생각하면 쉬움
'''
    import travle.thailand
    trip_to = travle.thailand.ThailandPackage()
    trip_to.detail()
'''

'''
    from travle.thailand import ThailandPackage
    trip_to = ThailandPackage()
    trip_to.detail()
'''

'''
    from travle import vietnam
    trip_to = vietnam.VietnamPackage()
    trip_to.detail()
'''

# all 사용
# from random import *

## * 사용을 위해서는 travle 폴더 안에 __init__.py 파일을 정의 해야함 
from travle import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()

trip_to = thailand.ThailandPackage()
trip_to.detail()
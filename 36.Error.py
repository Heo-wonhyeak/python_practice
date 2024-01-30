# 예외처리 
'''
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    nums.append(num1)
    nums.append(num2)
    # nums.append(int(nums[0]/nums[1]))

    # print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 값을 잘못 입력했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print(err)
'''

## 에러 발생 시키기
    
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except ZeroDivisionError as err:
    print(err)

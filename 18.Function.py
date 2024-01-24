# 함수

# 함수는 정의한 것이고 실행은 여기서 되지 않음
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account() # 여기에서 실행됨 

def deposit(balance, money): # 입금 (잔액, 입금액) 
    print("{0}원 입금이 완료되었습니다. 잔액은 {1}원 입니다.".format(money,balance+money))
    return balance + money

def withdrow(balance, money): # 출금 (잔액, 출금액)
    if balance >= money:
        print("{0}원 출금이 완료되었습니다. 잔액은 {1}원 입니다.".format(money,balance-money))
        return balance - money
    if balance < money:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdrow_night(balance, money):
    commission = 1000 # 수수료 1000원
    if balance >= money+commission:
        print("{0}원 출금이 완료되었습니다. 수수료는 {2}원 입니다. 잔액은 {1}원 입니다.".format(money,balance-money-commission,commission))
        return commission, balance - money - commission
    if balance < money+commission:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

balance = 0
money = 10000

balance = deposit(balance, money) # 10000원 입금이 완료되었습니다. 잔액은 10000원 입니다.
print(balance) # 10000

balance = deposit(balance, money) # 10000원 입금이 완료되었습니다. 잔액은 20000원 입니다.
balance = withdrow(balance, 50000) # 출금이 완료되지 않았습니다. 잔액은 20000원 입니다.
balance = withdrow(balance, money) # 10000원 출금이 완료되었습니다. 잔액은 10000원 입니다.

balance = withdrow_night(balance, money) # 출금이 완료되지 않았습니다. 잔액은 10000원 입니다.
balance = deposit(balance, 1000) # 1000원 입금이 완료되었습니다. 잔액은 11000원 입니다.
commission, balance = withdrow_night(balance, money) # 10000원 출금이 완료되었습니다. 수수료는 1000원 입니다. 잔액은 0원 입니다.
print(commission) # 1000
print(balance) # 0
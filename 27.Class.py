# 클래스
'''
###    스타크래프트 예시 - 테란


# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린" # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 : {0}, 공격력 : {1}".format(hp,damage))

# 탱크 : 공격 유닛, 탱크, 포를 쏠수 있는데, 일반 모드 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 : {0}, 공격력 : {1}".format(tank_hp,tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]".format(name,
                                                         location,damage))
    
attack(name, "1시", damage)
attack(tank_name, "1시" , tank_damage)

'''

## 상기 주석처리한 내용을 class 로 변경

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 : {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

## __init__ (언더바언더바 이닛 언더바언더바)
# marine3 = Unit("마린") 
# marine4 = Unit("마린", 40)
'''
    init 함수에 self를 제외한 객체를 모두 입력해야지 값을 전달 받을 수 있다.
    아닌 경우 오류! 
'''

## 멤버 변수 

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력: {1}".format(wraith1.name,wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# if wraith1.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith1.name))
# else:
#     print("{0}는 현재 클로킹 상태가 아닙니다.".format(wraith1.name))
    ### 아예 clocking이라는 오브젝트가 없어서 오류가 발생함 
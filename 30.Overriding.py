# 메서드 오버라이딩

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다 [속도 : {2}]"
              .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit): ## (괄호 안에 입력한 클래스 상속)
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) # 일반유닛에서 상속받은 내용 
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"
              .format(self.name, location, self.damage))
        
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} :  현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병 
# 드랍쉽 :  공중 유닛, 수송기, 다른 지상 유닛들을 수송. 공격 불가

# 날 수 있는 기능을 가진 클래스
class Flyable:    
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"
              .format(name, location, self.flying_speed))
        
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 공중유닛은 지상의 속도가 없기 때문에 0 값을 입력 
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루져 : 공중 유닛, 체력이 좋고, 공격력이 좋음
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

## 이렇게 하면 공중 지상을 구분해야함 
vulture.move("11시")
battlecruiser.fly(battlecruiser.name,"9시")

## move로 메서드 오버라이딩 후
vulture.move("11시")
battlecruiser.move("9시")

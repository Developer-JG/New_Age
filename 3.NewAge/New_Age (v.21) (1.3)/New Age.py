from random import choice
from random import randint

import time

print("\nthe New_Age (basilisk) game project\n")


# 스토리
def story():
    print("오래전 이땅은 인간의 것이 아니였다.")
    time.sleep(1.8)
    print("개척자였던 에나가 괴물을 물리치자 평화가 찾아왔고,")
    time.sleep(2.5)
    print("이땅에 마지막으로 국가가 세워졌다.")
    time.sleep(1.8)
    print("에나의 후손은 황제가 되어 에나의 힘을 계승해 나갔지만")
    time.sleep(2.5)
    print("피가 연해질수록 괴물들을 막아내기 어려워졌다.")
    time.sleep(2.3)
    print("고대의 에나는 전설의 무기가 잘못 하용될경우를 대비하여 봉인하였지만")
    time.sleep(3)
    print("사람들은 전설의 무기를 되찾아 평화를 되찾아 평화를 되찾고자 한다.")
    time.sleep(4)
    print("\nNew_Age (새로운_시대)")

    
# 체크
def check (message, start, end):
    if message in list(map(str, range(start, end+1))):
        message = int(message)
        return message
    else:
        return message

    
# 플래이어 클래스
class Player:
    def __init__(self, name, point, equipment, inven, health, money, damage, defense, hunger, liv, exp):
        self.name = name
        self.point = point
        self.equipment = {"atk" : ["없음"], "def" : ["없음"]}
        self.inven = {"atk" : [], "def" : [], "re" : [], "food" : [], "drop" : [], "item" : []}
        self.health = health
        self.damage = damage
        self.money = money
        self.defense = defense
        self.hunger = hunger
        self.liv = liv
        self.exp = exp

    # 현재 상태 확인
    def showinfo(self):
        print("{0:=^25}".format("나의 상태"))
        if len(self.equipment['atk']) == 2 and len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][1].name} \n레벨 : {self.liv}")
        elif len(self.equipment['atk']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][0]} \n레벨 : {self.liv}")
        elif len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][0]}\n갑옷 : {self.equipment['def'][1].name} \n레벨 : {self.liv}")
        else:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][0]}\n갑옷 : {self.equipment['def'][0]} \n레벨 : {self.liv}")
    #전투 상태확인
    def m_showinfo(self):
        print("{0:=^25}".format("나의 상태"))
        if len(self.equipment['atk']) == 2 and len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage}\n방어력 : {self.defense} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][1].name} \
                    \n레벨 : {self.liv}")
        elif len(self.equipment['atk']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage}\n방어력 : {self.defense} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][0].name} \
                    \n레벨 : {self.liv}")
        elif len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage}\n방어력 : {self.defense} \
                    \n무기 : {self.equipment['atk'][0].name}\n갑옷 : {self.equipment['def'][1].name} \
                    \n레벨 : {self.liv}")
        else:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage}\n방어력 : {self.defense} \
                    \n무기 : {self.equipment['atk'][0].name}\n갑옷 : {self.equipment['def'][0].name} \
                    \n레벨 : {self.liv}")


# 메인
def main():

    try:
        import save
    except:

        #story()

        player_name = ""
        player_name = input("플레이어 이름을 입력하십시오. = ")
        while player_name == "":
            print("\n유효한 이름을 입력하십시오")
            player_name = input("플레이어 이름을 입력하십시오. = ")
            
        player_1 = Player(player_name, 1, [], [], 100, 0, 0, 0, 20, 0, 0)
        player_x = 10
        player_y = 10

        player_liv = 0

        plag = 0

    print("\n정상적으로 로그인 되었습니다.")
    print("정보 불러오는 중...")
    print("환영합니다." + player_name + "님")

    while True:

        print("\n" * 39)

        # 마을 버프
        if player_1.point == 1:
            player_1.health = player_1.health + 50
            player_1.hunger = 20
            
        # 체력,허기 최대치
        if player_1.health > 100:
            player_1.health = 100
        if player_1.hunger > 20:
            player_1.hunger = 20

        player_1.showinfo()
        
        input()

if __name__ == "__main__":
    main()
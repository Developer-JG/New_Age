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
        print(f"{'나의 상태':=^25}")
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

class Player:
    def __init__(self, name, point, equipment, inven, health, money, damage, defense, hunger, liv, exp):
        self.name = name
        self.point = point
        self.equipment = {"atk" : ["없음"], "def_1" : ["없음"], "def_2" : ["없음"], "def_3" : ["없음"], "def_4" : ["없음"]}
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
        print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                        \n방어력 : {self.defense}\n허기 : {self.hunger}")

        if len(self.equipment['atk']) == 2:
            print(f"무기 : {self.equipment['atk'][1].name}")
        else:
            print(f"무기 : {self.equipment['atk'][0]}")

        if len(self.equipment['def_1']) == 2:
            print(f"갑옷_모자 : {self.equipment['def_1'][1].name}")
        else:
            print(f"갑옷_모자 : {self.equipment['def_1'][0]}")

        if len(self.equipment['def_2']) == 2:
            print(f"갑옷_상의 : {self.equipment['def_2'][1].name}")
        else:
            print(f"갑옷_상의 : {self.equipment['def_2'][0]}")

        if len(self.equipment['def_3']) == 2:
            print(f"갑옷_하의 : {self.equipment['def_3'][1].name}")
        else:
            print(f"갑옷_하의 : {self.equipment['def_3'][0]}")

        if len(self.equipment['def_4']) == 2:
            print(f"갑옷_신발 : {self.equipment['def_4'][1].name}")
        else:
            print(f"갑옷_신발 : {self.equipment['def_4'][0]}")

        print(f"레벨 : {self.liv}")

    #전투 상태확인
    def m_showinfo(self):
        print("{0:=^25}".format("나의 상태"))
        print(f"{'나의 상태':=^25}")
        if len(self.equipment['atk']) == 2 and len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage}\n방어력 : {self.defense}")

            if len(self.equipment['atk']) == 2:
                print(f"무기 : {self.equipment['atk'][1].name}")
            else:
                print(f"무기 : {self.equipment['atk'][0]}")

            if len(self.equipment['def_1']) == 2:
                print(f"갑옷_모자 : {self.equipment['def_1'][1].name}")
            else:
                print(f"갑옷_모자 : {self.equipment['def_1'][0]}")

            if len(self.equipment['def_2']) == 2:
                print(f"갑옷_상의 : {self.equipment['def_2'][1].name}")
            else:
                print(f"갑옷_상의 : {self.equipment['def_2'][0]}")

            if len(self.equipment['def_3']) == 2:
                print(f"갑옷_하의 : {self.equipment['def_3'][1].name}")
            else:
                print(f"갑옷_하의 : {self.equipment['def_3'][0]}")

            if len(self.equipment['def_4']) == 2:
                print(f"갑옷_신발 : {self.equipment['def_4'][1].name}")
            else:
                print(f"갑옷_신발 : {self.equipment['def_4'][0]}")

            print(f"레벨 : {self.liv}")
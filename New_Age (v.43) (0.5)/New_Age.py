from random import choice
from random import randint
import time

print("\nthe New_Age (basilisk) game project\n")


higt_health = 60

# 스토리
def story():
    print("오래전 이땅은 인간의 것이 아니었다.")
    time.sleep(1.8)
    print("개척자가 흑룡의 힘으로 괴물들을 물리치자 평화가 찾아왔고,")
    time.sleep(2.3)
    print("처음이자 마지막으로 이 땅에 제국이 세워졌다.")
    time.sleep(1.8)
    print("개척자의 후손들은 황제가 되어 흑룡의 힘을 계승해나갔지만,")
    time.sleep(2.3)
    print("그들은 개척자의 피가 연해질수록 흑룡의 광기를 감당하지 못했다.")
    time.sleep(2.4)
    print("흑룡에 잡힌 황제는 폭정을 일삼았고,")
    time.sleep(1.8)
    print("그것을 참지 못한 4명의 영웅이 일어났다.")
    time.sleep(1.8)
    print("미노아, 디카이온, 시포니아, 네메시스")
    time.sleep(1.5)
    print("그들은 각각 주작, 백호, 청룡, 현무의 힘을 이용하여 황제를 물리쳤고,")
    time.sleep(2.6)
    print("이 세계는 잠깐의 평화를 되찾았다.")
    time.sleep(1.8)
    print("인간들은 강력한 힘인 흑룡과 사신수가 잘못 사용될 경우를 염려하여 봉인하였고,")
    time.sleep(2.8)
    print("사신수와 흑룡의 가호가 약해진 틈을 타고 잊혀 있던 고대 괴물들이 깨어나")
    time.sleep(2.6)
    print("이 세계는 다시 혼란에 휩싸였다.")
    time.sleep(1.5)
    print("그리하여 이 세계는 다시 한번 영웅을 필요로 한다.")
    time.sleep(4)
    print("\nNew_Age (새로운_시대)\n")

# 체크
def check (message, start, end):
    if message in list(map(str, range(start, end + 1))):
        message = int(message)
        return message
    else:
        return message

# 플레이어 클래스
class Player:
    def __init__(self, name, point, equipment, inven, health, money, damage, critical, defense, liv, exp):
        self.name = name
        self.point = point
        self.equipment = {"atk": ["없음"], "def_1": ["없음"], "def_2": ["없음"], "def_3": ["없음"], "def_4": ["없음"]}
        self.inven = {"atk": [], "def": [], "re": [], "month": [], "item": []}
        self.health = health
        self.money = money
        self.damage = damage
        self.critical = critical
        self.defense = defense
        self.liv = liv
        self.exp = exp

    # 현재 상태 확인
    def showinfo(self):
        print("{0:=^25}".format("나의 상태"))
        print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                        \n방어력 : {self.defense}\n레벨 : {self.liv}")

    # 전투 상태확인
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

    # 장착보기
    def atk_def_inventory(self):
        if len(self.equipment['atk']) == 2:
            print(f"무기 : {self.equipment['atk'][1].name}")
        else:
            print(f"무기 : {self.equipment['atk'][0]}")

        if len(self.equipment['def_1']) == 2:
            print(f"갑옷_투구 : {self.equipment['def_1'][1].name}")
        else:
            print(f"갑옷_투구 : {self.equipment['def_1'][0]}")

        if len(self.equipment['def_2']) == 2:
            print(f"갑옷_갑옷 : {self.equipment['def_2'][1].name}")
        else:
            print(f"갑옷_갑옷 : {self.equipment['def_2'][0]}")

        if len(self.equipment['def_3']) == 2:
            print(f"갑옷_바지 : {self.equipment['def_3'][1].name}")
        else:
            print(f"갑옷_바지 : {self.equipment['def_3'][0]}")

        if len(self.equipment['def_4']) == 2:
            print(f"갑옷_신발 : {self.equipment['def_4'][1].name}")
        else:
            print(f"갑옷_신발 : {self.equipment['def_4'][0]}")


# 흰색 (노말) 무기 아이템 클래스
class W_atk_item:
    def __init__(self, name, damage, cost, liv, need_power_stats, need_agility_stats, need_adventure_stats, critical, physical_absorption, use):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.liv = liv
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.use = use


# 보라색 (에픽) 무기 아이템 클래스
class P_atk_item:
    def __init__ (self, name, damage, liv, critical, physical_absorption, use):
        self.name = name
        self.damage = damage
        self.liv = liv
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.use = use


# 빨간색 (레전드) 렉스의 명작 아이템 클래스
class R_r_atk_item:
    def __init__(self, name, damage, need_power_stats, need_agility_stats, need_adventure_stats, critical, physical_absorption, use):
        self.name = name
        self.damage = damage
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.use = use


# 빨간색 (레전드) 사신수 무기 아이템 클래스
class R_s_atk_item:
    def __init__(self, name, damage, liv, need_power_stats, need_agility_stats, need_adventure_stats, critical, physical_absorption, use):
        self.name = name
        self.damage = damage
        self.liv = liv
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.use = use


# 저주받은 빨간색 (레전드) 흑룡 무기 아이템 클래스
class R_b_atk_item:
    def __init__(self, name, damage, liv, critical, use):
        self.name = name
        self.damage = damage
        self.liv = liv
        self.critical = critical
        self.use = use


# 선과 악 아이템 클래스
class g_e_atk_item:
    def __init__(self, name, damage, critical, physical_absorption, use):
        self.name = name
        self.damage = damage
        self.liv = liv
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.use = use


# 흰색 (노말) 방어구 아이템 클래스
class W_def_item:
    def __init__(self, name, defense, cost, part, liv, need_power_stats, need_agility_stats, need_adventure_stats, plus_power_stats, plus_agility_stats, plus_health, use):
        self.name = name
        self.defense = defense
        self.cost = cost
        self.part = part
        self.liv = liv
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.plus_health = plus_health
        self.use = use


# 보라색 (에픽) 방어구 아이템 클래스
class  P_def_item:
    def __init__ (self, name, defense, liv, part, need_power_stats, need_agility_stats, need_adventure_stats, use):
        self.name = name
        self.defense = defense
        self.liv = liv
        self.part = part
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.use = use


# 빨간색 (레전드) 렉스의 명작 아이템 클래스
class R_r_def_item:
    def __init__(self, name, defense, part, need_power_stats, need_agility_stats, need_adventure_stats, plus_power_stats, plus_agility_stats, plus_adventure_stats, use):
        self.name = name
        self.defense = defense
        self.part = part
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.plus_adventure_stats = plus_adventure_stats
        self.use = use

# 빨간색 (레전드) 사흉수 갑주 아이템 클래스
class R_s_def_item:
    def __init__(self, name, defense, part, liv, plus_power_stats, plus_agility_stats, plus_adventure_stats, use):
        self.name = name
        self.defense = defense
        self.liv = liv
        self.part = part
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.plus_adventure_stats = plus_adventure_stats
        self.use = use


# 저주받은 빨간색 (레전드) 흑룡의 갑주 아이템 클래스
class R_d_def_item:
    def __init__(self, name, defense, part, liv, plus_power_stats, plus_agility_stats, plus_adventure_stats, use):
        self.name = name
        self.defense = defense
        self.liv = liv
        self.part = part
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.plus_adventure_stats = plus_adventure_stats
        self.use = use


# 강화서 아이템 클래스
class fortification_item:
    def __init__(self, name, cost, use_effect):
        self.name = name
        self.cost = cost
        self.use_effect = use_effect


# 회복 아이템 클래스
class Re_item:
    def __init__(self, name, recovery, cost, count, use):
        self.name = name
        self.recovery = recovery
        self.cost = cost
        self.count = count
        self.use = use


# 일반 아이템 클래스
class nomal_item:
    def __init__(self, name, count, use):
        self.name = name
        self.count = count
        self.use = use


# 일반 판매 아이템 클래스
class nomal_item_shop:
    def __init__(self, name, count, cost, use):
        self.name = name
        self.count = count
        self.cost = cost
        self.use = use


# 요구스텟 : 힘 : 민첩 : 모험

# 1월의 기억으로 구매
W_atk_item_101 = W_atk_item("검", 2, 15, 1, 0, 0, 0, 0, 0, "atk")
W_atk_item_102 = W_atk_item("몽둥아", 2, 15, 1, 0, 0, 0, 0, 0, "atk")
W_atk_item_103 = W_atk_item("철검", 13, 30, 5, 0, 0, 0, 0, 0, "atk")
W_atk_item_104 = W_atk_item("도끼", 13, 30, 5, 0, 0, 0, 0, 0, "atk")
W_atk_item_105 = W_atk_item("예리한 대검", 30, 65, 10, 0, 0, 0, 0, 0, "atk")
W_atk_item_106 = W_atk_item("예리한 도끼", 30, 65, 10, 0, 0, 0, 0, 0, "atk")
# 2월의 기억으로 구매
W_atk_item_201 = W_atk_item("반짝이는 검", 45, 25, 15, 40, 0, 0, 0, 0, "atk")  # 40 : 0 : 0
W_atk_item_202 = W_atk_item("반짝이는 도끼", 45, 25, 15, 20, 0, 20, 0, 45, "atk")  # 20 : 0 : 20 +체력흡수 45
W_atk_item_203 = W_atk_item("강철 단검", 35, 20, 15, 0, 40, 0, 6, 0, "atk")  # 0 : 40 : 0 +크리티컬 6%
W_atk_item_204 = W_atk_item("무쇠 건틀릿", 45, 25, 15, 20, 20, 0, 0, 0, "atk")  # 20 : 20 : 0
W_atk_item_205 = W_atk_item("푸른 방패", 35, 20, 15, 0, 0, 20, 0, 0, "atk")  # 0 : 0 : 40 +체력흡수 100
W_atk_item_206 = W_atk_item("붉은 검", 70, 40, 20, 60, 0, 20, 0, 0, "atk")  # 60 : 0 : 20
W_atk_item_207 = W_atk_item("붉은 도끼", 63, 40, 20, 30, 0, 30, 0, 0, "atk")  # 30 : 0 : 30 +체력흡수 63
W_atk_item_208 = W_atk_item("붉은 단검", 59, 40, 20, 0, 60, 0, 15, 63, "atk")  # 0 : 60 : 0 +체력흡수 63 +크리티컬 15%
W_atk_item_209 = W_atk_item("강철 방패", 49, 50, 20, 0, 0, 60, 0, 98, "atk")  # 0 : 0 : 60 +체력흡수 98
# 3월의 기억으로 구매
W_atk_item_301 = W_atk_item("칠흑의 검", 90, 40, 25, 70, 0, 0, 0, 0, "atk")  # 70 : 0 : 0
W_atk_item_302 = W_atk_item("흑백의 도끼", 81, 40, 25, 35, 0, 35, 0, 41, "atk")  # 35 : 0 : 35 +체력흡수 41
W_atk_item_303 = W_atk_item("거북의 방패", 63, 30, 25, 0, 0, 70, 0, 126, "atk")  # 0 : 0 : 70 +체력흡수 126
W_atk_item_304 = W_atk_item("푸른 불꽃검", 110, 50, 30, 90, 0, 0, 0, 0, "atk")  # 90 : 0 : 0
W_atk_item_305 = W_atk_item("악마 도끼", 99, 50, 30, 45, 0, 45, 0, 50, "atk")  # 45 : 0 : 45 +체력흡수 50
W_atk_item_306 = W_atk_item("순백의 방패", 77, 50, 30, 0, 0, 90, 0, 154, "atk")  # 0 : 0 : 90 +체력흡수 154
# 4월의 기억으로 구매
W_atk_item_401 = W_atk_item("은빛 하늘검", 130, 40, 35, 100, 0, 90, 0, 0,"atk")  # 100 : 0 : 0
W_atk_item_402 = W_atk_item("금빛 하늘검", 160, 50, 40, 120, 0, 45, 0, 0,"atk")  # 120 : 0 : 45
W_atk_item_403 = W_atk_item("자연의 일부", 144, 50, 40, 60, 0, 60, 0, 144,"atk")  # 60 : 0 : 60 +체력흡수 144


W_def_item_001 = W_def_item("가죽 갑옷",1,0,2,1,0,0,0,0,0,0,"def")
W_def_item_001 = W_def_item("가죽 신발",1,0,4,1,0,0,0,0,0,0,"def")
# 1월의 기억으로 구매
W_def_item_111 = W_def_item("녹슨 철 투구",5,15,1,10,0,0,0,0,0,0,"def")
W_def_item_112 = W_def_item("녹슨 철 갑옷",5,15,2,10,0,0,0,0,0,0,"def")
W_def_item_113 = W_def_item("녹슨 철 바지",5,15,3,10,0,0,0,0,0,0,"def")
W_def_item_114 = W_def_item("녹슨 철 신발",5,15,4,10,0,0,0,0,0,0,"def")
# 2월의 기억으로 구매
W_def_item_211 = W_def_item("힘의 철 투구",20,20,1,20,50,0,0,5,0,0,"def") # 힘 + 5 / 요구 힘 : 50
W_def_item_212 = W_def_item("힘의 철 갑옷",20,20,2,20,50,0,0,5,0,0,"def")
W_def_item_213 = W_def_item("힘의 철 바지",20,20,3,20,50,0,0,5,0,0,"def")
W_def_item_214 = W_def_item("힘의 철 신발",20,20,4,20,50,0,0,5,0,0,"def")
W_def_item_221 = W_def_item("민첩의 철 투구",15,22,1,20,0,50,0,0,5,0,"def") # 민첩 + 5 / 요구 민첩 : 50
W_def_item_222 = W_def_item("민첩의 철 갑옷",15,22,2,20,0,50,0,0,5,0,"def")
W_def_item_223 = W_def_item("민첩의 철 바지",15,22,3,20,0,50,0,0,5,0,"def")
W_def_item_224 = W_def_item("민첩의 철 신발",15,22,4,20,0,50,0,0,5,0,"def")
W_def_item_231 = W_def_item("모험의 철 투구",30,22,1,20,0,0,50,0,0,50,"def") # 추가 체력 + 50 / 요구 모험 : 50
W_def_item_232 = W_def_item("모험의 철 갑옷",30,22,2,20,0,0,50,0,0,50,"def")
W_def_item_233 = W_def_item("모험의 철 바지",30,22,3,20,0,0,50,0,0,50,"def")
W_def_item_234 = W_def_item("모험의 철 신발",30,22,4,20,0,0,50,0,0,50,"def")
# 3월의 기억으로 구매
W_def_item_311 = W_def_item("힘의 적표범 투구",30,22,1,30,85,0,0,10,0,0,"def") # 힘 + 10 / 요구 힘 : 85
W_def_item_312 = W_def_item("힘의 적표범 갑옷",30,22,2,30,85,0,0,10,0,0,"def")
W_def_item_313 = W_def_item("힘의 적표범 바지",30,22,3,30,85,0,0,10,0,0,"def")
W_def_item_314 = W_def_item("힘의 적표범 신발",30,22,4,30,85,0,0,10,0,0,"def")
W_def_item_321 = W_def_item("민첩의 적표범 투구",20,22,1,30,0,85,0,0,20,0,"def") # 민첩 + 20 / 요구 민첩 : 85
W_def_item_322 = W_def_item("민첩의 적표범 갑옷",20,22,2,30,0,85,0,0,20,0,"def")
W_def_item_323 = W_def_item("민첩의 적표범 바지",20,22,3,30,0,85,0,0,20,0,"def")
W_def_item_324 = W_def_item("민첩의 적표범 신발",20,22,4,30,0,85,0,0,20,0,"def")
W_def_item_331 = W_def_item("모험의 적표범 투구",40,22,1,30,0,0,85,0,0,100,"def") # 추가체력 + 100 / 요구 모험 : 85
W_def_item_332 = W_def_item("모험의 적표범 갑옷",40,22,2,30,0,0,85,0,0,100,"def")
W_def_item_333 = W_def_item("모험의 적표범 바지",40,22,3,30,0,0,85,0,0,100,"def")
W_def_item_334 = W_def_item("모험의 적표범 신발",40,22,4,30,0,0,85,0,0,100,"def")
# 4월의 기억으로 구매
W_def_item_411 = W_def_item("힘의 칠흑 투구",50,25,1,40,120,0,0,15,0,0,"def") # 힘 + 15 / 요구 힘 : 120
W_def_item_412 = W_def_item("힘의 칠흑 갑옷",50,25,2,40,120,0,0,15,0,0,"def")
W_def_item_413 = W_def_item("힘의 칠흑 바지",50,25,3,40,120,0,0,15,0,0,"def")
W_def_item_414 = W_def_item("힘의 칠흑 신발",50,25,4,40,120,0,0,15,0,0,"def")
W_def_item_421 = W_def_item("민첩의 칠흑 투구",25,25,1,40,0,120,0,0,35,0,"def") # 민첩 + 35 / 요구 민첩 : 120
W_def_item_422 = W_def_item("민첩의 칠흑 갑옷",25,25,2,40,0,120,0,0,35,0,"def")
W_def_item_423 = W_def_item("민첩의 칠흑 바지",25,25,3,40,0,120,0,0,35,0,"def")
W_def_item_424 = W_def_item("민첩의 칠흑 신발",25,25,4,40,0,120,0,0,35,0,"def")
W_def_item_431 = W_def_item("모험의 칠흑 투구",70,25,1,40,0,0,120,0,0,200,"def") # 추가체력 + 200 / 요구 모험 : 120
W_def_item_432 = W_def_item("모험의 칠흑 갑옷",70,25,2,40,0,0,120,0,0,200,"def")
W_def_item_433 = W_def_item("모험의 칠흑 바지",70,25,3,40,0,0,120,0,0,200,"def")
W_def_item_434 = W_def_item("모험의 칠흑 신발",70,25,4,40,0,0,120,0,0,200,"def")
# 5월의 기억으로 구매
W_def_item_511 = W_def_item("힘의 기사 투구",70,30,1,50,150,0,0,30,0,0,"def") # 힘 + 30 / 요구 힘 : 150
W_def_item_512 = W_def_item("힘의 기사 갑옷",70,30,2,50,150,0,0,30,0,0,"def")
W_def_item_513 = W_def_item("힘의 기사 바지",70,30,3,50,150,0,0,30,0,0,"def")
W_def_item_514 = W_def_item("힘의 기사 신발",70,30,4,50,150,0,0,30,0,0,"def")
W_def_item_521 = W_def_item("민첩의 기사 투구",50,30,1,50,0,150,0,0,60,0,"def") # 민첩 + 60 / 요구 민첩 : 150
W_def_item_522 = W_def_item("민첩의 기사 갑옷",50,30,2,50,0,150,0,0,60,0,"def")
W_def_item_523 = W_def_item("민첩의 기사 바지",50,30,3,50,0,150,0,0,60,0,"def")
W_def_item_524 = W_def_item("민첩의 기사 신발",50,30,4,50,0,150,0,0,60,0,"def")
W_def_item_531 = W_def_item("모험의 기사 투구",100,30,1,50,0,0,150,0,0,400,"def") # 추가체력 + 400 / 요구 모험 : 150
W_def_item_532 = W_def_item("모험의 기사 갑옷",100,30,2,50,0,0,150,0,0,400,"def")
W_def_item_533 = W_def_item("모험의 기사 바지",100,30,3,50,0,0,150,0,0,400,"def")
W_def_item_534 = W_def_item("모험의 기사 신발",100,30,4,50,0,0,150,0,0,400,"def")




# 50레벨 퀘스트 아이템
P_atk_item_501 = P_atk_item("불완전한 홍염의 날갯깃",320,50,30,150,"atk")

P_def_item_611 = P_def_item("부서진 핀그리드의 투구",75,50,1,20,20,20,"def")
P_def_item_612 = P_def_item("부서진 핀그리드의 갑옷",75,50,2,20,20,20,"def")
P_def_item_613 = P_def_item("부서진 핀그리드의 바지",75,50,3,20,20,20,"def")
P_def_item_614 = P_def_item("부서진 핀그리드의 신발",75,50,4,20,20,20,"def")


# 렉스의 명작
R_atk_item_601 = R_r_atk_item("렉스의 1번째 명작 '홍염의 날개깃'",250,70,70,70,10,300,"atk")
R_atk_item_602 = R_r_atk_item("렉스의 2번째 명작 '칼날 그림자'",100,140,0,0,70,0,"atk")
R_atk_item_603 = R_r_atk_item("렉스의 3번째 명작 '녹색 이빨'",4,0,0,0,0,0,"atk")
R_atk_item_604 = R_r_atk_item("렉스의 4번째 명작 '붉은 손아귀'",50,20,20,0,10,0,"atk")
R_atk_item_605 = R_r_atk_item("렉스의 5번째 명작 '인어의 검'",60,60,0,50,0,200,"atk")
R_atk_item_606 = R_r_atk_item("렉스의 6번째 명작 '불굴의 대지'",10,0,0,120,0,400,"atk")

R_atk_item_611 = R_r_atk_item("렉스의 7번째 명작 '고대갑주 쿠구'",30,0,0,0,100,0,0,"def")
R_atk_item_612 = R_r_atk_item("렉스의 8번째 명작 '고대갑주 갑옷'",100,0,0,0,0,0,100,"def")
R_atk_item_613 = R_r_atk_item("렉스의 9번째 명작 '고대갑주 바지'",60,35,35,35,0,0,0,"def")
R_atk_item_614 = R_r_atk_item("렉스의 10번째 명작 '고대갑주 신발'",5,0,0,0,0,100,0,"def")


# 각성된 랙스의 명작
R_atk_item_621 = R_r_atk_item("렉스의 1번째 명작 '그람'",450,80,80,80,35,350,"atk")
R_atk_item_622 = R_r_atk_item("렉스의 2번째 명작 '발뭉'",200,0,140,0,70,0,"atk")
R_atk_item_623 = R_r_atk_item("렉스의 3번째 명작 '레바테인'",150,0,0,0,35,0,"atk")
R_atk_item_624 = R_r_atk_item("렉스의 4번째 명작 '파프니르의 발톱'",250,70,70,0,20,0,"atk")
R_atk_item_625 = R_r_atk_item("렉스의 5번째 명작 '궁니르'",120,70,0,60,0,300,"atk")
R_atk_item_626 = R_r_atk_item("렉스의 6번째 명작 '란드그리드'",10,0,0,140,0,650,"atk")

R_atk_item_631 = R_r_atk_item("렉스의 7번째 명작 '필리아스의 쿠구'",60,0,0,0,100,0,0,"def")
R_atk_item_632 = R_r_atk_item("렉스의 8번째 명작 '필리아스의 갑옷'",200,0,0,0,0,0,100,"def")
R_atk_item_633 = R_r_atk_item("렉스의 9번째 명작 '필리아스의 바지'",120,35,35,35,0,0,0,"def")
R_atk_item_634 = R_r_atk_item("렉스의 10번째 명작 '필리아스의 신발'",10,0,0,0,0,100,0,"def")


# 사신수 무기
R_atk_item_701 = R_s_atk_item("사신수 무기 '청룡의 검'",420,50,50,50,120,20,430,"atk")
R_atk_item_702 = R_s_atk_item("사신수 무기 '백호의 도끼'",550,50,120,0,100,0,40,"atk")
R_atk_item_703 = R_s_atk_item("사신수 무기 '주작의 단검'",300,50,20,200,0,90,0,"atk")
R_atk_item_704 = R_s_atk_item("사신수 무기 '현무의 창'",400,50,110,110,0,40,0,"atk")


# 각성한 사신수 무기
R_atk_item_711 = R_s_atk_item("사신수 무기 '청룡의 검'",4000,70,50,50,120,20,430,"atk")
R_atk_item_712 = R_s_atk_item("사신수 무기 '백호의 도끼'",4000,70,120,0,100,0,40,"atk")
R_atk_item_713 = R_s_atk_item("사신수 무기 '주작의 단검'",4000,70,20,200,0,90,0,"atk")
R_atk_item_714 = R_s_atk_item("사신수 무기 '현무의 창'",4000,50,110,110,0,40,0,"atk")


# 사흉수 갑주
R_def_item_701 = R_s_def_item("사흉주 갑옷 '혼돈의 투구'",200,1,100,150,150,150,"atk")
R_def_item_702 = R_s_def_item("사흉수 갑옷 '도철의 갑옷'",200,2,100,150,150,150,"atk")
R_def_item_703 = R_s_def_item("사흉주 갑옷 '도올의 바지'",200,3,100,150,150,150,"atk")
R_def_item_704 = R_s_def_item("사흉수 갑옷 '궁기의 신발'",200,4,100,150,150,150,"atk")


# 카우아(흑룡)의 검
R_atk_item_801 = R_b_atk_item("힘을 잃은 흑룡의 검",1500,60,70,"atk")
R_atk_item_802 = R_b_atk_item("힘을 되찾은 흑룡의 검",2250,65,70,"atk")
R_atk_item_803 = R_b_atk_item("힘을 깨우친 카우아의 검",3000,70,70,"atk")

# 흑룡의 갑주 (65레벨)
R_def_item_801 = R_d_def_item("흑룡의 갑주 투구",100,1,65,100,100,100,"def")
R_def_item_802 = R_d_def_item("흑룡의 갑주 갑옷",100,2,65,100,100,100,"def")
R_def_item_803 = R_d_def_item("흑룡의 갑주 바지",100,3,65,100,100,100,"def")
R_def_item_804 = R_d_def_item("흑룡의 갑주 신발",100,4,65,100,100,100,"def")


# 흑룡의 갑주 (70레벨)
R_def_item_811 = R_d_def_item("흑룡의 갑주 투구",300,1,70,200,200,200,"def")
R_def_item_812 = R_d_def_item("흑룡의 갑주 갑옷",300,2,70,200,200,200,"def")
R_def_item_823 = R_d_def_item("흑룡의 갑주 바지",300,3,70,200,200,200,"def")
R_def_item_824 = R_d_def_item("흑룡의 갑주 신발",300,4,70,200,200,200,"def")


# 선과 악
g_e_atk_item_01 = g_e_atk_item("세번째 아이 '트리아'",30000,100,5000,"atk")
g_e_atk_item_02 = g_e_atk_item("첫번째 아이 '에나'",30000,100,5000,"atk")


# 강화서 (개척자의 증표로 구매)
fortification_item_101 = fortification_item("하급 무기강화", 1, "+ 3~18 데미지 (레벨 제한 3)")
fortification_item_201 = fortification_item("중급 무기강화", 1, "+ 3~27 데미지 (레벨 제한 4)")
fortification_item_202 = fortification_item("고급 무기강화", 3, "+ 18~27 데미지 (레벨 제한 5)")
fortification_item_203 = fortification_item("힘 강화", 1, "+ 3~9 데미지 (힘 스텟 제한 20")
fortification_item_204 = fortification_item("민첩 강화", 1, "크리티컬 + 3~5% (민첩 스텟 제한 20)")
fortification_item_205 = fortification_item("모험 강화", 1, "체력흡수 + 16~39 (모험 스텟 제한 20)")
fortification_item_206 = fortification_item("방어구 강화", 3, "+ 3~18 방어력 (레벨 제한 10)")
fortification_item_301 = fortification_item("저주받은 공격력 강화", 10, "+ 200 데미지 (체력 흡수 -50)")
fortification_item_302 = fortification_item("저주받은 크티티컬 강화", 10, "크리티컬 + 8% (체력 흡수 -50)")
fortification_item_303 = fortification_item("저주받은 방어구 강화", 10, "체력증가 + 500 (방어력 -50)")
fortification_item_401 = fortification_item("어둠의 강화", 5, "+ 25 데미 (레벨 제한 55)")


# 회복의 돌
re_item_01 = Re_item("최하급 회복의 돌",10,1,1,"re")
re_item_02 = Re_item("하급 회복의 돌",50,10,1,"re")
re_item_03 = Re_item("중급 회복의 돌",100,50,1,"re")
re_item_04 = Re_item("상급 회복의 돌",500,500,1,"re")
re_item_05 = Re_item("최상급 회복의 돌",1000,2000,1,"re")


# n월의 기억
month_item_01 = nomal_item_shop("1월의 기억", 1, 100, "nomal") #100원
month_item_02 = nomal_item("2월의 기억", 1, "nomal")
month_item_03 = nomal_item("3월의 기억", 1, "nomal")
month_item_04 = nomal_item("4월의 기억", 1, "nomal")
month_item_05 = nomal_item("5월의 기억", 1, "nomal")
month_item_06 = nomal_item("6월의 기억", 1, "nomal")
month_item_07 = nomal_item("7월의 기억", 1, "nomal")
month_item_08 = nomal_item("8월의 기억", 1, "nomal")
month_item_09 = nomal_item("9월의 기억", 1, "nomal")
month_item_10 = nomal_item("10월의 기억", 1, "nomal")
month_item_11 = nomal_item("11월의 기억", 1, "nomal")

nomal_item_00 = nomal_item("개척자의 증표", 1, "nomal")



W_atk_item_list = [W_atk_item_101, W_atk_item_102, W_atk_item_103, W_atk_item_104, W_atk_item_105, W_atk_item_106, \
                   W_atk_item_201, W_atk_item_202, W_atk_item_203, W_atk_item_204, W_atk_item_205, W_atk_item_206, \
                   W_atk_item_207, W_atk_item_208, W_atk_item_209, \
                   W_atk_item_301, W_atk_item_302, W_atk_item_303, W_atk_item_304, W_atk_item_305, W_atk_item_306, \
                   W_atk_item_401, W_atk_item_402, W_atk_item_403]

W_atk_item_list_1 = [W_atk_item_101, W_atk_item_102, W_atk_item_103, W_atk_item_104, W_atk_item_105, W_atk_item_106]
W_atk_item_list_2 = [W_atk_item_201, W_atk_item_202, W_atk_item_204, W_atk_item_205, W_atk_item_206, W_atk_item_207, W_atk_item_209]
W_atk_item_list_3 = [W_atk_item_301, W_atk_item_302, W_atk_item_303, W_atk_item_304, W_atk_item_305, W_atk_item_306]
W_atk_item_list_4 = [W_atk_item_401, W_atk_item_402, W_atk_item_403]

R_atk_item_list_1 = [R_atk_item_701, R_atk_item_702, R_atk_item_703, R_atk_item_704, \
                     R_atk_item_711, R_atk_item_712, R_atk_item_713, R_atk_item_714, \
                     R_def_item_701, R_def_item_702, R_def_item_703, R_def_item_704]

R_atk_item_list_2 = [R_atk_item_801, R_atk_item_802, R_atk_item_803, \
                     R_def_item_801, R_def_item_802, R_def_item_803, R_def_item_714, \
                     R_def_item_701, R_def_item_702, R_def_item_703, R_def_item_704]

W_def_item_list = [W_def_item_111, W_def_item_112, W_def_item_113, W_def_item_114, \
                    W_def_item_211, W_def_item_212, W_def_item_213, W_def_item_214, W_def_item_221, W_def_item_222, W_def_item_223, W_def_item_224,\
                    W_def_item_231, W_def_item_232, W_def_item_233, W_def_item_234, W_def_item_241, W_def_item_242, W_def_item_243, W_def_item_244,\
                    W_def_item_311, W_def_item_312, W_def_item_313, W_def_item_314, W_def_item_321, W_def_item_322, W_def_item_323, W_def_item_324,\
                    W_def_item_331, W_def_item_332, W_def_item_333, W_def_item_334, W_def_item_341, W_def_item_342, W_def_item_343, W_def_item_344,\
                    W_def_item_411, W_def_item_412, W_def_item_413, W_def_item_414, W_def_item_421, W_def_item_422, W_def_item_423, W_def_item_424,\
                    W_def_item_431, W_def_item_432, W_def_item_433, W_def_item_434, W_def_item_441, W_def_item_442, W_def_item_443, W_def_item_444,\
                    W_def_item_511, W_def_item_512, W_def_item_513, W_def_item_514, W_def_item_521, W_def_item_522, W_def_item_523, W_def_item_524,\
                    W_def_item_531, W_def_item_532, W_def_item_533, W_def_item_534, W_def_item_541, W_def_item_552, W_def_item_543, W_def_item_544]

W_def_item_list_1 = [W_def_item_111, W_def_item_112, W_def_item_113, W_def_item_114]
W_def_item_list_2 = [W_def_item_211, W_def_item_212, W_def_item_213, W_def_item_214, W_def_item_221, W_def_item_222, W_def_item_223, W_def_item_224,\
                    W_def_item_231, W_def_item_232, W_def_item_233, W_def_item_234, W_def_item_241, W_def_item_242, W_def_item_243, W_def_item_244]
W_def_item_list_3 = [W_def_item_311, W_def_item_312, W_def_item_313, W_def_item_314, W_def_item_321, W_def_item_322, W_def_item_323, W_def_item_324,\
                    W_def_item_331, W_def_item_332, W_def_item_333, W_def_item_334, W_def_item_341, W_def_item_342, W_def_item_343, W_def_item_344]
W_def_item_list_4 = [W_def_item_411, W_def_item_412, W_def_item_413, W_def_item_414, W_def_item_421, W_def_item_422, W_def_item_423, W_def_item_424,\
                    W_def_item_431, W_def_item_432, W_def_item_433, W_def_item_434, W_def_item_441, W_def_item_442, W_def_item_443, W_def_item_444]
W_def_item_list_5 = [W_def_item_511, W_def_item_512, W_def_item_513, W_def_item_514, W_def_item_521, W_def_item_522, W_def_item_523, W_def_item_524,\
                    W_def_item_531, W_def_item_532, W_def_item_533, W_def_item_534, W_def_item_541, W_def_item_552, W_def_item_543, W_def_item_544]

re_item_list = [re_item_01, re_item_02, re_item_03, re_item_04, re_item_05]

nomal_item_list = [month_item_01, month_item_02, month_item_03, month_item_04, month_item_05, \
                   month_item_06, month_item_07, month_item_08, month_item_09, month_item_10, month_item_11]


# 몬스터 클래스
class monster:
    def __init__(self, name, liv, health, damage, recovery_health, drop_exp, drop_money, drop_item, drop_item_count, spawn_point):
        self.name = name
        self.liv = liv
        self.health = health
        self.damage = damage
        self.recovery_health = recovery_health
        self.drop_exp = drop_exp
        self.drop_money = drop_money
        self.drop_item = drop_item
        self.drop_item_count = drop_item_count
        self.spawn_point = spawn_point


# 1월의 기억 드랍
nomal_monster_0001 = monster("화난닭",0,1,2,0,0,0,[month_item_01],1,66)

nomal_monster_0101 = monster("화난닭",0,1,2,0,0,0,[month_item_01],1,32)
nomal_monster_0102 = monster("돌돌이",1,25,8,0,1,1,[month_item_01],2,32)
nomal_monster_0103 = monster("돌순이",2,35,20,0,1,1,[month_item_01],3,32)
nomal_monster_0104 = monster("돌멍이",3,60,35,5,2,2,[month_item_01],4,32)
nomal_monster_0105 = monster("돌전사",6,150,75,7,4,3,[month_item_01],5,32)
nomal_monster_0106 = monster("왕돌이",6,1500,500,50,200,200,[month_item_01],6,32)

nomal_monster_0002 = monster("화난소",0,300,100,100,15,0,[],0,1)
nomal_monster_0003 = monster("핀 그리드",0,15000,2500,4000,3000,1000,[R_atk_item_601],1,1) # 렉스의 1번째 명작 '홍염의 날개깃' 드랍 / 중복 x

nomal_monster_0201 = monster("오염된 슬라임 요정",6,160,60,8,6,5,[month_item_01],6,4)
nomal_monster_0202 = monster("오염된 뼈슬라임",7,200,80,10,7,5,[month_item_01],7,4)
nomal_monster_0203 = monster("오염된 하늘슬라임",8,250,85,13,8,5,[month_item_01],8,4)
nomal_monster_0204 = monster("오염된 키다리 슬라임",8,240,125,12,7,5,[month_item_01],9,4)
nomal_monster_0205 = monster("사악한 마녀",9,2000,300,100,250,2000,[month_item_01],10,4)

# 2월의 기억 드랍
nomal_monster_0301 = monster("어설픈 해적앵무새",9,260,95,13,10,7,[month_item_02],1,7)
nomal_monster_0302 = monster("어설픈 해적 조무래기",10,280,115,14,11,7,[month_item_02],2,7)
nomal_monster_0303 = monster("어설픈 해적 견습생",11,300,120,15,12,7,[month_item_02],3,7)
nomal_monster_0304 = monster("어설픈 해적",12,325,145,16,13,7,[month_item_02],4,6)
nomal_monster_0305 = monster("어설픈 해적선장",13,4000,500,300,250,4000,[month_item_02],4,6)

nomal_monster_0401 = monster("파란 위습",13,375,170,17,15,10,[month_item_02],5, )
nomal_monster_0402 = monster("초록 위습",14,400,190,18,16,10,[month_item_02],6, )

nomal_monster_0501 = monster("엘프 전사 견습생",15,450,220,20,17,12,[month_item_02],7,15)
nomal_monster_0502 = monster("엘프 전사",16,500,250,22,18,14,[month_item_02],8,15)
nomal_monster_0503 = monster("엘프 여왕",17,8000,700,500,300,7000,[month_item_02],10,15)

# 3월의 기억 드랍
nomal_monster_0601 = monster("감염된 여성",18,550,280,24,20,16,[month_item_03],1,10)
nomal_monster_0602 = monster("감염된 남성",19,650,300,28,21,18,[month_item_03],2,10)
nomal_monster_0603 = monster("거대 바이러스 골렘",20,10000,1200,800,500,15000,[month_item_03],3,10)

nomal_monster_0701 = monster("초보 드워프",20,720,400,40,34,30,[month_item_03],5,14)
nomal_monster_0702 = monster("붉은 드워프",21,800,450,44,40,35,[month_item_03],6,14)
nomal_monster_0703 = monster("땅꼬마 드워프",22,880,500,48,46,40,[month_item_03],7,14)
nomal_monster_0704 = monster("덩치 드워프",23,960,550,52,52,45,[month_item_03],8,14)
nomal_monster_0705 = monster("드워프 왕",24,15000,1600,1000,800,50,[month_item_03],10,14)

# 4월의 기억 드랍
nomal_monster_0801 = monster("인어 견습 전사",24,1000,600,60,70,60,[month_item_04],1,12)
nomal_monster_0802 = monster("인어 전사",25,1100,650,70,80,70,[month_item_04],2,12)
nomal_monster_0803 = monster("인어 베테랑 전사",26,1200,700,80,90,80,[month_item_04],3,12)
nomal_monster_0804 = monster("인어 전사장",27,1300,750,90,100,90,[month_item_04],4,12)
nomal_monster_0805 = monster("인어 대장",28,18000,2000,1200,1000,1000,[month_item_04],5,12)

nomal_monster_0901 = monster("아기 거미",28,1450,800,100,110,100,[month_item_04],6,25)
nomal_monster_0902 = monster("거미 전사",29,1600,900,120,130,110,[month_item_04],7,25)
nomal_monster_0903 = monster("거미 마법사",30,1750,1000,140,150,120,[month_item_04],8,25)
nomal_monster_0904 = monster("거미 대장",31,1900,1100,160,170,130,[month_item_04],9,25)
nomal_monster_0905 = monster("거미 여왕",32,23000,3000,1500,1300,1400,[month_item_04],10,25)

# 5월의 기억 드랍
nomal_monster_1001 = monster("허약한 선녀",32,2100,1300,180,190,150,[month_item_05],1,8)
nomal_monster_1002 = monster("가녀린 선녀",33,2300,1450,210,220,170,[month_item_05],2,8)
nomal_monster_1003 = monster("길쭉한 선녀",34,2500,1600,240,250,190,[month_item_05],3,8)
nomal_monster_1004 = monster("키가 작은 선녀",35,2700,1750,260,270,210,[month_item_05],4,8)

# 이벤트 및 특수
special_monster_0004 = monster("인내의 돌")

monster_month_1_list = [nomal_monster_0001, nomal_monster_0002, nomal_monster_0003, \
                        nomal_monster_0101, nomal_monster_0102, nomal_monster_0103, nomal_monster_0104, nomal_monster_0105, nomal_monster_0106, \
                        nomal_monster_0201, nomal_monster_0202, nomal_monster_0203, nomal_monster_0204, nomal_monster_0205]

monster_month_2_list = [nomal_monster_0301, nomal_monster_0302, nomal_monster_0303, nomal_monster_0304, nomal_monster_0305, \
                        nomal_monster_0401, nomal_monster_0402, \
                        nomal_monster_0501, nomal_monster_0502, nomal_monster_0503]

monster_month_3_list = [nomal_monster_0601, nomal_monster_0602, nomal_monster_0603, \
                        nomal_monster_0701, nomal_monster_0702, nomal_monster_0703, nomal_monster_0704, nomal_monster_0705]

monster_month_4_list = [nomal_monster_0801, nomal_monster_0802, nomal_monster_0803, nomal_monster_0804, nomal_monster_0805, \
                        nomal_monster_0901, nomal_monster_0902, nomal_monster_0903, nomal_monster_0904, nomal_monster_0905]

monster_month_5_list = [nomal_monster_1001, nomal_monster_1002, nomal_monster_1003, nomal_monster_1004]

mon_dict = []


# 몬스터 고르기
def monster_sel(self):
    while True:
        per = choice(list(mon_dict.keys()))
        if per == self.point:
            sel_monster = choice(list(mon_dict[per]))
            return sel_monster
            break
        else:
            continue

# 몬스터 프린트
def print_mon(sel_monster):
    print("\n\n{0:=^25}".format("Lv." + str(sel_monster.liv) + "_" + sel_monster.name))
    print("{0} : {1}\n{2} : {3}\n{4} : {5}".format( \
        '이름', sel_monster.name, \
        '체력', sel_monster.health, \
        '공격력', sel_monster.damage))


#플레이어 도망
def player_run(turn):
    per = choice("y" * 30 + "n" * turn + 5)
    return per

#공격
def attack(self, sel_monster, player_or_monster):
    if player_or_monster == "player":
        if len(self.equipment['atk']) == 2:
            per = choice("y" * self.critical + "n" * (100 - self.critical))
            if per == 'y':
                print("크리티컬")
                damage = self.damage * 2
            else:
                damage = self.damage
            sel_monster.health -= damage
            print("{0}에게 {1} 데미지를 입혔습니다\n".format(sel_monster.name, damage))
            return sel_monster.health
        elif len(self.equipment['atk']) == 1:
            print("{0}에게 0 데미지를 입혔습니다\n".format(sel_monster.name))
            return sel_monster_health
    elif player_or_monster == "monster":
        def_amount = 0
        if len(self.equipment['def_1']) == 2:
            def_amount = int({self.equipment['def_1'][1].defense}) + def_amount
        if len(self.equipment['def_2']) == 2:
            def_amount = int({self.equipment['def_2'][1].defense}) + def_amount
        if len(self.equipment['def_3']) == 2:
            def_amount = int({self.equipment['def_3'][1].defense}) + def_amount
        if len(self.equipment['def_4']) == 2:
            def_amount = int({self.equipment['def_4'][1].defense}) + def_amount
        damage = sel_monster.damage - def_amount
        if damage <= 0:
            damage = 0
        self.health -= damage
        print("{0} 데미지를 받았습니다\n".format(damage))
        return self.health

# 몬스터 출현
def monster_hello(move, self):
    if move == 'w' or move == 'a' or move == 's' or move == 'd':
        # 몬스터 등장
        while True:
            per = choice("m" * 30 + "n" * 70)
            if per == "m":
                sel_monster = monster_sel(self)
                print("\n야생의 {0}이(가) 나타났다\n".format(sel_monster.name))
                turn = 1
                run_turn = 0
                # 전투
                while True:
                    print("\n\n{0:_^30}\n".format("Round" + str(turn)))
                    if turn % 2 == 0:
                        sel_monster.health += sel_monster.recovery_health
                    print_mon(sel_monster)
                    print('\n{0:=^25}\n'.format("Vs"))
                    self.m_showinfo()
                    if run_turn == 0:
                        ans = input("\n공격(q) 아이템(w) 도망(e)\n:")
                    else:
                        ans = input("\n공격(q) 아이템(w)\n:")
                    # 공격
                    if ans == 'q':
                        sel_monster.health = attack(self,sel_monster,'player')
                        if sel_monster.health <= 0:
                            self.exp += sel_monster.drop_exp
                            self.money += sel_monster.drop_money
                            print("{0}가 죽었습니다".format(sel_monster.name))
                            print("\n돈 {0}를 얻었습니다".format(sel_monster.drop_money))
                            if len(sel_monster.drop_item_count) != 0:
                                for i in sel_monster.drop_item_count:
                                    per = choice('y' * 40 + 'n' * 60)
                                    if per == 'y':
                                        if sel_monster.drop_item in self.inven["month"]:
                                            num = self.inven["month"].index(sel_monster.drop_item)
                                            self.inven["month"][num].count += 1
                                        else:
                                            self.inven["month"].append(sel_monster.drop_item)
                                    elif per == 'n':
                                        pass
                                print("\n\n")
                            return self
                        attack(self, sel_monster, "monster")
                        if self.health <= 0:
                            break
                        turn += 1
                    # 아이템
                    elif ans == 'w':
                        inventory(self)
                    if run_turn == 0:
                        # 도망
                        if ans == 'e':
                            per = player_run(turn)
                            if per == 'y':
                                print("도망에 성공하였다")
                                input("(enter)")
                                break
                            elif per == 'n':
                                run_turn = 1
                            pass
                    if run_turn == 0:
                        if ans != "q" or "w" or "e":
                            print("올바른 문자를 입력하세요")
                    else:
                        if ans != "q" or "w":
                            print("올바른 문자를 입력하세요")
            elif per == "n":
                break
            break


# 아이템 정보 프린트
def print_item_1 (item):
    if item.use == 'atk':
        print("{0:^25}{1:^10}{2:^10}".format( \
            '이름', item.name, \
            '공격력', item.damage, \
            '무기레벨', item.liv))
    elif item.use == 'def':
        print("{0:^25}{1:^10}{2:^10}".format( \
            '이름', item.name, \
            '방어력', item.defense, \
            '제한레벨', item.liv))
    elif item.use == 're':
        print("{0:^25}{1:^10}{2:^10}".format( \
            '이름', item.name, \
            '체력 회복량', item.recovery)

def print_item_2 (item):
    if item.use == 'atk':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}".format( \
            '이름', item.name, \
            '공격력', item.damage, \
            '가격', item.cost, \
            '제한레벨', item.liv))

        if item.need_power_stats in globals()
            need_power_stats == item.need_power_stats
        if item.need_agility_stats in globals()
            need_need_agility_stats == item.need_agility_stats
        if item.need_adventure_stats in globals()
            need_adventure_stats == item.need_adventure_stats

        print("{0} : {1}/{2}/{3}").format( \
            '필요스텟 (힘, 민첩, 모험)', need_power_stats, need_agility_stats, need_adventure_stats)


        if item.plus_power_stats in globals()
            plus_power_stats == item.plus_power_stats
        if item.plus_agility_stats in globals()
            plus_agility_stats == item.plus_agility_stats
        if item.plus_adventure_stats in globals()
            plus_adventure_stats == item.plus_adventure_stats

        if plus_power_stats != 0 and plus_agility_stats != 0 and plus_adventure_stats != 0:
            print("{0} : {1}/{2}/{3}").format( \
                '추가스텟 (힘, 민첩, 모험)', plus_power_stats, plus_agility_stats, plus_adventure_stats)
        if item.critical in globals()
            print("{0} : {1}").format( \
                '크리티컬', item.critical)
        if item.physical_absorption in glonals()
            print("{0} : {1}").format( \
                    '체력추가', item.physical_absorption)

    elif item.use == 'def':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}".format( \
            '이름', item.name, \
            '방어력', item.defense, \
            '가격', item.cost, \
            '제한레벨', item.liv))

        need_power_stats = 0
        need_agility_stats = 0
        need_adventure_stats = 0

        if item.need_power_stats in globals()
            need_power_stats == item.need_power_stats
        if item.need_agility_stats in globals()
            need_need_agility_stats == item.need_agility_stats
        if item.need_adventure_stats in globals()
            need_adventure_stats == item.need_adventure_stats

        print("{0} : {1}/{2}/{3}").format( \
            '필요스텟 (힘, 민첩, 모험)', need_power_stats, need_agility_stats, need_adventure_stats)

        if item.plus_power_stats in globals()
            plus_power_stats == item.plus_power_stats
        if item.plus_agility_stats in globals()
            plus_agility_stats == item.plus_agility_stats
        if item.plus_adventure_stats in globals()
            plus_adventure_stats == item.plus_adventure_stats

        if plus_power_stats != 0 and plus_agility_stats != 0 and plus_adventure_stats != 0:
            print("{0} : {1}/{2}/{3}").format( \
                '추가스텟 (힘, 민첩, 모험)', plus_power_stats, plus_agility_stats, plus_adventure_stats)
        if item.critical in globals()
            print("{0} : {1}").format( \
                '크리티컬', item.critical)
        if item.physical_absorption in glonals()
            print("{0} : {1}").format( \
                '체력추가', item.physical_absorption)
    elif item.use == 're':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}".format( \
            '이름', item.name, \
            '체력회복', item.recovery, \
            '가격', item.cost)

# 포션 사용
def re_use(self, use, item, ans):
    while True:
        print_item_2(item[ans])
        ans_1 = input("\n{0}을(를) 사용하시겟습니까? (y / n) : ".format(item[ans].name))
        if ans_1 == "y":
            tem = qw(item[sel],use,1)
            if use == 're': self.health += tem
            elif use == 'food': self.hunger += tem
            item[sel].count -= 1
            if item[sel].count <= 0:
                del item[sel]
            return self
        elif sel_1 == "n":
                break
        else:
            print("올바른 문자를 입력하세요")

# 무기 장착
# def equipment(self, use, item, ans):
    while True:
        print_item_2(item[ans])
        ans_1 = input("\n{0} 무기를 장착하시겟습니까? (y / n) : ".format(item[ans].name))
        if ans_1 == "y":
            if len(self.equipment[use]) == 2:
                self.inven[use].append(pl.equipment[use][1])
                reset_info(self, self.equipment[use][1], 'd', use)
                del self.equipment[use][1]
                self.equipment[use].append(item[ans])
                del item[ans]
                reset_info(self, self.equipment[use][1], 'u', use)
                print("\n{0} 무기를 장착하였습니다: ".format(self.equipment[use][1].name))
                input("나가려면(enter)")
                return self
                break
            elif len(self.equipment[use]) == 1:
                self.equipment[use].append(item[ans])
                reset_info(self, self.equipment[use][1], 'u', use)
                del item[ans]
                print("\n{0} 무기를 장착하였습니다: ".format(self.equipment[use][1].name))
                input("나가려면(enter)")
                return self
                break
        elif ans_1 == "n":
                break
        else:
            print("올바른 문자를 입력하세요")

# 인벤토리
def inventory(self):
    while True:
        ans = input("\n인벤토리를 선택하세요 [무기(q) /방어구(w) /포션(e) /기억(r) /일반(t)]")
        print("나가려면 (enter)")
        if ans == "q" or ans == "w" or ans == "e" or ans == "r" or ans == "t":
            ans = change_3(ans)
            inventory_print(self, ans)
        elif ans == "":
            break
        else:
            print("올바른 문자를 입력하세요")


# 인벤토리 출력
def inventory_print(self, ans):
    while True:
        ans_1 = change_1(ans)
        print("{0:=^25}".format(str(ans_1) + " 인벤토리"))
        print("{0:^12}{1:^12}".format("Num", "Name"))
        if len(self.inven[ans]) == 0:
            print("{0:^12}{1:^12}".format("없음", "없음"))
        if ans == 'atk' or ans == 'def':
            for i in range(len(self.inven[ans])):
                print("{0:^12}{1:^12}".format(i + 1, self.inven[ans][i].name))
        else:
            for i in range(len(self.inven[ans])):
                print("{0:^12}{1:^12}".format(i + 1, self.inven[ans][i].name + "  x" + str(self.inven[ans][i].count)))
        print("{0:=^25}".format("인벤토리"))
        ans_2 = input("아이템의 정보를 보고 싶다면 해당 아이템의 번호를 입력하세요\n나가려면 (enter)\n:")
        ans_2 = check(ans_2, 1, len(self.inven[ans]))
        if type(ans_2) == type(0):
            print("\n{0:=^25}".format("Num" + str(ans_2) + " 정보"))
            ans_2 -= 1
            if ans == 'atk' or ans == 'def':
                equipment(self, ans, self.inven[ans], ans_2)
            elif ans == 're':
                re_use(self, ans, self.inven[sel], ans_2)
        elif ans_2 == "":
            break
        else:
            print("올바른 숫자를 입력하세요")


# 상점 구매
def buyshop(self, count, item):
    while True:
        cou = input("\n몇개를 구매하시겠습니까? \n나가려면 (enter): ")
        cou = check(cou, 1, 1000)
        if type(cou) == type(0):
            if self.money - item[count].cost * cou >= 0:
                if self.liv >= item[count].liv:
                    self.money -= item[count].cost * cou
                    use = qwe(item[count])
                    if item[count].use == 'atk' or item[count].use == 'def':
                        for a in range(cou):
                            self.inven[use].append(item[count])
                    elif item[count].use == 're' or item[count].use == 'food':
                        if item[count] in self.inven[use]:
                            num_1 = self.inven[use].index(item[count])
                            self.inven[use][num_1].count *= cou
                        else:
                            self.inven[use].append(item[count])
                            num_1 = self.inven[use].index(item[count])
                            self.inven[use][num_1].count *= cou

                    print("\n{0} 아이템을 {1}개 구매하였습니다.".format(item[count].name, cou))
                    break
                else:
                    print("레벨이 부족합니다.")
                    print("필요레벨 : {0} / 현재레벨 : {1}".format(item[count].liv, self.liv))
            elif self.money - item[count].cost * cou < 0:
                print("\n돈이 부족합니다")
                print("필요금액 : {0} / 현재 가지고 있는 돈 : {1}".format(item[count].cost * cou, self.money))
            else:
                print("\n올바른 숫자를 입력하세요")
        elif cou == "":
            break
        else:
            print("\n올바른 숫자를 입력하세요")

        print("\n{0:=^25}".format(item[count].name + " 정보"))
        print_item_Ver2(item[count])
        print("\n나의 돈 {0}\n나의 레벨 {1}\n".format(self.money, self.liv))

    return self.money, self.inven, self.equipment

# 상점 보기
def showshop(self):
    point = chang_9(self)
    while point != '':
        print("\n상점을 선택하세요 [무기 상점(q) /방어구 상점(w) /포션 상점(e) /음식 상점(r)]")
        ans = input("(상점 선택에서 나가려면 엔터)\n:")
        if ans == "":
            break
        elif ans == "q" or ans == "w" or ans == "e" or ans == "r":
            while True:
                use_1 = change_3(ans)
                use_2 = change_2(use_1)
                print("\n{0:=^25}".format(use_2 + " 상점"))
                count = 0
                sel_list = (point + "_" + use_1 + "_item_list")
                for i in sel_list:
                    count += 1
                    print(count, i.name)
                sel_item = str(input(f"\n{use_2} 번호를 입력하세요\n(나가려면 enter)\n: "))
                sel_item = check(sel_item, 1, len(sel_list))
                if sel_item in range(1, len(sel_list) + 1):
                    sel_item -= 1
                    while True:
                        print("\n{0:=^25}".format(sel_list[sel_item].name + "정보"))
                        print_item_2(sel_list[sel_item])
                        print("=" * 26)
                        print("\n{나의 돈 {0}, 나의 레벨 {1}}\n{나의 스텟 (힘, 민첩, 모험) : {2}/{3}/{4}\n".format(self.money, self.liv, h_count, a_count, c_count))
                        ans = input("구매하시겠습니까 (y / n) : ")
                        if ans == "y":
                            buyshop(self, ch, shop_item_list[use])
                            break
                        elif ans == "n":
                            break
                        else:
                            print("올바른 문자를 입력하세요")
                            continue
                elif sel_item == "":
                    break
                else:
                    print("올바른 숫자를 입력하세요")
        else:
            print("올바른 문자를 입력하세요")
            continue


# 아이템별 스탯변화
# def reset_info(pl, item, u_d, use):
    if use == 'atk':
        if u_d == 'd':
            pl.damage -= int(item.damage + (item.damage * pl.ak / 100))
        elif u_d == 'u':
            pl.damage += int(item.damage + (item.damage * pl.ak / 100))
        return pl.damage
    elif use == 'def':
        if u_d == 'd':
            pl.defense -= item.defense
        elif u_d == 'u':
            pl.defense += item.defense
        return pl.defense

# 글씨 바꾸기
def change_1(item):
    if item.use == 'atk':
        return 'atk'
    elif item.use == 'def':
        return 'def'
    elif item.use == 're':
        return 're'
    elif item.use == 'food':
        return 'food'
    elif item.use == 'drop':
        return 'drop'
    elif item.use == 'item':
        return 'item'
def change_2(word):
    if word == 'atk':
        return '무기'
    elif word == 'def':
        return '방어구'
    elif word == 're':
        return '포션'
    elif word == 'food':
        return '음식'
    elif word == 'drop':
        return '드롭'
    elif word == 'item':
        return '일반'
def change_3(word):
    if word == 'q':
        return "atk"
    elif word == 'w':
        return "def"
    elif word == 'e':
        return "re"
    elif word == 'r':
        return "month"
    elif word == 't':
        return "item"
def change_4(self, word):
    if word == 'atk':
        return self.damage
    elif word == 'def':
        return self.defense
    elif word == 're':
        return self.health
def change_5(self, word, num):
    if word == 'atk':
        return self.equipment[word][num].damage
    elif word == 'def':
        return self.equipment[word][num].defense
def change_6(item, word):
    if word == 'atk':
        return item.damage
    elif word == 'def':
        return item.defense
def change_7(me, word, num):
    if num == 0:
        if word == 're':
            return me.health
    elif num == 1:
        if word == 're':
            return me.recovery
def change_8(self): # 구역 : 36 / 지역 : 24 / 바다   성 : 1, 2, 3, 5, 19, 22, 28, 36
    if self.point == 1:
        return '에나 성' # 성
    elif self.point == 2:
        return '뒤오 성' # 성
    elif self.point == 3:
        return '트리아 성' # 성
    elif self.point == 4:
        return '오염된 강'
    elif self.point == 5:
        return '누군가의 성' # 성
    elif self.point == 6:
        return '해적소굴'
    elif self.point == 7:
        return '불탄 점령지'
    elif self.point == 8:
        return '선녀 호수'
    elif self.point == 9:
        return '발길이 머무르는 곳'
    elif self.point == 10:
        return '오염된 마을'
    elif self.point == 11:
        return '심연의 갱도'
    elif self.point == 12:
        return '인어 왕국'
    elif self.point == 13:
        return '누군가의 무덤'
    elif self.point == 14:
        return '드워프 마을'
    elif self.point == 15:
        return '엘프 유적'
    elif self.point == 16:
        return '에나 동쪽 항구'
    elif self.point == 17:
        return '에나 낚시터'
    elif self.point == 18:
        return '세상을 등진곳'
    elif self.point == 19:
        return '얼음성' # 성
    elif self.point == 20:
        return '드워프 유적지'
    elif self.point == 21:
        return '심연의 갱도'
    elif self.point == 22:
        return '신기루 성' # 성
    elif self.point == 23:
        return '마니라 리'
    elif self.point == 24:
        return '봉인된 신전'
    elif self.point == 25:
        return '거미 동굴'
    elif self.point == 26:
        return '모험의 갈림길'
    elif self.point == 27:
        return '숨겨진 드워프 마을'
    elif self.point == 28:
        return '오래된 성' # 성
    elif self.point == 29:
        return '바다 신전'
    elif self.point == 30:
        return '세상을 등진곳 동쪽 항구'
    elif self.point == 31:
        return '신기루성 남쪽 항구'
    elif self.point == 32:
        return '고대 유적의 섬'
    elif self.point == 33:
        return '고대 유적의 섬 선착장'
    elif self.point == 34:
        return '신들의 고향 선착장'
    elif self.point == 35:
        return '생기의 마을'
    elif self.point == 36:
        return '오크의 성' # 성

    elif self.point == 50:
        return '에나'
    elif self.point == 51:
        return '뒤오'
    elif self.point == 52:
        return '트리아'
    elif self.point == 53:
        return '생명의 숲'
    elif self.point == 54:
        return '가벼운 무법지'
    elif self.point == 55:
        return '평화로운곳'
    elif self.point == 56:
        return '대륙의 통로'
    elif self.point == 57:
        return '파도가 부숴지는 해변'
    elif self.point == 58:
        return '발길이 머무르는곳'
    elif self.point == 59:
        return '구름의 휴식처'
    elif self.point == 60:
        return '태양의 열망'
    elif self.point == 61:
        return '바람 길목'
    elif self.point == 62:
        return '신화가 잠든 대지'
    elif self.point == 63:
        return '물거품의 바다'
    elif self.point == 64:
        return '고대 유적의 섬'
    elif self.point == 65:
        return '개척자의 섬'
    elif self.point == 66:
        return '신들의 고향'
    elif self.point == 67:
        return '비명의 바다'
    elif self.point == 68:
        return '죽음의 바다'
    elif self.point == 69:
        return '탄식의 바다'
    elif self.point == 70:
        return '생기가 있는 섬'
    elif self.point == 71:
        return '여유로운 바다'
    elif self.point == 72:
        return '갈 수 없는 섬'
    elif self.point == 73:
        return '돌아올 수 없는 섬'
    elif self.point == 74:
        return '잊혀진 섬'
    else:
        return '바다'

# 스텟
def level_up(self):
    print("\n" * 2)
    print("=" * 25)
    print("=" * 25)
    print("{0:=^25}".format(" 레벨 업 "))
    print("=" * 25)
    print("=" * 25)
    self.liv += 1
    print('Lv. ' + str(self.liv) + ' 로 레벨업을 하였습니다\n')
    self.exp = 0

    while True:
        print("{0:=^25}".format(" 스텟 "))
        print("1 힘 스텟 {0}\
            \n2 민첩 스텟 {1}\
            \n3 모험 스텟 {2}".format(h_count, a_count, c_count))

        num = input(":")
        if num == '1':
            print("{0:=^25}".format(" 힘 스텟 "))
            print("스텟 1당 공격력이 0.5 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                self.damage += 0.5
                print("공격력 0.5가 추가 됩니다")
                h_count += 1
                break
            elif ans == 'n':
                continue

        elif num == '2':
            if a_count == 20:
                continue
            print("{0:=^25}".format(" 민첩 스텟 "))
            print("스텟 1당 크리티컬 확률이 0.1% 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                self.critical += 1
                print("크리티컬 확률 0.1%가 추가 됩니다")
                a_count += 1
                break
            elif sel == 'n':
                continue

        elif num == '3':
            if c_count == 20:
                continue
            print("{0:=^25}".format(" 모험 스텟 "))
            print("스텟 1당 체력이 6 증가합니다.")
            sel = input("y / n : ")
            if sel == 'y':
                self.health += 6
                print("체력이 6 추가 됩니다.")
                c_count += 1
                break
            elif sel == 'n':
                continue
        else:
            print("올바른 문자를 입력하세요")
    else:
        pass

# 레벨, 위치, 패시브 체크
def turn_chack(self, player_x, player_y, plag):

    # 레벨업 체크
    level_up_count = 0

    if self.liv == 1:
        if self.exp >= 4:
            self.exp -= 4
            self.liv += 1
            level_up_count += 1
    elif self.liv == 2:
        if self.exp >= 400:
            self.exp -= 400
            self.liv += 1
    elif 3 <= self.liv <= 4:
        if self.exp >= 300:
            self.exp -= 300
            self.liv += 1
            level_up_count += 1
    elif 5 <= self.exp <= 10:
        if self.exp >= self.exp * 100:
            self.liv += 1
            level_up_count += 1
    elif 11 <= self.exp <= 20:
        if self.exp >= 1000 + (self.exp - 10) * 200:
            self.liv += 1
            level_up_count += 1
    elif 21 <= self.exp <= 30:
        if self.exp >= 3000 + (self.exp - 20) * 300:
            self.liv += 1
            level_up_count += 1
    elif 31 <= self.exp <= 40:
        if self.exp >= 6000 + (self.exp - 30) * 400:
            self.liv += 1
            level_up_count += 1
    elif 41 <= self.exp <= 50:
        if self.exp >= 10000 + (self.exp - 40) * 500:
            self.liv += 1
            level_up_count += 1
    elif 51 <= self.exp <= 60:
        if self.exp >= 15000 + (self.exp - 50) * 600:
            self.liv += 1
            level_up_count += 1
    elif 61 <= self.exp <= 70:
        if self.exp >= 21000 + (self.exp - 60) * 700:
            self.liv += 1
            level_up_count += 1
    elif 71 <= self.exp <= 80:
        if self.exp >= 28000 + (self.exp - 70) * 800:
            self.liv += 1
            level_up_count += 1
    elif 81 <= self.exp <= 90:
        if self.exp >= 36000 + (self.exp - 80) * 900:
            self.liv += 1
            level_up_count += 1
    elif 91 <= self.exp <= 100:
        if self.exp >= 45000 + (self.exp - 90) * 1000:
            self.liv += 1
            level_up_count += 1
    elif 101 <= self.exp:
        if self.exp >= 5500:
            self.liv += 1
            level_up_count += 1

    if level_up_count != 0:
        level_up(self)

    # 지역
    point_count == 0

    if point_count == 0:
        if 83 <= player_x <= 91:
            if 48 <= player_y <= 56:
                self.point == 1
                point_count += 1
        if 80 <= player_x <= 86:
            if 64 <= player_y <= 70:
                self.point == 2
                point_count += 1
        if 68 <= player_x <= 74:
            if 77 <= player_y <= 83:
                self.point == 3
                point_count += 1
        if 74 <= player_x <= 78:
            if 46 <= player_y <= 50:
                self.point == 4
                point_count += 1
        if 65 <= player_x <= 69:
            if 37 <= player_y <= 41:
                self.point == 5
                point_count += 1
        if 64 <= player_x <= 66:
            if 46 <= player_y <= 48:
                self.point == 6
                point_count += 1
        if 66 <= player_x <= 69:
            if 48 <= player_y <= 52:
                self.point == 7
                point_count += 1
        if 72 <= player_x <= 76:
            if 55 <= player_y <= 59:
                self.point == 8
                point_count += 1
        if 64 <= player_x <= 70:
            if 62 <= player_y <= 68:
                self.point == 9
                point_count += 1
        if 75 <= player_x <= 79:
            if 63 <= player_y <= 67:
                self.point == 10
                point_count += 1
        if 63 <= player_x <= 67:
            if 76 <= player_y <= 80:
                self.point == 11
                point_count += 1
        if 63 <= player_x <= 67:
            if 81 <= player_y <= 85:
                self.point == 12
                point_count += 1
        if 77 <= player_x <= 79:
            if 74 <= player_y <= 76:
                self.point == 13
                point_count += 1
        if 81 <= player_x <= 87:
            if 77 <= player_y <= 83:
                self.point == 14
                point_count += 1
        if 94 <= player_x <= 98:
            if 65 <= player_y <= 69:
                self.point == 15
                point_count += 1
        if 92 <= player_x <= 93:
            if 51 <= player_y <= 54:
                self.point == 16
                point_count += 1
        if 85 <= player_x <= 88:
            if 46 <= player_y <= 47:
                self.point == 17
                point_count += 1
        if 23 <= player_x <= 29:
            if 73 <= player_y <= 79:
                self.point == 18
                point_count += 1
        if 18 <= player_x <= 22:
            if 68 <= player_y <= 72:
                self.point == 19
                point_count += 1
        if 28 <= player_x <= 32:
            if 58 <= player_y <= 62:
                self.point == 20
                point_count += 1
        if 24 <= player_x <= 26:
            if 54 <= player_y <= 56:
                self.point == 21
                point_count += 1
        if 30 <= player_x <= 36:
            if 49 <= player_y <= 55:
                self.point == 22
                point_count += 1
        if 39 <= player_x <= 41:
            if 67 <= player_y <= 69:
                self.point == 23
                point_count += 1
        if 48 <= player_x <= 52:
            if 67 <= player_y <= 71:
                self.point == 24
                point_count += 1
        if 46 <= player_x <= 52:
            if 57 <= player_y <= 63:
                self.point == 25
                point_count += 1
        if 40 <= player_x <= 44:
            if 50 <= player_y <= 54:
                self.point == 26
                point_count += 1
        if 38 <= player_x <= 40:
            if 46 <= player_y <= 48:
                self.point == 27
                point_count += 1
        if 44 <= player_x <= 50:
            if 42 <= player_y <= 48:
                self.point == 28
                point_count += 1
        if 48 <= player_x <= 52:
            if 31 <= player_y <= 35:
                self.point == 29
                point_count += 1
        if 31 <= player_x <= 32:
            if 74 <= player_y <= 76:
                self.point == 30
                point_count += 1
        if 31 <= player_x <= 33:
            if 46 <= player_y <= 47:
                self.point == 31
                point_count += 1
        if 3 <= player_x <= 8:
            if 33 <= player_y <= 38:
                self.point == 32
                point_count += 1
        if 14 <= player_x <= 16:
            if 25 <= player_y <= 26:
                self.point == 33
                point_count += 1
        if 16 <= player_x <= 18:
            if 14 <= player_y <= 15:
                self.point == 34
                point_count += 1
        if 9 <= player_x <= 11:
            if 49 <= player_y <= 51:
                self.point == 35
                point_count += 1
        if 49 <= player_x <= 51:
            if 94 <= player_y <= 96:
                self.point == 36
                point_count += 1

    if point_count == 0:
        if 77 <= player_x <= 93:
            if 46 <= player_y <= 62:
                self.point == 50
                point_count += 1
        if 77 <= player_x <= 87:
            if 63 <= player_y <= 73:
                self.point == 51
                point_count += 1
        if 68 <= player_x <= 76:
            if 75 <= player_y <= 83:
                self.point == 52
                point_count += 1
        if 88 <= player_x <= 98:
            if 63 <= player_y <= 73:
                self.point == 53
                point_count += 1
        if 64 <= player_x <= 76:
            if 36 <= player_y <= 48:
                self.point == 54
                point_count += 1
        if 66 <= player_x <= 76:
            if 49 <= player_y <= 59:
                self.point == 55
                point_count += 1
        if 62 <= player_x <= 76:
            if 60 <= player_y <= 74:
                self.point == 56
                point_count += 1
        if 58 <= player_x <= 59:
            if 61 <= player_y <= 63:
                self.point == 56
                point_count += 1
        if 60 <= player_x <= 61:
            if 62 <= player_y <= 65:
                self.point == 56
                point_count += 1
        if 57 <= player_x <= 67:
            if 75 <= player_y <= 85:
                self.point == 57
                point_count += 1
        if 77 <= player_x <= 88:
            if 74 <= player_y <= 84:
                self.point == 58
                point_count += 1
        if 18 <= player_x <= 32:
            if  <= player_y <= :
                self.point == 59
                point_count += 1
        if 18 <= player_x <= 36:
            if  <= player_y <= :
                self.point == 60
                point_count += 1
        if 37 <= player_x <= 51:
            if  <= player_y <= :
                self.point == 61
                point_count += 1
        if 37 <= player_x <= 53:
            if  <= player_y <= :
                self.point == 62
                point_count += 1
        if 54 <= player_x <= 55:
            if  <= player_y <= :
                self.point == 62
                point_count += 1
        if 56 <= player_x <= 57:
            if  <= player_y <= :
                self.point == 62
                point_count += 1
        if 43 <= player_x <= 53:
            if  <= player_y <= :
                self.point == 63
                point_count += 1
        if 2 <= player_x <= 16:
            if 25 <= player_y <= 39:
                self.point == 64
                point_count += 1
        if 23 <= player_x <= 29:
            if 19 <= player_y <= 25:
                self.point == 65
                point_count += 1
        if 16 <= player_x <= 22:
            if 9 <= player_y <= 15:
                self.point == 66
                point_count += 1
        if 44 <= player_x <= 48:
            if 26 <= player_y <= 20:
                self.point == 67
                point_count += 1
        if 44 <= player_x <= 48:
            if 11 <= player_y <= 15:
                self.point == 68
                point_count += 1
        if 49 <= player_x <= 55:
            if 13 <= player_y <= 19:
                self.point == 69
                point_count += 1
        if 6 <= player_x <= 12:
            if 87 <= player_y <= :
                self.point == 70
                point_count += 1
        if 8 <= player_x <= 12:
            if 82 <= player_y <= :
                self.point == 71
                point_count += 1
        if 47 <= player_x <= 51:
            if 93 <= player_y <= :
                self.point == 72
                point_count += 1
        if 47 <= player_x <= 53:
            if 84 <= player_y <= :
                self.point == 73
                point_count += 1
        if 43 <= player_x <= 45:
            if 78 <= player_y <= :
                self.point == 74
                point_count += 1

# 게임 종료
def game_over():
    print("\n게임을 종료하시겠습니까?")
    while True:
        end_ans = input("y / n : ")
        if end_ans == "y":
            print("\n게임을 종료합니다")

            print("gmae over")
            break
        if end_ans == "n":
            print("\n게임을 계속 진행합니다.")
            main()


# 메인
def main():
    input("게임을 시작하려면 엔터")

    print("\n" * 38)

    try:
        import save
    except:

        story()

        player_name = input("\n플레이어 이름을 입력하십시오. = ")
        while player_name == "":
            print("\n유효한 이름을 입력하십시오")
            player_name = input("플레이어 이름을 입력하십시오. = ")
        player_1 = Player(player_name, 1.1, [], [], 60, 0, 0 ,0, 0, 50, 0, 0)

        player_x = 87
        player_y = 52

        plag = 0

    time.sleep(1.3)
    print('\n' * 2)
    print("정상적으로 로그인 되었습니다.")
    time.sleep(0.7)
    print("정보 불러오는 중...")
    time.sleep(0.7)
    print("환영합니다." + player_name + "님")
    time.sleep(1)

    while True:

        print("\n" * 38)

        turn_chack(self, player_x, player_y, plag) # 레벨, 위치, 패시브

        # 마을 버프
        if 1 <= player_1.point <= 3 or player_1.point == 5 or player_1.point == 19 or player_1.point == 22 or player_1.point == 28 or player_1.point == 36:
            player_1.health = player_1.health + 50

        # 체력,허기 최대치
        if player_1.health > higt_health:
            player_1.health = higt_health

        player_1.showinfo()

        print("나의 위치 (" + change_8(player_1) + ") : " + str(player_x) + "," + str(player_y))

        if plag == 0:
            print("\n도움을 원한다면 'h' 입력")

        ans = input("\n무엇을 하시겠습니까? : ")

        if ans == "w":
            player_y += 1
            print("앞으로 이동")
        elif ans == "s":
            player_y -= 1
            print("뒤로 이동")
        elif ans == "d":
            player_x += 1
            print("오른쪽으로 이동")
        elif ans == "a":
            player_x -= 1
            print("왼쪽으로 이동")

        if ans == "w" or ans == "a" or ans == "s" or ans == "d":

            move_count = 0

            if player_x > 100:
                player_x = 100
                move_count += 1
            if player_x < 0:
                player_x = 0
                move_count += 1
            if player_y > 100:
                player_y = 100
                move_count += 1
            if player_y < 0:
                player_y = 0
                move_count += 1

            if plag > 15:
                if move_count != 0:
                    print("최대 활동범위는 1~100,1~100 입니다.")

            if move_count == 0:
                if 50 <= player_1.point <= 74:
                    monster_hello(ans, self)

        elif ans == "e":
            inventory(self)
            continue
        elif ans == "f":
            showshop(self)
            continue
        elif ans == "m":
            show_map()
        elif ans == "q":
            atk_def_inventory(item)
        elif ans == "r":
            warp_manager(player_x, player_y)
        elif ans == "h":
            print("\n게임설명\n방향 조작은 w,a,s,d 입니다.\n인벤토리는 e 키로 열 수 있습니다.\n장착중인 장비는 q 키로 열수 있습니다.\
                  \nf 키를 누르면 상점에 진입합니다.\nm 키로 지도를 볼수 있습니다.\
                  \n에나와 에나 중심가에서는 체력이 회복되고 허기가 닳지 않습니다.\n에나 중심가에 있는 npc에게 퀘스트를 받을 수 있습니다.\
                  \n특정 몬스터는 특정 장소에서만 스폰됩니다\n채집은 일반지역에서만 가능합니다.(몬스터 지역 제외)\
                  \n한국어를 웬만하면 누르지 마세요.(버그의 원인이 됩니다.)\
                  \n최종보스를 물리치면 승리합니다.\n다 읽으셨다면 enter.")
            input()
        elif ans == "p":
            game_over()
        else:
            print("다시 입력해 주십시오")

        if player_1.health <= 0:
            player_1.money -= int(self.money / 2)
            print("에나 번화가로 리스폰 됩니다")
            player_1.health = 100
            player_x = 87
            player_y = 52

        plag += 1


if __name__ == "__main__":
    main()
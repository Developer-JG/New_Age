from random import choice
from random import randint
import time

print("\nthe New_Age (basilisk) game project\n")


# 죽는거 추가해야됨

higt_health = 100

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


# 플레이어 클래스
class Player:
    def __init__(self, name, point, equipment, inven, health, money, damage, critical, defense, liv, exp):
        self.name = name
        self.point = point
        self.equipment = {"atk": ["없음"], "def_1": ["없음"], "def_2": ["없음"], "def_3": ["없음"], "def_4": ["없음"]}
        self.inven = {"atk": [], "def": [], "re": [], "food": [], "drop": [], "item": []}
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
    def __init__ (self, name, damage, liv, critical, physical_absorption, use)
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
    def __init__ (self, name, defense, liv, part, need_power_stats, need_agility_stats, need_adventure_stats, use)
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
        self.plus_health = plus_health
        self.use = use


# 강화서 아이템 클래스
class fortification_item:
    def __init__(self, name, cost, use_effect):
        self.name = name
        self.cost = cost
        self.use_effect = use_effect


# 회복 아이템 클래스
class Re_item:
    def __init__(self, name, recovery, cost, liv, count, use):
        self.name = name
        self.recovery = recovery
        self.cost = cost
        self.liv = liv
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
W_atk_item_101 = W_atk_item("검", 2, 15, 1, 0, 0, 0, 0, 0, "W_atk")
W_atk_item_102 = W_atk_item("몽둥아", 2, 15, 1, 0, 0, 0, 0, 0, "W_atk")
W_atk_item_103 = W_atk_item("철검", 13, 30, 5, 0, 0, 0, 0, 0, "W_atk")
W_atk_item_104 = W_atk_item("도끼", 13, 30,, 5, 0, 0, 0, 0, 0, "W_atk")
W_atk_item_105 = W_atk_item("예리한 대검", 30, 65, 10, 0, 0, 0, 0, 0, "W_atk")
W_atk_item_106 = W_atk_item("예리한 도끼", 30, 65, 10, 0, 0, 0, 0, 0, "W_atk")
# 2월의 기억으로 구매
W_atk_item_201 = W_atk_item("반짝이는 검", 45, 25, 15, 40, 0, 0, 0, 0, "W_atk")  # 40 : 0 : 0
W_atk_item_202 = W_atk_item("반짝이는 도끼", 45, 25, 15, 20, 0, 20, 0, 45, "W_atk")  # 20 : 0 : 20 +체력흡수 45
W_atk_item_203 = W_atk_item("강철 단검", 35, 20, 15, 0, 40, 0, 6, 0, "W_atk")  # 0 : 40 : 0 +크리티컬 6%
W_atk_item_204 = W_atk_item("무쇠 건틀릿", 45, 25, 15, 20, 20, 0, 0, 0, "W_atk")  # 20 : 20 : 0
W_atk_item_205 = W_atk_item("푸른 방패", 35, 20, 15, 0, 0, 20, 0, 0, "W_atk")  # 0 : 0 : 40 +체력흡수 100
W_atk_item_206 = W_atk_item("붉은 검", 70, 40, 20, 60, 0, 20, 0, 0, "W_atk")  # 60 : 0 : 20
W_atk_item_207 = W_atk_item("붉은 도끼", 63, 40, 20, 30, 0, 30, 0, 0, "W_atk")  # 30 : 0 : 30 +체력흡수 63
W_atk_item_208 = W_atk_item("붉은 단검", 59, 40, 20, 0, 60, 0, 15, 63, "W_atk")  # 0 : 60 : 0 +체력흡수 63 +크리티컬 15%
W_atk_item_209 = W_atk_item("강철 방패", 49, 50, 20, 0, 0, 60, 0, 98, "W_atk")  # 0 : 0 : 60 +체력흡수 98
# 3월의 기억으로 구매
W_atk_item_301 = W_atk_item("칠흑의 검", 90, 40, 25, 70, 0, 0, 0, 0, "W_atk")  # 70 : 0 : 0
W_atk_item_302 = W_atk_item("흑백의 도끼", 81, 40, 25, 35, 0, 35, 0, 41, "W_atk")  # 35 : 0 : 35 +체력흡수 41
W_atk_item_303 = W_atk_item("거북의 방패", 63, 30, 25, 0, 0, 70, 0, 126, "W_atk")  # 0 : 0 : 70 +체력흡수 126
W_atk_item_304 = W_atk_item("푸른 불꽃검", 110, 50, 30, 90, 0, 0, 0, 0, "W_atk")  # 90 : 0 : 0
W_atk_item_305 = W_atk_item("악마 도끼", 99, 50, 30, 45, 0, 45, 0, 50, "W_atk")  # 45 : 0 : 45 +체력흡수 50
W_atk_item_306 = W_atk_item("순백의 방패", 77, 50, 30, 0, 0, 90, 0, 154, "W_atk")  # 0 : 0 : 90 +체력흡수 154
# 4월의 기억으로 구매
W_atk_item_401 = W_atk_item("은빛 하늘검", 130, 40, 35, 100, 0, 90, 0, 0,"W_atk")  # 100 : 0 : 0
W_atk_item_402 = W_atk_item("금빛 하늘검", 160, 50, 40, 120, 0, 45, 0, 0,"W_atk")  # 120 : 0 : 45
W_atk_item_403 = W_atk_item("자연의 일부", 144, 50, 40, 60, 0, 60, 0, 144,"W_atk")  # 60 : 0 : 60 +체력흡수 144


# 1월의 기억으로 구매
W_def_item_111 = W_def_item("녹슨 철 투구",5,15,1,10,0,0,0,0,0,0,"W_def")
W_def_item_112 = W_def_item("녹슨 철 갑옷",5,15,2,10,0,0,0,0,0,0,"W_def")
W_def_item_113 = W_def_item("녹슨 철 바지",5,15,3,10,0,0,0,0,0,0,"W_def")
W_def_item_114 = W_def_item("녹슨 철 신발",5,15,4,10,0,0,0,0,0,0,"W_def")
# 2월의 기억으로 구매
W_def_item_211 = W_def_item("힘의 철 투구",20,20,1,20,50,0,0,5,0,0,"W_def") # 힘 + 5 / 요구 힘 : 50
W_def_item_212 = W_def_item("힘의 철 갑옷",20,20,2,20,50,0,0,5,0,0,"W_def")
W_def_item_213 = W_def_item("힘의 철 바지",20,20,3,20,50,0,0,5,0,0,"W_def")
W_def_item_214 = W_def_item("힘의 철 신발",20,20,4,20,50,0,0,5,0,0,"W_def")
W_def_item_221 = W_def_item("민첩의 철 투구",15,22,1,20,0,50,0,0,5,0,"W_def") # 민첩 + 5 / 요구 민첩 : 50
W_def_item_222 = W_def_item("민첩의 철 갑옷",15,22,2,20,0,50,0,0,5,0,"W_def")
W_def_item_223 = W_def_item("민첩의 철 바지",15,22,3,20,0,50,0,0,5,0,"W_def")
W_def_item_224 = W_def_item("민첩의 철 신발",15,22,4,20,0,50,0,0,5,0,"W_def")
W_def_item_231 = W_def_item("모험의 철 투구",30,22,1,20,0,0,50,0,0,50,"W_def") # 추가 체력 + 50 / 요구 모험 : 50
W_def_item_232 = W_def_item("모험의 철 갑옷",30,22,2,20,0,0,50,0,0,50,"W_def")
W_def_item_233 = W_def_item("모험의 철 바지",30,22,3,20,0,0,50,0,0,50,"W_def")
W_def_item_234 = W_def_item("모험의 철 신발",30,22,4,20,0,0,50,0,0,50,"W_def")
# 3월의 기억으로 구매
W_def_item_311 = W_def_item("힘의 적표범 투구",30,22,1,30,85,0,0,10,0,0,"W_def") # 힘 + 10 / 요구 힘 : 85
W_def_item_312 = W_def_item("힘의 적표범 갑옷",30,22,2,30,85,0,0,10,0,0,"W_def")
W_def_item_313 = W_def_item("힘의 적표범 바지",30,22,3,30,85,0,0,10,0,0,"W_def")
W_def_item_314 = W_def_item("힘의 적표범 신발",30,22,4,30,85,0,0,10,0,0,"W_def")
W_def_item_321 = W_def_item("민첩의 적표범 투구",20,22,1,30,0,85,0,0,20,0,"W_def") # 민첩 + 20 / 요구 민첩 : 85
W_def_item_322 = W_def_item("민첩의 적표범 갑옷",20,22,2,30,0,85,0,0,20,0,"W_def")
W_def_item_323 = W_def_item("민첩의 적표범 바지",20,22,3,30,0,85,0,0,20,0,"W_def")
W_def_item_324 = W_def_item("민첩의 적표범 신발",20,22,4,30,0,85,0,0,20,0,"W_def")
W_def_item_331 = W_def_item("모험의 적표범 투구",40,22,1,30,0,0,85,0,0,100,"W_def") # 추가체력 + 100 / 요구 모험 : 85
W_def_item_332 = W_def_item("모험의 적표범 갑옷",40,22,2,30,0,0,85,0,0,100,"W_def")
W_def_item_333 = W_def_item("모험의 적표범 바지",40,22,3,30,0,0,85,0,0,100,"W_def")
W_def_item_334 = W_def_item("모험의 적표범 신발",40,22,4,30,0,0,85,0,0,100,"W_def")
# 4월의 기억으로 구매
W_def_item_411 = W_def_item("힘의 칠흑 투구",50,25,1,40,120,0,0,15,0,0,"W_def") # 힘 + 15 / 요구 힘 : 120
W_def_item_412 = W_def_item("힘의 칠흑 갑옷",50,25,2,40,120,0,0,15,0,0,"W_def")
W_def_item_413 = W_def_item("힘의 칠흑 바지",50,25,3,40,120,0,0,15,0,0,"W_def")
W_def_item_414 = W_def_item("힘의 칠흑 신발",50,25,4,40,120,0,0,15,0,0,"W_def")
W_def_item_421 = W_def_item("민첩의 칠흑 투구",25,25,1,40,0,120,0,0,35,0,"W_def") # 민첩 + 35 / 요구 민첩 : 120
W_def_item_422 = W_def_item("민첩의 칠흑 갑옷",25,25,2,40,0,120,0,0,35,0,"W_def")
W_def_item_423 = W_def_item("민첩의 칠흑 바지",25,25,3,40,0,120,0,0,35,0,"W_def")
W_def_item_424 = W_def_item("민첩의 칠흑 신발",25,25,4,40,0,120,0,0,35,0,"W_def")
W_def_item_431 = W_def_item("모험의 칠흑 투구",70,25,1,40,0,0,120,0,0,200,"W_def") # 추가체력 + 200 / 요구 모험 : 120
W_def_item_432 = W_def_item("모험의 칠흑 갑옷",70,25,2,40,0,0,120,0,0,200,"W_def")
W_def_item_433 = W_def_item("모험의 칠흑 바지",70,25,3,40,0,0,120,0,0,200,"W_def")
W_def_item_434 = W_def_item("모험의 칠흑 신발",70,25,4,40,0,0,120,0,0,200,"W_def")
# 5월의 기억으로 구매
W_def_item_511 = W_def_item("힘의 기사 투구",70,30,1,50,150,0,0,30,0,0,"W_def") # 힘 + 30 / 요구 힘 : 150
W_def_item_512 = W_def_item("힘의 기사 갑옷",70,30,2,50,150,0,0,30,0,0,"W_def")
W_def_item_513 = W_def_item("힘의 기사 바지",70,30,3,50,150,0,0,30,0,0,"W_def")
W_def_item_514 = W_def_item("힘의 기사 신발",70,30,4,50,150,0,0,30,0,0,"W_def")
W_def_item_521 = W_def_item("민첩의 기사 투구",50,30,1,50,0,150,0,0,60,0,"W_def") # 민첩 + 60 / 요구 민첩 : 150
W_def_item_522 = W_def_item("민첩의 기사 갑옷",50,30,2,50,0,150,0,0,60,0,"W_def")
W_def_item_523 = W_def_item("민첩의 기사 바지",50,30,3,50,0,150,0,0,60,0,"W_def")
W_def_item_524 = W_def_item("민첩의 기사 신발",50,30,4,50,0,150,0,0,60,0,"W_def")
W_def_item_531 = W_def_item("모험의 기사 투구",100,30,1,50,0,0,150,0,0,400,"W_def") # 추가체력 + 400 / 요구 모험 : 150
W_def_item_532 = W_def_item("모험의 기사 갑옷",100,30,2,50,0,0,150,0,0,400,"W_def")
W_def_item_533 = W_def_item("모험의 기사 바지",100,30,3,50,0,0,150,0,0,400,"W_def")
W_def_item_534 = W_def_item("모험의 기사 신발",100,30,4,50,0,0,150,0,0,400,"W_def")


# 50레벨 퀘스트 아이템
P_atk_item_501 = P_atk_item("불완전한 홍염의 날갯깃",320,50,30,150,"P_atk")

P_def_item_611 = P_def_item("부서진 핀그리드의 투구",75,50,1,20,20,20,"P_def")
P_def_item_612 = P_def_item("부서진 핀그리드의 갑옷",75,50,2,20,20,20,"P_def")
P_def_item_613 = P_def_item("부서진 핀그리드의 바지",75,50,3,20,20,20,"P_def")
P_def_item_614 = P_def_item("부서진 핀그리드의 신발",75,50,4,20,20,20,"P_def")


# 렉스의 명작
R_atk_item_601 = R_r_atk_item("렉스의 1번째 명작 '홍염의 날개깃'",250,70,70,70,10,300,"Rex's masterpiece")
R_atk_item_602 = R_r_atk_item("렉스의 2번째 명작 '칼날 그림자'",100,0,140,0,70,0,"Rex's masterpiece")
R_atk_item_603 = R_r_atk_item("렉스의 3번째 명작 '녹색 이빨'",0,0,0,0,0,00,"Rex's masterpiece")
R_atk_item_604 = R_r_atk_item("렉스의 4번째 명작 '붉은 손아귀'",50,20,20,0,10,0,"Rex's masterpiece")
R_atk_item_605 = R_r_atk_item("렉스의 5번째 명작 '인어의 검'",60,60,0,50,0,200,"Rex's masterpiece")
R_atk_item_606 = R_r_atk_item("렉스의 6번째 명작 '불굴의 대지'",10,0,0,120,0,400,"Rex's masterpiece")

R_atk_item_611 = R_r_atk_item("렉스의 7번째 명작 '고대갑주 쿠구'",30,0,0,0,100,0,0,"Rex's masterpiece")
R_atk_item_612 = R_r_atk_item("렉스의 8번째 명작 '고대갑주 갑옷'",100,0,0,0,0,0,100,"Rex's masterpiece")
R_atk_item_613 = R_r_atk_item("렉스의 9번째 명작 '고대갑주 바지'",60,35,35,35,0,0,0,"Rex's masterpiece")
R_atk_item_614 = R_r_atk_item("렉스의 10번째 명작 '고대갑주 신발'",5,0,0,0,0,100,0,"Rex's masterpiece")


# 강화서
fortification_item_101 = fortification_item("하급 무기강화", 200000, "+ 3~18 데미지 (레벨 제한 3)")
fortification_item_201 = fortification_item("중급 무기강화", 200000, "+ 3~27 데미지 (레벨 제한 4)")
fortification_item_202 = fortification_item("고급 무기강화", 600000, "+ 18~27 데미지 (레벨 제한 5)")
fortification_item_203 = fortification_item("힘 강화", 200000, "+ 3~9 데미지 (힘 스텟 제한 20")
fortification_item_204 = fortification_item("민첩 강화", 200000, "크리티컬 + 3~5% (민첩 스텟 제한 20)")
fortification_item_205 = fortification_item("모험 강화", 200000, "체력흡수 + 16~39 (모험 스텟 제한 20)")
fortification_item_206 = fortification_item("방어구 강화", 600000, "+ 3~18 방어력 (레벨 제한 10)")
fortification_item_301 = fortification_item("저주받은 공격력 강화", 2000000, "+ 200 데미지 (체력 흡수 -50)")
fortification_item_302 = fortification_item("저주받은 크티티컬 강화", 2000000, "크리티컬 + 8% (체력 흡수 -50)")
fortification_item_303 = fortification_item("저주받은 방어구 강화", 2000000, "체력증가 + 500 (방어력 -50)")
fortification_item_401 = fortification_item("어둠의 강화", 1000000, "+ 25 데미 (레벨 제한 55)")



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



W_atk_item_list = [W_atk_item_101, W_atk_item_102, W_atk_item_103, W_atk_item_104, W_atk_item_105, W_atk_item_106, \
                   W_atk_item_201, W_atk_item_202, W_atk_item_203, W_atk_item_204, W_atk_item_205, W_atk_item_206,
                   W_atk_item_207, W_atk_item_208, W_atk_item_209, \
                   W_atk_item_301, W_atk_item_302, W_atk_item_303, W_atk_item_304, W_atk_item_305, W_atk_item_306, \
                   W_atk_item_401, W_atk_item_402, W_atk_item_403]

W_atk_item_list_1 = [W_atk_item_101, W_atk_item_102, W_atk_item_103, W_atk_item_104, W_atk_item_105, W_atk_item_106]
W_atk_item_list_2 = [W_atk_item_201, W_atk_item_202, W_atk_item_203, W_atk_item_204, W_atk_item_205, W_atk_item_206, W_atk_item_207, W_atk_item_208, W_atk_item_209]
W_atk_item_list_3 = [W_atk_item_301, W_atk_item_302, W_atk_item_303, W_atk_item_304, W_atk_item_305, W_atk_item_306]
W_atk_item_list_4 = [W_atk_item_401, W_atk_item_402, W_atk_item_403]


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

re_item_list = []
food_item_list = []

nomal_item_list = [month_item_01, month_item_02, month_item_03, month_item_04, month_item_05, \
                   month_item_06, month_item_07, month_item_08, month_item_09, month_item_10, month_item_11]

shop_item_list = {'atk': W_atk_item_list, 'def': def_item_list, 'food': food_item_list}


# 아이템 정보 프린트 (1)
def print_item_1(item):
    if item.use == 'W_atk':
        print("{0:^25}{1:^10}{2:^10}{3:^10}{4:^10}".format(item.name, item.damage, item.cost \
                                                           , item.reinforce, item.liv))
    elif item.use == 'def':
        print("{0:^25}{1:^10}{2:^10}{3:^10}{4:^10}".format(item.name, item.defense, item.cost \
                                                           , item.reinforce, item.liv))
    elif item.use == 're':
        print("{0:^25}{1:^10}{2:^10}{3:^10}".format(item.name, item.recovery, item.cost, item.liv))

    elif item.use == 'food':
        print("{0:^25}{1:^10}{2:^10}".format(item.name, item.re_hunger, item.cost))

    elif item.use == 'item':
        print("{0:^25}".format(item.name))


# 아이템 정보 프린트 (2)
def print_item_2(item):
    if item.use == 'W_atk':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format( \
            '이름', item.name, \
            '공격력', item.damage, \
            '가격', item.cost, \
            '무기레벨', item.liv))
    elif item.use == 'def':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format( \
            '이름', item.name, \
            '방어력', item.defense, \
            '가격', item.cost, \
            '강화', item.durability, \
            '제한레벨', item.liv))
    elif item.use == 're':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}".format( \
            '이름', item.name, \
            '체력회복', item.recovery, \
            '가격', item.cost, \
            '제한레벨', item.liv))


# 장착보기
def atk_def_inventory(item):
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


# 몬스터 클래스
class monster:
    def __init__(self, name, health, damage, drop_money, drop_item, spawn_point, liv):
        self.name = name
        self.health = health
        self.damage = damage
        self.drop_money = drop_money
        self.drop_item = drop_item
        self.spawn_point = spawn_point
        self.liv = liv


# 몬스터 프린트
def print_mon(mon, health):
    print("\n\n{0:=^25}".format("Lv." + str(mon.liv) + "_" + mon.name))
    print("{0} : {1}\n{2} : {3}\n{4} : {5}".format( \
        '이름', mon.name, \
        '체력', health, \
        '공격력', mon.damage))


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
                player_1.health += 6
                print("체력이 6 추가 됩니다.")
                c_count += 1
                break
            elif sel == 'n':
                continue
        else:
            print("올바른 문자를 입력하세요")
    else:
        pass


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
        return "food"
    elif word == 't':
        return "drop"
    elif word == 'y':
        return "item"


def change_4(player_1, word):
    if word == 'atk':
        return player_1.damage
    elif word == 'def':
        return player_1.defense
    elif word == 're':
        return player_1.health


def change_5(player_1, word, num):
    if word == 'atk':
        return player_1.equipment[word][num].damage
    elif word == 'def':
        return player_1.equipment[word][num].defense


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


def change_8(player_1):
    if player_1.point == 1:
        return '에나'
    else:
        return ' - '


# 인벤토리
def inventory(self):
    while True:
        ans = input("\n인벤토리를 선택하세요 [무기(q) /방어구(w) /포션(e) /음식(r) /드랍(t) /일반(y)]")
        print("나가려면 (enter)")
        if ans == "q" or ans == "w" or ans == "e" or ans == "r" or ans == "t" or ans == "y":
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
        if sel == 'atk' or sel == 'def':
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
            elif ans == 're' or ans == 'food':
                re_food_use(self, ans, self.inven[sel], ans_2)
        elif ans_2 == "":
            break
        else:
            print("올바른 숫자를 입력하세요")


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

        # story()

        player_name = input("\n플레이어 이름을 입력하십시오. = ")
        while player_name == "":
            print("\n유효한 이름을 입력하십시오")
            player_name = input("플레이어 이름을 입력하십시오. = ")
        player_1 = Player(player_name, 1.1, [], [], 100, 0, 0 ,0, 0, 50, 0, 0)

        player_x = 50
        player_y = 50

        player_liv = 0

        move_count = 0

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

        # 마을 버프
        if player_1.point == 1 or player_1.point == 1.1:
            player_1.health = player_1.health + 50

        # 체력,허기 최대치
        if player_1.health > higt_health:
            player_1.health = higt_health

        player_1.showinfo()

        print("나의 위치 (" + change_8(player_1) + ") : " + str(player_x) + "," + str(player_y))

        if plag == 0:
            print("\n도움을 원한다면 'h' 입력")

        plag += 1

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

        # 위치

        '''
        if self.exp >=:

        if self.health <= 0:
            self.money -= int(self.money / 2)
            print("가장 가까운 마을로 리스폰 됩니다")
            self.health = 100
            player_x =
            player_y =
        '''
        plag += 1


if __name__ == "__main__":
    main()

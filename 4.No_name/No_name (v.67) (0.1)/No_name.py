from random import choice
from random import randint
import time

print("\nthe No_name game project\n")



# 플레이어 클래스
class Player:
    def __init__(self, name, point, equipment, inven, print_inven, health, max_health, stats_health, result_health,
                 money, damage, critical, defense, def_physical_absorption, atk_physical_absorption, liv, exp, po_count,
                 plus_po_count, ag_count, plus_ag_count, ad_count, plus_ad_count, player_x, player_y, warp_manager):
        self.name = name
        self.point = point
        self.equipment = {"atk": ["없음"], "def_1": ["없음"], "def_2": ["없음"], "def_3": ["없음"], "def_4": ["없음"]}
        self.inven = {"atk": [], "def": [], "potion": [], "month": [], "item": []}
        self.print_inven = []
        self.health = health
        self.max_health = max_health
        self.stats_health = stats_health
        self.result_health = result_health
        self.money = money
        self.damage = damage
        self.critical = critical
        self.defense = defense
        self.def_physical_absorption = def_physical_absorption
        self.atk_physical_absorption = atk_physical_absorption
        self.liv = liv
        self.exp = exp
        self.po_count = po_count
        self.plus_po_count = plus_po_count
        self.ag_count = ag_count
        self.plus_ag_count = plus_ag_count
        self.ad_count = ad_count
        self.plus_ad_count = plus_ad_count
        self.player_x = player_x
        self.player_y = player_y
        self.warp_manager = []



# 무기,방어구 클래스

# 흰색 (노말) 무기 아이템 클래스
class W_atk_item:
    def __init__(self, liv, name, damage, month, cost, need_liv, need_power_stats, need_agility_stats, need_adventure_stats, critical,
                 physical_absorption, count, use):
        self.liv = liv
        self.name = name
        self.damage = damage
        self.month = month
        self.cost = cost
        self.need_liv = need_liv
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.count = count
        self.use = use

# 1월의 기억으로 구매
W_atk_item_101 = W_atk_item(0, "검", 3, 1, 15, 1, 0, 0, 0, 0, 0, 1, "atk")
W_atk_item_102 = W_atk_item(0, "몽둥이", 3, 1, 15, 1, 0, 0, 0, 0, 0, 1, "atk")
W_atk_item_103 = W_atk_item(0, "철검", 13, 1, 30, 5, 0, 0, 0, 0, 0, 1, "atk")
W_atk_item_104 = W_atk_item(0, "도끼", 13, 1, 30, 5, 0, 0, 0, 0, 0, 1, "atk")
W_atk_item_105 = W_atk_item(0, "예리한 대검", 30, 1, 65, 10, 0, 0, 0, 0, 0, 1, "atk")
W_atk_item_106 = W_atk_item(0, "예리한 도끼", 30, 1, 65, 10, 0, 0, 0, 0, 0, 1, "atk")
# 2월의 기억으로 구매
W_atk_item_201 = W_atk_item(0, "반짝이는 검", 45, 2, 25, 15, 40, 0, 0, 0, 0, 0, "atk")  # 40 : 0 : 0
W_atk_item_202 = W_atk_item(0, "반짝이는 도끼", 45, 2, 25, 15, 20, 0, 20, 0, 45, 0, "atk")  # 20 : 0 : 20 +체력흡수 45
W_atk_item_203 = W_atk_item(0, "강철 단검", 35, 2, 20, 15, 0, 40, 0, 6, 0, 0, "atk")  # 0 : 40 : 0 +크리티컬 6%
W_atk_item_204 = W_atk_item(0, "무쇠 건틀릿", 45, 2, 25, 15, 20, 20, 0, 0, 0, 0, "atk")  # 20 : 20 : 0
W_atk_item_205 = W_atk_item(0, "푸른 방패", 35, 2, 20, 15, 0, 0, 20, 0, 100, 0, "atk")  # 0 : 0 : 40 +체력흡수 100
W_atk_item_206 = W_atk_item(0, "붉은 검", 70, 2, 40, 20, 60, 0, 20, 0, 0, 0, "atk")  # 60 : 0 : 20
W_atk_item_207 = W_atk_item(0, "붉은 도끼", 63, 2, 40, 20, 30, 0, 30, 0, 63, 0, "atk")  # 30 : 0 : 30 +체력흡수 63
W_atk_item_208 = W_atk_item(0, "붉은 단검", 59, 2, 40, 20, 0, 60, 0, 15, 63, 0, "atk")  # 0 : 60 : 0 +체력흡수 63 +크리티컬 15%
W_atk_item_209 = W_atk_item(0, "강철 방패", 49, 2, 50, 20, 0, 0, 60, 0, 98, 0, "atk")  # 0 : 0 : 60 +체력흡수 98

# 스텟별 아이템 (2,3월의 기억으로 구매)
W_atk_item_241 = W_atk_item(0, "초보자용 대검", 58, 2, 30, 10, 50, 0, 0, -20, 0, 0, "atk") # 50 : 0 : 0 -크리티컬 20%
W_atk_item_242 = W_atk_item(0, "날카로운 강철장검", 82, 2, 40, 20, 100, 0, 0, -20, 0, 0, "atk") # 100 : 0 : 0 -크리티컬 20%
W_atk_item_341 = W_atk_item(0, "길들여진 전쟁장검", 104, 3, 30, 30, 150, 0, 0, -20, 0, 0, "atk") # 150 : 0 : 0 -크리티컬 20%
W_atk_item_342 = W_atk_item(0, "전장의 공포장검", 127, 3, 50, 40, 200, 0, 0, -20, 0, 0, "atk") # 200 : 0 : 0 -크리티컬 20%

W_atk_item_251 = W_atk_item(0, "기본 단검", 33, 2, 30, 10, 0, 50, 0, 13, 0, 0, "atk") # 0 : 50 : 0 +크리티컬 13%
W_atk_item_252 = W_atk_item(0, "빛나는 강철단검", 66, 2, 50, 20, 0, 100, 0, 21, 0, 0, "atk") # 0 : 100 : 0 +크리티컬 21%
W_atk_item_351 = W_atk_item(0, "푸른 은색단검", 89, 3, 30, 30, 0, 150, 0, 29, 0, 0, "atk") # 0 : 150 : 0 +크리티컬 29%
W_atk_item_352 = W_atk_item(0, "붉은 전쟁단검", 101, 3, 50, 40, 0, 200, 0, 35, 0, 0, "atk") # 0 : 200 : 0 +크리티컬 35%

W_atk_item_261 = W_atk_item(0, "녹슨 손도끼", 19, 2, 30, 10, 25, 25, 0, 0, 0, 0, "atk") # 25 : 25 : 0
W_atk_item_262 = W_atk_item(0, "사냥용 푸른도끼", 42, 2, 50, 20, 50, 50, 0, 0, 0, 0, "atk") # 50 : 50 : 0
W_atk_item_361 = W_atk_item(0, "날카로운 전쟁도끼", 64, 3, 30, 30, 75, 75, 0, 0, 0, 0, "atk") # 75 : 75 : 0
W_atk_item_362 = W_atk_item(0, "금빛 공포도끼", 132, 3, 50, 40, 0, 100, 100, 0, 0, 0, "atk") # 100 : 100 : 0

W_atk_item_271 = W_atk_item(0, "나무 방패", 52, 2, 30, 10, 0, 0, 50, 0, 0, 0, "atk") # 0 : 0 : 50
W_atk_item_272 = W_atk_item(0, "강철 방패", 73, 2, 50, 20, 0, 0, 100, 0, 73, 0, "atk") # 0 : 0 : 100 +체력흡수 73
W_atk_item_371 = W_atk_item(0, "단단한 전쟁방패", 55, 3, 30, 30, 0, 0, 150, 0, 0, 0, "atk") # 0 : 0 : 150 +체력흡수 102
W_atk_item_372 = W_atk_item(0, "찬란한 전쟁공포 방패", 89, 3, 50, 40, 0, 0, 200, 0, 0, 0, "atk") # 0 : 0 : 200 +체력흡수 63

# 3월의 기억으로 구매
W_atk_item_301 = W_atk_item(0, "칠흑의 검", 90, 3, 40, 25, 70, 0, 0, 0, 0, 0, "atk")  # 70 : 0 : 0
W_atk_item_302 = W_atk_item(0, "흑백의 도끼", 81, 3, 40, 25, 35, 0, 35, 0, 41, 0, "atk")  # 35 : 0 : 35 +체력흡수 41
W_atk_item_303 = W_atk_item(0, "거북의 방패", 63, 3, 30, 25, 0, 0, 70, 0, 126, 0, "atk")  # 0 : 0 : 70 +체력흡수 126
W_atk_item_304 = W_atk_item(0, "푸른 불꽃검", 110, 3, 50, 30, 90, 0, 0, 0, 0, 0, "atk")  # 90 : 0 : 0
W_atk_item_305 = W_atk_item(0, "악마 도끼", 99, 3, 50, 30, 45, 0, 45, 0, 50, 0, "atk")  # 45 : 0 : 45 +체력흡수 50
W_atk_item_306 = W_atk_item(0, "순백의 방패", 77, 3, 50, 30, 0, 0, 90, 0, 154, 0, "atk")  # 0 : 0 : 90 +체력흡수 154
# 4월의 기억으로 구매
W_atk_item_401 = W_atk_item(0, "은빛 하늘검", 130, 4, 40, 35, 100, 0, 90, 0, 0, 0, "atk")  # 100 : 0 : 0
W_atk_item_402 = W_atk_item(0, "금빛 하늘검", 160, 4, 50, 40, 120, 0, 45, 0, 0, 0, "atk")  # 120 : 0 : 45
W_atk_item_403 = W_atk_item(0, "자연의 일부", 144, 4, 50, 40, 60, 0, 60, 0, 144, 0, "atk")  # 60 : 0 : 60 +체력흡수 144

point_1_atk_shop = []
point_2_atk_shop = []
point_3_atk_shop = []
point_5_atk_shop = []
point_19_atk_shop = []
point_22_atk_shop = []
point_28_atk_shop = []
point_36_atk_shop = []

# 흰색 (노말) 방어구 아이템 클래스
class W_def_item:
    def __init__(self, liv, name, defense, month, cost, part, need_liv, need_power_stats, need_agility_stats, need_adventure_stats,
                 plus_power_stats, plus_agility_stats, physical_absorption, count, use):
        self.liv = liv
        self.name = name
        self.defense = defense
        self.month = month
        self.cost = cost
        self.part = part
        self.need_liv = need_liv
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.physical_absorption = physical_absorption
        self.count = count
        self.use = use

W_def_item_001 = W_def_item(0, "가죽 갑옷", 1, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, "def")
W_def_item_002 = W_def_item(0, "가죽 신발", 1, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, "def")
# 1월의 기억으로 구매
W_def_item_111 = W_def_item(0, "녹슨 청동 투구", 5, 1, 15, 1, 10, 0, 0, 0, 0, 0, 0, 0, "def")
W_def_item_112 = W_def_item(0, "녹슨 청동 갑옷", 5, 1, 15, 2, 10, 0, 0, 0, 0, 0, 0, 0, "def")
W_def_item_113 = W_def_item(0, "녹슨 청동 바지", 5, 1, 15, 3, 10, 0, 0, 0, 0, 0, 0, 0, "def")
W_def_item_114 = W_def_item(0, "녹슨 청동 신발", 5, 1, 15, 4, 10, 0, 0, 0, 0, 0, 0, 0, "def")
# 2월의 기억으로 구매
W_def_item_211 = W_def_item(0, "초보 전사의 모자", 20, 2, 20, 1, 20, 50, 0, 0, 5, 0, 0, 0, "def")  # 힘 + 5 / 요구 힘 : 50
W_def_item_212 = W_def_item(0, "초보 전사의 갑옷", 20, 2, 20, 2, 20, 50, 0, 0, 5, 0, 0, 0, "def")
W_def_item_213 = W_def_item(0, "초보 전사의 바지", 20, 2, 20, 3, 20, 50, 0, 0, 5, 0, 0, 0, "def")
W_def_item_214 = W_def_item(0, "초보 전사의 신발", 20, 2, 20, 4, 20, 50, 0, 0, 5, 0, 0, 0, "def")
W_def_item_221 = W_def_item(0, "초보 암살자의 모자", 15, 2, 22, 1, 20, 0, 50, 0, 0, 5, 0, 0, "def")  # 민첩 + 5 / 요구 민첩 : 50
W_def_item_222 = W_def_item(0, "초보 암살자의 갑옷", 15, 2, 22, 2, 20, 0, 50, 0, 0, 5, 0, 0, "def")
W_def_item_223 = W_def_item(0, "초보 암살자의 바지", 15, 2, 22, 3, 20, 0, 50, 0, 0, 5, 0, 0, "def")
W_def_item_224 = W_def_item(0, "초보 암살자의 신발", 15, 2, 22, 4, 20, 0, 50, 0, 0, 5, 0, 0, "def")
W_def_item_231 = W_def_item(0, "초보 모험가의 모자", 30, 2, 22, 1, 20, 0, 0, 50, 0, 0, 50, 0, "def")  # 추가 체력 + 50 / 요구 모험 : 50
W_def_item_232 = W_def_item(0, "초보 모험가의 갑옷", 30, 2, 22, 2, 20, 0, 0, 50, 0, 0, 50, 0, "def")
W_def_item_233 = W_def_item(0, "초보 모험가의 바지", 30, 2, 22, 3, 20, 0, 0, 50, 0, 0, 50, 0, "def")
W_def_item_234 = W_def_item(0, "초보 모험가의 신발", 30, 2, 22, 4, 20, 0, 0, 50, 0, 0, 50, 0, "def")
# 3월의 기억으로 구매
W_def_item_311 = W_def_item(0, "숙련된 전사의 가죽모자", 30, 3, 22, 1, 30, 85, 0, 0, 10, 0, 0, 0, "def")  # 힘 + 10 / 요구 힘 : 85
W_def_item_312 = W_def_item(0, "숙련된 전사의 갑옷", 30, 3, 22, 2, 30, 85, 0, 0, 10, 0, 0, 0, "def")
W_def_item_313 = W_def_item(0, "숙련된 전사의 바지", 30, 3, 22, 3, 30, 85, 0, 0, 10, 0, 0, 0, "def")
W_def_item_314 = W_def_item(0, "숙련된 전사의 신발", 30, 3, 22, 4, 30, 85, 0, 0, 10, 0, 0, 0, "def")
W_def_item_321 = W_def_item(0, "숙련된 암살자의 모자", 20, 3, 22, 1, 30, 0, 85, 0, 0, 20, 0, 0, "def")  # 민첩 + 20 / 요구 민첩 : 85
W_def_item_322 = W_def_item(0, "숙련된 암살자의 갑옷", 20, 3, 22, 2, 30, 0, 85, 0, 0, 20, 0, 0, "def")
W_def_item_323 = W_def_item(0, "숙련된 암살자의 바지", 20, 3, 22, 3, 30, 0, 85, 0, 0, 20, 0, 0, "def")
W_def_item_324 = W_def_item(0, "숙련된 암살자의 신발", 20, 3, 22, 4, 30, 0, 85, 0, 0, 20, 0, 0, "def")
W_def_item_331 = W_def_item(0, "숙련돤 모험가의 모자", 40, 3, 22, 1, 30, 0, 0, 85, 0, 0, 100, 0, "def")  # 추가체력 + 100 / 요구 모험 : 85
W_def_item_332 = W_def_item(0, "숙련된 모험가의 갑옷", 40, 3, 22, 2, 30, 0, 0, 85, 0, 0, 100, 0, "def")
W_def_item_333 = W_def_item(0, "숙련된 모험가의 바지", 40, 3, 22, 3, 30, 0, 0, 85, 0, 0, 100, 0, "def")
W_def_item_334 = W_def_item(0, "숙련된 모험가의 신발", 40, 3, 22, 4, 30, 0, 0, 85, 0, 0, 100, 0, "def")
# 4월의 기억으로 구매
W_def_item_411 = W_def_item(0, "금장 철모자", 50, 4, 25, 1, 40, 120, 0, 0, 15, 0, 0, 0, "def")  # 힘 + 15 / 요구 힘 : 120
W_def_item_412 = W_def_item(0, "금장 철갑옷", 50, 4, 25, 2, 40, 120, 0, 0, 15, 0, 0, 0, "def")
W_def_item_413 = W_def_item(0, "금장 철바지", 50, 4, 25, 3, 40, 120, 0, 0, 15, 0, 0, 0, "def")
W_def_item_414 = W_def_item(0, "금장 철신발", 50, 4, 25, 4, 40, 120, 0, 0, 15, 0, 0, 0, "def")
W_def_item_421 = W_def_item(0, "실전용 암살자의 모자", 25, 4, 25, 1, 40, 0, 120, 0, 0, 35, 0, 0, "def")  # 민첩 + 35 / 요구 민첩 : 120
W_def_item_422 = W_def_item(0, "실전용 암살자의 갑옷", 25, 4, 25, 2, 40, 0, 120, 0, 0, 35, 0, 0, "def")
W_def_item_423 = W_def_item(0, "실전용 암살자의 바지", 25, 4, 25, 3, 40, 0, 120, 0, 0, 35, 0, 0, "def")
W_def_item_424 = W_def_item(0, "실전용 암살자의 신발", 25, 4, 25, 4, 40, 0, 120, 0, 0, 35, 0, 0, "def")
W_def_item_431 = W_def_item(0, "탐험용 모험가의 모자", 70, 4, 25, 1, 40, 0, 0, 120, 0, 0, 200, 0, "def")  # 추가체력 + 200 / 요구 모험 : 120
W_def_item_432 = W_def_item(0, "탐험용 모험가의 갑옷", 70, 4, 25, 2, 40, 0, 0, 120, 0, 0, 200, 0, "def")
W_def_item_433 = W_def_item(0, "탐험용 모험가의 바지", 70, 4, 25, 3, 40, 0, 0, 120, 0, 0, 200, 0, "def")
W_def_item_434 = W_def_item(0, "탐험용 모험가의 신발", 70, 4, 25, 4, 40, 0, 0, 120, 0, 0, 200, 0, "def")
# 5월의 기억으로 구매
W_def_item_511 = W_def_item(0, "보라빛나는 강철모자", 70, 5, 30, 1, 50, 150, 0, 0, 30, 0, 0, 0, "def")  # 힘 + 30 / 요구 힘 : 150
W_def_item_512 = W_def_item(0, "보라빛나는 강철갑옷", 70, 5, 30, 2, 50, 150, 0, 0, 30, 0, 0, 0, "def")
W_def_item_513 = W_def_item(0, "보라빛나는 강철바지", 70, 5, 30, 3, 50, 150, 0, 0, 30, 0, 0, 0, "def")
W_def_item_514 = W_def_item(0, "보라빛나는 강철신발", 70, 5, 30, 4, 50, 150, 0, 0, 30, 0, 0, 0, "def")
W_def_item_521 = W_def_item(0, "검붉은 암살전용 모자", 50, 5, 30, 1, 50, 0, 150, 0, 0, 60, 0, 0, "def")  # 민첩 + 60 / 요구 민첩 : 150
W_def_item_522 = W_def_item(0, "검붉은 암살전용 갑옷", 50, 5, 30, 2, 50, 0, 150, 0, 0, 60, 0, 0, "def")
W_def_item_523 = W_def_item(0, "검붉은 암살전용 바지", 50, 5, 30, 3, 50, 0, 150, 0, 0, 60, 0, 0, "def")
W_def_item_524 = W_def_item(0, "검붉은 암살전용 신발", 50, 5, 30, 4, 50, 0, 150, 0, 0, 60, 0, 0, "def")
W_def_item_531 = W_def_item(0, "유적 탐험전용 모자", 100, 5, 30, 1, 50, 0, 0, 150, 0, 0, 400, 0, "def")  # 추가체력 + 400 / 요구 모험 : 150
W_def_item_532 = W_def_item(0, "유적 탐험전용 갑옷", 100, 5, 30, 2, 50, 0, 0, 150, 0, 0, 400, 0, "def")
W_def_item_533 = W_def_item(0, "유적 탐험전용 바지", 100, 5, 30, 3, 50, 0, 0, 150, 0, 0, 400, 0, "def")
W_def_item_534 = W_def_item(0, "유적 탐험전용 신발", 100, 5, 30, 4, 50, 0, 0, 150, 0, 0, 400, 0, "def")

point_1_def_shop = []
point_2_def_shop = []
point_3_def_shop = []
point_5_def_shop = []
point_19_def_shop = []
point_22_def_shop = []
point_28_def_shop = []
point_36_def_shop = []

# 보라색 (에픽) 무기 아이템 클래스
class P_atk_item:
    def __init__(self, liv, name, damage, need_liv, critical, physical_absorption, count, use):
        self.liv = liv
        self.name = name
        self.damage = damage
        self.need_liv = need_liv
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.count = count
        self.use = use

# 50레벨 퀘스트 아이템
P_atk_item_600 = P_atk_item(0, "불완전한 홍염의 날갯깃", 320, 50, 30, 150, 0, "atk")


# 보라색 (에픽) 방어구 아이템 클래스
class P_def_item:
    def __init__(self, liv, name, defense, need_liv, part, need_power_stats, need_agility_stats, need_adventure_stats, count, use):
        self.liv = liv
        self.name = name
        self.defense = defense
        self.need_liv = need_liv
        self.part = part
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.count = count
        self.use = use

# 50레벨 퀘스트 아이템
P_def_item_611 = P_def_item(0, "부서진 핀그리드의 투구", 75, 50, 1, 20, 20, 20, 0, "def")
P_def_item_612 = P_def_item(0, "부서진 핀그리드의 갑옷", 75, 50, 2, 20, 20, 20, 0, "def")
P_def_item_613 = P_def_item(0, "부서진 핀그리드의 바지", 75, 50, 3, 20, 20, 20, 0, "def")
P_def_item_614 = P_def_item(0, "부서진 핀그리드의 신발", 75, 50, 4, 20, 20, 20, 0, "def")


# 빨간색 (레전드) 렉스의 명작 무기 아이템 클래스
class R_r_atk_item:
    def __init__(self, liv, name, damage, need_power_stats, need_agility_stats, need_adventure_stats, critical,
                 physical_absorption, count, use):
        self.liv = liv
        self.name = name
        self.damage = damage
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.count = count
        self.use = use

# 렉스의 명작
R_atk_item_601 = R_r_atk_item(0, "렉스의 1번째 명작 '홍염의 날개깃'", 250, 70, 70, 70, 10, 300, 0, "atk")
R_atk_item_602 = R_r_atk_item(0, "렉스의 2번째 명작 '칼날 그림자'", 100, 140, 0, 0, 70, 0, 0, "atk")
R_atk_item_603 = R_r_atk_item(0, "렉스의 3번째 명작 '녹색 이빨'", 4, 0, 0, 0, 0, 0, 0, "atk")
R_atk_item_604 = R_r_atk_item(0, "렉스의 4번째 명작 '붉은 손아귀'", 50, 20, 20, 0, 10, 0, 0, "atk")
R_atk_item_605 = R_r_atk_item(0, "렉스의 5번째 명작 '인어의 검'", 60, 60, 0, 50, 0, 200, 0, "atk")
R_atk_item_606 = R_r_atk_item(0, "렉스의 6번째 명작 '불굴의 대지'", 10, 0, 0, 120, 0, 400, 0, "atk")

# 각성된 랙스의 명작
R_atk_item_621 = R_r_atk_item(0, "강화된 렉스의 1번째 명작 '그람'", 450, 80, 80, 80, 35, 350, 0, "atk")
R_atk_item_622 = R_r_atk_item(0, "강화된 렉스의 2번째 명작 '발뭉'", 200, 0, 140, 0, 70, 0, 0, "atk")
R_atk_item_623 = R_r_atk_item(0, "강화된 렉스의 3번째 명작 '레바테인'", 150, 0, 0, 0, 35, 0, 0, "atk")
R_atk_item_624 = R_r_atk_item(0, "강화된 렉스의 4번째 명작 '파프니르의 발톱'", 250, 70, 70, 0, 20, 0, 0, "atk")
R_atk_item_625 = R_r_atk_item(0, "강화된 렉스의 5번째 명작 '궁니르'", 120, 70, 0, 60, 0, 300, 0, "atk")
R_atk_item_626 = R_r_atk_item(0, "강화된 렉스의 6번째 명작 '란드그리드'", 10, 0, 0, 140, 0, 650, 0, "atk")


# 빨간색 (레전드) 렉스의 명작 방어구 아이템 클래스
class R_r_def_item:
    def __init__(self, liv, name, defense, part, need_power_stats, need_agility_stats, need_adventure_stats,
                 plus_power_stats, plus_agility_stats, plus_adventure_stats, count, use):
        self.liv = liv
        self.name = name
        self.defense = defense
        self.part = part
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.plus_adventure_stats = plus_adventure_stats
        self.count = count
        self.use = use

# 렉스의 명작
R_def_item_711 = R_r_def_item(0, "렉스의 7번째 명작 '고대갑주 투구'", 30, 1, 0, 0, 0, 100, 0, 0, 0, "def")
R_def_item_712 = R_r_def_item(0, "렉스의 8번째 명작 '고대갑주 갑옷'", 100, 2, 0, 0, 0, 0, 0, 100, 0, "def")
R_def_item_713 = R_r_def_item(0, "렉스의 9번째 명작 '고대갑주 바지'", 60, 3, 35, 35, 35, 0, 0, 0, 0, "def")
R_def_item_714 = R_r_def_item(0, "렉스의 10번째 명작 '고대갑주 신발'", 5, 4, 0, 0, 0, 0, 100, 0, 0, "def")

# 각성된 랙스의 명작
R_def_item_731 = R_r_def_item(0, "강화된 랙스의 7번째 명작 '필리아스의 쿠구'", 60, 1, 0, 0, 0, 100, 0, 0, 0, "def")
R_def_item_732 = R_r_def_item(0, "강화된 렉스의 8번째 명작 '필리아스의 갑옷'", 200, 2, 0, 0, 0, 0, 0, 100, 0, "def")
R_def_item_733 = R_r_def_item(0, "강화된 렉스의 9번째 명작 '필리아스의 바지'", 120, 3, 35, 35, 35, 0, 0, 0, 0, "def")
R_def_item_734 = R_r_def_item(0, "강화된 렉스의 10번째 명작 '필리아스의 신발'", 10, 4, 0, 0, 0, 0, 100, 0, 0, "def")


# 빨간색 (레전드) 사신수 무기 아이템 클래스
class R_s_atk_item:
    def __init__(self, liv, name, damage, need_liv, need_power_stats, need_agility_stats, need_adventure_stats, critical,
                 physical_absorption, count, use):
        self.liv = liv
        self.name = name
        self.damage = damage
        self.need_liv = need_liv
        self.need_power_stats = need_power_stats
        self.need_agility_stats = need_agility_stats
        self.need_adventure_stats = need_adventure_stats
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.count = count
        self.use = use

# 사신수 무기
R_atk_item_701 = R_s_atk_item(0, "사신수 무기 '청룡의 검'", 420, 50, 50, 50, 120, 20, 430, 0, "atk")
R_atk_item_702 = R_s_atk_item(0, "사신수 무기 '백호의 도끼'", 550, 50, 120, 0, 100, 0, 40, 0, "atk")
R_atk_item_703 = R_s_atk_item(0, "사신수 무기 '주작의 단검'", 300, 50, 20, 200, 0, 90, 0, 0, "atk")
R_atk_item_704 = R_s_atk_item(0, "사신수 무기 '현무의 창'", 400, 50, 110, 110, 0, 40, 0, 0, "atk")

# 각성한 사신수 무기
R_atk_item_721 = R_s_atk_item(0, "강화된 사신수 무기 '청룡의 검'", 4000, 70, 50, 50, 120, 20, 430, 0, "atk")
R_atk_item_722 = R_s_atk_item(0, "강화된 사신수 무기 '백호의 도끼'", 4000, 70, 120, 0, 100, 0, 40, 0, "atk")
R_atk_item_723 = R_s_atk_item(0, "강화된 사신수 무기 '주작의 단검'", 4000, 70, 20, 200, 0, 90, 0, 0, "atk")
R_atk_item_724 = R_s_atk_item(0, "강화된 사신수 무기 '현무의 창'", 4000, 50, 110, 110, 0, 40, 0, 0, "atk")


# 빨간색 (레전드) 사흉수 갑주 아이템 클래스
class R_s_def_item:
    def __init__(self, liv, name, defense, part, need_liv, plus_power_stats, plus_agility_stats, plus_adventure_stats, count, use):
        self.name = name
        self.defense = defense
        self.need_liv = need_liv
        self.part = part
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.plus_adventure_stats = plus_adventure_stats
        self.count = count
        self.use = use

# 사흉수 갑주
R_def_item_811 = R_s_def_item(0, "사흉수 갑옷 '혼돈의 투구'", 200, 1, 100, 150, 150, 150, 0, "atk")
R_def_item_812 = R_s_def_item(0, "사흉수 갑옷 '도철의 갑옷'", 200, 2, 100, 150, 150, 150, 0, "atk")
R_def_item_813 = R_s_def_item(0, "사흉주 갑옷 '도올의 바지'", 200, 3, 100, 150, 150, 150, 0, "atk")
R_def_item_814 = R_s_def_item(0, "사흉수 갑옷 '궁기의 신발'", 200, 4, 100, 150, 150, 150, 0, "atk")

# 필리아스의 갑옷 (60레벨)
R_def_item_821 = R_s_def_item(0, "투명한 달빛 투구", 180, 1, 120, 0, 0, 600, 0, "def")
R_def_item_822 = R_s_def_item(0, "투명한 달빛 갑옷", 180, 2, 120, 600, 0, 0, 0, "def")
R_def_item_823 = R_s_def_item(0, "투명한 달빛 바지", 180, 3, 120, 0, 600, 0, 0, "def")
R_def_item_824 = R_s_def_item(0, "투명한 달빛 신발", 180, 4, 120, 300, 300, 300, 0, "def")


# 저주받은 빨간색 (레전드) 흑룡 무기 아이템 클래스
class R_b_atk_item:
    def __init__(self, liv, name, damage, need_liv, critical, count, use):
        self.liv = liv
        self.name = name
        self.damage = damage
        self.need_liv = need_liv
        self.critical = critical
        self.count = count
        self.use = use

# 카우아(흑룡)의 검
R_atk_item_801 = R_b_atk_item(0, "힘을 잃은 흑룡의 검", 1500, 60, 70, 0, "atk")
R_atk_item_802 = R_b_atk_item(0, "힘을 되찾은 흑룡의 검", 2250, 65, 70, 0, "atk")
R_atk_item_803 = R_b_atk_item(0, "힘을 깨우친 카우아(흑룡)의 검", 3000, 70, 70, 0, "atk")


# 저주받은 빨간색 (레전드) 흑룡의 갑주 아이템 클래스
class R_d_def_item:
    def __init__(self, liv, name, defense, part, need_liv, plus_power_stats, plus_agility_stats, plus_adventure_stats, count, use):
        self.liv = liv
        self.name = name
        self.defense = defense
        self.need_liv = need_liv
        self.part = part
        self.plus_power_stats = plus_power_stats
        self.plus_agility_stats = plus_agility_stats
        self.plus_adventure_stats = plus_adventure_stats
        self.count = count
        self.use = use

# 흑룡의 갑주 (65레벨)
R_def_item_911 = R_d_def_item(0, "흑룡의 갑주 투구", 100, 1, 65, 100, 100, 100, 0, "def")
R_def_item_912 = R_d_def_item(0, "흑룡의 갑주 갑옷", 100, 2, 65, 100, 100, 100, 0, "def")
R_def_item_913 = R_d_def_item(0, "흑룡의 갑주 바지", 100, 3, 65, 100, 100, 100, 0, "def")
R_def_item_914 = R_d_def_item(0, "흑룡의 갑주 신발", 100, 4, 65, 100, 100, 100, 0, "def")

# 흑룡의 갑주 (70레벨)
R_def_item_931 = R_d_def_item(0, "강화된 흑룡의 갑주 투구", 300, 1, 70, 200, 200, 200, 0, "def")
R_def_item_932 = R_d_def_item(0, "강화된 흑룡의 갑주 갑옷", 300, 2, 70, 200, 200, 200, 0, "def")
R_def_item_933 = R_d_def_item(0, "강화된 흑룡의 갑주 바지", 300, 3, 70, 200, 200, 200, 0, "def")
R_def_item_934 = R_d_def_item(0, "강화된 흑룡의 갑주 신발", 300, 4, 70, 200, 200, 200, 0, "def")


# 선과 악 아이템 클래스
class g_e_atk_item:
    def __init__(self, liv, name, damage, critical, physical_absorption, count, use):
        self.liv = liv
        self.name = name
        self.damage = damage
        self.critical = critical
        self.physical_absorption = physical_absorption
        self.count = count
        self.use = use

# 선과 악
g_e_atk_item_901 = g_e_atk_item(0, "신의 첫번째 아이 '에나'", 30000, 100, 5000, 0, "atk")
g_e_atk_item_902 = g_e_atk_item(0, "신의 두번째 아이 '뒤오'", 50000000, 0, 0, 0, "atk")
g_e_atk_item_903 = g_e_atk_item(0, "신의 세번째 아이 '트리아'", 30000, 100, 5000, 0, "atk")


# 아이템

# 강화서 아이템 클래스
class fortification_item:
    def __init__(self, name, cost, count, use):
        self.name = name
        self.cost = cost
        self.count = count
        self.count = count
        self.use = use

# 강화서
fortification_item_101 = fortification_item("무기 강화권", 5000, 0, "item") # 일반 무기강화
fortification_item_111 = fortification_item("방어구 강화권", 4000, 0, "item") # 일반 무기강화
fortification_item_201 = fortification_item("힘 강화권", 16000, 0, "item") # 필요 힘 하락
fortification_item_202 = fortification_item("민첩 강화권", 16000, 0, "item") # 필요 민첩 하락
fortification_item_203 = fortification_item("모험 강화권", 16000, 0, "item") # 필요 모험 하락
fortification_item_301 = fortification_item("파괴 방지권", 20000, 0, "item") # 파괴 방지

fortification_shop = [fortification_item_101, fortification_item_111, fortification_item_201, fortification_item_202,
                      fortification_item_203, fortification_item_301]

# 회복 아이템 클래스
class potion_item:
    def __init__(self, name, recovery, cost, count, use):
        self.name = name
        self.recovery = recovery
        self.cost = cost
        self.count = count
        self.use = use

# 회복의 돌
potion_item_01 = potion_item("최하급 회복의 돌", 10, 1, 0, "potion")
potion_item_02 = potion_item("하급 회복의 돌", 50, 10, 0, "potion")
potion_item_03 = potion_item("중급 회복의 돌", 100, 50, 0, "potion")
potion_item_04 = potion_item("상급 회복의 돌", 500, 500, 0, "potion")
potion_item_05 = potion_item("최상급 회복의 돌", 1000, 2000, 0, "potion")

potion_shop = [potion_item_01, potion_item_02, potion_item_03, potion_item_04, potion_item_05]

# 일반 아이템 클래스
class nomal_item:
    def __init__(self, name, count, use):
        self.name = name
        self.count = count
        self.use = use

# n월의 기억
month_item_02 = nomal_item("2월의 기억", 0, "month")
month_item_03 = nomal_item("3월의 기억", 0, "month")
month_item_04 = nomal_item("4월의 기억", 0, "month")
month_item_05 = nomal_item("5월의 기억", 0, "month")
month_item_06 = nomal_item("6월의 기억", 0, "month")
month_item_07 = nomal_item("7월의 기억", 0, "month")
month_item_08 = nomal_item("8월의 기억", 0, "month")
month_item_09 = nomal_item("9월의 기억", 0, "month")
month_item_10 = nomal_item("10월의 기억", 0, "month")
month_item_11 = nomal_item("11월의 기억", 0, "month")

# 일반 판매 아이템 클래스
class nomal_item_shop:
    def __init__(self, name, count, cost, use):
        self.name = name
        self.count = count
        self.cost = cost
        self.use = use

month_item_01 = nomal_item_shop("1월의 기억", 0, 100, "month")  # 100원

month_shop = [month_item_01]

atk_item_list = [W_atk_item_101, W_atk_item_102, W_atk_item_103, W_atk_item_104, W_atk_item_105, W_atk_item_106,
                 W_atk_item_201, W_atk_item_202, W_atk_item_203, W_atk_item_204, W_atk_item_205, W_atk_item_206,
                 W_atk_item_207, W_atk_item_208, W_atk_item_209, W_atk_item_241, W_atk_item_242, W_atk_item_251,
                 W_atk_item_252, W_atk_item_261, W_atk_item_262, W_atk_item_271, W_atk_item_272, W_atk_item_301,
                 W_atk_item_302, W_atk_item_303, W_atk_item_304, W_atk_item_305, W_atk_item_306, W_atk_item_341,
                 W_atk_item_342, W_atk_item_351, W_atk_item_352, W_atk_item_361, W_atk_item_362, W_atk_item_371,
                 W_atk_item_372, W_atk_item_401, W_atk_item_402, W_atk_item_403, P_atk_item_600, R_atk_item_601,
                 R_atk_item_602, R_atk_item_603, R_atk_item_604, R_atk_item_605, R_atk_item_606, R_atk_item_621,
                 R_atk_item_622, R_atk_item_623, R_atk_item_624, R_atk_item_625, R_atk_item_626, R_atk_item_701,
                 R_atk_item_702, R_atk_item_703, R_atk_item_704, R_atk_item_721, R_atk_item_722, R_atk_item_723,
                 R_atk_item_724, R_atk_item_801, R_atk_item_802, R_atk_item_803, g_e_atk_item_901, g_e_atk_item_902,
                 g_e_atk_item_903]
def_item_list = [W_def_item_001, W_def_item_002, W_def_item_111, W_def_item_112, W_def_item_113, W_def_item_114,
                 W_def_item_211, W_def_item_212, W_def_item_213, W_def_item_214, W_def_item_221, W_def_item_222,
                 W_def_item_223, W_def_item_224, W_def_item_231, W_def_item_232, W_def_item_233, W_def_item_234,
                 W_def_item_311, W_def_item_312, W_def_item_313, W_def_item_314, W_def_item_321, W_def_item_322,
                 W_def_item_323, W_def_item_324, W_def_item_331, W_def_item_332, W_def_item_333, W_def_item_334,
                 W_def_item_411, W_def_item_412, W_def_item_413, W_def_item_414, W_def_item_421, W_def_item_422,
                 W_def_item_423, W_def_item_424, W_def_item_431, W_def_item_432, W_def_item_433, W_def_item_434,
                 W_def_item_511, W_def_item_512, W_def_item_513, W_def_item_514, W_def_item_521, W_def_item_522,
                 W_def_item_523, W_def_item_524, W_def_item_531, W_def_item_532, W_def_item_533, W_def_item_534,
                 P_def_item_611, P_def_item_612, P_def_item_613, P_def_item_614, R_def_item_711, R_def_item_712,
                 R_def_item_713, R_def_item_714, R_def_item_731, R_def_item_732, R_def_item_733, R_def_item_734,
                 R_def_item_811, R_def_item_812, R_def_item_813, R_def_item_814, R_def_item_911, R_def_item_912,
                 R_def_item_913, R_def_item_914, R_def_item_931, R_def_item_932, R_def_item_933, R_def_item_934]
potion_item_list = [potion_item_01, potion_item_02, potion_item_03, potion_item_04, potion_item_05]
month_item_list = [month_item_01, month_item_02, month_item_03, month_item_04, month_item_05, month_item_06,
                   month_item_07, month_item_08, month_item_09, month_item_10, month_item_11]
fortification_item_list = [fortification_item_101, fortification_item_111, fortification_item_201, fortification_item_202,
                            fortification_item_203, fortification_item_301]



# 몬스터 클래스
class monster:
    def __init__(self, name, liv, health, max_health, damage, recovery_health, drop_exp, drop_money, drop_item, drop_item_count, point):
        self.name = name
        self.liv = liv
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.recovery_health = recovery_health
        self.drop_exp = drop_exp
        self.drop_money = drop_money
        self.drop_item = drop_item
        self.drop_item_count = drop_item_count
        self.point = point

# 1월의 기억 드랍
nomal_monster_0004 = monster("화난닭", 0, 1, 1, 2, 0, 0, 0, month_item_01, 1, 66)

nomal_monster_0101 = monster("화난닭", 0, 1, 1, 2, 0, 0, 0, month_item_01, 1, 32)
nomal_monster_0102 = monster("돌돌이", 1, 25, 25, 8, 0, 1, 1, month_item_01, 2, 32)
nomal_monster_0103 = monster("돌순이", 2, 35, 35, 20, 0, 1, 1, month_item_01, 3, 32)
nomal_monster_0104 = monster("돌멍이", 3, 60, 60, 35, 5, 2, 2, month_item_01, 4, 32)
nomal_monster_0105 = monster("돌전사", 6, 150, 150, 75, 7, 4, 3, month_item_01, 5, 32)
nomal_monster_0106 = monster("왕돌이", 6, 1500, 1500, 500, 50, 200, 200, month_item_01, 6, 32)

nomal_monster_0201 = monster("오염된 슬라임 요정", 6, 160, 160, 60, 8, 6, 5, month_item_01, 6, 4)
nomal_monster_0202 = monster("오염된 뼈슬라임", 7, 200, 200, 80, 10, 7, 5, month_item_01, 7, 4)
nomal_monster_0203 = monster("오염된 하늘슬라임", 8, 250, 250, 85, 13, 8, 5, month_item_01, 8, 4)
nomal_monster_0204 = monster("오염된 키다리 슬라임", 8, 240, 240, 125, 12, 7, 5, month_item_01, 9, 4)
nomal_monster_0205 = monster("사악한 마녀", 9, 2000, 300, 300, 100, 250, 2000, month_item_01, 10, 4)

# 2월의 기억 드랍
nomal_monster_0301 = monster("어설픈 해적앵무새", 9, 260, 260, 95, 13, 10, 7, month_item_02, 1, 7)
nomal_monster_0302 = monster("어설픈 해적 조무래기", 10, 280, 280, 115, 14, 11, 7, month_item_02, 2, 7)
nomal_monster_0303 = monster("어설픈 해적 견습생", 11, 300, 300, 120, 15, 12, 7, month_item_02, 3, 7)
nomal_monster_0304 = monster("어설픈 해적", 12, 325, 325, 145, 16, 13, 7, month_item_02, 4, 6)
nomal_monster_0305 = monster("어설픈 해적선장", 13, 4000, 4000, 500, 300, 250, 4000, month_item_02, 4, 6)

nomal_monster_0401 = monster("파란 위습", 13, 375, 375, 170, 17, 15, 10, month_item_02, 5, 7)
nomal_monster_0402 = monster("초록 위습", 14, 400, 400, 190, 18, 16, 10, month_item_02, 6, 7)

nomal_monster_0501 = monster("엘프 전사 견습생", 15, 450, 450, 220, 20, 17, 12, month_item_02, 7, 15)
nomal_monster_0502 = monster("엘프 전사", 16, 500, 500, 250, 22, 18, 14, month_item_02, 8, 15)
nomal_monster_0503 = monster("엘프 여왕", 17, 8000, 8000, 700, 500, 300, 7000, month_item_02, 10, 15)

# 3월의 기억 드랍
nomal_monster_0601 = monster("감염된 여성", 18, 550, 550, 280, 24, 20, 16, month_item_03, 1, 10)
nomal_monster_0602 = monster("감염된 남성", 19, 650, 650, 300, 28, 21, 18, month_item_03, 2, 10)
nomal_monster_0603 = monster("거대 바이러스 골렘", 20, 10000, 10000, 1200, 800, 500, 15000, month_item_03, 3, 10)

nomal_monster_0701 = monster("초보 드워프", 20, 720, 720, 400, 40, 34, 30, month_item_03, 5, 14)
nomal_monster_0702 = monster("붉은 드워프", 21, 800, 800, 450, 44, 40, 35, month_item_03, 6, 14)
nomal_monster_0703 = monster("땅꼬마 드워프", 22, 880, 880, 500, 48, 46, 40, month_item_03, 7, 14)
nomal_monster_0704 = monster("덩치 드워프", 23, 960, 960, 550, 52, 52, 45, month_item_03, 8, 14)
nomal_monster_0705 = monster("드워프 왕", 24, 15000, 15000, 1600, 1000, 800, 50, month_item_03, 10, 14)

# 4월의 기억 드랍
nomal_monster_0801 = monster("인어 견습 전사", 24, 1000, 1000, 600, 60, 70, 60, month_item_04, 1, 12)
nomal_monster_0802 = monster("인어 전사", 25, 1100, 1100, 650, 70, 80, 70, month_item_04, 2, 12)
nomal_monster_0803 = monster("인어 베테랑 전사", 26, 1200, 1200, 700, 80, 90, 80, month_item_04, 3, 12)
nomal_monster_0804 = monster("인어 전사장", 27, 1300, 1300, 750, 90, 100, 90, month_item_04, 4, 12)
nomal_monster_0805 = monster("인어 대장", 28, 18000, 18000, 2000, 1200, 1000, 1000, month_item_04, 5, 12)

nomal_monster_0901 = monster("아기 거미", 28, 1450, 1450, 800, 100, 110, 100, month_item_04, 6, 25)
nomal_monster_0902 = monster("거미 전사", 29, 1600, 1600, 900, 120, 130, 110, month_item_04, 7, 25)
nomal_monster_0903 = monster("거미 마법사", 30, 1750, 1750, 1000, 140, 150, 120, month_item_04, 8, 25)
nomal_monster_0904 = monster("거미 대장", 31, 1900, 1900, 1100, 160, 170, 130, month_item_04, 9, 25)
nomal_monster_0905 = monster("거미 여왕", 32, 23000, 23000, 3000, 1500, 1300, 1400, month_item_04, 10, 25)

# 5월의 기억 드랍
nomal_monster_1001 = monster("허약한 선녀", 32, 2100, 2100, 1300, 180, 190, 150, month_item_05, 1, 8)
nomal_monster_1002 = monster("가녀린 선녀", 33, 2300, 2300, 1450, 210, 220, 170, month_item_05, 2, 8)
nomal_monster_1003 = monster("길쭉한 선녀", 34, 2500, 2500, 1600, 240, 250, 190, month_item_05, 3, 8)
nomal_monster_1004 = monster("키가 작은 선녀", 35, 2700, 2700, 1750, 260, 270, 210, month_item_05, 4, 8)

# 이벤트 및 특수
special_monster_0001 = monster("화난소", 0, 300, 300, 100, 100, 15, 0, " ", 0, 1)
special_monster_0002 = monster("핀 그리드", 0, 15000, 15000, 2500, 4000, 3000, 1000, R_atk_item_601, 1, 1)  # 렉스의 1번째 명작 '홍염의 날개깃' 드랍
special_monster_0003 = monster("인내의 돌", 1, 200000, 200000, 0, 30, 0, 0, R_atk_item_603, 1, 1)  # 렉스의 3번째 명작 '녹색 이빨' 드랍

monster_list_66 = [nomal_monster_0004]
monster_list_23 = [nomal_monster_0101, nomal_monster_0102, nomal_monster_0103, nomal_monster_0104, nomal_monster_0105, nomal_monster_0106]
monster_list_04 = [nomal_monster_0201, nomal_monster_0202, nomal_monster_0203, nomal_monster_0204, nomal_monster_0205]
monster_list_06 = [nomal_monster_0301, nomal_monster_0302, nomal_monster_0303, nomal_monster_0304, nomal_monster_0305]
monster_list_07 = [nomal_monster_0401, nomal_monster_0402]
monster_list_15 = [nomal_monster_0501, nomal_monster_0502, nomal_monster_0503]
monster_list_10 = [nomal_monster_0601, nomal_monster_0602, nomal_monster_0603]
monster_list_14 = [nomal_monster_0701, nomal_monster_0702, nomal_monster_0703, nomal_monster_0704, nomal_monster_0705]
monster_list_12 = [nomal_monster_0801, nomal_monster_0802, nomal_monster_0803, nomal_monster_0804, nomal_monster_0805]
monster_list_25 = [nomal_monster_0901, nomal_monster_0902, nomal_monster_0903, nomal_monster_0904, nomal_monster_0905]
monster_list_08 = [nomal_monster_1001, nomal_monster_1002, nomal_monster_1003, nomal_monster_1004]
monster_list_01 = [special_monster_0001, special_monster_0002, special_monster_0003]



# 공간 마법사
class warp_manager:
    def __init__(self, name, count, x, y):
        self.name = name
        self.count = count
        self.x = x
        self.y = y

warp_manager_1 = warp_manager("1. 에나 동쪽항구", 0, 92, 53)
warp_manager_2 = warp_manager("2. 에나 번화가", 0, 87, 52)
warp_manager_3 = warp_manager("3. 에나 서쪽", 0, 79, 53)
warp_manager_4 = warp_manager("4. 에나 북쪽", 0, 87, 60)
warp_manager_5 = warp_manager("5. 에나 낚시터", 0, 86, 47)
warp_manager_6 = warp_manager("6. 오염된 강", 0, 76, 48)
warp_manager_7 = warp_manager("7. 불탄 점령지", 0, 67, 50)
warp_manager_8 = warp_manager("8. 해적 소굴", 0, 65, 47)
warp_manager_9 = warp_manager("9. 생명의 숲", 0, 92, 67)
warp_manager_10 = warp_manager("10, 뒤오", 0, 83, 67)
warp_manager_11 = warp_manager("11, 엘프 유적", 0, 96, 67)
warp_manager_12 = warp_manager("12. 인어 왕국", 0, 65, 83)
warp_manager_13 = warp_manager("13. 발길이 머무르는 곳", 0, 67, 65)
warp_manager_14 = warp_manager("14. 누군가의 무덤", 0, 78, 75)
warp_manager_15 = warp_manager("15. 대륙의 통로", 0, 73, 71)
warp_manager_16 = warp_manager("16. 누군가의 성", 0, 67, 39)
warp_manager_17 = warp_manager("17. 트리아", 0, 68, 77)
warp_manager_18 = warp_manager("18. 대륙의 다리", 0, 58, 62)
warp_manager_19 = warp_manager("19. 선녀 호수", 0, 74, 57)
warp_manager_20 = warp_manager("20. 드워프 마을", 0, 84, 80)
warp_manager_21 = warp_manager("21. 심연의 갱도", 0, 65, 78)
warp_manager_22 = warp_manager("22. 생기의 마을", 0, 10, 88)
warp_manager_23 = warp_manager("23. 오크의 성", 0, 50, 95)
warp_manager_24 = warp_manager("24. 고대 유적의 섬", 0, 10, 31)
warp_manager_25 = warp_manager("25. 고대 유적의 섬 선착장", 0, 14, 26)
warp_manager_26 = warp_manager("26. 개척자들의 섬", 0, 26, 22)
warp_manager_27 = warp_manager("27. 신들의 고향 선착장", 0, 18, 14)
warp_manager_28 = warp_manager("28. 비명의 바다 해변가", 0, 46, 18)
warp_manager_29 = warp_manager("29. 탄식의 바다 절벽", 0, 52, 16)
warp_manager_30 = warp_manager("30. 선과악의 전쟁터", 0, 4, 37)
warp_manager_31 = warp_manager("31. 세상을 등진곳 중심부", 0, 26, 76)
warp_manager_32 = warp_manager("32. 세상을 등진곳 동쪽", 0, 31, 76)
warp_manager_33 = warp_manager("33. 얼음성", 0, 20, 70)
warp_manager_34 = warp_manager("34. 매마른 사막 입구", 0, 25, 64)
warp_manager_35 = warp_manager("35. 드워프 유적지", 0, 30, 60)
warp_manager_36 = warp_manager("36. 신기루 성", 0, 33, 52)
warp_manager_37 = warp_manager("37. 신기루 성 남쪽 항구", 0, 33, 47)
warp_manager_38 = warp_manager("38. 봉인된 신전", 0, 50, 69)
warp_manager_39 = warp_manager("39. 거미 동굴", 0, 49, 60)
warp_manager_40 = warp_manager("40. 모험의 갈림길", 0, 42, 52)
warp_manager_41 = warp_manager("41. 오래된 성", 0, 47, 45)
warp_manager_42 = warp_manager("42. 바다 신전", 0, 50, 33)

warp_manager_list = [warp_manager_1, warp_manager_2, warp_manager_3, warp_manager_4, warp_manager_5, warp_manager_6,
                     warp_manager_7, warp_manager_8, warp_manager_9, warp_manager_10, warp_manager_11, warp_manager_12,
                     warp_manager_13, warp_manager_14, warp_manager_15, warp_manager_16, warp_manager_17, warp_manager_18,
                     warp_manager_19, warp_manager_20, warp_manager_21, warp_manager_22, warp_manager_23, warp_manager_24,
                     warp_manager_25, warp_manager_26, warp_manager_27, warp_manager_28, warp_manager_29, warp_manager_30,
                     warp_manager_31, warp_manager_32, warp_manager_33, warp_manager_34, warp_manager_35, warp_manager_36,
                     warp_manager_37, warp_manager_38, warp_manager_39, warp_manager_40, warp_manager_41, warp_manager_42]



# 스타포스 강화 확률
class star_force_persent:
    def __init__(self, liv, success, fail, fall, destruction):
        self.liv = liv
        self.success = success
        self.fail = fail
        self.fall = fall
        self.destruction = destruction

star_force_1 = star_force_persent(1, 100, 0, 0, 0)
star_force_2 = star_force_persent(2, 90, 9, 1, 0)
star_force_3 = star_force_persent(3, 80, 16, 4, 0)
star_force_4 = star_force_persent(4, 70, 20, 10, 0)
star_force_5 = star_force_persent(5, 60, 23, 17, 0)
star_force_6 = star_force_persent(6, 50, 23, 26, 1)
star_force_7 = star_force_persent(7, 40, 20, 38, 2)
star_force_8 = star_force_persent(8, 30, 16, 51, 3)
star_force_9 = star_force_persent(9, 20, 9, 67, 4)
star_force_10 = star_force_persent(10, 10, 0, 95, 5)

star_force_list = [star_force_1, star_force_2, star_force_3, star_force_4, star_force_5, star_force_6, star_force_7,
                   star_force_8, star_force_9, star_force_10]



# 현재 상태 확인 (상태창 : 1 / 전투중 : 2 / 인벤토리 : 3)
def showinfo(player_1, call):
    if call == 1 or call == 2:
        print(f"{' 나의 상태 ':=^60}")
        if call == 2:
            print(f"이름 : {player_1.name}   체력 : {player_1.health}\n공격력 : {player_1.damage}   방어력 : {player_1.defense}\n")
        elif call == 1:
            print(f"Lv.{player_1.liv} {player_1.name}\n체력 : ({player_1.health}/ {player_1.result_health})   공격력/방어력 : {player_1.damage}/ {player_1.defense}\
                \n스텟 (힘, 민첩, 모험) : ({player_1.po_count}, {player_1.ag_count}, {player_1.ad_count})\n위치 : {point_to_txt(player_1)}({player_1.player_x}, {player_1.player_y})   돈 : {player_1.money}")

    if call == 3:
        if len(player_1.equipment['atk']) == 2:
            try:
                if player_1.equipment['atk'][1].liv != 0:
                    print(f"무기 : liv.{player_1.equipment['atk'][1].liv}_{player_1.equipment['atk'][1].name}")
                else:
                    print(f"무기 : {player_1.equipment['atk'][1].name}")
            except:
                print(f"무기 : {player_1.equipment['atk'][1].name}")
        else:
            print(f"무기 : {player_1.equipment['atk'][0]}")

        if len(player_1.equipment['def_1']) == 2:
            print(f"갑옷 모자 : {player_1.equipment['def_1'][1].name}", end='   ')
        else:
            print(f"갑옷 모자 : {player_1.equipment['def_1'][0]}", end='   ')

        if len(player_1.equipment['def_2']) == 2:
            print(f"갑옷 상의 : {player_1.equipment['def_2'][1].name}")
        else:
            print(f"갑옷 상의 : {player_1.equipment['def_2'][0]}")

        if len(player_1.equipment['def_3']) == 2:
            print(f"갑옷 하의 : {player_1.equipment['def_3'][1].name}", end='   ')
        else:
            print(f"갑옷 하의 : {player_1.equipment['def_3'][0]}", end='   ')

        if len(player_1.equipment['def_4']) == 2:
            print(f"갑옷 신발 : {player_1.equipment['def_4'][1].name}")
        else:
            print(f"갑옷 신발 : {player_1.equipment['def_4'][0]}")



# 무기 세부정보
def detailed_print_item(player_1, select, ans, call):
    try:
        if player_1.print_inven[ans].liv != 0:
            print(f"이름 : liv.{player_1.print_inven[ans].liv}_{player_1.print_inven[ans].name}")
        else:
            print(f"이름 : {player_1.print_inven[ans].name}")
    except:
        print(f"이름 : {player_1.print_inven[ans].name}")

    if select == 'atk':
        print(f"공격력 : {player_1.print_inven[ans].damage}")
        if call == 'shop':
            print(f"가격 : {player_1.inven['month'][player_1.print_inven[ans].month - 1].name} X {player_1.print_inven[ans].cost}")
        else:
            print()

        print(f"제한레벨 : {player_1.print_inven[ans].need_liv}")

        try:
            need_power_stats = player_1.print_inven[ans].need_power_stats
        except:
            need_power_stats = 0
        try:
            need_agility_stats = player_1.print_inven[ans].need_agility_stats
        except:
            need_agility_stats = 0
        try:
            need_adventure_stats = player_1.print_inven[ans].need_adventure_stats
        except:
            need_adventure_stats = 0

        print(f"필요스텟 (힘, 민첩, 모험) : ({need_power_stats}, {need_agility_stats}, {need_adventure_stats})")

        try:
            print(f"크리티컬 : {player_1.print_inven[ans].critical}")
        except:
            print()
        try:
            print(f"체력흡수 : {player_1.print_inven[ans].physical_absorption}")
        except:
            print()

    elif select == 'def':
        print(f"방어력 : {player_1.print_inven[ans].defense}")
        if call == 'shop':
            print(f"가격 : {player_1.inven['month'][player_1.print_inven[ans].month - 1].name} X {player_1.print_inven[ans].cost}")
        else:
            print()

        print(f"제한레벨 : {player_1.print_inven[ans].need_liv}")

        try:
            plus_power_stats = player_1.print_inven[ans].plus_power_stats
        except:
            plus_power_stats = 0
        try:
            plus_agility_stats = player_1.print_inven[ans].plus_agility_stats
        except:
            plus_agility_stats = 0
        try:
            plus_adventure_stats = player_1.print_inven[ans].plus_adventure_stats
        except:
            plus_adventure_stats = 0

        print(f"추가스텟 (힘, 민첩, 모험) : ({plus_power_stats}, {plus_agility_stats}, {plus_adventure_stats})")

        try:
            print(f"체력흡수 : {player_1.print_inven[ans].physical_absorption}")
        except:
            print()

    elif select == 'potion':
        print(f"회복량 : {player_1.print_inven[ans].recovery}")
        if call == 'shop':
            print(f"가격 : {player_1.print_inven[ans].cost}")
        else:
            print()
        print("\n" * 2)

    elif select == "month":
        if call == 'shop':
            print(f"가격 : {player_1.print_inven[ans].cost}")
        else:
            print()
        print("\n" * 3)

    elif select == "item":
        if call == 'shop':
            print(f"가격 : {player_1.print_inven[ans].cost}")
        else:
            print()
        print("\n" * 3)


# 무기 장착
def equipment(player_1, select, ans):
    print("\n" * 1)
    while True:
        print("\n" * 4)
        detailed_print_item(player_1, select, ans, 'equipment')
        try:
            if player_1.print_inven[ans].liv != 0:
                ans_1 = input(f"\n'liv.{player_1.print_inven[ans].liv}_{player_1.print_inven[ans].name}' 을(를) 장착하시겟습니까? (y / n) : ")
            else:
                ans_1 = input(f"\n'{player_1.print_inven[ans].name}' 을(를) 장착하시겟습니까? (y / n) : ")
        except:
            ans_1 = input(f"\n'{player_1.print_inven[ans].name}' 을(를) 장착하시겟습니까? (y / n) : ")
        if ans_1 == "y":
            if player_1.liv >= player_1.print_inven[ans].need_liv:
                if select == 'atk':
                    if player_1.po_count >= player_1.print_inven[ans].need_power_stats:
                        if player_1.ag_count >= player_1.print_inven[ans].need_agility_stats:
                            if player_1.ad_count >= player_1.print_inven[ans].need_adventure_stats:
                                if len(player_1.equipment[select]) == 2:
                                    del player_1.equipment[select][1]
                                    player_1.equipment[select].append(player_1.print_inven[ans])
                                elif len(player_1.equipment[select]) == 1:
                                    player_1.equipment[select].append(player_1.print_inven[ans])
                                print("\n" * 12)
                                try:
                                    if player_1.print_inven[ans].liv != 0:
                                        print(f"\n'liv.{player_1.print_inven[ans].liv}_{player_1.print_inven[ans].name}' 을(를) 장착하였습니다.")
                                    else:
                                        print(f"\n'{player_1.print_inven[ans].name}' 을(를) 장착하였습니다.")
                                except:
                                    print(f"\n'{player_1.print_inven[ans].name}' 을(를) 장착하였습니다.")
                            else:
                                print("\n모험스텟이 부족합니다.")
                                break
                        else:
                            print("\n민첩스텟이 부족합니다.")
                            break
                    else:
                        print("\n힘스텟이 부족합니다.")
                        break

                if select == 'def':
                    if player_1.print_inven[ans].part == 1:
                        select_1 = 'def_1'
                    elif player_1.print_inven[ans].part == 2:
                        select_1 = 'def_2'
                    elif player_1.print_inven[ans].part == 3:
                        select_1 = 'def_3'
                    elif player_1.print_inven[ans].part == 4:
                        select_1 = 'def_4'

                    if len(player_1.equipment[select_1]) == 2:
                        del player_1.equipment[select_1][1]
                        player_1.equipment[select_1].append(player_1.print_inven[ans])
                    elif len(player_1.equipment[select_1]) == 1:
                        player_1.equipment[select_1].append(player_1.print_inven[ans])
                    print("\n" * 12)
                    try:
                        if player_1.print_inven[ans].liv != 0:
                            print(
                                f"\n'liv.{player_1.print_inven[ans].liv}_{player_1.print_inven[ans].name}' 을(를) 장착하였습니다.")
                        else:
                            print(f"\n'{player_1.print_inven[ans].name}' 을(를) 장착하였습니다.")
                    except:
                        print(f"\n'{player_1.print_inven[ans].name}' 을(를) 장착하였습니다.")
                input("나가려면(enter)")
                print("\n" * 2)
                break
            elif player_1.liv < player_1.print_inven[ans].need_liv:
                print("\n레벨이 부족합니다.")
                break
        elif ans_1 == "n":
            print("\n" * 2)
            break
        else:
            print("\n올바른 문자를 입력하세요.")



# 포션 사용
def potion_use(player_1, ans):
    print("\n" * 2)
    while player_1.print_inven[ans].count > 0:
        print("\n" * 10)
        ans_1 = input(f"\n{player_1.print_inven[ans].name}을(를) 사용하시겟습니까? (y / n) : ")
        if ans_1 == "y":
            if player_1.health >= player_1.result_health:
                print("체력이 충분하여 아이템을 사용할 수 없습니다.")
            else:
                player_1.print_inven[ans].count = player_1.print_inven[ans].count - 1
                player_1.health = player_1.health + player_1.print_inven[ans].recovery
                if player_1.health > player_1.result_health:
                    player_1.health = player_1.result_health
                print("\n성공적으로 사용하였습니다.\n")
        elif ans_1 == "n":
            print("\n" * 2)
            break
        else:
            print("\n올바른 문자를 입력하세요.\n")



# 아이템 정보 프린트
def print_item(player_1, select, ans):
    print("\n" * 6)

    while True:
        print("{0:=^60}".format(" '" + player_1.print_inven[ans].name + "' 아이템 정보 "))
        if select == 'atk':
            try:
                if player_1.print_inven[ans].liv != 0:
                    print(f"\n이름 : liv.{player_1.print_inven[ans].liv}_{player_1.print_inven[ans].name}\n공격력 : {player_1.print_inven[ans].damage}\n장착제한 레벨 : {player_1.print_inven[ans].need_liv}")
                else:
                    print(f"\n이름 : {player_1.print_inven[ans].name}\n공격력 : {player_1.print_inven[ans].damage}\n장착제한 레벨 : {player_1.print_inven[ans].need_liv}")
            except:
                print(f"\n이름 : {player_1.print_inven[ans].name}\n공격력 : {player_1.print_inven[ans].damage}\n장착제한 레벨 : {player_1.print_inven[ans].need_liv}")
        elif select == 'def':
            try:
                if player_1.print_inven[ans].liv != 0:
                    print(f"\n이름 : liv.{player_1.print_inven[ans].liv}_{player_1.print_inven[ans].name}\n방어력 : {player_1.print_inven[ans].defense}\n장착제한 레벨 : {player_1.print_inven[ans].need_liv}")
                else:
                    print(f"\n이름 : {player_1.print_inven[ans].name}\n방어력 : {player_1.print_inven[ans].defense}\n장착제한 레벨 : {player_1.print_inven[ans].need_liv}")
            except:
                print(f"\n이름 : {player_1.print_inven[ans].name}\n방어력 : {player_1.print_inven[ans].defense}\n장착제한 레벨 : {player_1.print_inven[ans].need_liv}")
        elif select == 'potion':
            print(f"\n이름 : {player_1.print_inven[ans].name}\n체력 회복량 : {player_1.print_inven[ans].recovery}\n")
        elif select == 'item':
            print(f"\n이름 : {player_1.print_inven[ans].name}\n\n")

        if select == 'atk' or select == 'def':
            print("\n\n돌아가기 : q / 장착하기 : w")
        elif select == 'potion':
            print("\n\n돌아가기 : q / 사용하기 : w")
        else:
            print("\n\n돌아가기 : q")
        ans_1 = input(" : ")

        if ans_1 == 'q':
            print("\n" * 2)
            break
        elif ans_1 == 'w':
            if select == 'atk' or select == 'def':
                equipment(player_1, select, ans)
                break
            elif select == 'potion':
                potion_use(player_1, ans)
                break
            else:
                print("\n올바른 문자를 입력하세요.\n")
                print("\n" * 3)
        else:
            print("\n올바른 문자를 입력하세요.\n")
            print("\n" * 3)



# 인벤토리
def inventory_select(call):
    while True:
        if call == 1:
            print("\n원하는 인벤토리를 선택하세요 [무기(q) /방어구(w) /포션(e) /세계의 기억(r) /일반(t)]\n돌아가려면 (enter)")
        elif call == 2:
            print("\n원하는 상점을 선택하세요 [무기(q) /방어구(w) /포션(e) /세계의 기억(r) /일반(t)]\n돌아가려면 (enter)")
        elif call == 5:
            print("\n원하는 강화아이템을 선택하세요 [무기(q) /방어구(w)]\n돌아가려면 (enter)")
        ans = input(" : ")
        if call == 1 or call == 2:
            if ans == "q" or ans == "w" or ans == "e" or ans == "r" or ans == "t" or ans == "":
                return ans
            else:
                print("\n올바른 문자를 입력하세요.")
                print("\n" * 9)
        elif call == 5:
            if ans == "q" or ans == "w" or ans == "":
                return ans
            else:
                print("\n올바른 문자를 입력하세요.")
                print("\n" * 9)



# 인벤토리 출력 (인벤토리 : 1 / 상점 : 2 / 공간마법사 : 3,4 / 강화 : 5 / 환전(세계의 기억) : 6)
def inventory(player_1, call):
    if call == 1 or call == 2 or call == 5:
        print("\n" * 11)
        select = simple_to_txt(inventory_select(call))
        print()
    else:
        select = 0

    try:
        print("\n" * 1)
        player_1.print_inven = []
        if call == 1 or call == 5:
            j = 0
            for i in range(len(player_1.inven[select])):
                if player_1.inven[select][j].count != 0:
                    player_1.print_inven.append(player_1.inven[select][j])
                j = j + 1
        elif call == 2:
            if select == 'atk:':
                if player_1.point == 1:
                    player_1.print_inven = point_1_atk_shop
                elif player_1.point == 2:
                    player_1.print_inven = point_2_atk_shop
                elif player_1.point == 3:
                    player_1.print_inven = point_3_atk_shop
                elif player_1.point == 5:
                    player_1.print_inven = point_5_atk_shop
                elif player_1.point == 19:
                    player_1.print_inven = point_19_atk_shop
                elif player_1.point == 22:
                    player_1.print_inven = point_22_atk_shop
                elif player_1.point == 28:
                    player_1.print_inven = point_28_atk_shop
                elif player_1.point == 36:
                    player_1.print_inven = point_36_atk_shop
            elif select == 'def':
                if player_1.point == 1:
                    player_1.print_inven = point_1_def_shop
                elif player_1.point == 2:
                    player_1.print_inven = point_2_def_shop
                elif player_1.point == 3:
                    player_1.print_inven = point_3_def_shop
                elif player_1.point == 5:
                    player_1.print_inven = point_5_def_shop
                elif player_1.point == 19:
                    player_1.print_inven = point_19_def_shop
                elif player_1.point == 22:
                    player_1.print_inven = point_22_def_shop
                elif player_1.point == 28:
                    player_1.print_inven = point_28_def_shop
                elif player_1.point == 36:
                    player_1.print_inven = point_36_def_shop
            elif select == 'potion':
                player_1.print_inven = potion_shop
            elif select == 'month':
                player_1.print_inven = month_shop
            elif select == 'item':
                player_1.print_inven = fortification_shop
        elif call == 3:
            j = 0
            for i in range(len(player_1.warp_manager)):
                if player_1.warp_manager[j].count != 0:
                    player_1.print_inven.append(player_1.warp_manager[j])
                j = j + 1
        elif call == 6:
            player_1.print_inven = list(month_item_list)
            print()

        if call != 4:
            plag = 0
            n = 8
            k = 1
            while True:
                if call == 1:
                    print("{0:=^60}".format(" " + use_to_korean(select) + " 아이템 인벤토리 (" + str(plag + 1) + " 페이지) "))
                elif call == 2:
                    print("{0:=^60}".format(" " + use_to_korean(select) + " 아이템 상점 (" + str(plag + 1) + " 페이지) "))
                elif call == 3:
                    print("{0:=^60}".format(" 공간마법사 (" + str(plag + 1) + " 페이지) "))
                elif call == 5:
                    print("{0:=^60}".format(" 강화하고자 하는 아이템을 선택하세요 (" + str(plag + 1) + " 페이지) "))
                elif call == 6:
                    print("{0:=^60}".format(" 세계의 기억 환전소 (" + str(plag + 1) + " 페이지) "))

                if len(player_1.print_inven) != 0:
                    k = plag * n
                    for i in range(plag * (n - 1), plag * (n - 1) + n):
                        k = k + 1
                        try:
                            if call == 1 or call == 2 or call == 3 or call == 5:
                                if select == 'atk' or select == 'def':
                                    try:
                                        if player_1.print_inven[plag + i].liv != 0:
                                            print(f"{k}. liv.{player_1.print_inven[plag + i].liv}_{player_1.print_inven[plag + i].name} X {player_1.print_inven[plag + i].count}")
                                        else:
                                            print(f"{k}. {player_1.print_inven[plag + i].name} X {player_1.print_inven[plag + i].count}")
                                    except:
                                        print(f"{k}. {player_1.print_inven[plag + i].name} X {player_1.print_inven[plag + i].count}")
                                else:
                                    print(f"{k}. {player_1.print_inven[plag + i].name} X {player_1.print_inven[plag + i].count}")
                            elif call == 3:
                                print(f"({k}) '{player_1.print_inven[plag + i].name}'")
                            elif call == 6:
                                print(f"{k}. {player_1.print_inven[plag + i].name} X 10 -> {player_1.print_inven[plag + i + 1].name} X 1")
                        except:
                            print()
                else:
                    print(f"{k}. 없음 X 없음")
                    print("\n" * (n - 2))

                print("\n돌아가기 : q / 이전페이지 : w / 다음페이지 : e")
                if call == 1 or call == 2:
                    if select != 'month':
                        print("[아이템의 정보를 보고 싶다면 해당 아이템의 번호를 입력하세요.]")
                    else:
                        print()
                elif call == 3:
                    print("[이동하고자 하는 공간마법사 번호를 입력하세요.]")
                elif call == 5:
                    print("[강화하고자 하는 아이템 번호를 입력하세요.]")
                elif call == 6:
                    print("[교환하고자 하는 아이템 번호를 입력하세요.]")

                ans = input(" : ")

                if ans == "q":
                    print("\n" * 1)
                    break
                elif ans == "w":
                    if plag == 0:
                        plag = (len(player_1.print_inven) // n)
                    else:
                        plag = plag - 1
                    print("\n" * 2)
                elif ans == "e":
                    if plag == (len(player_1.print_inven) // n):
                        plag = 0
                    else:
                        plag = plag + 1
                    print("\n" * 2)
                else:
                    try:
                        if 1 <= int(ans) <= len(player_1.print_inven):
                            pass
                    except:
                        print("\n다시 입력해 주십시오.\n")
                    else:
                        if 1 <= int(ans) <= len(player_1.print_inven):
                            if call == 1:
                                if select != 'month' or select != 'item':
                                    print_item(player_1, select, int(ans) - 1)
                                else:
                                    print("\n다시 입력해 주십시오.\n")
                            elif call == 2:
                                buy_item(player_1, select, int(ans) - 1)
                            elif call == 3:
                                player_1.player_x = player_1.print_inven[int(ans) - 1].x
                                player_1.player_y = player_1.print_inven[int(ans) - 1].y
                                print("\n성공적으로 이동하였습니다.\n")
                            elif call == 5:
                                ster_force(player_1, select, int(ans) - 1)
                            elif call == 6:
                                exchange(player_1, int(ans) - 1)
                        else:
                            print("\n올바른 숫자를 입력하세요.\n")
        elif call == 4:
            while True:
                print("\n" * 9)
                for i in range(len(warp_manager_list)):
                    if player_1.player_x == player_1.warp_manager[i].x and player_1.player_y == player_1.warp_manager[i].y:
                        print(f"공간마법사 : '{player_1.warp_manager[i].name}'")
                print("\n공간마법사를 등록하시겠습니까? (y / n)")
                ans = input(" : ")
                if ans == 'y':
                    for i in range(len(warp_manager_list)):
                        if player_1.player_x == player_1.warp_manager[i].x and player_1.player_y == player_1.warp_manager[i].y:
                            if player_1.warp_manager[i].count != 0:
                                print("\n" * 12)
                                print("이미 등록된 공간마법사 입니다.")
                            elif player_1.warp_manager[i].count == 0:
                                player_1.warp_manager[i].count = 1
                                print("\n" * 12)
                                print("공간마법사가 성공적으로 등록되었습니다.")
                    break
                elif ans == 'n':
                    print("\n" * 1)
                    break
                else:
                    print("\n다시 입력해 주십시오.")
    except:
        print()



# 상점 구매
def buy_item(player_1, select, ans):
    print("\n" * 5)

    buy_type = 0
    if select == 'atk' or select == 'def':
        buy_type = 1
    elif select == 'potion' or select == 'month' or select == 'item':
        buy_type = 2

    while True:
        print("{0:-^60}".format(" 구매 "))
        detailed_print_item(player_1, select, ans, 'shop')

        if buy_type == 1:
            print("\n돌아가기 : q / 구매하기 : w")
        elif buy_type == 2:
            print("\n돌아가기 : q / [구매하려면 수량 입력]")

        ans_1 = input(" : ")
        if ans_1 == "q":
            print("\n" * 2)
            break
        elif ans_1 == "w":
            if buy_type == 1:
                try:
                    if player_1.inven['month'][player_1.print_inven[ans].month - 1].count >= player_1.print_inven[ans].cost:
                        player_1.inven['month'][player_1.print_inven[ans].month - 1].count = player_1.inven['month'][player_1.print_inven[ans].month - 1].count - player_1.print_inven[ans].cost
                        player_1.inven[select][ans].count = player_1.inven[select][ans].count + 1
                        print(f"\n{player_1.print_inven[ans].name}을/를 성공적으로 구매하였습니다.\n")
                        break
                    else:
                        print(f"\n{player_1.inven['month'][player_1.print_inven[ans].month - 1].name}이 부족합니다.")
                        print("\n" * 2)
                except:
                    pass
            elif buy_type == 2:
                try:
                    if int(ans_1) == 0:
                        print("\n" * 2)
                        break
                    elif 0 < int(ans_1):
                        if player_1.money >= player_1.print_inven[ans].cost * int(ans_1):
                            player_1.money = player_1.money - (player_1.print_inven[ans].cost * int(ans_1))
                            player_1.inven[select][ans].count = player_1.inven[select][ans].count + int(ans_1)
                            print(f"\n({player_1.print_inven[ans].name}) {ans_1}개를 성공적으로 구매하였습니다.\n")
                            break
                        else:
                            print("\n돈이 부족합니다.")
                            print("\n" * 2)
                    elif 0 > int(ans_1):
                        print("\n올바른 양수값을 입력하여 주십시오.")
                        print("\n" * 2)
                except:
                    print("\n다시 입력해 주십시오.")
                    print("\n" * 2)
        else:
            print("\n다시 입력해 주십시오.")
            print("\n" * 2)



# 세계의 기억 교환
def exchange(player_1, ans):
    print("\n" * 1)
    while True:
        print("\n" * 4)
        print("{0:-^60}".format(" 세계의 기억 교환 "))
        print(f"{player_1.inven['month'][ans].name} X 10 -> {player_1.inven['month'][ans + 1].name} X 1")
        print(f"{player_1.inven['month'][ans].name}의 개수 : {player_1.inven['month'][ans].count}")
        print(f"{player_1.inven['month'][ans + 1].name}의 개수 : {player_1.inven['month'][ans + 1].count}")
        print("\n\n\n교환취소 : q / [구매하려면 수량 입력]")
        ans_1 = input(" : ")
        if ans_1 == 'q':
            print("\n" * 2)
            break
        else:
            try:
                ans_1 = int(ans_1)
                if player_1.inven['month'][ans].count >= ans_1 * 10:
                    player_1.inven['month'][ans].count = player_1.inven['month'][ans].count - ans_1 * 10
                    player_1.inven['month'][ans + 1].count = player_1.inven['month'][ans + 1].count + ans_1
                    print("\n성공적으로 교환하였습니다.\n")
                    break
                else:
                    print(f"{player_1.inven['month'][ans].name}이 부족합니다.")
            except:
                print("\n다시 입력해 주십시오.")


# 강화
def ster_force(player_1, select, ans):
    print("\n" * 3)
    while 0 <= player_1.print_inven[ans].liv < 10:

        print("{0:-^60}".format(" 아이템 세부사항 "))
        detailed_print_item(player_1, select, ans, 'ster_force')
        print("\n\n돌아가기 : q", end='')
        if select == 'atk':
            print(" / 무기 강화 : w", end='')
            if player_1.print_inven[ans].need_power_stats >= 5:
                print(" / 힘 강화 : e", end = '')
            if player_1.print_inven[ans].need_agility_stats >= 5:
                print(" / 민첩 강화 : r", end = '')
            if player_1.print_inven[ans].need_adventure_stats >= 5:
                print(" / 모험 강화 : t", end = '')
        elif select == 'def':
            print(" / 방어구 강화 : w", end='')
            if player_1.print_inven[ans].plus_power_stats >= 5:
                print(" / 힘 강화 : e", end = '')
            if player_1.print_inven[ans].plus_agility_stats >= 5:
                print(" / 민첩 강화 : r", end = '')
            if player_1.print_inven[ans].plus_adventure_stats >= 5:
                print(" / 모험 강화 : t", end = '')
        ans_1 = input("\n : ")

        if ans_1 == 'q':
            print("\n" * 2)
            break
        elif ans_1 == 'w':
            print("\n" * 1)
            while True:
                print("\n" * 5)
                print("{0:=^60}".format(" 나의 강화권 상황 "))
                if select == 'atk':
                    print(f"\n나의 무기 강화권 개수 : {player_1.inven['item'][player_1.inven['item'].index(fortification_item_101)].count}")
                elif select == 'def':
                    print(f"\n나의 방어구 강화권 개수 : {player_1.inven['item'][player_1.inven['item'].index(fortification_item_111)].count}")

                print("\n\n\n강화취소 : q / 강화 : w")
                ans_2 = input(" : ")

                if ans_2 == 'q':
                    break
                elif ans_2 == 'w':
                    if select == 'atk':
                        if player_1.inven['item'][player_1.inven['item'].index(fortification_item_101)].count > 0:
                            break
                        else:
                            print("\n강화권이 부족합니다.")
                    elif select == 'def':
                        if player_1.inven['item'][player_1.inven['item'].index(fortification_item_111)].count > 0:
                            break
                        else:
                            print("\n강화권이 부족합니다.")
                else:
                    print("\n다시 입력해 주십시오.")

            print("\n" * 1)
            while ans_2 != 'q' and player_1.print_inven[ans].liv >= 5:
                print("\n" * 5)
                print("{0:=^60}".format(" 나의 강화권 상황 "))
                print(f"\n파괴 방지권 : {player_1.inven['item'][player_1.inven['item'].index(fortification_item_301)].count}")
                print("\n\n\n사용하지 않음 : q / 파괴 방지권 : w")
                ans_3 = input(" : ")

                if ans_3 == 'q':
                    break
                elif ans_3 == 'w':
                    if player_1.inven['item'][player_1.inven['item'].index(fortification_item_301)].count > 0:
                        break
                    else:
                        print("\n파괴 방지권이 부족합니다.")
                else:
                    print("\n다시 입력해 주십시오.")

            print("\n" * 1)
            while ans_2 != 'q':
                success = star_force_list[player_1.print_inven[ans].liv].success
                fail = star_force_list[player_1.print_inven[ans].liv].fail
                fall = star_force_list[player_1.print_inven[ans].liv].fall
                destruction = star_force_list[player_1.print_inven[ans].liv].destruction

                try:
                    if ans_3 == 'w':
                        player_1.inven['item'][player_1.inven['item'].index(fortification_item_301)].count = \
                            player_1.inven['item'][player_1.inven['item'].index(fortification_item_301)].count - 1
                        fall = fall + destruction
                        destruction = 0
                except:
                    pass

                print()
                print("{0:-^60}".format(" 강화 "))
                print(f"\n\n\n성공 확률 : {success}%\n실패 확률 : {fail}%\n하락 확률 : {fall}%\n파괴 확률 : {destruction}%\n\n\n돌아가기 : q / 강화하기 : w\n")
                ans_4 = input(" : ")

                if ans_4 == 'q':
                    break
                elif ans_4 == 'w':
                    if select == 'atk':
                        player_1.inven['item'][player_1.inven['item'].index(fortification_item_101)].count = \
                            player_1.inven['item'][player_1.inven['item'].index(fortification_item_101)].count - 1
                    elif select == 'def':
                        player_1.inven['item'][player_1.inven['item'].index(fortification_item_111)].count = \
                            player_1.inven['item'][player_1.inven['item'].index(fortification_item_111)].count - 1

                    try:
                        if ans_3 == 'w':
                            player_1.inven['item'][player_1.inven['item'].index(fortification_item_301)].count = \
                                player_1.inven['item'][player_1.inven['item'].index(fortification_item_301)].count - 1
                    except:
                        pass

                    plus = 0

                    persent = choice("q" * success + "w" * fail + "e" * fall + "r" * destruction)

                    if persent == 'q':
                        for i in range(len(player_1.inven[select])):
                            if player_1.inven[select][i].name == player_1.print_inven[ans].name:
                                if player_1.inven[select][i].liv == 0:
                                    if select == 'atk':
                                        plus = player_1.inven[select][i].damage * 0.1
                                    elif select == 'def':
                                        plus = player_1.inven[select][i].defense * 0.1

                                if player_1.inven[select][i].liv == player_1.print_inven[ans].liv + 1:
                                    player_1.inven[select][i - 1].count = player_1.inven[select][i - 1].count - 1
                                    player_1.inven[select][i].count = player_1.inven[select][i].count + 1
                                    print("\n성공적으로 강화하였습니다.")
                                    break
                        else:
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count = \
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count - 1
                            player_1.inven[select].insert(player_1.inven[select].index(player_1.print_inven[ans]) + 1,
                                                          player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])])
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].count = 1
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].liv = \
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].liv + 1
                            if select == 'atk':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].damage = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].damage + plus
                            elif select == 'def':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].defense = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].defense + plus
                            print("\n성공적으로 강화하였습니다.")
                        break

                    elif persent == 'w':
                        print("\n강화를 실패하였습니다. (실패)")
                        break
                    elif persent == 'e':
                        for i in range(len(player_1.inven[select])):
                            if player_1.inven[select][i].name == player_1.print_inven[ans].name:
                                if player_1.inven[select][i].liv == player_1.print_inven[ans].liv - 1:
                                    player_1.inven[select][i + 1].count = player_1.inven[select][i + 1].count - 1
                                    player_1.inven[select][i].count = player_1.inven[select][i].count + 1
                                    print("\n강화를 실패하였습니다. (하락)")
                                    break
                    elif persent == 'r':
                        for i in range(len(player_1.inven[select])):
                            if player_1.inven[select][i].name == player_1.print_inven[ans].name:
                                if player_1.inven[select][i].liv == player_1.print_inven[ans].liv:
                                    player_1.inven[select][i].count = player_1.inven[select][i].count - 1
                                    print("\n강화를 실패하였습니다. (파괴)")
                                    break
                else:
                    print("\n다시 입력해 주십시오.")

        elif ans_1 == 'e':
            if player_1.print_inven[ans].need_power_stats >= 5 or player_1.print_inven[ans].plus_power_stats >= 5:
                print("\n" * 1)
                while True:
                    print("\n" * 5)
                    print("{0:=^60}".format(" 나의 강화권 상황 "))
                    print(f"\n 힘 강화권 : {player_1.inven['item'][player_1.inven['item'].index(fortification_item_201)].count}\n\n\n강화취소 : q / 강화 : w")
                    ans_2 = input(" : ")

                    if ans_2 == 'q':
                        break
                    elif ans_2 == 'w':
                        if player_1.inven['item'][player_1.inven['item'].index(fortification_item_201)].count > 0:
                            break
                        else:
                            print("\n강화권이 부족합니다.")
                    else:
                        print("\n다시 입력해 주십시오.")

                print("\n" * 1)
                while ans_2 != 'q':
                    print()
                    print("{0:-^60}".format(" 강화 "))
                    print( f"\n\n\n성공 확률 : 100%\n실패 확률 : 0%\n하락 확률 : 0%\n파괴 확률 : 0%\n\n\n돌아가기 : q / 강화하기 : w\n")
                    ans_3 = input(" : ")

                    if ans_3 == 'q':
                        break
                    elif ans_3 == 'w':
                        player_1.inven['item'][player_1.inven['item'].index(fortification_item_201)].count = \
                            player_1.inven['item'][player_1.inven['item'].index(fortification_item_201)].count - 1

                        for i in range(len(player_1.inven[select])):
                            if player_1.inven[select][i].name == player_1.print_inven[ans].name:
                                if player_1.inven[select][i].plus_power_stats == player_1.print_inven[ans].plus_power_stats - 5:
                                    player_1.inven[select][i - 1].count = player_1.inven[select][i - 1].count - 1
                                    player_1.inven[select][i].count = player_1.inven[select][i].count + 1
                                    print("\n성공적으로 강화하였습니다.")
                                    break
                        else:
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count = \
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count - 1
                            player_1.inven[select].insert(player_1.inven[select].index(player_1.print_inven[ans]) + 1,
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])])
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].count = 1
                            if select == 'atk':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].need_power_stats = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].need_power_stats - 5
                            elif select == 'def':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].plus_power_stats = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].plus_power_stats - 5
                            print("\n성공적으로 강화하였습니다.")
                        break
                    else:
                        print("\n다시 입력해 주십시오.")

        elif ans_1 == 'r':
            if player_1.print_inven[ans].need_agility_stats >= 5 or player_1.print_inven[ans].plus_agility_stats >= 5:
                print("\n" * 1)
                while True:
                    print("\n" * 5)
                    print("{0:=^60}".format(" 나의 강화권 상황 "))
                    print(
                        f"\n 민첩 강화권 : {player_1.inven['item'][player_1.inven['item'].index(fortification_item_202)].count}\n\n\n강화취소 : q / 강화 : w")
                    ans_2 = input(" : ")

                    if ans_2 == 'q':
                        break
                    elif ans_2 == 'w':
                        if player_1.inven['item'][player_1.inven['item'].index(fortification_item_202)].count > 0:
                            break
                        else:
                            print("\n강화권이 부족합니다.")
                    else:
                        print("\n다시 입력해 주십시오.")

                print("\n" * 1)
                while ans_2 != 'q':
                    print()
                    print("{0:-^60}".format(" 강화 "))
                    print(f"\n\n\n성공 확률 : 100%\n실패 확률 : 0%\n하락 확률 : 0%\n파괴 확률 : 0%\n\n\n돌아가기 : q / 강화하기 : w\n")
                    ans_3 = input(" : ")

                    if ans_3 == 'q':
                        break
                    elif ans_3 == 'w':
                        player_1.inven['item'][player_1.inven['item'].index(fortification_item_202)].count = \
                            player_1.inven['item'][player_1.inven['item'].index(fortification_item_202)].count - 1

                        for i in range(len(player_1.inven[select])):
                            if player_1.inven[select][i].name == player_1.print_inven[ans].name:
                                if player_1.inven[select][i].plus_agility_stats == player_1.print_inven[ans].plus_agility_stats - 5:
                                    player_1.inven[select][i - 1].count = player_1.inven[select][i - 1].count - 1
                                    player_1.inven[select][i].count = player_1.inven[select][i].count + 1
                                    print("\n성공적으로 강화하였습니다.")
                                    break
                        else:
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count = \
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count - 1
                            player_1.inven[select].insert(player_1.inven[select].index(player_1.print_inven[ans]) + 1,
                                                          player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])])
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].count = 1
                            if select == 'atk':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].need_agility_stats = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].need_agility_stats - 5
                            elif select == 'def':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].plus_agility_stats = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].plus_agility_stats - 5
                            print("\n성공적으로 강화하였습니다.")
                        break
                    else:
                        print("\n다시 입력해 주십시오.")

        elif ans_1 == 't':
            if player_1.print_inven[ans].need_adventure_stats >= 5 or player_1.print_inven[ans].plus_adventure_stats >= 5:
                print("\n" * 1)
                while True:
                    print("\n" * 5)
                    print("{0:=^60}".format(" 나의 강화권 상황 "))
                    print(
                        f"\n 모험 강화권 : {player_1.inven['item'][player_1.inven['item'].index(fortification_item_203)].count}\n\n\n강화취소 : q / 강화 : w")
                    ans_2 = input(" : ")

                    if ans_2 == 'q':
                        break
                    elif ans_2 == 'w':
                        if player_1.inven['item'][player_1.inven['item'].index(fortification_item_203)].count > 0:
                            break
                        else:
                            print("\n강화권이 부족합니다.")
                    else:
                        print("\n다시 입력해 주십시오.")

                print("\n" * 1)
                while ans_2 != 'q':
                    print()
                    print("{0:-^60}".format(" 강화 "))
                    print(f"\n\n\n성공 확률 : 100%\n실패 확률 : 0%\n하락 확률 : 0%\n파괴 확률 : 0%\n\n\n돌아가기 : q / 강화하기 : w\n")
                    ans_3 = input(" : ")

                    if ans_3 == 'q':
                        break
                    elif ans_3 == 'w':
                        player_1.inven['item'][player_1.inven['item'].index(fortification_item_203)].count = \
                            player_1.inven['item'][player_1.inven['item'].index(fortification_item_203)].count - 1

                        for i in range(len(player_1.inven[select])):
                            if player_1.inven[select][i].name == player_1.print_inven[ans].name:
                                if player_1.inven[select][i].plus_adventure_stats == player_1.print_inven[ans].plus_adventure_stats - 5:
                                    player_1.inven[select][i - 1].count = player_1.inven[select][i - 1].count - 1
                                    player_1.inven[select][i].count = player_1.inven[select][i].count + 1
                                    print("\n성공적으로 강화하였습니다.")
                                    break
                        else:
                            player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count = \
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])].count - 1
                            player_1.inven[select].insert(player_1.inven[select].index(player_1.print_inven[ans]) + 1,
                                                          player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans])])
                            player_1.inven[select][
                                player_1.inven[select].index(player_1.print_inven[ans]) + 1].count = 1
                            if select == 'atk':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].need_adventure_stats = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].need_adventure_stats - 5
                            elif select == 'def':
                                player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].plus_adventure_stats = \
                                    player_1.inven[select][player_1.inven[select].index(player_1.print_inven[ans]) + 1].plus_adventure_stats - 5
                            print("\n성공적으로 강화하였습니다.")
                        break
                    else:
                        print("\n다시 입력해 주십시오.")
        else:
            print("\n다시 입력해 주십시오.")
            print("\n" * 2)

    if player_1.print_inven[ans].liv == 10:
        print(f"\n10레벨이 최고레벨 입니다.")
        print("\n" * 2)
    elif player_1.print_inven[ans].liv == -1:
        print(f"\n강화가 불가능한 아이템입니다.")
        print("\n" * 2)



# 몬스터
def monster_print(select_monster):
    print(f"{' Lv.' + str(select_monster.liv) + '_' + select_monster.name + ' ':=^60}")
    print(f"체력 : {select_monster.health}   공격력 : {select_monster.damage}")

def monster(player_1):
    if player_1.point == 1:
        appear = choice("y" * 5 + "n" * 95)
    else:
        appear = choice("y" * 30 + "n" * 70)

    if appear == "y":
        if player_1.point == 66:
            select_ = choice(list(monster_list_66))
            select = monster_list_66.index(select_)
            select_monster = monster_list_66[select]
        elif player_1.point == 23:
            select_ = choice(list(monster_list_23))
            select = monster_list_23.index(select_)
            select_monster = monster_list_23[select]
        elif player_1.point == 4:
            select_ = choice(list(monster_list_04))
            select = monster_list_04.index(select_)
            select_monster = monster_list_04[select]
        elif player_1.point == 6:
            select_ = choice(list(monster_list_06))
            select = monster_list_06.index(select_)
            select_monster = monster_list_06[select]
        elif player_1.point == 7:
            select_ = choice(list(monster_list_07))
            select = monster_list_07.index(select_)
            select_monster = monster_list_07[select]
        elif player_1.point == 15:
            select_ = choice(list(monster_list_15))
            select = monster_list_15.index(select_)
            select_monster = monster_list_15[select]
        elif player_1.point == 10:
            select_ = choice(list(monster_list_10))
            select = monster_list_10.index(select_)
            select_monster = monster_list_10[select]
        elif player_1.point == 14:
            select_ = choice(list(monster_list_14))
            select = monster_list_14.index(select_)
            select_monster = monster_list_14[select]
        elif player_1.point == 12:
            select_ = choice(list(monster_list_12))
            select = monster_list_12.index(select_)
            select_monster = monster_list_12[select]
        elif player_1.point == 25:
            select_ = choice(list(monster_list_25))
            select = monster_list_25.index(select_)
            select_monster = monster_list_25[select]
        elif player_1.point == 8:
            select_ = choice(list(monster_list_08))
            select = monster_list_08.index(select_)
            select_monster = monster_list_08[select]
        elif player_1.point == 1:
            select_ = choice(list(monster_list_01))
            select = monster_list_01.index(select_)
            select_monster = monster_list_01[select]
        else:
            select_monster = "none"

        if select_monster != 'none':
            print(f"\n야생의 {select_monster.name} 이(가) 나타났다.\n")
            turn = 1

            while True:
                if turn % 4 == 0:
                    select_monster.health = select_monster.health + select_monster.recovery_health
                    if select_monster.health > select_monster.max_health:
                        select_monster.health = select_monster.max_health
                monster_print(select_monster)
                print("\n" * 1)
                showinfo(player_1, 2)

                if turn == 1:
                    ans = input("\n공격(q) 아이템(w) 도망(e)\n : ")
                else:
                    ans = input("\n공격(q) 아이템(w)\n : ")

                if ans == "q":
                    attack(player_1, select_monster, 'player')

                    if select_monster.health <= 0:
                        print("\n" * 4)
                        player_1.exp = player_1.exp + select_monster.drop_exp
                        player_1.money = player_1.money + select_monster.drop_money
                        print(f"{select_monster.name} 이(가) 죽었습니다.")
                        print(f"\n돈 {select_monster.drop_money} 원 을 얻었습니다.\n경험치 {select_monster.drop_exp} 을(를) 얻었습니다.")
                        if select_monster.drop_item_count != 0:
                            if select_monster.drop_item in month_item_list:
                                count = 0
                                for i in range(1, select_monster.drop_item_count):
                                    acquire = choice('y' * 70 + 'n' * 30)
                                    if acquire == 'y':
                                        if select_monster.drop_item in player_1.inven["month"]:
                                            num = player_1.inven["month"].index(select_monster.drop_item)
                                            player_1.inven["month"][num].count = player_1.inven["month"][num].count + 1
                                            count = count + 1
                                    elif acquire == 'n':
                                        pass
                                print(f"{select_monster.drop_item.name}을 {count}개 얻었습니댜.")
                            elif select_monster.drop_item.name == "렉스의 3번째 명작 '녹색 이빨'" or select_monster.drop_item.name == "렉스의 1번째 명작 '홍염의 날개깃'":
                                num = player_1.inven["atk"].index(select_monster.drop_item)
                                num_1 = num
                                plag = 0
                                while True:
                                    if player_1.inven["atk"][num_1].name == select_monster.drop_item.name:
                                        if player_1.inven["atk"][num].count <= 1:
                                            plag = plag + 1
                                            break
                                    else:
                                        break

                                    if num + 10 == num_1:
                                        break

                                    num_1 = num_1 + 1

                                if plag == 0:
                                    player_1.inven["atk"][num].count = player_1.inven["atk"][num].count + 1
                                    print(f"{select_monster.drop_item.name}을(를) 얻었습니댜.")
                                else:
                                    print()
                        else:
                            print()

                        input("\n\n[(enter)키를 누르세요]")
                        print("\n" * 1)
                        break
                    else:
                        attack(player_1, select_monster, 'monster')

                    if player_1.health <= 0:
                        input("[(enter)키를 누르세요]")
                        print("\n" * 1)
                        break

                    turn = turn + 1

                elif ans == "w":
                    inventory(player_1, 1)

                elif ans == "e":
                    if turn == 1:
                        run_away = choice("y" * 85 + "n" * 15)
                        if run_away == "y":
                            print("\n" * 13)
                            print("도망에 성공했습니다.")
                            input("[(enter)키를 누르세요]")
                            print("\n" * 1)
                            break
                        elif run_away == "n":
                            print("\n도망에 실패했습니다.\n\n\n")
                else:
                    print("\n올바른 문자를 입력하세요\n\n\n")
        else:
            pass
    elif appear == "n":
        pass

def attack(player_1, select_monster, object):
    if object == "player":
        if player_1.damage != 0:
            if player_1.critical > 100:
                critical_appear = "y"
            else:
                critical_appear = choice("y" * player_1.critical + "n" * (100 - player_1.critical))

            print("\n" * 11)
            damage = 0
            if critical_appear == "y":
                print("크리티컬!", end=' ')
                damage = player_1.damage * 2
            elif critical_appear == "n":
                damage = player_1.damage
                print()

            if select_monster.health < damage:
                damage = select_monster.health
                select_monster.health = 0
            else:
                select_monster.health = select_monster.health - damage

            print(f"\n{select_monster.name} 에게 {damage} 데미지를 입혔습니다.")
        else:
            print(f"{select_monster.name} 에게 0 데미지를 입혔습니다.")
    elif object == "monster":
        damage = select_monster.damage - player_1.defense
        if damage < 0:
            damage = 0

        if player_1.health < damage:
            damage = player_1.health
            player_1.health = 0
        else:
            player_1.health = player_1.health - damage

        if player_1.health >= 0:
            player_1.health = player_1.health + player_1.def_physical_absorption
            if player_1.health > player_1.result_health:
                player_1.health = player_1.result_health

        print(f"{select_monster.name} 에게로 부터 {damage} 데미지를 받았습니다.\n")



# 스텟
def stats(player_1):
    print('\nLv. ' + str(player_1.liv) + ' 로 레벨업 하였습니다.')

    if player_1.liv < 50:
        player_1.max_health = player_1.max_health + 40
    elif player_1.liv < 70:
        player_1.max_health = player_1.max_health + 80
    else:
        player_1.max_health = player_1.max_health + 500

    stats_point = 4

    while stats_point > 0:
        print("\n" * 5)
        print(f"{' 현재 스텟 ':=^60}")
        print(f"힘 스텟 : {player_1.po_count} / 민첩 스텟 : {player_1.ag_count} / 모험 스텟 : {player_1.ad_count}\n\n")
        print(f"남은 스텟포인트 : {stats_point}")
        print("\n힘 : q / 민첩 : w / 모험 : e")
        num = input(" : ")
        print("\n" * 8)
        if num == "q":
            print(f"{' 힘 스텟 ':-^60}")
            print(f"\n스텟 1당 공격력이 0.5 증가합니다.\n[현재 나의 힘 스탯 : {player_1.po_count}]\n\n")
            ans = input("y / n : ")
            if ans == 'y':
                print("\n공격력 0.5가 추가됩니다.")
                player_1.po_count = player_1.po_count + 1
                stats_point = stats_point - 1
            elif ans == 'n':
                print("\n" * 1)
            else:
                print("\n올바른 문자를 입력하세요.")

        elif num == "w":
            print(f"{' 민첩 스텟 ':-^60}")
            print(f"\n스텟 1당 크리티컬 확률이 0.1% 증가합니다.\n[현재 나의 민첩 스탯 : {player_1.ag_count}]\n\n")
            ans = input("y / n : ")
            if ans == 'y':
                print("\n크리티컬 확률 0.1%가 추가 됩니다.")
                player_1.ag_count = player_1.ag_count + 1
                stats_point = stats_point - 1
            elif ans == 'n':
                print("\n" * 1)
            else:
                print("\n올바른 문자를 입력하세요.")

        elif num == 'e':
            print(f"{' 모험 스텟 ':-^60}")
            print(f"\n스텟 1당 체력이 6 증가합니다.\n[현재 나의 모험 스탯 : {player_1.ad_count}]\n\n")
            ans = input("y / n : ")
            if ans == 'y':
                print("\n체력이 6 추가 됩니다.")
                player_1.ad_count = player_1.ad_count + 1
                stats_point = stats_point - 1
            elif ans == 'n':
                print("\n" * 1)
            else:
                print("\n올바른 문자를 입력하세요.")
        else:
            print("\n올바른 문자를 입력하세요.")
    print("\n" * 4)



# 글씨 바꾸기
def use_to_korean(word):
    if word == 'atk':
        return '무기'
    elif word == 'def':
        return '방어구'
    elif word == 'potion':
        return '포션'
    elif word == 'month':
        return '세계의 기억'
    elif word == 'item':
        return '일반'

def simple_to_txt(word):
    if word == 'q':
        return "atk"
    elif word == 'w':
        return "def"
    elif word == 'e':
        return "potion"
    elif word == 'r':
        return "month"
    elif word == 't':
        return "item"
    elif word == '':
        return "none"

def point_to_txt(player_1):  # 구역 : 36 / 지역 : 24 / 바다   성 : 1, 2, 3, 5, 19, 22, 28, 36
    if player_1.point == 0:
        return '바다'
    elif player_1.point == 1:
        return '에나 성'  # 성
    elif player_1.point == 2:
        return '뒤오 성'  # 성
    elif player_1.point == 3:
        return '트리아 성'  # 성
    elif player_1.point == 4:
        return '오염된 강'
    elif player_1.point == 5:
        return '누군가의 성'  # 성
    elif player_1.point == 6:
        return '해적소굴'
    elif player_1.point == 7:
        return '불탄 점령지'
    elif player_1.point == 8:
        return '선녀 호수'
    elif player_1.point == 9:
        return '발길이 머무르는 곳'
    elif player_1.point == 10:
        return '오염된 마을'
    elif player_1.point == 11:
        return '심연의 갱도'
    elif player_1.point == 12:
        return '인어 왕국'
    elif player_1.point == 13:
        return '누군가의 무덤'
    elif player_1.point == 14:
        return '드워프 마을'
    elif player_1.point == 15:
        return '엘프 유적'
    elif player_1.point == 16:
        return '에나 동쪽 항구'
    elif player_1.point == 17:
        return '에나 낚시터'
    elif player_1.point == 18:
        return '세상을 등진곳'
    elif player_1.point == 19:
        return '얼음성'  # 성
    elif player_1.point == 20:
        return '드워프 유적지'
    elif player_1.point == 21:
        return '심연의 갱도'
    elif player_1.point == 22:
        return '신기루 성'  # 성
    elif player_1.point == 23:
        return '마니라 리'
    elif player_1.point == 24:
        return '봉인된 신전'
    elif player_1.point == 25:
        return '거미 동굴'
    elif player_1.point == 26:
        return '모험의 갈림길'
    elif player_1.point == 27:
        return '숨겨진 드워프 마을'
    elif player_1.point == 28:
        return '오래된 성'  # 성
    elif player_1.point == 29:
        return '바다 신전'
    elif player_1.point == 30:
        return '세상을 등진곳 동쪽 항구'
    elif player_1.point == 31:
        return '신기루성 남쪽 항구'
    elif player_1.point == 32:
        return '고대 유적의 섬'
    elif player_1.point == 33:
        return '고대 유적의 섬 선착장'
    elif player_1.point == 34:
        return '신들의 고향 선착장'
    elif player_1.point == 35:
        return '생기의 마을'
    elif player_1.point == 36:
        return '오크의 성'  # 성
    
    elif player_1.point == 50:
        return '에나'
    elif player_1.point == 51:
        return '뒤오'
    elif player_1.point == 52:
        return '트리아'
    elif player_1.point == 53:
        return '생명의 숲'
    elif player_1.point == 54:
        return '가벼운 무법지'
    elif player_1.point == 55:
        return '평화로운곳'
    elif player_1.point == 56:
        return '대륙의 통로'
    elif player_1.point == 57:
        return '파도가 부숴지는 해변'
    elif player_1.point == 58:
        return '발길이 머무르는곳'
    elif player_1.point == 59:
        return '구름의 휴식처'
    elif player_1.point == 60:
        return '태양의 열망'
    elif player_1.point == 61:
        return '바람 길목'
    elif player_1.point == 62:
        return '신화가 잠든 대지'
    elif player_1.point == 63:
        return '물거품의 바다'
    elif player_1.point == 64:
        return '고대 유적의 섬'
    elif player_1.point == 65:
        return '개척자의 섬'
    elif player_1.point == 66:
        return '신들의 고향'
    elif player_1.point == 67:
        return '비명의 바다'
    elif player_1.point == 68:
        return '죽음의 바다'
    elif player_1.point == 69:
        return '탄식의 바다'
    elif player_1.point == 70:
        return '생기가 있는 섬'
    elif player_1.point == 71:
        return '여유로운 바다'
    elif player_1.point == 72:
        return '갈 수 없는 섬'
    elif player_1.point == 73:
        return '돌아올 수 없는 섬'
    elif player_1.point == 74:
        return '잊혀진 섬'



# 체력 체크
def plus_stats(player_1):
    po_count_amount = 0
    try:
        po_count_amount = int(player_1.equipment['def_1'][1].plus_power_stats) + po_count_amount
    except:
        pass
    try:
        po_count_amount = int(player_1.equipment['def_2'][1].plus_power_stats) + po_count_amount
    except:
        pass
    try:
        po_count_amount = int(player_1.equipment['def_3'][1].plus_power_stats) + po_count_amount
    except:
        pass
    try:
        po_count_amount = int(player_1.equipment['def_4'][1].plus_power_stats) + po_count_amount
    except:
        pass
    player_1.plus_po_count = po_count_amount

    ag_count_amount = 0
    try:
        ag_count_amount = int(player_1.equipment['def_1'][1].plus_agility_stats) + ag_count_amount
    except:
        pass
    try:
        ag_count_amount = int(player_1.equipment['def_2'][1].plus_agility_stats) + ag_count_amount
    except:
        pass
    try:
        ag_count_amount = int(player_1.equipment['def_3'][1].plus_agility_stats) + ag_count_amount
    except:
        pass
    try:
        ag_count_amount = int(player_1.equipment['def_4'][1].plus_agility_stats) + ag_count_amount
    except:
        pass
    player_1.plus_ag_count = ag_count_amount

    ad_count_amount = 0
    try:
        ad_count_amount = int(player_1.equipment['def_1'][1].plus_adventure_stats) + ad_count_amount
    except:
        pass
    try:
        ad_count_amount = int(player_1.equipment['def_2'][1].plus_adventure_stats) + ad_count_amount
    except:
        pass
    try:
        ad_count_amount = int(player_1.equipment['def_3'][1].plus_adventure_stats) + ad_count_amount
    except:
        pass
    try:
        ad_count_amount = int(player_1.equipment['def_4'][1].plus_adventure_stats) + ad_count_amount
    except:
        pass
    player_1.plus_ad_count = ad_count_amount

    player_1.stats_health = (player_1.ad_count + player_1.plus_ad_count) * 6
    player_1.result_health = player_1.max_health + player_1.stats_health



# 공격력 / 방어력 체크
def attack_defense(player_1):
    def_amount = 0
    def_physical_absorption_amount = 0
    try:
        def_amount = int(player_1.equipment['def_1'][1].defense) + def_amount
        def_physical_absorption_amount = int(player_1.equipment['def_1'][1].physical_absorption_amount) + def_physical_absorption_amount
    except:
        pass
    try:
        def_amount = int(player_1.equipment['def_2'][1].defense) + def_amount
        def_physical_absorption_amount = int(player_1.equipment['def_2'][1].physical_absorption_amount) + def_physical_absorption_amount
    except:
        pass
    try:
        def_amount = int(player_1.equipment['def_3'][1].defense) + def_amount
        def_physical_absorption_amount = int(player_1.equipment['def_3'][1].physical_absorption_amount) + def_physical_absorption_amount
    except:
        pass
    try:
        def_amount = int(player_1.equipment['def_4'][1].defense) + def_amount
        def_physical_absorption_amount = int(player_1.equipment['def_4'][1].physical_absorption_amount) + def_physical_absorption_amount
    except:
        pass
    player_1.defense = def_amount
    player_1.def_physical_absorption = def_physical_absorption_amount

    damage_amount = 0
    critical_amount = 0
    atk_physical_absorption_amount = 0
    try:
        damage_amount = int(player_1.equipment['atk'][1].damage) + damage_amount
    except:
        damage_amount = damage_amount + 1
    try:
        critical_amount = int(player_1.equipment['atk'][1].critical) + critical_amount
    except:
        pass
    try:
        atk_physical_absorption_amount = int(player_1.equipment['atk'][1].physical_absorption) + atk_physical_absorption_amount
    except:
        pass
    player_1.damage = ((player_1.po_count + player_1.plus_po_count) * 0.5) + damage_amount
    player_1.critical = ((player_1.ag_count + player_1.plus_ag_count) * 0.1) + critical_amount
    player_1.atk_physical_absorption = atk_physical_absorption_amount



# 지역 체크
def point(player_1):
    point_count = 0

    if 83 <= player_1.player_x <= 91:
        if 48 <= player_1.player_y <= 56:
            player_1.point = 1
            point_count += 1
    if 80 <= player_1.player_x <= 86:
        if 64 <= player_1.player_y <= 70:
            player_1.point = 2
            point_count += 1
    if 68 <= player_1.player_x <= 74:
        if 77 <= player_1.player_y <= 83:
            player_1.point = 3
            point_count += 1
    if 74 <= player_1.player_x <= 78:
        if 46 <= player_1.player_y <= 50:
            player_1.point = 4
            point_count += 1
    if 65 <= player_1.player_x <= 69:
        if 37 <= player_1.player_y <= 41:
            player_1.point = 5
            point_count += 1
    if 64 <= player_1.player_x <= 66:
        if 46 <= player_1.player_y <= 48:
            player_1.point = 6
            point_count += 1
    if 66 <= player_1.player_x <= 69:
        if 48 <= player_1.player_y <= 52:
            player_1.point = 7
            point_count += 1
    if 72 <= player_1.player_x <= 76:
        if 55 <= player_1.player_y <= 59:
            player_1.point = 8
            point_count += 1
    if 64 <= player_1.player_x <= 70:
        if 62 <= player_1.player_y <= 68:
            player_1.point = 9
            point_count += 1
    if 75 <= player_1.player_x <= 79:
        if 63 <= player_1.player_y <= 67:
            player_1.point = 10
            point_count += 1
    if 63 <= player_1.player_x <= 67:
        if 76 <= player_1.player_y <= 80:
            player_1.point = 11
            point_count += 1
    if 63 <= player_1.player_x <= 67:
        if 81 <= player_1.player_y <= 85:
            player_1.point = 12
            point_count += 1
    if 77 <= player_1.player_x <= 79:
        if 74 <= player_1.player_y <= 76:
            player_1.point = 13
            point_count += 1
    if 81 <= player_1.player_x <= 87:
        if 77 <= player_1.player_y <= 83:
            player_1.point = 14
            point_count += 1
    if 94 <= player_1.player_x <= 98:
        if 65 <= player_1.player_y <= 69:
            player_1.point = 15
            point_count += 1
    if 92 <= player_1.player_x <= 93:
        if 51 <= player_1.player_y <= 54:
            player_1.point = 16
            point_count += 1
    if 85 <= player_1.player_x <= 88:
        if 46 <= player_1.player_y <= 47:
            player_1.point = 17
            point_count += 1
    if 23 <= player_1.player_x <= 29:
        if 73 <= player_1.player_y <= 79:
            player_1.point = 18
            point_count += 1
    if 18 <= player_1.player_x <= 22:
        if 68 <= player_1.player_y <= 72:
            player_1.point = 19
            point_count += 1
    if 28 <= player_1.player_x <= 32:
        if 58 <= player_1.player_y <= 62:
            player_1.point = 20
            point_count += 1
    if 24 <= player_1.player_x <= 26:
        if 54 <= player_1.player_y <= 56:
            player_1.point = 21
            point_count += 1
    if 30 <= player_1.player_x <= 36:
        if 49 <= player_1.player_y <= 55:
            player_1.point = 22
            point_count += 1
    if 39 <= player_1.player_x <= 41:
        if 67 <= player_1.player_y <= 69:
            player_1.point = 23
            point_count += 1
    if 48 <= player_1.player_x <= 52:
        if 67 <= player_1.player_y <= 71:
            player_1.point = 24
            point_count += 1
    if 46 <= player_1.player_x <= 52:
        if 57 <= player_1.player_y <= 63:
            player_1.point = 25
            point_count += 1
    if 40 <= player_1.player_x <= 44:
        if 50 <= player_1.player_y <= 54:
            player_1.point = 26
            point_count += 1
    if 38 <= player_1.player_x <= 40:
        if 46 <= player_1.player_y <= 48:
            player_1.point = 27
            point_count += 1
    if 44 <= player_1.player_x <= 50:
        if 42 <= player_1.player_y <= 48:
            player_1.point = 28
            point_count += 1
    if 48 <= player_1.player_x <= 52:
        if 31 <= player_1.player_y <= 35:
            player_1.point = 29
            point_count += 1
    if 31 <= player_1.player_x <= 32:
        if 74 <= player_1.player_y <= 76:
            player_1.point = 30
            point_count += 1
    if 31 <= player_1.player_x <= 33:
        if 46 <= player_1.player_y <= 47:
            player_1.point = 31
            point_count += 1
    if 3 <= player_1.player_x <= 8:
        if 33 <= player_1.player_y <= 38:
            player_1.point = 32
            point_count += 1
    if 14 <= player_1.player_x <= 16:
        if 25 <= player_1.player_y <= 26:
            player_1.point = 33
            point_count += 1
    if 16 <= player_1.player_x <= 18:
        if 14 <= player_1.player_y <= 15:
            player_1.point = 34
            point_count += 1
    if 9 <= player_1.player_x <= 11:
        if 49 <= player_1.player_y <= 51:
            player_1.point = 35
            point_count += 1
    if 49 <= player_1.player_x <= 51:
        if 94 <= player_1.player_y <= 96:
            player_1.point = 36
            point_count += 1

    if point_count == 0:
        if 77 <= player_1.player_x <= 93:
            if 46 <= player_1.player_y <= 62:
                player_1.point = 50
        if 77 <= player_1.player_x <= 87:
            if 63 <= player_1.player_y <= 73:
                player_1.point = 51
        if 68 <= player_1.player_x <= 76:
            if 75 <= player_1.player_y <= 83:
                player_1.point = 52
        if 88 <= player_1.player_x <= 98:
            if 63 <= player_1.player_y <= 73:
                player_1.point = 53
        if 64 <= player_1.player_x <= 76:
            if 36 <= player_1.player_y <= 48:
                player_1.point = 54
        if 66 <= player_1.player_x <= 76:
            if 49 <= player_1.player_y <= 59:
                player_1.point = 55
        if 62 <= player_1.player_x <= 76:
            if 60 <= player_1.player_y <= 74:
                player_1.point = 56
        if 58 <= player_1.player_x <= 59:
            if 61 <= player_1.player_y <= 63:
                player_1.point = 56
        if 60 <= player_1.player_x <= 61:
            if 62 <= player_1.player_y <= 65:
                player_1.point = 56
        if 57 <= player_1.player_x <= 67:
            if 75 <= player_1.player_y <= 85:
                player_1.point = 57
        if 77 <= player_1.player_x <= 88:
            if 74 <= player_1.player_y <= 84:
                player_1.point = 58
        if 18 <= player_1.player_x <= 32:
            if 65 <= player_1.player_y <= 79:
                player_1.point = 59
        if 18 <= player_1.player_x <= 36:
            if 46 <= player_1.player_y <= 64:
                player_1.point = 60
        if 37 <= player_1.player_x <= 51:
            if 41 <= player_1.player_y <= 55:
                player_1.point = 61
        if 37 <= player_1.player_x <= 53:
            if 56 <= player_1.player_y <= 72:
                player_1.point = 62
        if 54 <= player_1.player_x <= 55:
            if 58 <= player_1.player_y <= 61:
                player_1.point = 62
        if 56 <= player_1.player_x <= 57:
            if 60 <= player_1.player_y <= 62:
                player_1.point = 62
        if 43 <= player_1.player_x <= 53:
            if 30 <= player_1.player_y <= 40:
                player_1.point = 63
        if 2 <= player_1.player_x <= 16:
            if 25 <= player_1.player_y <= 39:
                player_1.point = 64
        if 23 <= player_1.player_x <= 29:
            if 19 <= player_1.player_y <= 25:
                player_1.point = 65
        if 16 <= player_1.player_x <= 22:
            if 9 <= player_1.player_y <= 15:
                player_1.point = 66
        if 44 <= player_1.player_x <= 48:
            if 26 <= player_1.player_y <= 20:
                player_1.point = 67
        if 44 <= player_1.player_x <= 48:
            if 11 <= player_1.player_y <= 15:
                player_1.point = 68
        if 49 <= player_1.player_x <= 55:
            if 13 <= player_1.player_y <= 19:
                player_1.point = 69
        if 6 <= player_1.player_x <= 12:
            if 87 <= player_1.player_y <= 93:
                player_1.point = 70
        if 8 <= player_1.player_x <= 12:
            if 82 <= player_1.player_y <= 86:
                player_1.point = 71
        if 47 <= player_1.player_x <= 51:
            if 93 <= player_1.player_y <= 98:
                player_1.point = 72
        if 47 <= player_1.player_x <= 53:
            if 84 <= player_1.player_y <= 90:
                player_1.point = 73
        if 43 <= player_1.player_x <= 45:
            if 78 <= player_1.player_y <= 80:
                player_1.point = 74



# 레벨 체크
def level(player_1):
    if player_1.liv == 1:
        if player_1.exp >= 4:
            player_1.exp = player_1.exp - 4
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif player_1.liv == 2:
        if player_1.exp >= 400:
            player_1.exp = player_1.exp - 400
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 3 <= player_1.liv <= 4:
        if player_1.exp >= 300:
            player_1.exp = player_1.exp - 300
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 5 <= player_1.exp <= 10:
        if player_1.exp >= player_1.exp * 100:
            player_1.exp = player_1.exp - 100
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 11 <= player_1.exp <= 20:
        if player_1.exp >= 1000 + (player_1.liv - 10) * 200:
            player_1.exp = player_1.exp - (1000 + (player_1.liv - 10) * 200)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 21 <= player_1.exp <= 30:
        if player_1.exp >= 3000 + (player_1.liv - 20) * 300:
            player_1.exp = player_1.exp - (3000 + (player_1.liv - 20) * 300)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 31 <= player_1.exp <= 40:
        if player_1.exp >= 6000 + (player_1.liv - 30) * 400:
            player_1.exp = player_1.exp - (6000 + (player_1.liv - 30) * 400)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 41 <= player_1.exp <= 50:
        if player_1.exp >= 10000 + (player_1.liv - 40) * 500:
            player_1.exp = player_1.exp - (10000 + (player_1.liv - 40) * 500)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 51 <= player_1.exp <= 60:
        if player_1.exp >= 15000 + (player_1.liv - 50) * 600:
            player_1.exp = player_1.exp - (15000 + (player_1.liv - 50) * 600)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 61 <= player_1.exp <= 70:
        if player_1.exp >= 21000 + (player_1.liv - 60) * 700:
            player_1.exp = player_1.exp - (21000 + (player_1.liv - 60) * 700)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 71 <= player_1.exp <= 80:
        if player_1.exp >= 28000 + (player_1.liv - 70) * 800:
            player_1.exp = player_1.exp - (28000 + (player_1.liv - 70) * 800)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 81 <= player_1.exp <= 90:
        if player_1.exp >= 36000 + (player_1.liv - 80) * 900:
            player_1.exp = player_1.exp - (36000 + (player_1.liv - 80) * 900)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 91 <= player_1.exp <= 100:
        if player_1.exp >= 45000 + (player_1.liv - 90) * 1000:
            player_1.exp = player_1.exp - (45000 + (player_1.liv - 90) * 1000)
            player_1.liv = player_1.liv + 1
            stats(player_1)
    elif 101 <= player_1.exp:
        if player_1.exp >= 5500:
            player_1.exp = player_1.exp - 5500
            player_1.liv = player_1.liv + 1
            stats(player_1)



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
    print("\n" * 9)
    print("\nNo_name\n")
    print("(이 게임은 15칸의 로그 화면을 요구합니다.)\n\n[시작하려면 (enter)]")
    input(" : ")
    print("\n" * 15)


# 게임 종료
def game_over():
    print("\n" * 14)
    print("게임을 종료하시겠습니까?")
    while True:
        end_ans = input("y / n : ")
        if end_ans == "y":
            print("\n게임을 종료합니다.")

            print("gmae over")
            break
        if end_ans == "n":
            print("\n게임을 계속 진행합니다.")
            main()



# 메인
def main():
    input("게임을 시작하려면 엔터")

    print("\n" * 14)

    # story()

    player_name = input("플레이어 이름을 입력하십시오. = ")
    while player_name == "":
        print("\n" * 13)
        print("유효한 이름을 입력하십시오")
        player_name = input("플레이어 이름을 입력하십시오. = ")

    try:
        player_1 = Player(player_name, 1, [], [], [], 60, 60, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 87, 52, [])
        village = 1

        player_1.inven['atk'] = list(atk_item_list)
        player_1.inven['def'] = list(def_item_list)
        player_1.inven['potion'] = list(potion_item_list)
        player_1.inven['month'] = list(month_item_list)
        player_1.inven['item'] = list(fortification_item_list)

        player_1.warp_manager = list(warp_manager_list)

        if player_name == 'admin':
            player_1.equipment['atk'].append(R_atk_item_801)
            player_1.equipment['def_1'].append(R_def_item_931)
            player_1.equipment['def_2'].append(R_def_item_932)
            player_1.equipment['def_3'].append(R_def_item_933)
            player_1.equipment['def_4'].append(R_def_item_934)

    except:
        time.sleep(1.3)
        print('\n' * 13)
        print("게임로드중 오류가 발생하였습니다.")
        time.sleep(0.7)
        print("게임을 재시작하여 주십시오.")
        time.sleep(0.7)
        print("오류가 지속될경우 다음의연락처로 개발자에게 연락하여주세요.\nh5638880@naver.com")
        time.sleep(1)
        print()
        while True:
            input("RESTART")
    else:
        time.sleep(1.3)
        print('\n' * 13)
        print("정상적으로 로그인 되었습니다.")
        time.sleep(0.7)
        print("정보 불러오는 중...")
        time.sleep(0.7)
        if player_name == 'admin':
            print(f"환영합니다. 개발자님")
        else:
            print(f"환영합니다. {player_1.name} 님")
        time.sleep(1)
        print("\n" * 1)

    while True:

        print("\n" * 4)

        plus_stats(player_1)
        attack_defense(player_1)
        point(player_1)
        level(player_1)

        # 마을 버프
        if player_1.point == 1 or player_1.point == 2 or player_1.point == 3 or player_1.point == 5 or player_1.point == 19 or \
                player_1.point == 22 or player_1.point == 28 or player_1.point == 36:
            player_1.health = player_1.health + 50

        # 체력 최대치
        if player_1.health > player_1.result_health:
            player_1.health = player_1.result_health

        showinfo(player_1, 1)

        warp_manager_count = 0
        for i in range(len(warp_manager_list)):
            if player_1.player_x == player_1.warp_manager[i].x and player_1.player_y == player_1.warp_manager[i].y:
                print(f"공간마법사 : '{player_1.warp_manager[i].name}'")
                if player_1.warp_manager[i].count == 0:
                    warp_manager_count = 1
                elif player_1.warp_manager[i].count == 1:
                    warp_manager_count = 2
        if warp_manager_count == 0:
            print()

        if village == 1:
            if player_1.point == 1 or player_1.point == 2 or player_1.point == 3 or player_1.point == 5 or player_1.point == 19 or \
                    player_1.point == 22 or player_1.point == 28 or player_1.point == 36:
                if warp_manager_count == 1:
                    print("\n이동하기 : w,a,s,d / 마을 진입 : q / 인벤토리 : e / 공간마법사 등록 : f")
                elif warp_manager_count == 2:
                    print("\n이동하기 : w,a,s,d / 마을 진입 : q / 인벤토리 : e / 공간마법사 : f")
                else:
                    print("\n이동하기 : w,a,s,d / 마을 진입 : q / 인벤토리 : e")
            else:
                if warp_manager_count == 1:
                    print("\n이동하기 : w,a,s,d / 인벤토리 : e / 공간마법사 등록 : f")
                elif warp_manager_count == 2:
                    print("\n이동하기 : w,a,s,d / 인벤토리 : e / 공간마법사 : f")
                else:
                    print("\n이동하기 : w,a,s,d / 인벤토리 : e")

        if village == 2:
            print("\n마을 나가기 : q : 상점 : w / 횐전소 : e / 강화소 : r")

        ans = input(" : ")

        if village == 1:
            if ans == "w":
                player_1.player_y = player_1.player_y + 1
                if player_1.player_y > 100:
                    player_1.player_y = 100
                    print("\n최대 활동범위는 1~100,1~100 입니다.")
                else:
                    print("\n앞으로 이동")
                    monster(player_1)
            elif ans == "s":
                player_1.player_y = player_1.player_y - 1
                if player_1.player_y < 0:
                    player_1.player_y = 0
                    print("\n최대 활동범위는 1~100,1~100 입니다.")
                else:
                    print("\n뒤로 이동")
                    monster(player_1)
            elif ans == "d":
                player_1.player_x = player_1.player_x + 1
                if player_1.player_x > 100:
                    player_1.player_x = 100
                    print("\n최대 활동범위는 1~100,1~100 입니다.")
                else:
                    print("\n오른쪽으로 이동")
                    monster(player_1)
            elif ans == "a":
                player_1.player_x = player_1.player_x - 1
                if player_1.player_y < 0:
                    player_1.player_y = 0
                    print("\n최대 활동범위는 1~100,1~100 입니다.")
                else:
                    print("\n왼쪽으로 이동")
                    monster(player_1)

            elif ans == "q":
                if player_1.point == 1 or player_1.point == 2 or player_1.point == 3 or player_1.point == 5 or player_1.point == 19 or \
                        player_1.point == 22 or player_1.point == 28 or player_1.point == 36:
                    village = 2
                    ans = ''
                    print("\n" * 1)

            elif ans == "e":
                print("\n" * 13)
                print("[장착보기 : q / 인벤토리 : w]")
                ans_1 = input(" : ")
                if ans_1 == 'q':
                    print("\n" * 9)
                    showinfo(player_1, 3)
                    print("\n돌아가려면 (enter)")
                    input(" : ")
                    print("\n" * 1)
                elif ans_1 == 'w':
                    inventory(player_1, 1)
                else:
                    print("\n" * 1)

            elif ans == "f":
                if warp_manager_count == 1:
                    inventory(player_1, 4)
                elif warp_manager_count == 2:
                    inventory(player_1, 3)
                else:
                    print("\n주변에 공간마법사갸 없습니다.")

            elif ans == "p":
                game_over()

            else:
                print("\n다시 입력해 주십시오.")

        if village == 2:
            if ans == "q":
                village = 1
                print("\n" * 1)

            elif ans == "w":
                inventory(player_1, 2)

            elif ans == "e":
                inventory(player_1, 6)

            elif ans == "r":
                inventory(player_1, 5)

            else:
                print("\n다시 입력해 주십시오.")


        if player_1.health <= 0:
            player_1.money = player_1.money - int(player_1.money // 2)
            player_1.exp = player_1.exp - int(player_1.exp // 6)
            print("\n" * 10)
            print("체력이 0보다 적어 에나 번화가로 귀환합니다.\n돌아가려면 (enter)")
            input(" : ")
            print("\n" * 1)
            player_1.health = player_1.result_health
            player_1.player_x = 87
            player_1.player_y = 52


if __name__ == "__main__":
    main()
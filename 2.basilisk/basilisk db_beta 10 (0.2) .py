# 아이템 조합
# 몬스터 출현
# 퀘스트 진행
#엔딩크레딧

'''
showshop(self
equip(self, use
inventory(inv
'''

#인벤토리 접근 안됨

from random import randint
import time
from pygame import mixer

print("\nthe print game project\n")


# 노래재생
'''
def sound():
    mixer.init()
    mixer.music.load('')
    mixer.music.play()
'''
    

# 스토리
def story():
    '''
    print("\n" * 39)
    print("비상이다. 비상")
    time.sleep(1.3)
    print("JL-B1 생명체가")
    time.sleep(2)
    print("도 망 쳤 다")
    time.sleep(2)
    print("생명체 이름은 바실리크스")
    time.sleep(2)
    print("숨결이 닿기도전에 관목은 말라죽고 풀은타버리며 돌은 부숴진다지..")
    time.sleep(5)
    print("상상의 동물을 되살리는 프로젝트를 하지 말아야 헸어..")
    time.sleep(5)
    print("아마 언론에 이 이야기가 들린다면 사회적 파장이 클걸세")
    time.sleep(5)
    print("그래서 그런데..")
    time.sleep(3)
    print("자네가 좀 잡아줄수 있겠나?")
    time.sleep(3)
    print("아마 멀리가진 못했을걸세")
    time.sleep(2)
    print("JL-B1 생명체만 잡아준다면 사례는 톡톡히 해주지")
    time.sleep(5)
    print("자네의 딸이 지금 많이 아프다지?")
    time.sleep(3)
    print("지금 자네의 딸이 아프다는것을 우리 연구소에서 알고있었네")
    time.sleep(5)
    print("마침 우연의 일치일지...")
    time.sleep(3)
    print("아마 우리 연구소에서 백신을 곧 만들수 있을거 같은데..")
    time.sleep(5)
    print("이 일만 잘 해결해준다면야")
    time.sleep(3)
    print("당신 딸에게 우선권을 주는거야 식은죽 먹기지")
    time.sleep(3)
    print("이정도 제안이면 해볼만 하지 않은가")
    time.sleep(3)
    print("어떻게 해 보겠는가?")
    time.sleep(2.5)
    '''
    
    no_count = 0
    while True:
        if no_count <= 4:
            str_ans = input("\ny / x : ")
            if str_ans == "y":
                '''
                print("\n그래 잘 선택했네")
                time.sleep(3)
                print("지금 바로 순간이동을 시켜주겠네")
                time.sleep(4)
                print("잘 부탁하네")
                time.sleep(4)
                print("위잉...\n")
                time.sleep(5)
                '''
                break
                main()
            elif str_ans == "x":
                if no_count < 20:
                    print("\n자네 딸이 죽어가고 있는데..")
                    time.sleep(2)
                    print("정말로 하지 않겠나?")
                    time.sleep(2)
                    print("현명한 선택을 하기 바라네..")
                    time.sleep(2.5)
                    no_count = no_count + 1
            else:
                print("\n안타깝지만")
                time.sleep(2)
                print("다른선택지는 없다네..")
                time.sleep(2)
                print("Y / X 둘중 하나를 고르게나")
                time.sleep(2)
                no_count = no_count + 1

        else:
            print("\n당신의 뜻을 알겠네")
            time.sleep(3)
            print("게임을 하기 싫은가보군..")
            game_over()
            
# 체크
def check (message, start, end):
    if message in list(map(str, range(start, end+1))):
        message = int(message)
        return message
    else:
        pass

# 플래이어 클래스
class player:
    def __init__(self, name, equipment, inven, health, money, defense, hunger, liv):
        self.name = name
        self.equipment = {"atk" : ["없음"], "def" : ["없음"]}
        self.inven = {"atk" : [], "def" : [], "re" : [], "food" : [], "drop" : [], "item" : []}
        self.health = health
        self.money = money
        self.defense = defense
        self.hunger = hunger
        self.liv = liv

    # 현재 상태 확인
    def showinfo(self):
        print("{0:=^25}".format("현재 상태"))
        if len(self.equipment['atk']) and len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][1].name} \n레벨 : {self.liv}")
        elif len(self.equipment['atk']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][0]} \n레벨 : {self.liv}")
        elif len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][0]}\n갑옷 : {self.equipment['def'][1].name} \n레벨 : {self.liv}")
        else:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][0]}\n갑옷 : {self.equipment['def'][0]} \n레벨 : {self.liv}")
            

    # 상한선
        if self.health > 100:
            self.health = 100

        if self.hunger > 10:
            self.hunger = 10
            

# 공격 아이템 클래스
class atk_item:
    def __init__(self, name, damage, cost, durability, liv, use):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.durability = durability
        self.liv = liv
        self.use = use

        
# 방어 아이템 클래스
class def_item:
    def __init__(self, name, defense, cost, durability, liv, use):
        self.name = name
        self.defense = defense
        self.cost = cost
        self.durability = durability
        self.liv = liv
        self.use = use


# 회복 아이템 클래스
class re_item:
    def __init__(self, name, recovery, cost, liv, use):
        self.name = name
        self.recovery = recovery
        self.cost = cost
        self.liv = liv
        self.use = use


# 음식 아이템 클래스
class food_item:
    def __init__(self, name, re_hunger, cost, liv, use):
        self.name = name
        self.re_hunger = re_hunger
        self.cost = cost
        self.liv = liv
        self.use = use


# 드롭 아이템 클래스
class drop_item:
    def __init__(self, name, explanation, use):
        self.name = name
        self.explanation = explanation
        self.use = use


# 일반 아이템 클래스
class nomal_item:
    def __init__(self, name, explanation, use):
        self.name = name
        self.explanation = explanation
        self.use = use

        
# 아이템 설정
item_001 = atk_item("기본검",2,0,20,1,"atk")

item_101 = atk_item("검",3,5,5,1,"atk")
item_102 = atk_item("철검",6,8,10,1,"atk")
item_103 = atk_item("예리한 대검",11,13,21,1,"atk")
item_104 = atk_item("반짝이는 도끼",16,18,26,5,"atk")
item_105 = atk_item("붉은 도끼",30,20,50,5,"atk")
item_106 = atk_item("칠흑의 검",45,25,55,15,"atk")
item_107 = atk_item("악마 도끼",50,30,60,15,"atk")
item_108 = atk_item("푸른불꽃검",60,36,65,20,"atk")
item_109 = atk_item("은빛하늘검",70,40,70,20,"atk")
item_110 = atk_item("금빛하늘검",80,55,75,25,"atk")
atk_item_list = [item_101, item_102, item_103, item_104, item_105, item_106, item_107, \
                  item_108, item_109, item_110]

item_201 = def_item("녹슨 철 갑옷",5,5,20,1,"def")
item_202 = def_item("철 갑옷",15,15,30,1,"def")
item_203 = def_item("적표범 갑옷",25,25,40,10,"def")
item_204 = def_item("칠흑 갑옷",35,35,50,10,"def")
item_205 = def_item("기사 갑옷",45,45,60,20,"def")
item_206 = def_item("청룡 갑주",55,60,1000,30,"def")
item_207 = def_item("백호 갑주",55,60,1000,30,"def")
item_208 = def_item("주작 갑주",55,60,1000,30,"def")
item_209 = def_item("현무 갑주",55,60,1000,30,"def")
item_210 = def_item("흑룡 갑주",70,80,1000,40,"def")
def_item_list = [item_201, item_202, item_203, item_204, item_205, item_206, item_207, \
                 item_208, item_209, item_210]

item_301 = re_item("초보자용 회복포션",6,2,1,"re")
item_302 = re_item("일반용 회복포션",16,5,1,"re")
item_303 = re_item("전문가용 회복포션",26,10,5,"re")
item_304 = re_item("고농축 회복포션",36,15,5,"re")
item_305 = re_item("강화된 고농축 회복포션",46,10,10,"re")
item_306 = re_item("천상의 회복포션",56,25,10,"re")
item_307 = re_item("강화된 천상의 회복포션",66,30,10,"re")
item_308 = re_item("생명 열매",76,35,10,"re")
item_309 = re_item("생명 수정",86,40,10,"re")
item_310 = re_item("축복의 손길",100,45,20,"re")
re_item_list = [item_301, item_302, item_303, item_304, item_305, item_306, item_307, \
                 item_308, item_309, item_310]

item_401 = food_item("스켈레톤의 뼈다귀",2,2,0,"food")
item_402 = food_item("마녀의 포화포션",4,4,0,"food")
item_403 = food_item("골렘의 식사",6,6,0,"food")
item_404 = food_item("드래곤의 날갯잎",8,8,0,"food")
food_item_list = [item_401, item_402, item_403, item_404]

item_501 = drop_item("코카트라스의 눈빛","'바실리스크'를 만나러 가자","drop")
item_502 = drop_item("불의 원소","불의 원소이다.","drop")
item_503 = drop_item("물의 원소","물의 원소이다.","drop")
item_504 = drop_item("흙의 원소","흙의 원소이다.","drop")
item_505 = drop_item("바람의 원소이다","바람의 원소이다.","drop")
item_506 = drop_item("글레이 골렘의 점토조각","무었을 만들수 있을까?","drop")
item_507 = drop_item("플래시 골렘의 살점","이건 먹는게 아니다.","drop")
item_508 = drop_item("아이언골렘의 철조각","제련을 하기에는..;;","drop")
item_509 = drop_item("스톤골렘의 자갈","사람에게 던지면 안된다.","drop")
item_510 = drop_item("골렘의 심장","골렘에게 심장이 있었던가?","drop")
item_511 = drop_item("타다남은 파이어 자이언트의 살점","타다 남은건 먹으면 몸에 안좋다.","drop")
item_512 = drop_item("딱딱한 프로스트 자이언트의 살점","먹다가는 이다 다 부숴질수도..","drop")
item_513 = drop_item("몸에 좋을거 같은 힐 자이언트의 살점","보기에 좋다고 다 먹기좋은건 아니다.","drop")
item_514 = drop_item("돌같은 스톤자이언트의 살점","돌이 사이사이에 밖혀있어 먹기 불편하다.","drop")
item_515 = drop_item("자이언트의 찟어진 옷조각","자이언트의 찢어진 옷조각이다","drop")
item_516 = drop_item("블랙 드래곤의 검은빛의 숨결","검은빛을 띄는 용의 숨결이다.","drop")
item_517 = drop_item("블루 드래곤의 푸른빛의 숨결","푸른빛을 띄는 용의 숨결이다.","drop")
item_518 = drop_item("실버 드래곤의 은빛 숨결","은색을 띄는 용의 숨결이다.","drop")
item_519 = drop_item("골드 드래곤의 금빛 숨결","금색을 띄는 용의 숨결이다.","drop")
item_520 = drop_item("레드 드래곤의 붉은빛 숨결","붉은빛을 띄는 용의 숨결이다.","drop")
item_521 = drop_item("드래곤의 날개짓","드래곤들의 날개짓이다.","drop")

item_601 = nomal_item("막대기","일반적인 막대기이다.","item")
item_602 = nomal_item("비밀의 열쇠","어디에 사용하는것일까?","item")
item_603 = nomal_item("보스의 위치 (X)","보스의 X위치를 알려준다.","item")
item_604 = nomal_item("보스의 위치 (Y)","보스의 Y위치를 알려준다.","item")


# 모든 아이템 설정
def print_item(item):
    if item.use == 'atk':
        print("{0:^25}{1:^10}{2:^10}{3:^10}{4:^10}".format(item.name,item.damage,item.cost \
                                                            ,item.durability, item.liv))
    elif item.use == 'def':
        print("{0:^25}{1:^10}{2:^10}{3:^10}{4:^10}".format(item.name,item.defense,item.cost \
                                        ,item.durability, item.liv))
    elif item.use == 're':
        print("{0:^25}{1:^10}{2:^10}{3:^10}".format(item.name,item.recovery,item.cost, item.liv))

    elif item.use == 'food':
        print("{0:^25}{1:^10}{2:^10}".format(item.name,item.re_hunger,item.cost))

    elif item.use == 'drop':
        print("{0:^25}{1:^10}".format(item.name,item.explanation))
        
    elif item.use == 'item':
        print("{0:^25}{1:^10}".format(item.name,item.explanation))

def qwe(item):
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

def qwer(item):
    if item.use == 'atk':
        return '무기'
    elif item.use == 'def':
        return '방어구'
    elif item.use == 're':
        return '포션'
    elif item.use == 'food':
        return '음식'
    elif item.use == 'drop':
        return '드롭'
    elif item.use == 'item':
        return '일반'
    
    
# 상점 구매
def buyshop(self, count, item):
    cou = input("몇개를 구매하시겠습니까? : ")
    cou = check(cou, 1, 100)
    if type(cou) == type(0):
        if self.money - item[count].cost * cou >= 0:
            if self.liv >= item[count].liv:
                self.money -= item[count].cost * cou
                use = qwe(item[count])
                for a in range(cou):
                    self.inven[use].append(item[count])
                print("\n{0} 아이템을 {1}개 구매하였습니다.".format(item[count].name, cou))
            else:
                print("레벨이 부족합니다.")
                print("필요레벨 : {0} / 현재레벨 : {1}".format(item[count].liv, self.liv))
        elif self.money - item[count].cost * cou < 0:
            print("\n돈이 부족합니다")
            print("필요금액 : {0} / 현재 가지고 있는 돈 : {1}".format(item[count].money, self.money))
        else:
            print("\n올바른 숫자를 입력하세요")
    else:
        print("\n올바른 숫자를 입력하세요")
    time.sleep(2)
    return self.money
        

# 상점 보기
def showshop(self):
    while True:
        print("\n" * 39)
        print("\n상점을 선택하세요 [무기 상점(q) /방어구 상점(w) /포션 상점(e) /음식 상점(r)]")
        shop_ch = input("(상점 선택에서 나가려면 엔터)\n:")
        count = 0
        
        # 무기상점
        if shop_ch == "q":
            while True:
                print("\n" * 39)
                print("\n{0:=^25}".format("무기 상점"))
                count = 0
                for i in atk_item_list:
                    count += 1
                    print(count, i.name)
                ch = input("\n무기 번호를 입력하세요\n(나가려면 enter)\n: ")
                if ch == "":
                    break
                ch = check(ch,1,10)
                if ch in range(1,11):
                    count = ch - 1
                    print("\n" * 39)
                    print("\n{0:=^25}".format(atk_item_list[count].name + " 정보"))
                    print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format(\
                                                                        '이름', atk_item_list[count].name, \
                                                                        '공격력', atk_item_list[count].damage,\
                                                                        '가격', atk_item_list[count].cost,\
                                                                        '내구도', atk_item_list[count].durability,\
                                                                        '제한레벨', atk_item_list[count].liv))

                    print("\n나의 돈 {0}\n나의 레벨 {1}\n".format(self.money, self.liv))
                    sel = input("구매하시겠습니까 (y / x) : ")
                    if sel == "y":
                        buyshop(self, count, atk_item_list)
                    elif sel == "x":
                        break
                    else:
                        print("올바른 문자를 입력하세요")
                        continue
                else:
                    print("올바른 숫자를 입력하세요")
                    time.sleep(1)
                    continue

        # 방어구 상점
        elif shop_ch == "w":
            while True:
                print("\n" * 39)
                print("\n{0:=^25}".format("방어구 상점"))
                count = 0
                for i in def_item_list:
                    count += 1
                    print(count, i.name)
                ch = input("\n방어구 번호를 입력하세요\n(나가려면 enter)\n: ")
                if ch == "":
                    break
                ch = check(ch,1,10)
                if ch in range(1,11):
                    count = ch - 1
                    print("\n" * 39)
                    print("\n{0:=^25}".format(def_item_list[count].name + " 정보"))
                    print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format(\
                                                                        '이름', def_item_list[count].name, \
                                                                        '방어력', def_item_list[count].defense,\
                                                                        '가격', def_item_list[count].cost,\
                                                                        '내구도', def_item_list[count].durability,\
                                                                        '제한레벨', def_item_list[count].liv))

                    print("\n나의 돈 {0}\n나의 레벨 {1}\n".format(self.money, self.liv))
                    sel = input("\n구매하시겠습니까 (y / x) : ")
                    if sel == "y":
                        buyshop(self, count, def_item_list)
                    elif sel == "x":
                        break
                    else:
                        print("올바른 문자를 입력하세요")
                        continue
                else:
                    print("올바른 숫자를 입력하세요")
                    time.sleep(1)
                    continue

        # 포션 상점
        elif shop_ch == "e":
            while True:
                print("\n" * 39)
                print("\n{0:=^25}".format("포션 상점"))
                count = 0
                for i in re_item_list:
                    count += 1
                    print(count, i.name)
                ch = input("\n포션 번호를 입력하세요\n(나가려면 enter)\n: ")
                if ch == "":
                    break
                ch = check(ch,1,10)
                if ch in range(1,11):
                    count = ch - 1
                    print("\n" * 39)
                    print("\n{0:=^25}".format(re_item_list[count].name + " 정보"))
                    print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}".format(\
                                                                        '이름', re_item_list[count].name, \
                                                                        '체력회복', re_item_list[count].recovery,\
                                                                        '가격', re_item_list[count].cost,\
                                                                        '제한레벨', re_item_list[count].liv))
                    
                    print("\n나의 돈 {0}\n나의 레벨 {1}\n".format(self.money, self.liv))
                    sel = input("구매하시겠습니까 (y / x) : ")
                    if sel == "y":
                        buyshop(self, count, re_item_list)
                    elif sel == "x":
                        break
                    else:
                        print("올바른 문자를 입력하세요")
                        continue
                else:
                    print("올바른 숫자를 입력하세요")
                    time.sleep(1)
                    continue

                
        # 음식 상점
        elif shop_ch == "r":
            while True:
                print("\n" * 39)
                print("\n{0:=^25}".format("음식 상점"))
                count = 0
                for i in food_item_list:
                    count += 1
                    print(count, i.name)
                ch = input("\n음식 번호를 입력하세요\n(나가려면 enter)\n: ")
                if ch == "":
                    break
                ch = check(ch,1,4)
                if ch in range(1,11):
                    count = ch - 1
                    print("\n" * 39)
                    print("\n{0:=^25}".format(food_item_list[count].name + " 정보"))
                    print("{0} : {1}\n{2} : {3}\n{4} : {5}".format('이름', food_item_list[count].name, \
                                                                        '포화', food_item_list[count].re_hunger,\
                                                                        '가격', food_item_list[count].cost))
                    
                    print("\n나의 돈 {0}\n나의 레벨 {1}\n".format(self.money, self.liv))
                    sel = input("구매하시겠습니까 (y / x) : ")
                    if sel == "y":
                        buyshop(self, count, food_item_list)
                    elif sel == "x":
                        continue
                    elif sel == "x":
                        break
                    else:
                        print("올바른 문자를 입력하세요")
                        continue
                else:
                    print("올바른 숫자를 입력하세요")
                    time.sleep(1)
                    continue

        else:
            break


# 무기 장착
def equip(self, use):
    sel = input("\n장착할 무기의 번호를 입력하세요 (무기를 빼려면 0)")
    print("\n" * 39)
    print("\n{0:=^25}".format(self.inven[use][sel].name + " 정보"))
    sel = check(sel,1,len(self.inven[use]))
    if type(sel) == type(0):
        sel -= 1
        print_item(self.inven[use][sel])
        sel_1 = input("\n{0} 무기를 장착하시겟습니까? (y / x) : ".format(self.inven[use][sel].name))
        if sel_1 == "y":
            pass
        elif sel_1 == "x":
            pass
        else:
            print("올바른 문자를 입력하세요")
    elif sel == "0":
        if len(self.equipment[use]) == 2:
            pass
        elif len(self.equipment[use]) == 1:
            pass
    else:
        print("올바른 숫자를 입력하세요")
    input()

        
# 몬스터 클래스
class monster:
    def __init__(self, name, health, damage, drop_money, liv):
        self.name = name
        self.health = health
        self.damage = damage
        self.drop_money = drop_money
        self.liv = liv

        
# 몬스터 설정
mon_0 = monster("바실리크스",2000,45,0,12000)
mon_1 = monster("코카트리스",1000,30,200,5000)

mon_0101 = monster("불의 정령 카샤",6,1,1,1)
mon_0102 = monster("물의 정령 운디네",6,1,1,1)
mon_0103 = monster("흙의 정령 노움",6,1,1,1)
mon_0104 = monster("바람의 정령 실프",6,1,1,1)

mon_0201 = monster("그램린",10,5,2,2)
mon_0202 = monster("스켈레톤",10,5,2,2)
mon_0203 = monster("스파이더",10,5,2,2)
mon_0204 = monster("좀비",10,5,2,2)

mon_0301 = monster("마녀",20,5,3,3)
mon_0302 = monster("서큐버스",25,3,3,3)
mon_0303 = monster("인큐버스",25,3,3,3)

mon_0401 = monster("드루이드",40,5,4,4)

mon_0501 = monster("메피스토펠레스",50,5,5,5)

mon_0601 = monster("몰록",55,5,6,6)

mon_0901 = monster("베리얼",100,7,9,9)
mon_0902 = monster("데모고곤",70,9,9,9)

mon_1001 = monster("글레이 골렘",150,10,10,10)
mon_1002 = monster("플레시 골렘",150,10,10,10)
mon_1003 = monster("아이언 골렘",150,10,10,10)
mon_1004 = monster("스톤 골렘",150,10,10,10)

mon_1301 = monster("미노타우르스",170,15,13,13)

mon_1501 = monster("파이어 자이언트",100,15,15,15)
mon_1502 = monster("프로스트 자이언트",100,15,15,15)
mon_1503 = monster("힐 자이언트",100,15,15,15)
mon_1504 = monster("스톤 자이언트",100,15,15,15)

mon_2001 = monster("블랙 드래곤",200,20,20,20)
mon_2002 = monster("블루 드래곤",200,20,20,20)
mon_2003 = monster("실버 드래곤",200,20,20,20)
mon_2004 = monster("골드 드래곤",200,20,20,20)
mon_2005 = monster("레드 드래곤",200,20,20,20)


# 몬스터 출현
def mon_hello():
    pass


# 인벤토리
def inventory(inv):
    sel = input("\n인벤토리를 선택하세요 [무기(q) /방어구(w) /포션(e) /음식(r) /드랍(t) /일반(y)] : ")
    if sel == "q":
        sel == "atk"
        inventory_print(sel)
    elif sel == "w":
        sel == "def"
        inventory_print(sel)
    elif sel == "e":
        sel == "re"
        inventory_print(sel)
    elif sel == "r":
        sel == "food"
        inventory_print(sel)
    elif sel == "t":
        sel == "drop"
        inventory_print(sel)
    elif sel == "y":
        sel == "item"
        inventory_print(sel)
    else:
        print("올바른 문자를 입력하세요")

def inventory_print(sel):
    name = qwer(sel)
    print("\n" * 39)
    print("{0:=^25}".format(name + " 인벤토리"))
    print("{0:^12}{1:^12}".format("Num","Name"))
    for i in range(len(inv[sel])):
        print("{0:^12}{1:^12}".format(i+1,inv[sel][i].name))
    print("{0:=^25}".format("인벤토리"))
    print("\n다 읽으셨다면 enter.")
    input()


# 보스 위치 셋팅
def boss_set():
    x = y = 0
    def boss(x):
        x = randint(5, 15)
        return x
    boss_x = boss(x)
    def boss(y):
        y = randint(5, 15)
        return y
    boss_y = boss(y)


# 게임 종료
def game_over():
    time.sleep(2)
    print("\n게임을 종료하시겠습니까?")
    while True:
        end_ans = input("y / x : ")
        if end_ans == "y":
            print("\n게임을 종료합니다")
            print("\n" * 39)
            print("gmae over")
        if end_ans == "x":
            print("\n게임을 계속 진행합니다.")
            main()


# 메인
def main():
    
    #sound()
    
    in_name = input("플레이어 이름을 입력하시오. = ")
    if in_name == "":
        print()
        sub_main()
    p_1 = player(in_name, [], [], 100, 2000, 0, 10, 150)
    self = p_1
    self.equipment["atk"].append(item_001)
    player_x = 10
    player_y = 10
    move_data = 0
    p_liv = 0
    plag = 0
    
    time.sleep(1.3)
    print("정상적으로 로그인 되었습니다.")
    time.sleep(0.7)
    print("정보 불러오는 중...")
    time.sleep(0.7)
    print("환영합니다." + in_name +"님")
    time.sleep(1)
    story()
    
    while True:
        
        # 최대 활동 범위
        move_max = 0
        if player_x > 20:
            player_x = 20
            move_max = move_max + 1
        if player_x < 1:
            player_x = 1
            move_max = move_max + 1

        if player_y > 20:
            player_y = 20
            move_max = move_max + 1
        if player_y < 1:
            player_y = 1
            move_max = move_max + 1

        if move_max != 0:
            print("\n최대 활동범위는 1~20,1~20 입니다.")
            time.sleep(3)
        
        print("\n" * 39)
        p_1.showinfo()
        print("\n나의 위치 :" + str(player_x) + "," + str(player_y))
        print("==============")
        
        # 명령 확인
        if plag == 0:
            print("\n도움을 원한다면 'help' 입력")
            
        ans = input("\n무엇을 하시겠습니까? : ")
        if ans == "w":
            player_x = player_x + 1
            print("앞으로 이동")
        elif ans == "s":
            player_x = player_x - 1
            print("뒤로 이동")
        elif ans == "d":
            player_y = player_y + 1
            print("오른쪽으로 이동")
        elif ans == "a":
            player_y = player_y - 1
            print("왼쪽으로 이동")
        elif ans == "e":
            inventory(self.inven)
        elif ans == "f":
            showshop(self)
        elif ans == "help":
            print("\n게임설명\n방향 조작은 w,a,s,d 입니다.\n인벤토리는 e 키로 열 수 있습니다.\
                  \nf 를 누르면 상점에 진입합니다.\n마을('10,10')에서는 퀘스트를 얻을 수 있습니다.\
                  \n한국어를 웬만하면 누르지 마세요.\n(버그의 원인이 됩니다.)\
                  \n최종보스를 물리치면 승리합니다.\n다 읽으셨다면 enter.")
            next_ = input()
        elif ans == "stop":
            game_over()
        else:
            print("다시 입력해 주십시오")
            
        # 허기 시스템
        if ans == "w" or "a" or "s" or "d":
            move_data = move_data + 1
            
        if move_data == 2:
            move_data = 0
            p_1.hunger = p_1.hunger - 1

        mon_hello()

        time.sleep(1)

        plag = plag + 1
    

if __name__ == "__main__":
    main()

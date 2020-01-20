from random import choice
from random import randint
from pygame import mixer
import time
import pickle

print("\nthe print game project\n")

#인벤 허기 오류

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
    
    print("비상이다. 비상")
    time.sleep(1.3)
    print("JL-B1 생명체가")
    time.sleep(2)
    print("도 망 쳤 다")
    time.sleep(2)
    print("생명체 이름은 바실리스크")
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
            str_ans = input("\ny / n : ")
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
            elif str_ans == "n":
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
                print("y / n 둘중 하나를 고르게나")
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
        return message

# 플래이어 클래스
class player:
    def __init__(self, name, equipment, inven, health, money, damage, defense, hunger, liv, exp, cri, ak, m_health):
        self.name = name
        self.equipment = {"atk" : ["없음"], "def" : ["없음"]}
        self.inven = {"atk" : [], "def" : [], "re" : [], "food" : [], "drop" : [], "item" : []}
        self.health = health
        self.damage = damage
        self.money = money
        self.defense = defense
        self.hunger = hunger
        self.liv = liv
        self.exp = exp
        self.cri = cri
        self.ak = ak
        self.m_health = m_health

    # 현재 상태 확인
    def showinfo(self):
        print("{0:=^25}".format("현재 상태"))
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
                    \n무기 : {self.equipment['atk'][1].name}\n무기 내구도 :{self.equipment['atk'][1].durability} \
                    \n갑옷 : {self.equipment['def'][1].name}\n갑옷 내구도 : {self.equipment['def'][1].durability} \
                    \n레벨 : {self.liv}")
        elif len(self.equipment['atk']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage}\n방어력 : {self.defense} \
                    \n무기 : {self.equipment['atk'][1].name}\n무기 내구도 :{self.equipment['atk'][1].durability} \
                    \n갑옷 : {self.equipment['def'][0]}\n갑옷 내구도 : {self.equipment['def'][0]} \
                    \n레벨 : {self.liv}")
        elif len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage}\n방어력 : {self.defense}\
                    \n무기 : {self.equipment['atk'][0]}\n무기 내구도 :{self.equipment['atk'][0]} \
                    \n갑옷 : {self.equipment['def'][1].name}\n갑옷 내구도 : {self.equipment['def'][1].durability} \
                    \n레벨 : {self.liv}")
        else:
            print(f"이름 : {self.name}\n체력 : {self.health}\n공격력 : {self.damage} \n방어력 : {self.defense} \
                    \n무기 : {self.equipment['atk'][0]}\n무기 내구도 :{self.equipment['atk'][0]} \
                    n갑옷 : {self.equipment['def'][0].name}\n갑옷 내구도 : {self.equipment['def'][0]} \
                    \n레벨 : {self.liv}")
            

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
    def __init__(self, name, defense, cost, durability, liv, use, tree):
        self.name = name
        self.defense = defense
        self.cost = cost
        self.durability = durability
        self.liv = liv
        self.use = use
        self.tree = tree


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

# 조합 아이템 클래스
class creaft_item:
    def __init__(self, name, damage, durability, explanation, liv, use):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.explanation = explanation
        self.liv = liv
        self.use = use
# 조합 아이템 클래스
        
# 아이템 설정
item_001 = atk_item("기본검",2,0,20,1,"atk")

item_101 = atk_item("검",3,5,5,1,"atk")
item_102 = atk_item("철검",6,8,10,1,"atk")
item_103 = atk_item("예리한 대검",11,13,21,1,"atk")
item_104 = atk_item("반짝이는 도끼",16,18,26,5,"atk")
item_105 = atk_item("악마 도끼",30,20,50,5,"atk")
item_106 = atk_item("칠흑의 검",45,25,55,15,"atk")
item_107 = atk_item("붉은 도끼",50,30,60,15,"atk")
item_108 = atk_item("푸른불꽃검",60,36,65,20,"atk")
item_109 = atk_item("은빛하늘검",70,40,70,20,"atk")
item_110 = atk_item("금빛하늘검",80,46,75,25,"atk")
item_111 = atk_item("흑빛하늘검",75,0,75,25,"atk")
# 흑빛하늘검(86) = 은빛하늘검(40) + 금빛하늘검(46)
atk_item_list = [item_101, item_102, item_103, item_104, item_105, item_106, item_107, \
                  item_108, item_109, item_110]

item_201 = def_item("녹슨 철 갑옷",5,5,20,1,"def","일반")
item_202 = def_item("철 갑옷",15,15,30,1,"def","일반")
item_203 = def_item("적표범 갑옷",25,25,40,10,"def","일반")
item_204 = def_item("칠흑 갑옷",35,35,50,10,"def","일반")
item_205 = def_item("백호 갑주",50,45,60,20,"def","사신수")
item_206 = def_item("주작 갑주",50,60,1000,30,"def","사신수")
item_207 = def_item("청룡 갑주",50,60,1000,30,"def","사신수")
item_208 = def_item("현무 갑주",50,60,1000,30,"def","사신수")
item_209 = def_item("흑룡 갑주",60,60,1000,30,"def","사흉수")
item_210 = def_item("기사 갑주",70,80,1000,40,"def","사신수")
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
item_505 = drop_item("바람의 원소","바람의 원소이다.","drop")
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

item_601 = creaft_item("백호의 도끼",120,10000,"백호의 혼이 깃든 첫번째 사신수 무기이다.",40,"creaft")
# 은빛하늘검(40) + 흙의 원소 x 10 + 딱딱한 프로스트 자이언트의 살점 x 5 + 실버 드래곤의 은빛 숨결 x 3
item_602 = creaft_item("주작의 삽",125,10000,"주작의 혼이 깃든 두번째 사신수 무기이다.",40,"creaft")
# 붉은도끼(30) + 불의 원소 x 10 + 타다남은 파이어 자이언트의 살점 x 5 + 레드 드래곤의 붉은빛 숨결 x 3
item_603 = creaft_item("청룡의 검",130,10000,"청룡의 혼이 깃든 세번째 사신수 무기이다.",40,"creaft")
# 푸른불꽃검(36) + 바람의 원소 x 10 + 몸에 좋을거 같은 힐 자이언트의 살점 x 5 + 골드 드래곤의 금빛 숨결 x 3
item_604 = creaft_item("현무의 낫",135,10000,"현무의 혼이 깃든 네번째 사신수 무기이다.",40,"creaft")
# 금빛하늘검(46) + 물의 원소 x 10 + 돌같은 스톤자이언트의 살점 x 5 + 블루 드래곤의 푸른빛의 숨결 x 3
item_605 = creaft_item("전설의 엑스칼리버",10000,10000,"아서왕 전설에 등장하는 전설의 무기이다.",60,"creaft")
# 사신수 무기 모두
item_606 = creaft_item("혼돈의 낫",150,10000,"혼돈의 혼이 깃든 첫번째 사흉수 무기이다.",40,"creaft")
# 칠흑의 검(25) + 글레이 골렘의 점토조각 x 8 + 골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓
item_607 = creaft_item("궁기의 파초선",155,10000,"궁기의 혼이 깃든 두번째 사흉수 무기이다.",40,"creaft")
# 칠흑의 검(25) + 플래시 골렘의 살점 x 8 + 골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓
item_608 = creaft_item("도월의 북",160,10000,"도월의 혼이 깃든 세번째 사흉수 무기이다.",40,"creaft")
# 악마도끼(30) + 아이언골렘의 철조각 x 8 + 골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓
item_609 = creaft_item("도철의 망치",165,10000,"도철의 혼이 깃든 네번째 사흉수 무기이다.",40,"creaft")
# 악마도끼(30) + 스톤골렘의 자갈 x 8 + 골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓
item_610 = creaft_item("흑룡의 검",400,10000,"사신수를 대적하는 흑룡의 혼이 깃든 사흉수 무기이다.",50,"creaft")
# 흑빛하늘검 + 사흉수 무기 모두

item_701 = nomal_item("막대기","일반적인 막대기이다.","item")
item_702 = nomal_item("비밀의 열쇠","어디에 사용하는것일까?","item")
item_703 = nomal_item("보스의 위치 (X)","보스의 X위치를 알려준다.","item")
item_704 = nomal_item("보스의 위치 (Y)","보스의 Y위치를 알려준다.","item")
item_705 = nomal_item("사신수 조합법","원하는 사신수의 조합법을 알려준다.","item")
item_706 = nomal_item("백호의 도끼 조합법","은빛하늘검(40) + 흙의 원소 x 10 + \
                        딱딱한 프로스트 자이언트의 살점 x 5 + 실버 드래곤의 은빛 숨결 x 3","item")
item_707 = nomal_item("주작의 삽 조합법","붉은도끼(30) + 불의 원소 x 10 + \
                        타다남은 파이어 자이언트의 살점 x 5 + 레드 드래곤의 붉은빛 숨결 x 3","item")
item_708 = nomal_item("청룡의 검 조합법","푸른불꽃검(36) + 바람의 원소 x 10 + \
                        몸에 좋을거 같은 힐 자이언트의 살점 x 5 + 골드 드래곤의 금빛 숨결 x 3","item")
item_709 = nomal_item("현무의 낫 조합법","금빛하늘검(46) + 물의 원소 x 10 + \
                        돌같은 스톤자이언트의 살점 x 5 + 블루 드래곤의 푸른빛의 숨결 x 3","item")
item_710 = nomal_item("혼돈의 낫 조합법","칠흑의 검(25) + 글레이 골렘의 점토조각 x 8 + \
                        골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓","item")
item_711 = nomal_item("궁기의 파초선 조합법","칠흑의 검(25) + 플래시 골렘의 살점 x 8 + \
                        골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓","item")
item_712 = nomal_item("도월의 북 조합법","악마도끼(30) + 아이언골렘의 철조각 x 8 + \
                        골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓","item")
item_713 = nomal_item("도철의 망치 조합법","악마도끼(30) + 스톤골렘의 자갈 x 8 + \
                        골렘의 심장 x 5 + 자이언트의 찟어진 옷조각 x 3 + 드래곤의 날개짓","item")

# 아이템 설정



shop_item_list = {'atk' : atk_item_list, 'def' : def_item_list, 're' : re_item_list, 'food' : food_item_list}

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

def print_item_Ver2(item):
    if item.use == 'atk':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format(\
                                                    '이름', item.name, \
                                                    '공격력', item.damage,\
                                                    '가격', item.cost,\
                                                    '내구도', item.durability,\
                                                    '제한레벨', item.liv))
    elif item.use == 'def':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format(\
                                                    '이름', item.name, \
                                                    '방어력', item.defense,\
                                                    '가격', item.cost,\
                                                    '내구도', item.durability,\
                                                    '제한레벨', item.liv))
    elif item.use == 're':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}".format(\
                                                    '이름', item.name, \
                                                    '체력회복', item.recovery,\
                                                    '가격', item.cost,\
                                                    '제한레벨', item.liv))
    elif item.use == 'food':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}".format(\
                                                    '이름', item.name, \
                                                    '포화', item.re_hunger,\
                                                    '가격', item.cost))
    elif item.use == 'drop':
        print("{0} : {1}\n{2} : {3}".format(\
                                                    '이름', item.name, \
                                                    '설명', item.explanation))
    elif item.use == 'item':
        print("{0} : {1}\n{2} : {3}".format(\
                                                    '이름', item.name, \
                                                    '설명', item.explanation))

class monster:
    def __init__(self, name, health, damage, drop_money, liv):
        self.name = name
        self.health = health
        self.damage = damage
        self.drop_money = drop_money
        self.liv = liv

#몬스터 프린트
def print_mon(mon, health):
    print("\n\n{0:=^25}".format("Lv." + str(mon.liv) + "_" + mon.name))
    print("{0} : {1}\n{2} : {3}\n{4} : {5}".format(\
                                                    '이름', mon.name, \
                                                    '체력', health,\
                                                    '공격력', mon.damage))
    
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

def qwer(word):
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
    
def qwert(word):
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

def p_qwerty(pl, word):
    if word == 'atk':
        return pl.damage
    elif word == 'def':
        return pl.defense
    elif word == 're':
        return pl.health
    elif word == 'food':
        return pl.hunger

def e_qwerty(pl,word,num):
    if word == 'atk':
        return pl.equipment[word][num].damage
    elif word == 'def':
        return pl.equipment[word][num].defense

def i_qwerty(item, word):
    if word == 'atk':
        return item.damage
    elif word == 'def':
        return item.defense

def qw(me, word, num):
    if num == 0:
        if word == 're':
            return me.health
        elif word == 'food':
            return me.hunger
    elif num == 1:
        if word == 're':
            return me.recovery
        elif word == 'food':
            return me.re_hunger
    
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
                    for a in range(cou):
                        self.inven[use].append(item[count])
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
            
    return self.money , self.inven , self.equipment
        

# 상점 보기
def showshop(self):
    while True:
        print("\n상점을 선택하세요 [무기 상점(q) /방어구 상점(w) /포션 상점(e) /음식 상점(r)]")
        shop_ch = input("(상점 선택에서 나가려면 엔터)\n:")
        if shop_ch == "":
            break
        elif shop_ch == "q" or shop_ch == "w" or shop_ch == "e" or shop_ch == "r" :
            while True:
                use = qwert(shop_ch)
                use_k = qwer(use)
                print("\n{0:=^25}".format(use_k + " 상점"))
                count = 0
                for i in shop_item_list[use]:
                    count += 1
                    print(count, i.name)
                ch = str(input(f"\n{use_k} 번호를 입력하세요\n(나가려면 enter)\n: "))
                ch = check(ch, 1, len(shop_item_list[use]))
                if ch in range(1, len(shop_item_list[use]) + 1):
                    ch -= 1
                    while True:
                        print("\n{0:=^25}".format(shop_item_list[use][ch].name + " 정보"))
                        print_item_Ver2(shop_item_list[use][ch])
                        print("\n나의 돈 {0}\n나의 레벨 {1}\n".format(self.money, self.liv))
                        sel = input("구매하시겠습니까 (y / n) : ")
                        if sel == "y":
                            buyshop(self, ch, shop_item_list[use])
                            break
                        elif sel == "n":
                            break
                        else:
                            print("올바른 문자를 입력하세요")
                            continue
                elif ch == "":
                    break
                else:
                    print("올바른 숫자를 입력하세요")
        else:
            print("올바른 문자를 입력하세요")
            continue

#아이템별 스탯변화
def reset_info(pl,item,u_d, use):
    if use == 'atk':
        if u_d == 'd':
            pl.damage -= item.damage
        elif u_d == 'u':
            pl.damage += item.damage
        return pl.damage
    elif use == 'def':
        if u_d == 'd':
            pl.defense -= item.defense
        elif u_d == 'u':
            pl.defense += item.defense
        return pl.defense
        


# 무기 장착
def equip(pl, use, item, sel):
    while True:
        print_item_Ver2(item[sel])
        sel_1 = input("\n{0} 무기를 장착하시겟습니까? (y / n) : ".format(item[sel].name))
        if sel_1 == "y":
            if len(pl.equipment[use]) == 2:
                pl.inven[use].append(pl.equipment[use][1])
                reset_info(pl, pl.equipment[use][1], 'd', use)
                del pl.equipment[use][1]
                pl.equipment[use].append(item[sel])
                del item[sel]
                reset_info(pl, pl.equipment[use][1], 'u', use)
                print("\n{0} 무기를 장착하였습니다: ".format(pl.equipment[use][1].name))
                input("나가려면(enter)")
                return pl
                break
            elif len(pl.equipment[use]) == 1:
                pl.equipment[use].append(item[sel])
                reset_info(pl, pl.equipment[use][1], 'u', use)
                del item[sel]
                print("\n{0} 무기를 장착하였습니다: ".format(pl.equipment[use][1].name))
                input("나가려면(enter)")
                return pl
                break
        elif sel_1 == "n":
                break
        else:
            print("올바른 문자를 입력하세요")
# 무기 장착

# 포션이나 음식 사용
def use_r_f(self, use, item, sel):
    while True:
        print_item_Ver2(item[sel])
        sel_1 = input("\n{0}을(를) 사용하시겟습니까? (y / n) : ".format(item[sel].name))
        if sel_1 == "y":
            tem = qw(item[sel],use,1)
            if use == 're': self.health += tem
            elif use == 'food': self.hunger += tem
            del item[sel]
            return self
        elif sel_1 == "n":
                break
        else:
            print("올바른 문자를 입력하세요")
# 포션이나 음식 사용
        
# 몬스터 클래스
class monster:
    def __init__(self, name, health, damage, drop_money, drop_item,liv):
        self.name = name
        self.health = health
        self.damage = damage
        self.drop_money = drop_money
        self.drop_item = drop_item
        self.liv = liv

        
# 몬스터 설정
mon_0 = monster("바실리크스",4000,45,0,[item_501],12000)#501 100%
mon_1 = monster("코카트리스",2000,30,200,[],5000)

mon_0101 = monster("불의 정령 카샤",6,1,1,[item_502],1)#502  각각 60%씩
mon_0102 = monster("물의 정령 운디네",6,1,1,[item_503],1)#503
mon_0103 = monster("흙의 정령 노움",6,1,1,[item_504],1)#504
mon_0104 = monster("바람의 정령 실프",6,1,1,[item_505],1)#505
#1레벨 몬스터 리스트
mon_01 = [mon_0101, mon_0102, mon_0103, mon_0104]

mon_0201 = monster("그램린",10,5,2,[],2)
mon_0202 = monster("스켈레톤",10,5,2,[],2)
mon_0203 = monster("스파이더",10,5,2,[],2)
mon_0204 = monster("좀비",10,5,2,[],2)
#2레벨 몬스터 리스트
mon_02 = [mon_0201, mon_0202, mon_0203, mon_0204]

mon_0301 = monster("마녀",20,5,3,[],3)
mon_0302 = monster("서큐버스",25,3,3,[],3)
mon_0303 = monster("인큐버스",25,3,3,[],3)
#3레벨 몬스터 리스트
mon_03 = [mon_0301, mon_0302, mon_0303]

mon_0401 = monster("드루이드",40,5,4,[],4)
#4레벨 몬스터 리스트
mon_04 = [mon_0401]

mon_0501 = monster("메피스토펠레스",50,5,5,[],5)
#5레벨 몬스터 리스트
mon_05 = [mon_0501]

mon_0601 = monster("몰록",55,5,6,[],6)
#6레벨 몬스터 리스트
mon_06 = [mon_0601]

mon_0901 = monster("베리얼",100,7,9,[],9)
mon_0902 = monster("데모고곤",70,9,9,[],9)
#9레벨 몬스터 리스트
mon_09 = [mon_0901, mon_0902]

mon_1001 = monster("글레이 골렘",150,10,10,[item_506, item_510],10)#506 , 510
mon_1002 = monster("플레시 골렘",150,10,10,[item_507, item_510],10)#507 , 510
mon_1003 = monster("아이언 골렘",150,10,10,[item_508, item_510],10)#508 , 510
mon_1004 = monster("스톤 골렘",150,10,10,[item_509, item_510],10)#509 , 510
#10레벨 몬스터 리스트
mon_10 = [mon_1001, mon_1002, mon_1003, mon_1004]

mon_1301 = monster("미노타우르스",170,15,13,[],13)
#13레벨 몬스터 리스트
mon_13 = [mon_1301]

mon_1501 = monster("파이어 자이언트",100,15,15,[item_511, item_515],15)#511 , 515
mon_1502 = monster("프로스트 자이언트",100,15,15,[item_512, item_515],15)#512 , 515
mon_1503 = monster("힐 자이언트",100,15,15,[item_513, item_515],15)#513 , 515
mon_1504 = monster("스톤 자이언트",100,15,15,[item_514, item_515],15)#514 , 515
#15레벨 몬스터 리스트
mon_15 = [mon_1501, mon_1502,  mon_1503, mon_1504]

mon_2001 = monster("블랙 드래곤",200,20,20,[item_516, item_521],20)#516 , 521
mon_2002 = monster("블루 드래곤",200,20,20,[item_517, item_521],20)#517 , 521
mon_2003 = monster("실버 드래곤",200,20,20,[item_518, item_521],20)#518 , 521
mon_2004 = monster("골드 드래곤",200,20,20,[item_519, item_521],20)#519 , 521
mon_2005 = monster("레드 드래곤",200,20,20,[item_520, item_521],20)#520 , 521
mon_20 = [mon_2001, mon_2002, mon_2003, mon_2004, mon_2005]
#20레벨 몬스터 리스트

mon_dict = {1 : mon_01, 2 : mon_02, 3 : mon_03, 4 : mon_04, 5 : mon_05, 6 : mon_06, 9 : mon_09, 10 : mon_10, 13 : mon_13, 15 : mon_15, 20 : mon_20}

#장비 파괴
def break_item(pl, use):
    if len(pl.equipment[use]) == 2:
        if pl.equipment[use][1].durability <= 0:
            del  pl.equipment[use][1]
            return pl.equipment
        else:
            pl.equipment[use][1].durability -= 1
            return pl.equipment[use]
    else:
        pass


#공격
def attack(pl, mon, m_health,p_m):
    if p_m == "pl":
        if len(pl.equipment['atk']) == 2:
            m_health -= pl.damage
            break_item(pl, 'atk')
            print("{1}에게 {0} 데미지를 입혔갔습니다\n".format(pl.damage, mon.name))
            return m_health
        elif len(pl.equipment['atk']) == 1:
            m_health -= 0
            break_item(pl, 'atk')
            print("효과가 없다\n")
            return m_health
    elif p_m == "mon":
        if len(pl.equipment['def']) == 2:
            damage = mon.damage - int(mon.damage * pl.defense / 100)
            pl.health -= damage
            break_item(pl, 'def')
            print("{0} 데미지를 받았습니다\n".format(damage))
            return pl.health
        elif len(pl.equipment['def'])== 1:
            pl.health -= mon.damage
            break_item(pl, 'def')
            print("{0}의 데미지를 받았습니다\n".format(int(mon.damage)))
            return pl.health
        
#몬스터 고르기
def who_mon(pl):
    while True:
        per = choice(list(mon_dict.keys()))
        if per <= pl.liv:
            mon = choice(list(mon_dict[per]))
            return mon
            break
        else:
            continue

#플레이어 도망
def pl_run(mon, mul):
    if mon.liv * mul >= 100:
        per_3 = choice('n' * 100)
    elif mon.liv * mul <100:
        ot = 100 - mon.liv
        per_3 = choice('n' * mul * mon.liv + 'r' * ot)
    return per_3



# 몬스터 출현
def mon_hello(lat, self):
    if lat == 'w' or lat == 'a' or lat == 's' or lat == 'd':
        #몬스터 등장
        while True:
            per = choice("m"*30 + "n"*70)
            if per == "m":
                mon = who_mon(self)
                print("\n야생의 {0}이(가) 나타났다\n".format(mon.name))
                turn = 1
                r_count = 0
                m_health = mon.health
                #전투
                while True:
                    print("\n\n{0:_^30}\n".format("Round" + str(turn)))
                    print_mon(mon, m_health)
                    print('\n{0:=^25}\n'.format("Vs"))
                    self.m_showinfo()
                    if r_count == 0:
                        sel = input("\n공격(q) 아이템(w) 도망(e)\n:")
                        #공격
                        if sel == 'q':
                            m_health = attack(self, mon, m_health,"pl")
                            if m_health <= 0:
                                self.exp += mon.liv
                                print("{0}가 죽었습니다".format(mon.name))
                                print("\n돈 {0}를 얻었습니다".format(mon.drop_money))
                                self.money += mon.drop_money
                                if len(mon.drop_item) == 0:
                                    pass
                                else:
                                    for i in mon.drop_item:
                                        per_2 = choice('y' * 60 + 'n' *40)
                                        if per_2 == 'y':
                                            print(f"{i.name}을 얻었습니다")
                                            self.inven["drop"].append(i)
                                        elif per_2 == 'n':
                                            pass
                                    print("\n\n")
                                return self
                            attack(self, mon, m_health, "mon")
                            if self.health <= 0:
                                break
                            turn += 1
                        #아이템
                        elif sel == 'w':
                            inventory(self)
                        #도망
                        elif sel == 'e':
                            r_count = 1
                            per_3 = pl_run(mon, 5)
                            if per_3 == 'r':
                                print("도망에 성공하였다")
                                input("(enter)")
                                break
                            elif per_3 == 'n':
                                r_count = 5
                                pass
                        else:
                            print("올바른 문자를 입력하세요")
                    #도망 X
                    else:
                        sel = input("\n공격(q) 아이템(w)\n:")
                        #공격
                        if sel == 'q':
                            attack(self, m_health,mon, "pl")
                            if m_health <= 0:
                                print("{0}가 죽었습니다".format(mon.name))
                                print("돈 {0}를 얻었습니다".format(mon.drop_money))
                                self.money += mon.drop_money
                                if len(mon.drop_item) == 0:
                                    pass
                                else:
                                    for i in mon.drop_item:
                                        per_2 = choice('y' * 60 + 'n' *40)
                                        if per_2 == 'y':
                                            self.inven.append(i)
                                        elif per_2 == 'n':
                                            pass
                                return self
                            attack(self, mon, m_health,"mon")
                            if self.health <= 0:
                                break
                            turn += 1
                        #아이템
                        elif sel == 'w':
                            inventory(self)
                        r_count -= 1 
            elif per == "n":
                break
            break
    

# 인벤토리
def inventory(self):
    while True:
        sel = input("\n인벤토리를 선택하세요 [무기(q) /방어구(w) /포션(e) /음식(r) /드랍(t) /일반(y)]")
        print("나가려면 (enter)")
        if sel == "q" or sel == "w" or sel == "e" or sel == "r" or sel == "t" or sel == "y":
            sel = qwert(sel)
            inventory_print(self , sel)
        elif sel == "":
            break
        else:
            print("올바른 문자를 입력하세요")

#인벤토리 출력
def inventory_print(self ,sel):
    while True:
        sel_k = qwer(sel)
        print("{0:=^25}".format(str(sel_k) + " 인벤토리"))
        print("{0:^12}{1:^12}".format("Num","Name"))
        if len(self.inven[sel]) == 0:
            print("{0:^12}{1:^12}".format("없음","없음"))
        for i in range(len(self.inven[sel])):
            print("{0:^12}{1:^12}".format(i+1,self.inven[sel][i].name))
        print("{0:=^25}".format("인벤토리"))
        sel_1 = input("아이템의 정보를 보고 싶다면 해당 아이템의 번호를 입력하세요\n나가려면 (enter)\n:")
        sel_1 = check(sel_1, 1, len(self.inven[sel]))
        if type(sel_1) == type(0):
            print("\n{0:=^25}".format("Num" + str(sel_1) + " 정보" ))
            sel_1 -= 1
            if sel == 'atk' or sel == 'def':
                equip(self, sel, self.inven[sel], sel_1)
            elif sel == 're' or sel == 'food':
                use_r_f(self, sel, self.inven[sel], sel_1)
        elif sel_1 == "":
            break
        else:
            print("올바른 숫자를 입력하세요")

# 보스 위치 셋팅
def boss_set():
    x = randint(5, 15)
    y = randint(5, 15)
    return x, y

def pl_s(pl):
    while True:
        print('===========스텟===========')
        print("1 체력 추가\
                    \n2 공격력 추가\
                    \n3 치명타")
        num = input(":")
        if num == '1':
            print('=========체력 추가=========')
            print("체력 추가당 체력이 5씩 증가합니다")
            sel = input("y / n : " )
            if sel == 'y':
                print("체력이 추가됩니다")
            elif sel == 'n':
                continue
        elif num == '2':
            print('=========공격력 추가=========')
            print("공격력 추가당 공격력 5씩 증가합니다")
            sel = input("y / n : " )
            if sel == 'y':
                print("공격력 추가됩니다")
            elif sel == 'n':
                continue
        elif num == '3':
            print('=========치명타 추가=========')
            print("치명타 추가당 확률이 1%씩 증가합니다")
            sel = input("y / n : " )
            if sel == 'y':
                print("치명타가 추가됩니다")
            elif sel == 'n':
                continue
        else:
            print("올바른 문자를 입력하세요")




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
    
    #sound()
    
    in_name = input("플레이어 이름을 입력하시오. = ")
    if in_name == "":
        print()
    p_1 = player(in_name, [], [], 100, 10, 0, 0, 10, 1, 0,0,0,100)
    self = p_1
    self.equipment["atk"].append(item_001)
    reset_info(self, item_001, 'u', 'atk')
    player_x = 10
    player_y = 10
    move_data = 0
    p_liv = 0
    plag = 0
    h_count = a_count = c_count = 0
    
    print("정상적으로 로그인 되었습니다.")
    print("정보 불러오는 중...")
    print("환영합니다." + in_name +"님")
    
    while True:
        #체력/허기 최대치
        num_1 = 100
        if self.health > self.m_health:
            self.health = self.m_health
        if self.hunger > 10:
            self.hunger = 10
        
        p_1.showinfo()
        print("\n나의 위치 :" + str(player_x) + "," + str(player_y))
        print("==============")
        
        # 명령 확인
        if plag == 0:
            print("\n도움을 원한다면 'help' 입력")
            
        ans = input("\n무엇을 하시겠습니까? : ")
        if ans == "w":
            if self.hunger == 0:
                print("허기를 채워주세요")
                self.health -= 5
                if self.health < 1:
                    self.health = 1
                continue
            player_x += 1
            print("앞으로 이동")
        elif ans == "s":
            if self.hunger == 0:
                print("허기를 채워주세요")
                self.health -= 5
                if self.health < 1:
                    self.health = 1
                continue
            player_x -= 1
            print("뒤로 이동")
        elif ans == "d":
            if self.hunger == 0:
                print("허기를 채워주세요")
                self.health -= 5
                if self.health < 1:
                    self.health = 1
                continue
            player_y += 1
            print("오른쪽으로 이동")
        elif ans == "a":
            if self.hunger == 0:
                print("허기를 채워주세요")
                self.health -= 5
                if self.health < 1:
                    self.health = 1
                continue
            player_y -= 1
            print("왼쪽으로 이동")
        elif ans == "e":
            inventory(self)
            continue
        elif ans == "f":
            showshop(self)
            continue
            '''
        elif ans == "help":
            print("\n게임설명\n방향 조작은 w,a,s,d 입니다.\n인벤토리는 e 키로 열 수 있습니다.\
                  \nf 를 누르면 상점에 진입합니다.\n마을('10,10')에서는 퀘스트를 얻을 수 있습니다.\
                  \n한국어를 웬만하면 누르지 마세요.\n(버그의 원인이 됩니다.)\
                  \n최종보스를 물리치면 승리합니다.\n다 읽으셨다면 enter.")
            input()
            '''
        elif ans == "stop":
            game_over()
            break
        else:
            print("다시 입력해 주십시오")
            continue
        
        # 최대 활동 범위
        move_max = 0
        if player_x > 20:
            player_x = 20
            move_max += 1
        if player_x < 1:
            player_x = 1
            move_max += 1

        if player_y > 20:
            player_y = 20
            move_max += 1
        if player_y < 1:
            player_y = 1
            move_max += 1

        if move_max != 0:
            print("\n최대 활동범위는 1~20,1~20 입니다.")
            continue
        
            
        # 허기 시스템
        if ans == "w" or ans == "a" or ans == "s" or ans == "d":
            move_data += 1
        if move_data == 2:
            move_data = 0
            p_1.hunger -= 1

        # 마을에 몬스터 없음
        if player_x == 10 and player_y == 10:
            pass
        else:
            mon_hello(ans, self)
            if self.exp >= self.liv:
                self.liv += 1
                if self.liv <= 60:
                    while True:
                        print('===========스텟===========')
                        print("1 체력 추가 {0}/20\
                                    \n2 공격력 추가 {1}/20\
                                    \n3 치명타 {2}/20".format(h_count,a_count,c_count))
                        num = input(":")
                        if num == '1':
                            if h_count == 20:
                              continue
                            print('=========체력 추가=========')
                            print("체력 추가당 체력이 5씩 증가합니다")
                            sel = input("y / n : " )
                            if sel == 'y':
                                self.m_health += 5
                                print("체력이 추가됩니다")
                                h_count += 1
                                break
                            elif sel == 'n':
                                continue
                        elif num == '2':
                            if a_count == 20:
                              continue
                            print('=========공격력 추가=========')
                            print("공격력 추가당 공격력 5%씩 증가합니다")
                            sel = input("y / n : " )
                            if sel == 'y':
                                self.ak += 5
                                print("공격력 추가됩니다")
                                a_count += 1
                            elif sel == 'n':
                                continue
                        elif num == '3':
                            if c_count == 20:
                              continue
                            print('=========치명타 추가=========')
                            print("치명타 추가당 확률이 1%씩 증가합니다")
                            sel = input("y / n : " )
                            if sel == 'y':
                                self.cri += 1
                                print("치명타가 추가됩니다")
                                c_count += 1
                            elif sel == 'n':
                                continue
                        else:
                            print("올바른 문자를 입력하세요")
                else:
                    pass
        
        #플레이어 사망시
        if self.health <= 0:
            self.money -= int(self.money / 10) 
            print("마을로 리스폰 됩니다")
            self.health = 100
            player_x = 10
            player_y = 10
        plag += 1
    

if __name__ == "__main__":
    
    main()

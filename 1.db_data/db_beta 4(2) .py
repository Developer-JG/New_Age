from random import randint
import time

print("the print game project\n")

# 플래이어 클래스
class player:
    def __init__(self, name, health, defense, hunger, weapon):
        self.name = name
        self.health = health
        self.defense = defense
        self.hunger = hunger
        self.weapon = weapon

    # 현재 상태 확인
    def showinfo(self):
        print("====현재 상태====")
        print(f"이름 : {self.name}\n체력 : {self.health} \
                \n방어력 : {self.defense} \n배고픔 : {self.hunger} \
                \n무기 : {self.weapon}")

    # 배고픔
    def hunger():
        self.hunger = self.hunger - 1

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
item_01 = atk_item("검",3,20,5,1,"atk")
item_02 = atk_item("철검",6,23,10,1,"atk")
item_03 = atk_item("예리한 대검",11,25,21,1,"atk")
item_04 = atk_item("반짝이는 도끼",16,28,26,5,"atk")
item_05 = atk_item("붉은 도끼",30,30,50,5,"atk")
item_06 = atk_item("칠흑의 검 ",45,33,55,15,"atk")
item_07 = atk_item("악마 도끼",50,35,60,15,"atk")
item_08 = atk_item("푸른불꽃검",60,50,65,20,"atk")
item_09 = atk_item("은빛하늘검",70,50,70,20,"atk")
item_10 = atk_item("금빛하늘검",80,50,75,25,"atk")

item_11 = def_item("녹슨 철 갑옷 세트",5,5,20,1,"def")
item_12 = def_item("철 갑옷",15,15,30,1,"def")
item_13 = def_item("적표범 갑옷",25,25,40,10,"def")
item_14 = def_item("칠흑 갑옷",35,35,50,10,"def")
item_15 = def_item("기사 갑옷",59,45,70,20,"def")

item_16 = re_item("초보자용 회복포션",6,2,1,"re")
item_17 = re_item("일반용 회복포션",16,5,1,"re")
item_18 = re_item("전문가용 회복포션",26,10,5,"re")
item_19 = re_item("고농축 회복포션",36,15,5,"re")
item_20 = re_item("천상의 회복포션",46,20,10,"re")
item_21 = re_item("축복의 손길",100,45,20,"re")

item_22 = drop_item("코카트라스의 눈빛","'바실리스크'를 만나러 가자","drop")
item_24 = drop_item("불의 원소","불의 원소이다.","drop")
item_25 = drop_item("물의 원소","물의 원소이다.","drop")
item_26 = drop_item("흙의 원소","흙의 원소이다.","drop")
item_27 = drop_item("바람의 원소이다","바람의 원소이다.","drop")
item_28 = drop_item("글레이 골렘의 점토조각","무었을 만들수 있을까?","drop")
item_29 = drop_item("플래시 골렘의 살점","이건 먹는게 아니다.","drop")
item_30 = drop_item("아이언골렘의 철조각","제련을 하기에는..;;","drop")
item_31 = drop_item("스톤골렘의 자갈","사람에게 던지면 안된다.","drop")
item_32 = drop_item("골렘의 심장","골렘에게 심장이 있었던가?","drop")
item_33 = drop_item("타다남은 파이어 자이언트의 살점","타다 남은건 먹으면 몸에 안좋다.","drop")
item_34 = drop_item("딱딱한 프로스트 자이언트의 살점","먹다가는 이다 다 부숴질수도..","drop")
item_35 = drop_item("몸에 좋을거 같은 힐 자이언트의 살점","보기에 좋다고 다 먹기좋은건 아니다.","drop")
item_36 = drop_item("돌같은 스톤자이언트의 살점","돌이 사이사이에 밖혀있어 먹기 불편하다.","drop")
item_37 = drop_item("자이언트의 찟어진 옷조각","자이언트의 찢어진 옷조각이다","drop")
item_38 = drop_item("블랙 드래곤의 검은빛의 숨결","검은빛을 띄는 용의 숨결이다.","drop")
item_39 = drop_item("블루 드래곤의 푸른빛의 숨결","푸른빛을 띄는 용의 숨결이다.","drop")
item_40 = drop_item("실버 드래곤의 은빛 숨결","은색을 띄는 용의 숨결이다.","drop")
item_41 = drop_item("골드 드래곤의 금빛 숨결","금색을 띄는 용의 숨결이다.","drop")
item_42 = drop_item("레드 드래곤의 붉은빛 숨결","붉은빛을 띄는 용의 숨결이다.","drop")
item_43 = drop_item("드래곤의 날개짓","드래곤들의 날개짓이다.","drop")

item_44 = nomal_item("막대기","일반적인 막대기이다.","item")
item_45 = nomal_item("비밀의 열쇠","어디에 사용하는것일까?","item")
item_46 = nomal_item("보스의 위치 (X)","보스의 X위치를 알려준다.","item")
item_47 = nomal_item("보스의 위치 (Y)","보스의 Y위치를 알려준다.","item")


# 모든 아이템 설정
def print_item(use, item):
    if item.use == "atk":
        print("{0}{1}{2}{3}{4}".format(item.name,item.damage,item.cost \
                                        ,item.durability, item.liv))
    elif item.use == 'def':
        print("{0}{1}{2}{3}{4}".format(item.name,item.defense,item.cost \
                                        ,item.durability, item.liv))
    elif item.use == 're':
        print("{0}{1}{2}{3}".format(item.name,item.recovery,item.cost, item.liv))

    elif item.use == 'drop':
        print("{0}{1}".format(item.name,item.explanation))
        
    elif item.use == 'item':
        print("{0}{1}".format(item.name,item.explanation))

        
# 몬스터 클래스
class monster:
    def __init__(self, name, health, damage, drop_money, drop_item, liv):
        self.name = name
        self.health = health
        self.damage = damage
        self.drop_money = drop_money
        self.drop_item = drop_item
        self.liv = liv

        
# 몬스터 설정
mon_1 = monster("바실리크스",2000,45,12000)
mon_2 = monster("코카트리스",1000,30,5000)
mon_3 = monster("불의 정령 카샤",6,1,1)
mon_4 = monster("물의 정령 운디네",6,1,1)
mon_5 = monster("흙의 정령 노움",6,1,1)
mon_6 = monster("바람의 정령 실프",6,1,10)
mon_7 = monster("글레이 골렘",150,10,10)
mon_8 = monster("플레시 골렘",150,10,10)
mon_9 = monster("아이언 골렘",150,10,10)
mon_10 = monster("스톤 골렘",150,10,10)
mon_11 = monster("파이어 자이언트",100,15,15)
mon_12 = monster("프로스트 자이언트",100,15,15)
mon_13 = monster("힐 자이언트",100,15,15)
mon_14 = monster("스톤 자이언트",100,15,15)
mon_15 = monster("블랙 드래곤",200,20,20)
mon_16 = monster("블루 드래곤",200,20,20)
mon_17 = monster("실버 드래곤",200,20,20)
mon_18 = monster("골드 드래곤",200,20,20)
mon_19 = monster("레드 드래곤",200,20,20)
mon_20 = monster("미노타우르스",170,15,13)
mon_21 = monster("메피스토펠레스",50,5,5)
mon_22 = monster("몰록",55,5,6)
mon_23 = monster("베리얼",100,7,9)
mon_24 = monster("서큐버스",25,3,3)
mon_25 = monster("인큐버스",25,3,3)
mon_26 = monster("데모고곤",70,9,9)
mon_27 = monster("위치",20,5,3)
mon_28 = monster("드루이드",40,5,4)
mon_29 = monster("그램린",10,5,2)
mon_30 = monster("스켈레톤",10,5,2)
mon_31 = monster("스파이더",10,5,2)
mon_32 = monster("좀비",10,5,2)


# 상점
def shop():
    pass


# 인벤토리 설정
inv = [item_10,item_15,item_21,item_21,item_21,item_21,item_23]


# 인벤토리
def invintory(inv):
    print("{0:=^25}".format("인벤토리"))
    print("{0:^12}{1:^12}".format("Num","Name"))
    for i in range(len(inv)):
        print("{0:^12}{1:^12}".format(i+1,inv[i].name))
    print("{0:=^25}".format("인벤토리"))
    print("\n다 읽으셨다면 enter.")


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


# 메인
def main():
    in_name = ""
    while in_name == "":
        in_name = input("플레이어 이름을 입력하시오. = ")
        p_1 = player(in_name, 100, 0, 10, 0,)
        self = p_1
        player_x = 10
        player_y = 10
        move_data = 0
        player_money = 0
        player_liv = 1
        player_liv_now = 0
        time.sleep(1.3)
        print("정상적으로 로그인 되었습니다.")
        time.sleep(0.7)
        print("정보 불러오는 중...")
        time.sleep(0.7)
        print("환영합니다." + in_name +"님\n")
        time.sleep(1)
        
        while True:
            print("\n" * 39)
            p_1.showinfo()
            print("\n나의 위치 :" + str(player_x) + "," + str(player_y))
            print("==============")
            # 명령 확인
            print("\n도움을 원한다면 'help' 입력")
            ans = input("무엇을 하시겠습니까? : ")
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
                invintory(inv)
                next_ = input()
            elif ans == "s":
                shop()
            elif ans == "help":
                print("\n게임설명\n방향 조작은 w,a,s,d 입니다.\n인벤토리는 e 키로 열 수 있습니다.\
                      \ns 를 누르면 상점에 진입합니다.\n마을('10,10')에서는 퀘스트를 얻을 수 있습니다.\
                      \n한국어를 웬만하면 누르지 마세요.\n(버그의 원인이 됩니다.)\
                      \n최종보스를 물리치면 승리합니다.\n다 읽으셨다면 enter.")
                next_ = input()
            elif ans == "stop":
                break
            else:

            # 허기 시스템
            if ans == "w" or "a" or "s" or "d":
                move_data = move_data + 1
                
            if move_data == 2:
                move_data = 0
                self.hunger = self.hunger - 1
                
                
                #몬스터 확률
                monster = randint(1,100)
                mon_liv = 0
                '''
                if boss_x == player_x and boss_y == player_y:
                    mon_liv = 50
                elif 1 <= monster <=45 :
                    print ("아무일도 일어나지 않았다.")
                elif 46 <= monster <=70:
                    pass
                elif 71 <= monster <=85:
                    pass
                elif 86 <= monster <=90:
                    pass
                elif 90 <= monster <=97:
                    pass
                else:
                    pass

                #몬스터 출현
                
                if  :
                    print("일반 몬스터를 만났다.")
                elif :
                    print("livel 중급 몬스터를 만났다.")
                elif m:
                    print("livel 보스 몬스터를 만났다.")
                '''

                #몬스터 대화
                if mon_liv >= 1:
                    print("싸운다 / 도망간다 / 아이템")
                    act = ("어떻게 할까? = ")
                    act_plag = 0
                    while act_plag != 0:
                        if act == "싸운다":
                            act_plag = 1
                        if act == "도망간다":
                            act_plag = 1
                        if act == "아이템":
                            act_plag = 1

            time.sleep(1)


if __name__ == "__main__":
    main()



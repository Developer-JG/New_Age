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
        pass

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


# 아이템 클래스
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

item_22 = nomal_item("막대기","일반적인 막대기이다.","item")
item_23 = nomal_item("비밀의 열쇠","어디에 사용하는것일까?","item")


# 모든 아이템 설정
def print_item(use, item):
    if item.use == "atk":
        print("{0}{1}{2}{3}".format(item.name,item.damage,item.cost \
                                    ,item.durability, item.liv))
    elif item.use == 'def':
        print("{0}{1}{2}{3}".format(item.name,item.defense,item.cost \
                                    ,item.durability, item.liv))
    elif item.use == 're':
        print("{0}{1}".format(item.name,item.recovery,item.cost, item.liv))
    elif item.use == 'item':
        print("{0}{1}".format(item.name,item.explanation))

        
# 몬스터 클래스
class monster:
    def __init__(self, name, health, damage, weapon, explanation):
        self.name = name
        self.health = health
        self.damage = damage
        self.weapon = weapon
        self.explanation = explanation

        
# 몬스터 설정
mon_1 = monster("바실리크스",2000,45,"바실리스크의 숨결", \
                "그 숨결이 닿기도 전에 그 숨결만으로도 관목이 말라 죽고 풀은 타버리며 돌은 부서진다.")
mon_2 = monster("코카트리스",1000,30,"코카트리스의 눈빛","먼저보면 살고 늦게 보면 죽는다.")
mon_3 = monster("불의 정령 카샤",6,1,"꼬마 불꽃","불을 관장하는 정령이다.")
mon_4 = monster("물의 정령 운디네",6,1,"빙결","물을 관장하는 정령이다.")
mon_5 = monster("흙의 정령 노움",6,1,"암석의 힘","흙을 관장하는 정령이다.")
mon_6 = monster("바람의 정령 실프",6,1,"토네이도","바람을 관장하는 정령이다.")


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
        p_1 = player(in_name, 100, 0, 10, "{0}".format(item_01))
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
        time.sleep(0.5)
        while True:
            print("\n" * 39)
            p_1.showinfo()
            print("\n나의 위치 :" + str(player_x) + "," + str(player_y))
            print("==============")
            # 명령 확인
            move = 0
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
                move = 1
            elif ans == "help":
                print("\n게임설명\n방향 조작은 w,a,s,d 입니다.\n인벤토리는 e 키로 열 수 있습니다.\
                      \n한국어를 웬만하면 누르지 마세요.\n(버그의 원인이 됩니다.)\n최종보스를 물리치면 승리합니다.\n다 읽으셨다면 enter.")
                next_ = input()
                move = 1
            else:
                move = 1

            # 허기 시스템
            if ans == "w" or "a" or "s" or "d":
                player.hunger()
                
            if move_data == 2:
                move_data = 0
                
                
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

            time.sleep(1.5)


if __name__ == "__main__":
    main()



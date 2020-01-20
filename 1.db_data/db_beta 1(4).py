from random import randint
import time

print("the print game project\n")

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

# 플래이어 클래스
class player:
    def __init__(self, name, health, defense, hunger, weapon):
        self.name = name
        self.health = health
        self.defense = defense
        self.hunger = hunger
        self.weapon = ["hend"]

# 공격 아이템 클래스
class item:
    def __init__(self, name, damage, durability, explanation, use):
        self.name = name
        self.damage = damage
        self.durability = durability
        self.explanation = explanation
        self.use = use

# 공격 아이템 설정

item_a_01 = item("단검",3,20,"기본적인 단검이다.","atk")
item_a_02 = item("단검",3,20,"기본적인 단검이다.","atk")
item_a_03 = item("단검",3,20,"기본적인 단검이다.","atk")


# 모든 아이템 설정
def print_item(use, item):
    if item.use == "atk":
        print("{0}{1}{2}{3}".format(item.name,item.damage,\
                                    item.durability, item.explanation))
    elif item.use == 'def':
        print("{0}{1}{2}{3}".format(item.name,item.Defense,\
                                    item.durability, item.explanation))
    elif item.use == 'item':
        print("{0}{1}".format(item.name,item.explanation))
        
# 몬스터 클래스

# 인벤토리 설정
inv = [item_a_01,item_a_02,item_a_03]

# 인벤토리
'''
def invintory(inv):
    print("{0:=^25}".format("인벤토리"))
    for i in range(len(inv)):
        print("Num : {0}    Name : {1}".format(i+1,inv[i].name))
    for i in range(9-len(inv)):
        print("{0:-^25}".format("비어있음")) 
    print("{0:=^25}".format("인벤토리"))
'''
def invintory(inv):
    print("{0:=^25}".format("인벤토리"))
    print("{0:^12}{1:^12}".format("Num","Name"))
    for i in range(len(inv)):
        print("{0:^12}{1:^12}".format(i+1,inv[i].name))
    print("{0:=^25}".format("인벤토리"))

# 메인
def main():
    in_name = input("플레이어 이름을 입력하시오. = ", )
    p_1 = player(in_name, 100, 0, 100, [])
    player_x = 10
    player_y = 10
    time.sleep(1.3)
    print("정상적으로 로그인 되었습니다.")
    time.sleep(0.7)
    print("환영합니다." + in_name +"님\n")
    time.sleep(0.5)
    print("\n" * 10)
    print("도움을 원한다면 'help' 입력\n")
    while True:
        move = 0
        ans = input(":")
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
        elif ans == "help":
            help_()
        else:
            move = 1

        if move == 0:
            print("\n나의 위치 :" + str(player_x) + "," + str(player_y))
            
        


if __name__ == "__main__":
    main()



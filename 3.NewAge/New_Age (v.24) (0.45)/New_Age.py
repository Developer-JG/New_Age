from random import choice
from random import randint
import time

import Player
import Atk_item
import Def_item
import Re_item
import Food_item
import Nomal_item


print("\nthe New_Age (basilisk) game project\n")


# 스토리
def story():
    print("오래전 이땅은 인간의 것이 아니였다.")
    time.sleep(1.8)
    print("개척자였던 에나가 괴물을 물리치자 평화가 찾아왔고,")
    time.sleep(2.5)
    print("이땅에 마지막으로 국가가 세워졌다.")
    time.sleep(1.8)
    print("에나의 후손들은 황제가 되어 에나의 힘을 계승해 나갔지만")
    time.sleep(2.5)
    print("피가 연해질수록 괴물들을 막아내기 어려워졌다.")
    time.sleep(2.3)
    print("고대의 에나는 전설의 무기가 잘못 하용될경우를 대비하여 봉인하였지만")
    time.sleep(3)
    print("사람들은 전설의 무기를 되찾아 평화를 되찾아 평화를 되찾고자 한다.")
    time.sleep(4)
    print("\nNew_Age (새로운_시대)\n")


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
        print('\n' * 2)
        player_1 = Player(player_name, 1, [], [], 100, 0, 0, 0, 20, 0, 0)

        player_x = 20
        player_y = 20

        player_liv = 0

        plag = 0

    time.sleep(1.3)
    print("정상적으로 로그인 되었습니다.")
    time.sleep(0.7)
    print("정보 불러오는 중...")
    time.sleep(0.7)
    print("환영합니다." + player_name + "님")
    time.sleep(1)

    while True:

        print("\n" * 38)

        # 마을 버프
        if player_1.point == 1:
            player_1.health = player_1.health + 50
            player_1.hunger = 20
            
        # 체력,허기 최대치
        if player_1.health > 100:
            player_1.health = 100
        if player_1.hunger > 20:
            player_1.hunger = 20

        # 맵 크기
        if player_x > 20:
            player_x = 20
            print("")
        if player_x < 0:

        if player_y > 20:

        if player_y > 20:

        player_1.showinfo()

        print("\n나의 위치 :" + str(player_x) + "," + str(player_y))
        print("==============")

        if plag == 0:
            print("\n도움을 원한다면 'help' 입력")

        ans = input("\n무엇을 하시겠습니까? : ")

        if ans == "w" or ans == "s" or ans == "d" or ans == "a":
            if player_1.hunger == 0:
                print("허기를 채워주세요")
                player_1.health -= 5


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

        time.sleep(5)

if __name__ == "__main__":
    main()

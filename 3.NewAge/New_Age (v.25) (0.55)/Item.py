class Atk_item:
    def __init__(self, name, damage, cost, reinforce, liv,  use):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.reinforce = reinforce
        self.liv = liv
        self.use = use

class Def_item:
    def __init__(self, name, defense, cost, reinforce, liv, use):
        self.name = name
        self.defense = defense
        self.cost = cost
        self.reinforce = reinforce
        self.liv = liv
        self.use = use

class Re_item:
    def __init__(self, name, recovery, cost, liv, count, use):
        self.name = name
        self.recovery = recovery
        self.cost = cost
        self.liv = liv
        self.count = count
        self.use = use

class Food_item:
    def __init__(self, name, re_hunger, cost, count, use):
        self.name = name
        self.re_hunger = re_hunger
        self.cost = cost
        self.count = count
        self.use = use

class nomal_item:
    def __init__(self, name, count, use):
        self.name = name
        self.count = count
        self.use = use

shop_item_list = {'atk': atk_item_list, 'def': def_item_list, 'food': food_item_list}

def print_item_1(item):
    if item.use == 'atk':
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
        print("{0:^25}".format(item.name)


def print_item_2(item):
    if item.use == 'atk':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format( \
            '이름', item.name, \
            '공격력', item.damage, \
            '가격', item.cost, \
            '강화', item.durability, \
            '제한레벨', item.liv))
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
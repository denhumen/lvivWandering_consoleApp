"""
Module with
classes for the game
"""
import random
import os

class Item():
    """
    Item class
    """
    def __init__(self, name) -> None:
        self.name = name

class Support(Item):
    """
    Support item class
    """
    item_type = 'support'

    def __init__(self, name, health) -> None:
        super().__init__(name)
        self.health = health
    
    def use(self, player):
        """
        Use item method
        """
        player.treat_player(self.health)

class Gun(Item):
    """
    Gun item class
    """
    item_type = 'gun'

    def __init__(self, name, damage) -> None:
        super().__init__(name)
        self.damage = damage

class Inventory():
    """
    Inventory class
    """

    __items = {}

    def __init__(self, inventory = []) -> None:
        self.items_list = inventory

    def add_item(self, item):
        """
        Add item method
        """
        self.items_list.append(item)
        self.__items[item.name] = item

    def get_items_dict(self):
        """
        Get items dict mathod
        """
        return self.__items

    def delete_item(self, item):
        """
        Delete item method
        """
        del self.__items[item.name]
        self.items_list.remove(item)

class Player():
    """
    Player class
    """
    inventory = Inventory()
    happy_end = False

    health = 100

    def __init__(self, key = False) -> None:
        self.key = key

    def treat_player(self, plus_health):
        """
        Treat player method
        """
        heal = int(self.health) + int(plus_health)
        # if heal > 100:
        #     heal = 100
        self.health = heal

    def print_player_info(self):
        """
        Print player info method
        """
        print(f"\nІнформація про персонажа:")
        print(f"ХП: {self.health}\n")

    def inventory_add(self, item):
        """
        Inventory add method
        """
        self.inventory.add_item(item)

    def print_inventory(self):
        """
        Print inventory method
        """
        print("\nТвій інвентар:")
        if self.inventory.items_list != []:
            for idx, item in enumerate(self.inventory.items_list):
                print(f"{idx+1}. {item.name}")
        else:
            print(f"Тут пусто. Ти можеш це виправити!")
        print()

class Person():
    """
    Person class
    """

    file_with_phrases = ""

    def __init__(self, type_man, type_woman) -> None:
        data = self.__get_rand_name()
        self.name, self.sex = data
        if data[1] == "Чоловік":
            self.type = type_man
        else:
            self.type = type_woman

    def set_key_true(self):
        """
        Set key true method
        """
        self.key = True

    def __get_rand_name(self):
        """
        Get random name method
        """
        with open('files/people.csv', 'r', encoding='utf-8') as names_file:
            data = names_file.read().splitlines()
        name_idx = random.randrange(0, len(data))
        return data[name_idx].split()

    def talk(self):
        """
        Talk method
        """
        try:
            with open(os.path.join('files', self.file_with_phrases), 'r', encoding="utf-8") as phrases_file:
                data = phrases_file.read().splitlines()
            ph_idx = random.randrange(0, len(data))
            return data[ph_idx]
        except FileNotFoundError:
            return 'Зараз зайнятий, не можу говорити'

    def print_person_info(self):
        """
        Print person info method
        """
        print(f"Людина: {self.name} | [{self.type}]")

class Policeman(Person):
    """
    Policeman class
    """
    file_with_phrases = "police.csv"

    def __init__(self, type_man = "поліцейський", type_woman = "поліцейська") -> None:
        super().__init__(type_man, type_woman)

    def talk(self):
        return super().talk()

class Fireman(Person):
    """
    Fireman class
    """
    file_with_phrases = "fire.csv"

    def __init__(self, type_man = "пожежник", type_woman = "пожежниця") -> None:
        super().__init__(type_man, type_woman)

    def talk(self):
        return super().talk()

class Military(Person):
    """
    Military class
    """
    file_with_phrases = "military.csv"

    def __init__(self, type_man = "військовий", type_woman = "військова") -> None:
        super().__init__(type_man, type_woman)

    def talk(self):
        return super().talk()

class Crazy(Person):
    """
    Crazy class
    """
    file_with_phrases = "crazy.csv"

    def __init__(self, type_man = "божевільний", type_woman = "божевільна") -> None:
        super().__init__(type_man, type_woman)

    def talk(self):
        return super().talk()

class Bandit(Person):
    """
    Bandit class
    """
    def __init__(self, type_man = "злодій", type_woman = "злодійка") -> None:
        super().__init__(type_man, type_woman)

    def talk(self):
        """
        Talk method
        """
        return "Ключ я тобі не віддам!"

class Street():
    """
    Street class
    """

    __is_visited = False
    __is_searched = False

    def __init__(self, name, ways, info) -> None:
        self.name = name
        self.ways = ways
        self.info = info

    def search_street(self):
        """
        Search street method
        """
        if self.__is_searched:
            return None
        else:
            with open('files/things.csv', 'r', encoding='utf-8') as things_file:
                data = things_file.read().splitlines()
            th_idx = random.randrange(0, len(data))
            self.__is_searched = True
            return data[th_idx]

    def print_street_info(self):
        """
        Print street info method
        """
        print(self.name)
        print('-----------------------')
        print(self.info)
        if self.name == "Стрийська":
            print("Ти бачиш перед собою великий сейф, ключ до якого тобі ще потрібно знайти")

    def set_visited(self):
        """
        Set visited
        """
        self.__is_visited = True

    def is_street_visited(self):
        """
        is street visited method
        """
        if self.__is_visited:
            return True
        return False

class LvivMap():
    """
    Map class
    """
    street_info = {
        "Стрийська": "Одна з семи магістральних вулиць Львова. Серед львівських вулиць Стрийська — одна з найдовших (близько 7,5 км)",
        "Івана Чмоли": "Вулиця у Сихівському районі міста Львова, у місцевості Новий Львів. З'єднує вулицю Стрийську з вулицею Козельницькою",
        "Козельницька": "Вулиця у Сихівському районі міста Львова, у місцевості Персенківка.",
        "Івана Франка": "Одна з перших серед вулиць Львова за кількістю пам'яток архітектури. На вулиці розташовано 52 кам'яниці, що є пам'ятками архітектури місцевого значення та містобудування міста Львова.",
        "Дмитра Вітовського": "Вулиця у Галицькому районі Львова.",
        "Княгині Ольги": "Вулиця у Франківському районі Львова. Починається від перехрестя вулиць Горбачевського і Сахарова",
        "Миколи Коперника": "Одна із центральних вулиць Львова, знаходиться у Галицькому районі міста",
        "Степана Бандери": "Вулиця на межі Галицького та Франківського районів міста Львова. Названа на честь радикального ідеолого українського націоналізму",
        "Героїва УПА": "Одна з магістральних вулиць у Франківському районі Львова, в історичній місцевості Новий Світ",
        "Кульпарківська": "Одна з магістральних вулиць Львова. Початок бере від колишньої Городоцької рогатки при вулиці Городоцькій",
        "Володимира Великого": "Одна з магістральних вулиць у Львові, знаходиться у Франківському районі",
        "Академіка А. Сахарова": "Вулиця у Франківському районі Львова, у місцевості Вулька, фактично є продовженням вулиці Коперника"
    }

    street_dict = {
        "Стрийська": ["Володимира Великого", "Івана Чмоли", "Академіка А. Сахарова"],
        "Івана Чмоли": ["Козельницька", "Стрийська"],
        "Козельницька": ["Івана Чмоли", "Івана Франка"],
        "Івана Франка": ["Козельницька", "Дмитра Вітовського"],
        "Дмитра Вітовського": ["Івана Франка", "Княгині Ольги"],
        "Княгині Ольги": ["Академіка А. Сахарова", "Миколи Коперника", "Володимира Великого", "Дмитра Вітовського"],
        "Миколи Коперника": ["Княгині Ольги", "Степана Бандери"],
        "Степана Бандери": ["Миколи Коперника", "Героїва УПА"],
        "Героїва УПА": ["Степана Бандери", "Кульпарківська"],
        "Кульпарківська": ["Героїва УПА", "Володимира Великого"],
        "Володимира Великого": ["Кульпарківська", "Княгині Ольги", "Стрийська"],
        "Академіка А. Сахарова": ["Стрийська", "Княгині Ольги"]
    }

    __current_street = None
    __privious_street = None
    __streets_object_dict = {}
    __street_people = {}

    def __init__(self, start_street="Стрийська") -> None:
        self.rooms = []
        for street, ways in self.street_dict.items():
            if street == start_street:
                self.__current_street = Street(street, ways, self.street_info[street])
            self.__streets_object_dict[street] = Street(street, ways, self.street_info[street])
            self.rooms.append(Street(street, ways, self.street_info[street]))
            rand_num = random.randrange(0, 31)
            if 0 <= rand_num < 6:
                self.__street_people[street] = Policeman()
            elif 6 <= rand_num < 15:
                self.__street_people[street] = Military()
            elif 15 <= rand_num < 21:
                self.__street_people[street] = Fireman()
            elif 21 <= rand_num < 26:
                self.__street_people[street] = Crazy()
            else:
                self.__street_people[street] = Bandit()

    def get_current_street(self):
        """
        Get current street method
        """
        return self.__current_street

    def print_current_person_speech(self):
        """
        Print current person speech method
        """
        current_person = self.__street_people[self.__current_street.name]
        print(f"\n{current_person.name}: {current_person.talk()}\n")

    def get_current_person(self):
        """
        Get current person method
        """
        return self.__street_people[self.__current_street.name]

    def print_current_person_info(self):
        """
        Print current person info
        """
        self.__street_people[self.__current_street.name].print_person_info()

    def change_current_street(self, new_street):
        """
        Change current street method
        """
        self.__streets_object_dict[self.__current_street.name].set_visited()
        self.__privious_street = self.__streets_object_dict[self.__current_street.name]
        self.__current_street = self.__streets_object_dict[new_street]

    def print_current_street_info(self):
        """
        Print current street info method
        """
        self.__current_street.print_street_info()

    def print_available_moves(self):
        """
        Print available moves method
        """
        print("Доступні маршрути:")
        for way in self.__current_street.ways:
            visited = ''
            if self.__streets_object_dict[way].is_street_visited():
                visited = "[відвідана]"

            if self.__privious_street != None and way == self.__privious_street.name:
                visited = "[тільки що відвідана]"
            print(f"вул. {way} {visited}")

"""
Main game
file
"""
from classes import LvivMap, Player, Gun, Support
import random

if __name__ == "__main__":
    is_game_ended = False
    lvivmap = LvivMap()
    player = Player()
    player.inventory.add_item(Gun("Hyi", 200))
    print(" ___           ___      ___  ___      ___      ___ ")
    print("|\  \         |\  \    /  /||\  \    |\  \    /  /|")
    print("\ \  \        \ \  \  /  / /\ \  \   \ \  \  /  / /")
    print(" \ \  \        \ \  \/  / /  \ \  \   \ \  \/  / / ")
    print("  \ \  \____    \ \    / /    \ \  \   \ \    / /  ")
    print("   \ \_______\   \ \__/ /      \ \__\   \ \__/ /   ")
    print("    \|_______|    \|__|/        \|__|    \|__|/    ")
    print("Вітаю! Ти опинився в мандрівній грі, головною локацією якої є українське місто Львів.")
    print("Доступні команди:")
    available_commands = ['почати гру']
    for idx, command in enumerate(available_commands):
         print(f"{idx+1}. {command}")
    startinp = input(">>> ")
    print()
    if startinp.lower() == "почати гру":
        while True:
            lvivmap.print_current_street_info()
            lvivmap.print_current_person_info()
            street_commands = ["поговорити", "обшукати вулицю", "переглянути інвентар", "інформація персонажа", "йти далі"]
            if lvivmap.get_current_person().type == "злодій" or lvivmap.get_current_person().type == "злодійка":
                street_commands.append("розібратись із злочинцем")
                street_commands.remove("обшукати вулицю")
            if lvivmap.get_current_street().name == "Стрийська":
                street_commands.append("поспати(стоврити карту з новими персонажами)")
                street_commands.append("відкрити сейф")
            print("Доступні дії:")
            for idx, command in enumerate(street_commands):
                print(f"{idx+1}. {command}")
            inp1 = input('>>> ')
            if inp1 == "йти далі":
                lvivmap.print_available_moves()
                inp2 = input(">>> вул. ")
                if inp2 in lvivmap.street_dict:
                    lvivmap.change_current_street(inp2)
                    print()
                else:
                    print("\nХибні вхідні дані!\n")
            elif inp1 == "поговорити":
                lvivmap.print_current_person_speech()
            elif inp1 == "відкрити сейф":
                if player.key:
                    player.happy_end = True
                    is_game_ended = True
                    break
                else:
                    print("\nСпочатку тобі потрібно знайти ключ\n")
            elif inp1 == "переглянути інвентар":
                player.print_inventory()
                print("Доступні дії:")
                print("1. скористатись предметом")
                print("2. вийти")
                inp3 = input(">>> ")
                if inp3 == "скористатись предметом":
                    print("Введи назву предмету, котрим хочеш скористатись(разом з типом зброї, що наведений в квадратних дужках)")
                    inp4 = input(">>> ")
                    if inp4 in player.inventory.get_items_dict():
                        item = player.inventory.get_items_dict()[inp4]
                        if item.item_type == 'support':
                            item.use(player)
                            player.inventory.delete_item(item)
                            print(f"\nТи підняв рівень свого здоров'я на {item.health}\n")
                        else:
                            print("\nЗброю ти можеш використовувати лише в бою\n")
                    else:
                        print("\nТакого предмету немає в інвентарі\n")
                else:
                    print()
            elif inp1 == "інформація персонажа":
                player.print_player_info()
            elif inp1 == "обшукати вулицю":
                thing = lvivmap.get_current_street().search_street()
                if thing == None:
                    print("\nТи тинявся по вулиці, обійшов кожен куточок, однак більше нічого не знайшов\n")
                else:
                    print(thing)
                    if thing.split()[1] == "зброя":
                        item = Gun(thing.split()[0], thing.split()[2])
                    else:
                        item = Support(thing.split()[0], thing.split()[2])
                    player.inventory_add(item)
                    print(f'\nТи знайшов предмет типу [{thing.split()[1]}].')
                    print(f"Назва предмету: {thing.split()[0]}\n")
            elif inp1 == "розібратись із злочинцем":
                player.print_inventory()
                print("Введи назву предмету, який хочеш використати:")
                inp5 = input(">>> ")
                if inp5 in player.inventory.get_items_dict():
                    item = player.inventory.get_items_dict()[inp5]
                    if item.item_type == 'support':
                        print("\nПоки ти розбирався який предмет використати, тебе вбив злочинець\n")
                        is_game_ended = True
                        break
                    else:
                        if item.damage >= 100:
                            damage = 20
                        else:
                            damage = 49
                        player.health -= 49
                        if player.health < 0:
                            player.happy_end = False
                            print(f"\nТи залишився лежати без сил на вулиці {lvivmap.get_current_street().name}\n")
                            is_game_ended = True
                            break
                        print(f"\nТи успішно вбив ворога, знизивши своє здоров'я на {damage}")
                        random_num = random.randrange(0, 100)
                        if random_num % 2 == 0:
                            print(f"В правій кишені штанів злочинця ти знайшов ключ від сейфу. Нарешті ти можеш його відкрити")
                            player.key = True
                        print()
                else:
                    print("\nТи не зміг обрати зброю для бою, тому злочинець тебе пристрелив\n")
            else:
                print('\nЩось пішло не так. Спробуй ще раз\n')
    else:
        print('Щось пішло не так. Спробуй ще раз')
    if is_game_ended:
        if player.happy_end:
            print("\nТи успішно відкрив сейф і зібрав усі скарби. Вітаю!\n")
        else:
            print("\nТи не зміг впоратись із завданням... Відпочинь і спробуй ще раз!\n")

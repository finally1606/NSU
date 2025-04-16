import random

# Константы (можно вынести в ru.py для локализации)
RESOURCES_TITLE = "\nРесурсы:"
FOOD = "Еда: {}"
WEAPONS = "Оружие: {}"
MEDICATIONS = "Медикаменты: {}"
MORALE = "Мораль: {}"
DAY_TITLE = "\n=== День {} ==="
GAME_OVER_TITLE = "\n=== ИГРА ОКОНЧЕНА ==="
DAYS_SURVIVED = "Вы продержались {} дней."
WIN_MESSAGE = "Вы выжили все 10 дней! Поздравляем!"
LOSE_MESSAGE = "Мораль одной из команд упала до нуля. Игра окончена."
PRESS_ENTER = "\nНажмите Enter, чтобы продолжить..."

BASE_FORTIFIED = "База укреплена. Мораль повышена."
FOUND_FOOD = "Вы нашли {} единиц еды."
USED_MEDICATIONS = "Вы использовали медикаменты. Мораль повышена."
NOT_ENOUGH_FOOD = "Недостаточно еды."
NOT_ENOUGH_MEDICATIONS = "Недостаточно медикаментов."
INVALID_CHOICE = "Неверный выбор."
ZOMBIE_ATTACK_WITH_WEAPONS = "Зомби атаковали! Вы использовали {} оружия, мораль снизилась."
ZOMBIE_ATTACK_NO_WEAPONS = "Зомби атаковали, но у вас не было оружия! Мораль резко упала."
FOUND_MEDICATIONS = "Вы нашли {} медикаментов."

def create_team(name):
    return {
        'name': name,
        'food': 100,
        'weapons': 5,
        'meds': 3,
        'morale': 100,
        'alive': True
    }

def clear_console():
    print("\n" * 100)

def display_team_resources(team):
    print(RESOURCES_TITLE)
    print(FOOD.format(team['food']))
    print(WEAPONS.format(team['weapons']))
    print(MEDICATIONS.format(team['meds']))
    print(MORALE.format(team['morale']))

def controlled_event(team, teams):
    print("\n1. Укрепить базу (-20 еды, +10 мораль)")
    print("2. Поиск еды (случайный результат)")
    print("3. Использовать медикаменты (+30 мораль)")
    print("4. Попросить помощь у другой команды")
    print("5. Совершить налёт на другую команду")

    choice = input("Выберите действие (1-5): ")

    if choice == "1":
        if team['food'] >= 20:
            team['food'] -= 20
            team['morale'] += 10
            print("\n" + BASE_FORTIFIED)
        else:
            print("\n" + NOT_ENOUGH_FOOD)

    elif choice == "2":
        found_food = random.randint(10, 50)
        team['food'] += found_food
        print("\n" + FOUND_FOOD.format(found_food))

    elif choice == "3":
        if team['meds'] >= 1:
            team['meds'] -= 1
            team['morale'] += 30
            print("\n" + USED_MEDICATIONS)
        else:
            print("\n" + NOT_ENOUGH_MEDICATIONS)

    elif choice == "4":
        print("\nВыберите команду для запроса помощи:")
        options = [t for t in teams if t != team and t['alive']]
        for i, t in enumerate(options):
            print(f"{i + 1}. {t['name']}")
        try:
            selected = int(input("Введите номер команды: ")) - 1
            target = options[selected]
            if target['food'] >= 10:
                target['food'] -= 10
                team['food'] += 10
                print(f"{target['name']} передала 10 еды команде {team['name']}.")
            else:
                print(f"{target['name']} не может помочь.")
        except:
            print("Неверный выбор.")

    elif choice == "5":
        print("\nВыберите команду для налёта:")
        options = [t for t in teams if t != team and t['alive']]
        for i, t in enumerate(options):
            print(f"{i + 1}. {t['name']}")
        try:
            selected = int(input("Введите номер команды: ")) - 1
            target = options[selected]
            if team['weapons'] > 0:
                loot = min(20, target['food'])
                team['food'] += loot
                target['food'] -= loot
                team['morale'] -= 15
                print(f"{team['name']} совершила налёт на {target['name']} и отняла {loot} еды!")
            else:
                print("У вас нет оружия для налёта!")
        except:
            print("Неверный выбор.")

    else:
        print("\n" + INVALID_CHOICE)

    input(PRESS_ENTER)

def uncontrolled_event(team):
    outcome = random.randint(1, 100)
    if outcome < 50:
        zombies = random.randint(1, 3)
        if team['weapons'] > 0:
            team['weapons'] = max(0, team['weapons'] - zombies)
            team['morale'] -= 20
            print("\n" + ZOMBIE_ATTACK_WITH_WEAPONS.format(zombies))
        else:
            team['morale'] -= 50
            print("\n" + ZOMBIE_ATTACK_NO_WEAPONS)
    else:
        found_meds = random.randint(0, 1)
        team['meds'] += found_meds
        print("\n" + FOUND_MEDICATIONS.format(found_meds))
    input(PRESS_ENTER)

def game_loop():
    days_survived = 0

    teams = []
    for i in range(3):
        name = input(f"Введите название команды для подъезда {i+1}: ")
        teams.append(create_team(name))

    while days_survived < 10 and any(t['morale'] > 0 for t in teams):
        for team in teams:
            if not team['alive'] or team['morale'] <= 0:
                team['alive'] = False
                continue
            clear_console()
            print(DAY_TITLE.format(days_survived + 1))
            print(f"Команда: {team['name']}")
            display_team_resources(team)
            controlled_event(team, teams)
            clear_console()
            print(DAY_TITLE.format(days_survived + 1))
            print(f"Команда: {team['name']}")
            display_team_resources(team)
            uncontrolled_event(team)

        days_survived += 1

    clear_console()
    print(GAME_OVER_TITLE)
    print(DAYS_SURVIVED.format(days_survived))
    if all(t['morale'] > 0 for t in teams):
        print(WIN_MESSAGE)
    else:
        print(LOSE_MESSAGE)

if __name__ == "__main__":
    game_loop()
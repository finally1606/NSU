import random

# Константы
RESOURCES_TITLE = "\nРесурсы:"
FOOD = "Еда: {} (сытость)"
WEAPONS = "Оружие: {} (сила)"
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
RAID_SUCCESS = "Успешный налёт! Вы забрали {} еды и {} оружия у {}."
RAID_FAILED = "Налёт провалился! Вы потеряли {} еды и {} оружия."
RAID_EQUAL = "Налёт не удался - силы равны. Ничего не произошло."
HUNGER_PENALTY = "Ваша команда голодает! Сила уменьшена."

def create_team(name):
    return {
        'name': name,
        'food': 100,
        'weapons': 5,
        'meds': 3,
        'morale': 100,
        'alive': True
    }

def calculate_power(team):
    base_power = team['weapons'] * 2 + team['morale'] // 15
    if team['food'] > 50:
        food_bonus = 5
    elif team['food'] > 20:
        food_bonus = 0
    else:
        food_bonus = -15
        print(HUNGER_PENALTY)
    return max(1, base_power + food_bonus)

def clear_console():
    print("\n" * 100)

def display_team_resources(team):
    print(RESOURCES_TITLE)
    print(FOOD.format(team['food']))
    print(WEAPONS.format(team['weapons']))
    print(MEDICATIONS.format(team['meds']))
    print(MORALE.format(team['morale']))
    print(f"Сила команды: {calculate_power(team)}")

def controlled_event(team, teams):
    print("\n1. Укрепить базу (-20 еды, +10 мораль)")
    print("2. Поиск еды (случайный результат)")
    print("3. Использовать медикаменты (+20 мораль)")
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
        found_food = random.randint(5, 30)
        team['food'] += found_food
        print("\n" + FOUND_FOOD.format(found_food))

    elif choice == "3":
        if team['meds'] >= 1:
            team['meds'] -= 1
            team['morale'] += 20
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
            pending_requests.append({'from': team, 'to': target})
            print(f"\nЗапрос помощи отправлен команде {target['name']}.")
        except:
            print("Неверный выбор.")

        input(PRESS_ENTER)

    elif choice == "5":
        print("\nВыберите команду для налёта:")
        options = [t for t in teams if t != team and t['alive']]
        for i, t in enumerate(options):
            print(f"{i + 1}. {t['name']} (сила: {calculate_power(t)})")
        try:
            selected = int(input("Введите номер команды: ")) - 1
            target = options[selected]

            attack_cost = 15
            if team['food'] < attack_cost:
                print(f"Недостаточно еды для атаки! Нужно {attack_cost} единиц.")
                input(PRESS_ENTER)
                return

            team['food'] -= attack_cost
            print(f"Израсходовано {attack_cost} еды на подготовку атаки.")

            attacker_power = calculate_power(team)
            defender_power = calculate_power(target)

            print(f"\nСила атакующей команды: {attacker_power}")
            print(f"Сила защищающейся команды: {defender_power}")

            if attacker_power > defender_power * 1.15:
                food_loot = min(30, target['food'] // 2)
                weapons_loot = min(2, target['weapons'] // 2)
                team['food'] += food_loot
                team['weapons'] += weapons_loot
                target['food'] -= food_loot
                target['weapons'] -= weapons_loot
                target['morale'] -= 15
                team['morale'] += 5
                print("\n" + RAID_SUCCESS.format(food_loot, weapons_loot, target['name']))

            elif attacker_power * 1.15 < defender_power:
                food_loss = min(20, team['food'] // 3)
                weapons_loss = min(1, team['weapons'])
                team['food'] -= food_loss
                team['weapons'] -= weapons_loss
                team['morale'] -= 30
                target['morale'] += 10
                print("\n" + RAID_FAILED.format(food_loss, weapons_loss))

            else:
                team['morale'] -= 10
                target['morale'] -= 5
                print("\n" + RAID_EQUAL)

        except:
            print("Неверный выбор.")

    else:
        print("\n" + INVALID_CHOICE)

    input(PRESS_ENTER)

def uncontrolled_event(team):
    outcome = random.randint(1, 100)
    if outcome < 70:
        zombies = random.randint(2, 4)
        if team['weapons'] > 0:
            used_weapons = min(zombies, team['weapons'])
            team['weapons'] -= used_weapons
            team['morale'] -= 30
            print("\n" + ZOMBIE_ATTACK_WITH_WEAPONS.format(used_weapons))
        else:
            team['morale'] -= 60
            print("\n" + ZOMBIE_ATTACK_NO_WEAPONS)
    else:
        found_meds = random.randint(0, 1)
        team['meds'] += found_meds
        print("\n" + FOUND_MEDICATIONS.format(found_meds))

    food_consumption = random.randint(5, 15)
    team['food'] = max(0, team['food'] - food_consumption)
    print(f"Команда потребила {food_consumption} единиц еды.")

    input(PRESS_ENTER)

def game_loop():
    global pending_requests
    pending_requests = []
    days_survived = 0
    teams = []
    for i in range(3):
        name = input(f"Введите название команды для подъезда {i + 1}: ")
        teams.append(create_team(name))

    while days_survived < 10 and any(t['alive'] and t['morale'] > 0 for t in teams):
        for team in teams:
            if not team['alive'] or team['morale'] <= 0:
                team['alive'] = False
                continue

            clear_console()
            print(DAY_TITLE.format(days_survived + 1))
            print(f"Команда: {team['name']}")
            display_team_resources(team)
            controlled_event(team, teams)
            uncontrolled_event(team)

            if team['morale'] <= 0:
                team['alive'] = False

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

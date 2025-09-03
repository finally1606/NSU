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


    elif choice == "5":
        print("\nВыберите команду для налёта:")
        options = [t for t in teams if t != team and t['alive']]
        for i, t in enumerate(options):
            print(f"{i + 1}. {t['name']} (сила: {calculate_power(t)})")
        try:
            selected = int(input("Введите номер команды: ")) - 1
            target = options[selected]

            # Расход еды на атаку
            attack_cost = 10
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

            if attacker_power > defender_power * 1.15:  # Успешная атака
                food_loot = min(30, target['food'] // 2)
                weapons_loot = min(2, target['weapons'] // 2)

                team['food'] += food_loot
                team['weapons'] += weapons_loot
                target['food'] -= food_loot
                target['weapons'] -= weapons_loot
                target['morale'] -= 15
                team['morale'] += 5

                print("\n" + RAID_SUCCESS.format(food_loot, weapons_loot, target['name']))

            elif attacker_power * 1.15 < defender_power:  # Провальная атака
                food_loss = min(20, team['food'] // 3)
                weapons_loss = min(1, team['weapons'])

                team['food'] -= food_loss
                team['weapons'] -= weapons_loss
                team['morale'] -= 20
                target['morale'] += 10

                print("\n" + RAID_FAILED.format(food_loss, weapons_loss))

            else:  # Ничья
                team['morale'] -= 10
                target['morale'] -= 5
                print("\n" + RAID_EQUAL)
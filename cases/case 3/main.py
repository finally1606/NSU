import random
from ru import *

#Global variables for storing game state
food_amount = 100
weapons_amount = 5
medications_amount = 3
morale_amount = 100
days_survived_count = 0


def clear_console():
    # function for cleaning the screen
    print('\n' * 100)


def display_resources():
    # function to display the resources a player has
    print(RESOURCES_TITLE)
    print(FOOD.format(food_amount))
    print(WEAPONS.format(weapons_amount))
    print(MEDICATIONS.format(medications_amount))
    print(MORALE.format(morale_amount))
    print()


def controlled_event():
    # player action selection function
    global food_amount, morale_amount, medications_amount

    print(CONTROLLED_EVENT_TITLE)
    print(CONTROLLED_EVENT_OPTION1)
    print(CONTROLLED_EVENT_OPTION2)
    print(CONTROLLED_EVENT_OPTION3)
    choice = input(CONTROLLED_EVENT_PROMPT)

    if choice == "1":
        if food_amount >= 20:
            food_amount -= 20
            morale_amount += 10
            print("\n" + BASE_FORTIFIED)
        else:
            print("\n" + NOT_ENOUGH_FOOD)

    elif choice == "2":
        found_food = random.randint(10, 50)
        food_amount += found_food
        print("\n" + FOUND_FOOD.format(found_food))

    elif choice == "3":
        if medications_amount >= 1:
            medications_amount -= 1
            morale_amount += 30
            print("\n" + USED_MEDICATIONS)
        else:
            print("\n" + NOT_ENOUGH_MEDICATIONS)

    else:
        print("\n" + INVALID_CHOICE)

    input("\n" + PRESS_ENTER)


def uncontrolled_event():
    # Choose whether the player will be attacked by zombies or find medical supplies
    global weapons_amount, morale_amount, medications_amount

    outcome = random.randint(1, 100)
    if outcome < 50:  # 50% Chance to zombie attack
        zombies = random.randint(1, 3)
        if weapons_amount > 0:
            weapons_amount -= zombies
            morale_amount -= 20
            print("\n" + ZOMBIE_ATTACK_WITH_WEAPONS.format(zombies))
        else:
            morale_amount -= 50
            print("\n" + ZOMBIE_ATTACK_NO_WEAPONS)
    else:
        found_meds = random.randint(0, 1)
        medications_amount += found_meds
        print("\n" + FOUND_MEDICATIONS.format(found_meds))
    input("\n" + PRESS_ENTER)


def game_loop():
    global days_survived_count

    while days_survived_count < 10 and morale_amount > 0:
        clear_console()
        print(DAY_TITLE.format(days_survived_count + 1))
        display_resources()
        controlled_event()

        clear_console()
        print(DAY_TITLE.format(days_survived_count + 1))
        display_resources()
        uncontrolled_event()
        days_survived_count += 1

    clear_console()
    print(GAME_OVER_TITLE)
    print(DAYS_SURVIVED.format(days_survived_count))
    if morale_amount > 0:
        print(WIN_MESSAGE)
    else:
        print(LOSE_MESSAGE)


if __name__ == "__main__":
    game_loop()

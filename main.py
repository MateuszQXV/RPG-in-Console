import time

import keyboard

from player import Player

from maps import MAP1, MAP2, create_map

from utils import clear, print_logo, pause


player = Player()

current_map_name = "map1"

map1 = create_map(MAP1)

map2 = create_map(MAP2)

player_x, player_y = 5, 5

map1[player_y][player_x] = "@"


def get_current_map():

    return map1 if current_map_name == "map1" else map2


def render_map():

    for row in get_current_map():
        print("".join(row))


def change_map():

    global current_map_name, player_x, player_y

    clear()

    print_logo("Next level")

    time.sleep(1.2)

    current = get_current_map()

    current[player_y][player_x] = "."

    if current_map_name == "map1":

        current_map_name = "map2"

        player_x, player_y = 1, 1

        map2[player_y][player_x] = "@"

    else:

        current_map_name = "map1"

        player_x, player_y = 5, 5

        map1[player_y][player_x] = "@"


def can_move(ny, nx):

    m = get_current_map()

    height = len(m)

    width = len(m[0])

    if not (0 <= ny < height and 0 <= nx < width):

        return False

    tile = m[ny][nx]

    return tile not in ("#", "N")


def try_move(dy, dx):

    global player_x, player_y

    ny = player_y + dy

    nx = player_x + dx

    if not can_move(ny, nx):

        return

    m = get_current_map()

    if m[ny][nx] == "$":

        change_map()

        return

    m[player_y][player_x] = "."

    player_y, player_x = ny, nx

    m[player_y][player_x] = "@"


def handle_movement():

    if keyboard.is_pressed("w"):

        try_move(-1, 0)

    elif keyboard.is_pressed("s"):

        try_move(1, 0)

    elif keyboard.is_pressed("a"):

        try_move(0, -1)

    elif keyboard.is_pressed("d"):

        try_move(0, 1)

    time.sleep(0.12)


def main_menu():

    clear()

    print_logo("Welcome to RPG")

    print("""
    1. New game
    2. Settings
    3. Creator
    4. Exit
    """)

    try:

        choice = int(input("# "))

    except ValueError:

        print("\nThis is not a number...")

        time.sleep(1.5)

        return main_menu()

    clear()

    if choice == 1:

        return select_class()

    elif choice == 2:

        print("\nThe game is console-based – settings are not available yet.\n")

        pause()

        exit()

    elif choice == 3:

        print("\nGame by Regis9\n")

        pause()

        exit()

    elif choice == 4:

        print("\nSee you later!!!\n")

        exit()

    else:

        print("\nInvalid choice. Restarting menu...\n")

        time.sleep(1.5)

        return main_menu()


def select_class():

    print("""
    Choose your class:

        1. Warrior
        2. Mage
        3. Archer
    """)

    try:

        choice = int(input("# "))

    except ValueError:

        print("Please enter a number.")

        time.sleep(1)

        return select_class()

    clear()

    if choice == 1:

        player.set_warrior()

    elif choice == 2:

        player.set_mage()

    elif choice == 3:

        player.set_archer()

    else:

        print("Invalid choice.")

        time.sleep(1)

        return select_class()

    player.show_stats()

    pause("\nPress Enter to start...")

    return choice


def show_intro(class_choice):

    clear()

    print_logo("Echo of the Fallen Kingdom")

    pause()

    clear()

    print("""
The kingdom of Elarion was destroyed 20 years ago by a mysterious catastrophe

known as the Black Rupture. A wave of dark energy descended from the sky,

monsters began to emerge from the ruins, and magic became unstable.
    """)

    pause()

    clear()

    print("""
Three factions arose from the ruins of the world:

    Bladeguard           – warriors protecting the survivors.
    Circle of Arcana     – mages investigating the source of the disaster.
    Shadows of the Forest – archers and scouts living beyond the walls.
    """)

    if class_choice == 1:

        print("\nYou belong to the Bladeguard faction.")

    elif class_choice == 2:

        print("\nYou belong to the Circle of Arcana faction.")

    else:

        print("\nYou belong to the Shadows of the Forest faction.")

    pause()

    clear()


if __name__ == "__main__":

    class_choice = main_menu()

    show_intro(class_choice)

    while True:

        print("\033[H", end="")

        render_map()

        handle_movement()


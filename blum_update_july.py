from pyautogui import *
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
from pynput.mouse import Button, Controller
import colorama
from colorama import Fore

colorama.init(autoreset=True)

mouse = Controller()

def print_intro():
    print(r"""

   ____  _          _       _     _                                 _ 
  / __ \| | ___ __ (_) __ _| |__ | |_ _ __   _____      _____  __ _(_)
 / / _` | |/ / '_ \| |/ _` | '_ \| __| '_ \ / _ \ \ /\ / / __|/ _` | |
| | (_| |   <| | | | | (_| | | | | |_| | | |  __/\ V  V /\__ \ (_| | |
 \ \__,_|_|\_\_| |_|_|\__, |_| |_|\__|_| |_|\___| \_/\_/ |___/\__,_|_|
  \____/              |___/                                           


""")
    print(Fore.RED + "knight news- t.me/knightnewsai")

def print_message(message):
    if "Play" in message:
        print(Fore.MAGENTA + message)
    else:
        print(message)

def click(x, y):
    mouse.position = (x, y + random.randint(1, 3))
    mouse.press(Button.left)
    mouse.release(Button.left)

def activate_window(window):
    try:
        if window.isMinimized:
            window.restore()
        window.activate()
        return True
    except Exception as e:
        return False

def click_play_button(is_first_time):
    try:
        if is_first_time:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.75), telegram_window.top + int(telegram_window.height * 0.6))
        else:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.5), telegram_window.top + int(telegram_window.height * 0.85) - 10)
        if not activate_window(telegram_window):
            pass
        click(play_button_coords[0], play_button_coords[1])
        print_message('[🌙] | Play button pressed.')
        time.sleep(1)
    except Exception as e:
        pass

def find_and_click_objects():
    scrn = pyautogui.screenshot(region=(telegram_window.left, telegram_window.top + 50, telegram_window.width, telegram_window.height - 100))
    width, height = scrn.size

    for x in range(0, width, 10):
        for y in range(0, height, 10):
            r, g, b = scrn.getpixel((x, y))

            if (b in range(50, 255)) and (r in range(150, 255)) and (g in range(0, 255)):
                if not (r > 240 and g > 240 and b > 240):
                    screen_x = telegram_window.left + x
                    screen_y = telegram_window.top + 50 + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)

def start_game():
    window_name = input('\n[⚡️] | Crypto Clickers Hub | Press 1')
    num_games = int(input('\n[☘️] | Enter the number of games you want to play: '))

    if window_name == '1':
        window_name = "TelegramDesktop"

    check = gw.getWindowsWithTitle(window_name)
    if not check:
        print(f"[❌] | Window - {window_name} not found!")
        exit()

    print(f"[☘️] | Window found - {window_name}\n[☘️] | Press 'q' to pause.")

    global telegram_window
    telegram_window = check[0]
    paused = False

    games_played = 0
    is_first_time = True

    while games_played < num_games:
        click_play_button(is_first_time)
        is_first_time = False

        game_start_time = time.time()
        while time.time() - game_start_time < 32:
            if keyboard.is_pressed('q'):
                paused = not paused
                if paused:
                    print('[🌙] | Pause')
                else:
                    print('[🌙] | Resumption of work')
                time.sleep(1)

            while paused:
                if keyboard.is_pressed('q'):
                    paused = False
                    print('[🌙] | Resumption of work')
                    time.sleep(1)

            if not activate_window(telegram_window):
                print("[❌] | Failed to activate window, try again...")
                time.sleep(1)
                continue

            find_and_click_objects()

        games_played += 1
        print(f"[🌕] | Game over. Games played: {games_played}")

        if games_played < num_games:
            is_first_time = False
            time.sleep(2)

    print(f'[☘️] | {num_games} tickets are spent, the script is suspended.')

if __name__ == "__main__":
    print_intro()
    while True:
        start_game()

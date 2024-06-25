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
    except Exception:
        return False

def click_play_button(is_first_time):
    try:
        if is_first_time:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.75), telegram_window.top + int(telegram_window.height * 0.6))
        else:
            play_button_coords = (telegram_window.left + int(telegram_window.width * 0.5), telegram_window.top + int(telegram_window.height * 0.85) - 10)  # Moved up
        if not activate_window(telegram_window):
            pass
        click(play_button_coords[0], play_button_coords[1])
        print_message('[🌙] |Play button pressed.')
        time.sleep(1)
    except Exception as e:
        pass

def find_and_click_bacteria():
    scrn = pyautogui.screenshot(region=(telegram_window.left, telegram_window.top, telegram_window.width, telegram_window.height))
    width, height = scrn.size

    bacteria_found = False

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            r, g, b = scrn.getpixel((x, y))

            
            if (b in range(0, 125)) and (r in range(102, 220)) and (g in range(200, 255)):
                is_bomb = False
                for bx in range(-5, 6):
                    for by in range(-5, 6):
                        if 0 <= x + bx < width and 0 <= y + by < height:
                            br, bg, bb = scrn.getpixel((x + bx, y + by))
                            if br in range(100, 160) and bg in range(100, 160) and bb in range(100, 160):
                                is_bomb = True
                                break
                    if is_bomb:
                        break

                if not is_bomb:
                    screen_x = telegram_window.left + x
                    screen_y = telegram_window.top + y
                    click(screen_x + 4, screen_y)
                    time.sleep(0.001)
                    bacteria_found = True

    return bacteria_found

def start_game():
    window_name = input('\n[⚡️] | knight news | Click 1 ')
    num_games = int(input('\n[☘️] |Enter the number of games, which you want to play: '))

    if window_name == '1':
        window_name = "TelegramDesktop"

    check = gw.getWindowsWithTitle(window_name)
    if not check:
        print(f"[❌] | Window - {window_name} not found!")
        exit()

    print(f"[☘️] | Window found - {window_name}\n[☘️] |Click 'q' for a pause.")

    global telegram_window
    telegram_window = check[0]
    paused = False

    games_played = 0
    is_first_time = True

    while games_played < num_games:
        
        click_play_button(is_first_time)
        is_first_time = False

        game_start_time = time.time()
        while time.time() - game_start_time < 31:  
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

            bacteria_found = find_and_click_bacteria()
            if not bacteria_found and not paused:
                time.sleep(0.1)  

        games_played += 1
        print(f"[🌕] | Game over. Games played: {games_played}")

        if games_played < num_games:
            is_first_time = False
            time.sleep(2)  

    print(f'[☘️] | {num_games} tickets spent, script suspended.')

if __name__ == "__main__":
    print_intro()
    while True:
        start_game()

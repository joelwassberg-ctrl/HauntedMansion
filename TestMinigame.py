import random
import sys
import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay) 
def slower_print(text, delay=0.4):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay) 
player={"health":10,"attack":10,"level":1}
game_over=False

exp=0
exp_gain=random.randint(3,10)
def checkexp():
    global exp
    global exp_gain
    exp+=exp_gain
    if exp>=player["level"]*10:
        exp-=player["level"]*10
        player["level"]+=1
        player["health"]+=5
        player["attack"]+=2
        print(f"\n\033[92mYou leveled up to level {player['level']}, +5 hp, +2 attack\033[0m")

#minigame:
def exp_test():
    global exp
    ask=input("Win or lose?: (w/l)")
    if ask.lower() in ["w","win"]:
        print("win")
        checkexp()
        print(f"you gained {exp_gain} EXP")
        print(f"lvl: {player["level"]}, exp: {exp}")
        return True
    elif ask.lower() in ["l","lose"]:
        print("lose")
        player["health"]-=5
        if player["health"]<=0:
            slow_print("You have died!\n")
            global game_over
            game_over=True
    else:
        slow_print("Invalid input. Please enter 'w' to win or 'l' to lose.\n")
        exp_test()

#def name_room():
def win_room():
    exp_test()

#name_room.name="Room Name"
win_room.name="win"

rooms=[win_room]

def askdirection():
    path=""
    print(" ")
    direction=input("What door do you enter? left right or middle: ").lower()
    if direction in ["left", "l"]:
        path += "L"
        return path
    elif direction in ["right", "r"]:
        path += "R"
        return path
    elif direction in ["middle", "m"]:
        path+= "C"
        return path
    else:
        slow_print("Invalid direction. Please choose left, right, or middle.\n")
        path+=""
        return path
        askdirection()

def action():
    print("|Go deeper| |Inventory| |Stats| |Give up|")
    action=input("What do you want to do?: ").lower()
    if action in ["go deeper","deeper","go","deeper","g","d"]:
        return "deeper"
    elif action in ["inventory","inv","i"]:
        return "inventory"
    elif action in ["stats","stat","s"]:
        return "stats"
    else:
        slow_print("Invalid action\n");time.sleep(0.5)


while not game_over:
    room=random.choice(rooms)
    clear_console()
    player_action=action()
    if player_action=="deeper":
        if askdirection() in ["L","R","C"]:
            clear_console()
            slow_print(f"|YOU HAVE ENTERED: \033[33m{room.name}\033[0m|\n");time.sleep(0.5)
            room()
            if not game_over:
                input("Press \033[92m[Enter]\033[0m to continue your adventure...")
    elif player_action=="inventory":
        input("aint done this yet")
    elif player_action=="stats":
        input(f"| \033[33mLVL: {player['level']}\033[0m | \033[92mHP: {player['health']}\033[0m | \033[31mATK: {player['attack']}\033[0m |\n")
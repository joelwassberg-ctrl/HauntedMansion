import random
import sys
import time
import os

roomcount=0

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
def fast_print(text, delay=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
player={"health":100,"attack":100,"level":1}
game_over=False

clear_console()
time.sleep(0.5)
print("╔════════════════════════════════════════════════════╗")
print("║                                                    ║")
print("║              Welcome, brave Player...              ║")
print("║                                                    ║")
print("╚════════════════════════════════════════════════════╝")
time.sleep(1)
slow_print("You find yourself standing before an ancient manor...\n")
time.sleep(1)
print("\n")
fast_print("       🏚️  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  🏚️\n")
fast_print("      ████████╗██╗  ██╗███████╗    ███╗   ███╗ █████╗ ███╗   ██╗███████╗██╗ ██████╗ ███╗   ██╗\n")
fast_print("      ╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔══██╗████╗  ██║██╔════╝██║██╔═══██╗████╗  ██║\n")
fast_print("         ██║   ███████║█████╗      ██╔████╔██║███████║██╔██╗ ██║███████╗██║██║   ██║██╔██╗ ██║\n")
fast_print("         ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██╔══██║██║╚██╗██║╚════██║██║██║   ██║██║╚██╗██║\n")
fast_print("         ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║██║ ╚████║███████║██║╚██████╔╝██║ ╚████║\n")
fast_print("         ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n")
fast_print("       🏚️  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  🏚️\n")
print()
print()
slow_print("        \033[32m🌲 HAUNTED WOODLAND MANSION 🌲\033[0m\n")
print()
time.sleep(0.5)
slow_print("Dark clouds loom overhead...\n")
slow_print("An eerie wind whispers through the trees...\n");time.sleep(1)
slow_print("You step forward...\n")
slow_print("A powerfull force pulls you towards the manor...\n");time.sleep(0.5)
slow_print("The massive doors creak open as you get dragged inwards")
slower_print("...\n")
time.sleep(1)

def RPS():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    slow_print(f"Computer chose: {computer_choice}\n")
    if user_choice == computer_choice:
        slow_print("its a tie! Play again.\n\n")
        return RPS()
    elif (user_choice == "rock" and computer_choice == "scissors" or user_choice=="r" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock" or user_choice=="p" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper" or user_choice=="s" and computer_choice == "paper"):
        slow_print(f"You deal \033[31m{player["attack"]}\033[0m damage to the Zombie!\n")
        return True
    elif user_choice not in choices and user_choice not in ["r","p","s"]:
        slow_print(f"The enemy is confused. \033[31m{user_choice}\033[0m is not a valid choice. Play again.\n")
        return RPS()
    else:
        return False
#print(RPS())
def RPS_fight():
    global game_over
    global roomcount
    boss={"health":25,"attack":random.randint(5,8)}
    Zombie={"health":8,"attack":random.randint(2,5)}
    if roomcount<10:
        Enemy=Zombie
    elif roomcount==10:
        Enemy=boss
    slow_print("A Zombie appears! Prepare to fight! It challanges you to rock paper scissors... \n")
    while Enemy["health"] > 0 and player["health"] > 0:
        print(f"Enemy hp: {Enemy["health"]}\n")
        if RPS():
            Enemy["health"] -= player["attack"]
        else:
            player["health"] -= Enemy["attack"]
            slow_print(f"Zombie deals \033[31m{Enemy["attack"]}\033[0m damage! Keep going!\n")
            print(f"Your hp: {player["health"]}")
        if Enemy["health"] <= 0:
            slow_print("You defeated the Zombie!\n")
            checkexp()
            break
        if player["health"] <= 0:
            slow_print("You have been defeated by the Zombie... \033[31mGAME OVER\033[0m")
            game_over=True
            return

def VAG_fight():
    global game_over
    global roomcount
    boss={"health":25,"attack":random.randint(5,8)}
    Vampire={"health":10,"attack":random.randint(3,6)}
    if roomcount<10:
        Enemy=Vampire
    elif roomcount==10:
        Enemy=boss
    print("A Vampire appears!: Let's play a game!")
    while Enemy["health"] > 0 and player["health"] > 0:
        print(f"Enemy stats: {Enemy}")
        if vampire_age_game():
            Enemy["health"] -= player["attack"]
        else:
            player["health"] -= Enemy["attack"]
            print(f"The Vampire deals \033[31m{Enemy["attack"]}\033[0m damage!")
            print(f"Your health: {player['health']}\n\n")
            slow_print("Try again! (another vampire appears.)")
        if Enemy["health"] <= 0:
            print("You defeated the Vampire!\n")
            checkexp()
            break
        if player["health"] <= 0:
            print("You have been defeated by the Vampire... \033[31mGAME OVER\033[0m")
            game_over=True
            return
def Roulette_fight():
    global game_over
    global roomcount
    boss={"health":25,"attack":random.randint(5,8)}
    Walter_white={"health":12,"attack":random.randint(4,7)}
    if roomcount<10:
        Enemy=Walter_white
    elif roomcount==10:
        Enemy=boss
    print("Walter White appears... He has a serious expression on his face. He challenges you to a game of Russian Roulette.")
    while Enemy["health"] > 0 and player["health"] > 0:
        print(f"Enemy stats: {Enemy}")
        if russian_roulette():
            Enemy["health"] -= player["attack"]
            print(f"You deal \033[31m{player["attack"]}\033[0m damage to Walter White!\n")
        else:
            player["health"] -= Enemy["attack"]
            print(f"You take \033[31m{Enemy["attack"]}\033[0m damage!\n")
            print(f"Your stats: {player}")
        if Enemy["health"] <= 0:
            print("You defeated Walter White!\n")
            checkexp()
            break
        if player["health"] <= 0:
            print("You have been defeated by Walter White... \033[31mGAME OVER\033[0m")
            game_over=True
            return
def vampire_age_game():
    age = random.randint(25, 75)
    ans = (input("Am i 50 years old? higher or lower?: ")).lower()
    if ans == "lower" or ans=="l" and age < 50:
        print("Correct! I am under 50!\n")
        return True
    elif ans == "higher" or ans=="h" and age >= 50:
        print("Correct! I am over 50!\n")
        return True
    else: 
        print("Wrong...\n")
        return False
#print(vampire_age_game())

def russian_roulette():
    chamber = random.randint(1,6)
    round = 0
    while round != chamber:
            slow_print("You start... The barrel is spun. \n")
            input("pull the trigger? [Enter]")
            round += 1
            if chamber == round:
                slower_print("...\n")
                print("BANG! You are shot!")
                return False
                break
            else:
                slower_print("...\n")
                print("Click! Blank.")
                input("Now it's Walters turn.\n")
                round += 1
                if chamber == round:
                    slower_print("...\n")
                    print(f"BANG! Walter White is shot")
                    return True
                    break
                else:
                    slower_print("...\n") 
                    print(" Click! Blank.")
                input("Your turn again.\n")
                round +=1
                if chamber == round:
                    slower_print("...\n")
                    print("BANG! You are shot.")
                    return False
                else: 
                    slower_print("...\n")
                    print("Click! Blank.")
                    input("Now it's Walter's turn.\n")
                    round += 1
                    if chamber == round:
                        slower_print("...\n")
                        print("BANG! Walter is shot.")
                        return True
                    else: 
                        slower_print("...\n")
                        print(" Click! Blank.")
                    input("Your turn again.\n")
                    round +=1
                    if chamber == round:
                        slower_print("...\n")
                        print("BANG! You are shot.")
                        return False
                    else:
                        slower_print("...\n")
                        print("Click! Blank.")
                        input("Walter takes the final shot...\n")
                        print("You won!")
                        return True
#print(russian_roulette())

def BR():
    global game_over
    man={"health":3,"attack":1}
    e=random.randint(2,3)
    
    live=random.randint(3,5)
    blank=random.randint(1,5)
    print(F"live {live}")
    print(F"blank {blank}")
    while not e==0:
        target=input("who do you want tho shoot? you(y) or enemy(e) ").lower()
        if live + blank == 0:
            print("empty")
            live+=random.randint(1,5)
            blank+=random.randint(1,5)
            print(f"live{live}")
            print(f"blank{blank}")
        gun=random.randint(1,live+blank)
        if gun <= live and not live ==0:
            print("\033[31m-1 live\033[0m")
            live-=1
            if target=="y":
                player["health"]-= man["attack"]
                print(f"you lost \033[31m{man["attack"]}\033[0m hp")
            if target=="e":
                man["health"]-=1
                print("enemy lost 1 hp")
            print(F"your hp is {player["health"]}")
            print(F"enemy hp is {man["health"]}")
        elif gun> live:
            if blank>0:
                print("klick")
                if target=="e":
                    print(f"Your oponent laughs in your face. Lose \033[31m{man["attack"]}\033[0m hp")
                    player["health"]-= man["attack"]
                blank-= 1
                print("\033[32m-1 blank\033[0m")
                print(f"your hp is {player["health"]}")
                print(f"enemy hp is {man["health"]}")
        if player["health"]<=0:
            print("You have been defeated by the Figure... \033[31mGAME OVER\033[0m")
            game_over=True
            return
        elif man["health"]<=0:
            print("you defeated the enemy\n")
            checkexp()
            return True

def hangman():
    mistakes=""
    guess=[]
    word=random.choice(["hippopotamus","python","voidveil","bedrock","deepwoken","pneumonoultramicroscopicsilicovolcanoconiosis","github","glaze"])
    count=7
    showcase=["_"]*len(word)
    while "_" in showcase:
        print("".join(showcase))
        choice=input("what letter: ").lower()
        guess+=choice
        print("")
        for i in range(len(word)):
            if word[i]==choice:
                showcase[i]=choice
        guesses=("".join(guess))
        if choice not in word and choice not in mistakes:
            mistakes+=choice
            count-=1
            print(f"you have \033[31m{count}\033[0m mistakes left\n")
            print("mistakes:", mistakes)
        if count==0:
            print("you lost")
            break
    if "_" not in showcase:
        print(f"\033[33m{word}\033[0m")
        print("you won")
        return True
def hang_fight():
    global game_over
    global roomcount
    boss={"health":25,"attack":random.randint(5,8)}
    Cool_Ghost={"health":5,"attack":random.randint(2,4)}
    if roomcount<10:
        Enemy=Cool_Ghost
    elif roomcount==10:
        Enemy=boss
    while player["health"]>0 and Enemy["health"]>0:
        print(f"Enemy stats: {Enemy}")
        if hangman():
            Enemy["health"]-=player["attack"]
            print(f"You deal \033[31m{player["attack"]}\033[0m damage to the Ghost!")
        else:
            player["health"]-=Enemy["attack"]
            print(f"The Ghost deals \033[31m{Enemy["attack"]}\033[0m damage!")
            print(f"Your stats: {player}")
        if Enemy["health"]<=0:
            print("You defeated the Ghost!\n")
            checkexp()
            break
        if player["health"]<=0:
            print("You have been defeated by the Ghost... \033[31mGAME OVER\033[0m")
            game_over=True
            return

fruit=["🍇","🍓","🥭"]
def gamble():
    win=""
    play=input("play the slot machine? cost 1 hp per play (yes/no): ").lower()
    if play in ["yes","y"]:
        risk=input("Play big or small? (big/small): ").lower()
        if risk in ["small","s"]:
            reels=[random.choice(fruit) for _ in range(3)]
            print("Spinning the reels")
            slower_print("...\n")
            if reels[0]==reels[1]==reels[2]:
                print(" | ".join(reels))
                print("JACKPOT! You won the slot machine!")
                win="small_jackpot"
                return win
            elif reels[0]==reels[1] or reels[1]==reels[2]:
                print(" | ".join(reels))
                print("You got two of a kind! You win a small prize!")
                win="small_win"
                return win
            else:
                print(" | ".join(reels))
                print("No match. Better luck next time!")
                win="no_win"
                return win
        elif risk in ["big","b"]:
            reels=[random.choice(fruit) for _ in range(4)]
            print("Spinning the reels for big bucks!")
            slower_print("...\n")
            if reels[0]==reels[1]==reels[2]==reels[3]:
                print(" | ".join(reels))
                print("JACKPOT! You won the big slot machine!")
                win="big_jackpot"
                return win
            else:
                print(" | ".join(reels))
                print("No match. Better luck next time!")
                win="no_win"
                return win
        else:
            slow_print("Invalid choice. Please enter big or small.\n")
            return gamble()
    elif play in ["no","n"]:
        print("Maybe next time!")
        win="no_play"
        return win
    else:
        slow_print("Invalid choice. Please enter yes or no.\n")
        return gamble()
def slot_fight():
    global game_over
    while True:
        result=gamble()
        if result=="no_play":
            break
        if result=="small_win":
            print("You heal 1 hp")
            player["health"]+=1
        elif result=="small_jackpot":
            print("You heal 2 hp")
            player["health"]+=2
        elif result=="big_jackpot":
            print("You heal 2hp and gain 2 attack power")
            player["attack"]+=2
            player["health"]+=2
        elif result=="no_win":
            print("You lose 1 hp")
            player["health"]-=1
            print(player)
        if player["health"]<=0:
            print("You died by gambling </3... \033[31mGAME OVER\033[0m")
            game_over=True

def trap_room():
    global game_over
    trap_damage=random.randint(3,5)
    slow_print("You enter a seemily empty room.)\n");time.sleep(1)
    slow_print("Suddenly you hear a click as you step on a hidden pressure plate!\n");time.sleep(1)
    slow_print(f"Arrows shoot out from the walls. You take \033[31m{trap_damage}\033[0m damage!\n");time.sleep(1)
    if player["health"]>0:
        player["health"]-=trap_damage
        print(f"Your health is now: \033[92m{player['health']}\033[0m\n")
        if player["health"]<=0:
            slow_print("You have died from the trap!\n")
            game_over=True

Boss_games=[RPS_fight,VAG_fight,Roulette_fight,hang_fight]

def Final_boss():
    global game_over
    global Boss_games
    while not game_over:
        slow_print("A towering figure stands before you, hiden by shadows.\n")
        game=Boss_games.copy()
        random.shuffle(game)
        First_game=game.pop()
        slow_print(f"The figure is changing shape... First game...\n")
        First_game()
        time.sleep(1)
        Second_game=game.pop()
        slow_print("The figure morphes violently")
        slower_print("...\n")
        slow_print("Second game...\n")
        Second_game()
        time.sleep(1)
        print("The figure is bending and twisting")
        slower_print("...\n")
        slow_print("Final game...\n")
        Third_game=game.pop()
        Third_game()
        slow_print("You gained \033[92m??? EXP\033[0m from defeating the final boss!\n You reached \033[33mLEVEL 10!\033[0m");time.sleep(1.5)
        player["level"]=10
        clear_console()
        slower_print("...\n")
        slow_print("The figure lies defeated on the ground ")
        slower_print("...\n");time.sleep(0.5)
        slow_print("You did it.");time.sleep(1)
        slow_print("Past the once menacing figure, a door glows. The light is coming from outside... ");time.sleep(2)
        slow_print("You made it out!\n")
        game_over=True
        print("\033[92mCONGRATULATIONS! YOU HAVE ESCAPED THE MANOR!\033[0m")

items_total_dmg=0
inventory_names=[]
def chest_room():
    global player
    remove_dmg=0
    Attack_potion={"Item":"Attack potion","Power":random.randint(1,2)}
    sword={"Item":"Sword","Power":random.randint(2,4)}
    dagger={"Item":"Dagger","Power":random.randint(1,3)}
    Halbert={"Item":"Halbert","Power":random.randint(3,5)}
    item_pool = [Attack_potion,sword,dagger,Halbert]
    mimic= random.randint(1,100)
    print("You enter a dimly lit room with a large chest in the center.")
    open_chest = input("Do you want to open the chest? (yes/no): ").lower()
    if open_chest == "yes" or open_chest=="y":
        if mimic == 1:
            print("As you open the chest, it transforms into a terrifying mimic and attacks you!")
            print("You must play Russian Roulette to survive.")
            Roulette_fight()
        else:
            print("You open the chest and find a treasure!")
            found_item = random.choice(item_pool)
            item =print(f"You found: \033[95m{found_item["Item"]}\033[0m")
            if len(inventory_names)>=5:
                print("Your inventory is full! Replace an item?.")
                print(f"Current inventory: {inventory_names}")
                replace=input("Do you want to replace an item? (yes/no): ").lower()
                if replace in ["yes","y"]:
                    item_to_replace=input("Enter the name of the item to replace (Name,DMG:x):  ")
                    for char in item_to_replace:
                        if char.isdigit():
                            remove_dmg+=int(char)
                    if item_to_replace in inventory_names:
                        player["attack"]-=remove_dmg
                        inventory_names.remove(item_to_replace)
                        inventory_names.append(f"{found_item['Item']},DMG:{found_item['Power']}")
                        player["attack"]+=found_item["Power"]
                        print(f"Your inventory now contains: {inventory_names}")
                    else:
                        print("Item not found in inventory(or not input correctly. ItemName,DMG:ItemDamage). You leave the new item behind.")
                else:
                    print("You leave the new item behind.")
            else:
                player["attack"] += found_item["Power"]
                inventory_names.append(f"{found_item['Item']},DMG:{found_item['Power']}")
                print(f"Your inventory now contains: {inventory_names}")
            
            return item
    else:
        item=("You decide not to open the chest and leave the room safely.")
        return item
    


def poker_room():
    print("You see a poker table with cards and chips")
    slow_print("Shady figure: Sit down. We are going to play buckshot roulette.\n")
    BR()
def kitchen():
    print("You see cookware and a delicious cake in the room")
    VAG_fight()
def suply_closet():
    print("You see cleaning supplies and a mop in the room")
    Roulette_fight()
def odd_room():
    print("You see random oddities and strange artifacts in the room")
    RPS_fight()
def slot_room():
    print("You see a shiny slot machine in the room")
    slot_fight()
def hang_room():
    print("You see a VERY cool ghost with red spiky shades in the room")
    hang_fight()
trap_room.name="Trap Room"
poker_room.name="Poker Room"
kitchen.name="Kitchen"
suply_closet.name="Supply Closet"
odd_room.name="Odd Room"
chest_room.name="Treasure Room"
slot_room.name="Slot-machine Room"
hang_room.name="Whiteboard Room"

rooms=[trap_room,poker_room,kitchen,suply_closet,odd_room,chest_room,slot_room,hang_room]

exp=0
def checkexp():
    global exp
    exp_gain=random.randint(5,20)
    print(f"You gained {exp_gain} EXP")
    exp+=exp_gain
    if exp>=player["level"]*10:
        exp-=player["level"]*10
        player["level"]+=1
        player["health"]+=5
        player["attack"]+=1
        print(f"lvl: {player["level"]}, exp: {exp}")
        

path=""
def askdirection():
    path=""
    print(" ")
    direction=input("Do you want to go left right or middle: ").lower()
    if direction in ["left", "l"]:
        path += "L"
        return path
    elif direction in ["right", "r"]:
        path += "R"
        return path
    elif direction in ["middle", "m"]:
        path+= "M"
        return path
    else:
        slow_print("Invalid direction. Please choose left, right, or middle.\n")
        path+=""
        return path
        askdirection()

def action():
    global roomcount
    print("|Go deeper| |Inventory| |Stats| |Give up|")
    action=input("What do you want to do?: ").lower()
    if action in ["go deeper","deeper","go","deeper","g","d"] and roomcount<10:
        return "deeper"
    elif action in ["go deeper","deeper","go","deeper","g","d"] and roomcount==10:
        return "boss_room"
    elif action in ["inventory","inv","i"]:
        return "inventory"
    elif action in ["stats","stat","s"]:
        return "stats"
    elif action in ["give up"]:
        global game_over
        game_over=True
        slow_print("You have given up your adventure...\n")
        slow_print("GAME OVER\n")
    else:
        slow_print("Invalid action\n");time.sleep(0.5)

while not game_over:
    room=random.choice(rooms)
    clear_console()
    slow_print("The walls are shifting...\n");time.sleep(0.5)
    print("Three doors stand infront of you in each direction.                      ROOMS CLEARED:",roomcount)
    player_action=action()
    if player_action=="deeper":
        if askdirection() in ["L","R","M"]:
            clear_console()
            slow_print(f"|YOU HAVE ENTERED: \033[33m{room.name}\033[0m|\n");time.sleep(0.5)
            room()
            if not game_over:
                roomcount+=1
                input("Press \033[92m[Enter]\033[0m to continue your adventure...")
    elif player_action=="boss_room":
        clear_console()
        input("You stand before the final door of the manor... Enter")
        Final_boss()
    elif player_action=="inventory":
        input("Your inventory contains: \033[95m" + " | ".join(inventory_names) + "\033[0m\n")
    elif player_action=="stats":
        input(f"| \033[33mLVL: {player['level']}\033[0m | \033[92mHP: {player['health']}\033[0m | \033[31mATK: {player['attack']}\033[0m |\n")
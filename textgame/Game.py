import random

money = 3000
life = 3
week_count = 0
continue_playing = ''
start = True
game_start = True
diamond_debt = False
ten_percent_interest = False
twenty_percent_interest = False
thirty_percent_interest = False

# Start of Game
while game_start:
    print("Welcome to the Gold Rush Game")
    start_game = input("Would you like to play the game. Yes or No: ").lower()
    if start_game == "yes":
        print('''__________________________________________
Lets start our game!
To quit the game at any time input 'quit'
To ask for a loan type 'loan'
__________________________________________''')
        break

    elif start_game == "no":
        print("Sorry to hear that please play later")
        start = False
        break

# START LOOP
while start:
    if money <= 0:
        print('''You have no more money :( 
Thank you for playing''')
        break

    elif life <= 0:
        print(''' Game Over:
    No More Lives :(
Thank you for playing''')
        break

    print('''Before we start, lets talk about the rules in this game.
1. This game is based on rng, you the player will be traveling to many sites to either earn money or lose money
2. If you run out of money or lives, its game over
3. Have fun and enjoy the game :)
Sites:
Site 1: ☘ Lucky Clover ☘
Site 2: ⟡ Diamond Mines ⟡
Site 3: ♥ Heart are Wild ♥
__________________________________________________________________________________________________________________
''')
    input("Lets continue, type any character: ")
    print("Game:")

    # ACTUAL GAME
    while money > 0 and life > 0:

        if diamond_debt:
            money -= 700

        if continue_playing == "quit":
            print("Sorry to hear that, please play next time :)")
            start = False
            break
        #BONUS #2
        if continue_playing == "loan":
            print('''What type of plan?
1. $1000 but 10% interest
2. $2000 but 20% interest
3. $5000 but 30% interest''')

            plan = input("Please type in the number of your plan: ")
            if plan == '1':
                agreev1 = (input("Are you sure you want to take plan 1.: Y or N : ").lower())
                if agreev1 == 'y':
                    money += 1000
                    ten_percent_interest = True
                elif agreev1 == 'n':
                    break

            elif plan == '2':
                agreev2 = (input("Are you sure you want to take plan 2.: Y or N ").lower())
                if agreev2 == 'y':
                    money += 2000
                    twenty_percent_interest = True
                elif agreev2 == 'n':
                    break

            elif plan == '3':
                agreev3 = (input("Are you sure you want to take plan 3.: Y or N ").lower())
                if agreev3 == 'y':
                    money += 5000
                    thirty_percent_interest = True
                elif agreev3 == 'n':
                    break

        if ten_percent_interest:
            money *= 0.1

        elif twenty_percent_interest:
            money *= 0.2

        elif thirty_percent_interest:
            money *= 0.3

        print(f"Week: {week_count}")
        rng = random.randint(1, 3)
        print(f'Money: ${money}')
        print(f'Lives: {life}')

        # SITE: 1 (COMPLETED)
        if rng == 1:
            print("""____________________________________________________
Welcome to ☘ Lucky Clover ☘
10% chance at $1000 payload
30% chance at $500 payload
60% chance of losing half of your money to a "thief" 
_____________________________________________________""")
            input("Lets test your luck, input any character: ")
            # Second RNG creator
            v1rng = random.randint(1, 10)
            if v1rng == 1:
                print("Woah you just gained $1000")
                money += 1000

            elif v1rng <= 4:
                print("Woah you just gained $500")
                money += 500

            elif v1rng > 5:
                # BONUS THIEF DIFFERENT ONES
                thief_rng = random.randint(1, 4)
                if thief_rng == 1:
                    print("The sneak thief stole all your money :( (-70%)")
                    money *= 0.7

                elif thief_rng == 2:
                    print("The VSCO thief stole all your money (-100%)")
                    money = -500

                elif thief_rng == 3:
                    print("The regular thief stole your money (-50%) :(")
                    money //= 2

                elif thief_rng == 4:
                    print("The pooh snatcher just stole all your money :( (puts you at $1)")
                    money = 1

            continue_playing = input(
                "Input any character to continue playing or type 'quit' to stop playing or get a loan: ").lower()
            print("______________________________________________________________________________")
            week_count += 1
            money += 500

        # SITE 2 (COMPLETED)
        if rng == 2:
            print("""____________________________________________________
Welcome to ⟡ Diamond Mines ⟡
20% chance at $800 payload
40% chance at $400 payload
40% chance of losing $700 every week from now on (for this week, you will lose an extra $200
_____________________________________________________""")
            input("Lets test your luck, input any character: ")
            v2rng = random.randint(1, 10)
            if v2rng < 2:
                print("Woah you just gained $800")
                money += 800

            elif v2rng <= 6:
                print("Woah you just gained $400")
                money += 400

            elif v2rng > 6:
                print("NOOOO! You now have diamond debt :( (-$700 every week)")
                diamond_debt = True

            continue_playing = input(
                "Input any character to continue playing or type 'quit' to stop playing or get a loan: ").lower()
            print("______________________________________________________________________________")
            week_count += 1
            money += 500

        # SITE 3 (COMPLETED)
        if rng == 3:
            print("""____________________________________________________
Welcome to ♥ Heart are Wild ♥
10% chance at $8000 payload
40% chance at $300 payload
50% chance of losing a life
_____________________________________________________""")
            input("Lets test your luck, input any character: ")
            v3rng = random.randint(1, 10)
            if v3rng == 1:
                print("Woah you just gained $8000")
                money += 8000

            elif v3rng <= 5:
                print("Woah you just gained $300")
                money += 300

            elif v3rng > 5:
                print("Boo Hoo you lost a life :(")
                life -= 1

            continue_playing = input(
                "Input any character to continue playing or type 'quit' to stop playing or get a loan: ").lower()
            print("______________________________________________________________________________")
            week_count += 1
            money += 500

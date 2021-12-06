import time, random, os, platform


# def start_game():
#     print("---Gotta Solve Em' All---")
#     checkans = input("BONUS: What is 1+1? ")  # test money and add money
#     while not checkans.isdigit():
#         print("Please type a number!")
#         checkans = input("BONUS: What is 1+1? ")
#     if float(checkans) == 2:
#         addmoney = random.randint(0, 1000)
#         prizemoney = "You have won a total of $%d " % addmoney
#     else:
#         addmoney = 0
#         prizemoney = (
#             "Unfortunately, you did not win anything today...\nBetter luck next time! "
#         )
#     ans = "Your answer of %s is ..... %r \n" % (checkans, float(checkans) == 2)
#     self.slowtype(ans)
#     self.slowtype(prizemoney)
#     self.gainmoney(addmoney)
#     self.checkmoney()
#     if float(checkans) == 2:  # testing losemoney function
#         self.slowtype(
#             "Actually, that question was too ez\nI am taking the money back.\n\nWhat, u not happy?\nIf u want it back, come get it!\n"
#         )
#         losemoney = "You lost $%d! " % addmoney
#         self.slowtype(losemoney)
#         self.losemoney(addmoney)
#         self.checkmoney()
#     return


class Images:
    def __init__(self):
        pass

    def concatimage(self, string1, string2):  # meme
        # print (string1,string2)
        c = ""
        listmaxlength = []
        string1 = string1.split("\n")
        string2 = string2.split("\n")
        if len(string1) < len(string2):
            for i in range((len(string2) - len(string1)) // 2):
                string1.insert(0, c)
            for i in range((len(string2) - len(string1))):
                string1.append(c)
        elif len(string2) < len(string1):
            for i in range((len(string1) - len(string2)) // 2):
                string2.insert(0, c)
            for i in range((len(string1) - len(string2))):
                string2.append(c)
        for i in range(len(string1)):
            listmaxlength.append(len(string1[i]))
            listmaxlength.append(len(string2[i]))
        addspace = max(listmaxlength)
        for i in range(len(string1)):
            blank = " "
            blank = blank * (addspace - len(string1[i]))
            string1[i] = string1[i] + blank
            blank = " "
            blank = blank * (addspace - len(string2[i]))
            string2[i] = string2[i] + blank
            c = c + string1[i] + string2[i] + "\n"
        return c

    def inverseimage(self, pixelart):  # prints a mirrored art
        lists = []
        highest = []
        makethiswork = ""
        string = ""
        for i in range(len(pixelart)):
            if pixelart[i] == "\n":
                lists.append(i)
        # print(lists)

        for j in range(len(lists)):
            if j + 1 < len(lists):
                b_lists = list(pixelart[lists[j] : lists[j + 1]])
                for y in range(len(b_lists)):
                    if b_lists[y] == "/":
                        b_lists[y] = "\\"
                    elif b_lists[y] == "\\":
                        b_lists[y] = "/"
                    makethiswork = makethiswork + (b_lists[y])
        # print(makethiswork)
        ls = makethiswork.split("\n")
        for i in range(len(ls)):
            highest.append(len(ls[i]))
        addspace = max(highest)
        for i in range(len(ls)):
            blank = " "
            if addspace > len(ls[i]):
                blank = blank * (addspace - len(ls[i]))
                ls[i] = ls[i] + blank
            if ls[i] == "/":
                ls[i] = "\\"
            elif ls[i] == "\\":
                ls[i] = "/"
            string = string + (ls[i][::-1]) + "\n"
        return string


class Currency:
    def __init__(self, money):
        self.money = int(money)

    def gainmoney(self, moneytoadd):
        self.money += moneytoadd
        pass

    def losemoney(self, moneytolose):
        self.money -= moneytolose
        pass

    def checkmoney(self):
        self.slowtype(f"Your current money is: ${self.money} \n")
        pass


# Pokemon class
class Pokemon:
    def __init__(self, name, types, move, health):
        self.name = name
        self.types = types
        self.move = move
        self.health = health
        pass


class Typing:
    def __init__(self):
        pass

    def slowtype(self, stringtoslowtype):
        stringtoslowtype += "\n"
        msgtoslowtype = ""
        for i in range(len(stringtoslowtype)):
            if stringtoslowtype[i] == "\n":
                msgtoslowtype = msgtoslowtype + "\n"
                for x in range(len(msgtoslowtype)):
                    if msgtoslowtype[x] == " ":
                        print(" ", end="")
                    elif msgtoslowtype[x] == ".":
                        print(msgtoslowtype[x], end="")  # print without spacing
                        time.sleep(0.5)
                    else:
                        print(msgtoslowtype[x], end="")  # print without spacing
                        time.sleep(0.05)
                msgtoslowtype = ""
            else:
                msgtoslowtype = (
                    msgtoslowtype + stringtoslowtype[i]
                )  # concatenate string

    def fasttype(self, stringtoslowtype):  # meme
        stringtoslowtype += "\n"
        msgtoslowtype = ""
        for i in range(len(stringtoslowtype)):
            if stringtoslowtype[i] == "\n":
                msgtoslowtype = msgtoslowtype + "\n"
                for x in range(len(msgtoslowtype)):
                    if msgtoslowtype[x] == " ":
                        print(" ", end="")
                    elif msgtoslowtype[x] == ".":
                        print(msgtoslowtype[x], end="")  # print without spacing
                        time.sleep(0.01)
                    else:
                        print(msgtoslowtype[x], end="")  # print without spacing
                        time.sleep(0.01)
                msgtoslowtype = ""
            else:
                msgtoslowtype = (
                    msgtoslowtype + stringtoslowtype[i]
                )  # concatenate string


class Pokemart:
    def pokemart(self):
        print("test")
        self.fasttype(
            r"""
        Welcome to the Store,
        Its your lucky day, our shipment just arrived so we have plenty in stock.
        
        What would you like to buy today?
        1. $500 | Potion (S) | Recovers 1 health bar 
        2. $1000 | Potion (M) | Recovers 2 heath bars
        3. $1500 | Potion (L) | Recovers 3 health bars
        
        To leave, press [Enter].
        """
        )
        ans = input("Option ")
        while not ans.isdigit() or not (1 <= int(ans) <= 3):
            print("Please type [number] and [enter] !")
            ans = input("Option ")
        option = int(ans)
        self.fasttype("You have selected %s" % ans)
        multiplier = input("How many of it would you like? (0 to 99) ")
        while (not multiplier.isdigit()) or not (0 <= int(multiplier) <= 99):
            print("Please type [number] and [enter]!")
            multiplier = input("How many of it would you like? (0 to 99) ")
        m = int(multiplier)
        if option == 1:
            itemprice = 500
        elif option == 2:
            itemprice = 1000
        elif option == 3:
            itemprice = 1500
        else:
            exit()
        itemprice = m * itemprice
        print(f"That would be a total of {itemprice}")
        self.slowtype(
            r""" 
        Thank you for shopping with us, 
        Hope to see you again! 
        """
        )
        self.losemoney(itemprice)
        self.checkmoney()


bulbasaur = r'''
                                           /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.\
       ____      |___._.  |       __               \ `.
     .'    `---""       ``"-.--"'`  \               .  \
    .  ,            __               `              |   .
    `,'         ,-"'  .               \             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  """""'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''"""""`.,^.`.--' 
            '''
oak = r"""
    #############       
    ##         ##      
    #  ~~   ~~  #    
    #  ()   ()  #      
    (     ^     )       
     |         |        
     |  {===}  |      
      \       /       
     /  -----  \      
  ---  |%\ /%|  ---     
 /     |%%%%%|     \    
       |%/ \%|                                    
        """  # https://www.asciiart.eu/people/faces
# P.start_game()
# secondb = P.inverseimage(bulbasaur)
# P.fasttype(P.concatimage(bulbasaur,bulbasaur))
# P.fasttype(P.concatimage(secondb,bulbasaur))
# P.fasttype(P.concatimage(bulbasaur,secondb))

# print(P.name)

# Functions used by later functions
def clear_screen():
    """
    Checks which os the system is using and adjusts the clear screen function based on it.
    """
    if platform.system() == "Windows":
        return os.system("cls")
    elif platform.system() in ("Darwin", "Linux"):
        return os.system("clear")


def random_generator(lower_limit, upper_limit):
    first_number = random.randint(lower_limit, upper_limit)
    second_number = random.randint(lower_limit, upper_limit)
    return first_number, second_number


def damage_enemy(P, P_enemy):
    for i in range(0, 3):
        clear_screen()
        print(
            ".                          ENEMY\n",
            "                  ",
            "=" * P_enemy.health,
            "\nYOU                            .\n",
            "=" * P.health,
        )
        time.sleep(0.2)
        clear_screen()
        print(
            ".                     OUCHOUCHOUCH\n",
            "                  ",
            "=" * P_enemy.health,
            "\nYOU                            .\n",
            "=" * P.health,
        )
        time.sleep(0.2)
        clear_screen()


def damage_self(P, P_enemy):
    for i in range(0, 3):
        print(
            ".                            ENEMY\n",
            "                  ",
            "=" * P_enemy.health,
            "\nYOU                            .\n",
            "=" * P.health,
        )
        time.sleep(0.2)
        clear_screen()
        print(
            ".                          ENEMY\n",
            "                  ",
            "=" * P_enemy.health,
            "\nOUCHOUCHOUCH                .\n",
            "=" * P.health,
        )
        time.sleep(0.2)
        clear_screen()


# Functions involved in main()
def introduction(player_name):
    print("------------------------------------------")
    print(  # https://www.asciiart.eu/people/faces
        r"""
    #############       
    ##         ##      
    #  ~~   ~~  #    
    #  ()   ()  #      
    (     ^     )       
     |         |        
     |  {===}  |      
      \       /       
     /  -----  \      
  ---  |%\ /%|  ---     
 /     |%%%%%|     \    
       |%/ \%|                                    
        """
    )
    print(
        f"Prof Chewbaka: Welcome to Mathematica Island, {player_name}!\n"
        "I am Professor Chewbaka, a researcher on this island.\n"
        "There are 2 Pokemons on the loose:\n"
        "Addition and Subtraction.\n"
        "Will you help me catch them?\n"
    )

    time.sleep(1)

    N = 0
    while True:
        choice = input("Help the Professor?(Y/N): ")

        if choice == "Y":
            print("Prof: Thank you so much!\n")
            return 1

        elif choice == "N":
            N += 1
            if N == 1:
                print("Come on... Don't you want to help me? :(")
            elif N == 2:
                print("I'll give you bonus marks for M&A assessment later...")
            elif N == 3:
                print("Sigh...No adventures for you then...")
                return 0
        else:
            print("Wait, what? I don't understand you.")


def pokemon_choose(player_name, starter_pokemon):
    print(
        f"\nYou will need a started Pokemon to hunt down the loose pokemon."
        f" \nChoose your starter Pokemon, {player_name}!"
    )

    for i in starter_pokemon:
        print(f"[{starter_pokemon.index(i)+1}] {i}")

    while True:
        try:
            choose_pokemon = int(input("Your starter pokemon is: ")) - 1
            if choose_pokemon in range(0, len(starter_pokemon)):
                chosen_pokemon = starter_pokemon[choose_pokemon]
                print(f"\nHooray. {chosen_pokemon} is now your Pokemon!\n")
                return chosen_pokemon
            else:
                print(
                    "Hey, I don't have that. Please only choose amongst the 3 pokemons here!"
                )

        except ValueError:
            print(
                "Hey, I don't have that. Please only choose amongst the 3 pokemons here!"
            )


def mode_selection(player_name):
    """
    Used to select mode the user wants to play
    """
    print(
        "There are a few Pokemons on the loose:\n" "[1]: Addition\n" "[2]: Subtraction"
    )
    pokemon_fight = ("Addition", "Subtraction")

    while True:
        try:
            option = int(input("Which pokemon do you want to catch? ")) - 1
            print(option)
            if option in (0, 1):
                print(
                    f"\nAlright, seems like you have chosen to catch {pokemon_fight[option]}.\n"
                    f"Good luck on your adventure, {player_name}!\n"
                )
                return option
            else:
                print("Huh? There is no such pokemon!")

        except ValueError:
            print("Huh? There is no such pokemon!")


def encounter(P, P_enemy):
    loop = 1
    while loop == 1:
        print(
            ".                          ENEMY\n",
            "                  ",
            "=" * P_enemy.health,
            "\nYOU                            .\n",
            "=" * P.health,
        )
        action = input("What would you like to do?\n" "[1] Attack\n" "[2] Portion\n")
        if action == "1":
            loop = 0
        elif action == "2":
            P.health += 1
            clear_screen()
            print("Health added")

        else:
            clear_screen()
            print("Invalid input!")


def solve_question(option, P, P_enemy):
    """
    Allows the user to input solution, and checks if user input is correct
    """
    two_numbers = random_generator(0, 1000)

    loop = 1
    while loop == 1:
        try:
            if option == 0:
                correct_ans = two_numbers[0] + two_numbers[1]
                ans = int(input(f"Solve sum of {two_numbers[0]} and {two_numbers[1]}:"))
                loop = 0

            elif option == 1:
                correct_ans = abs(two_numbers[0] - two_numbers[1])
                ans = int(
                    input(f"Solve difference of {two_numbers[0]} and {two_numbers[1]}:")
                )
                loop = 0

        except ValueError:
            print("Please only type integers!")

    if ans == correct_ans:
        P_enemy.health -= 1
        clear_screen()
        damage_enemy(P, P_enemy)
        print(
            "Nice!\n"
            "You inflicted 1 damage on enemy pokemon\n"
            f"Enemy pokemon has {P_enemy.health} health left!\n"
        )

    else:
        P.health -= 1
        clear_screen()
        damage_self(P, P_enemy)
        print(
            "On no!\n"
            "Your pokemon took 1 damage!\n"
            f"Your pokemon has {P.health} health left!\n"
        )


def game_over():
    print("Your pokemon has fainted... ")
    print("-----------\nGame Over\n-----------")
    loop = 1
    while loop == 1:
        play_again = input("Would you like to play again? (Y/N)")
        if play_again == "Y":
            main()
            loop = 0
        elif play_again == "N":
            print("Alright, goodbye!")
            loop = 0
        else:
            print("Sorry, I don't understand your input.")


# def victory():
#     print("Congratulations")
#     # gainexp()
# gainmoney()


def main():
    """
    The actual code will run from here
    """
    print("-----------------\n" "Gotta Solve Em All\n" "-----------------\n")

    # Variables
    P = Pokemon("no name", "no type", "no moves", 5)
    P_enemy = Pokemon("no name", "no type", "no moves", 5)
    player_name = input("What is your name? ")
    starter_pokemon = ["Pythagoras", "Franklin", "Euler"]
    # Code that run the program
    if introduction(player_name) == 1:
        pokemon_choose(player_name, starter_pokemon)
        option = mode_selection(player_name)

        clear_screen()
        print("Oh no, an encounter!")

        while P.health > 0 and P_enemy.health > 0:
            encounter(P, P_enemy)
            solve_question(option, P, P_enemy)

        if P.health == 0:
            game_over()
        elif P_enemy.health == 0:
            print("Congrats! You won!")

    else:
        pass


if __name__ == "__main__":
    try:
        clear_screen()
        main()
    except KeyboardInterrupt:
        print("Why have you forsaken me....")


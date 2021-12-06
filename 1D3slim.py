import time, random, os, platform


class Images:
    # put all the ACSII art under this class, call them from here
    chewie = r"""
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
    chewietalk = """
    Professor Chewie: Welcome to Mathematica Island! 
    I am Chewie, a researcher on this island.
    There are 2 Pokemons on the loose:
    Addition and Subtraction.
    Will you help me catch them?
            """
    icecream = r"""
        \________
        /  __  __\
        /   (.) (.)\
        /      (_/\_)\
        ______________
            """

    owl1 = r"""
        /\___/\
        ( =^.^=)
         (")(")_/
            """
    owl2 = r"""
        (\ _ /)
        ( 'X' )
        C(")(")
            """
    owl3 = r"""
         ^---^
        ( 'o' )
        (  uu )
            """


class Typing:  # For text effect and animation
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
                        time.sleep(0.2)
                    else:
                        print(msgtoslowtype[x], end="")  # print without spacing
                        time.sleep(0.01)
                msgtoslowtype = ""
            else:
                msgtoslowtype = (
                    msgtoslowtype + stringtoslowtype[i]
                )  # concatenate string

    def concatimage(self, string1, string2):  # meme
        c = ""
        listmaxlength = []
        listmaxlength2 = []
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
            listmaxlength2.append(len(string2[i]))
        addspace = max(listmaxlength)
        addspace2 = max(listmaxlength2)
        if addspace > addspace2:
            addspace = addspace2
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
        for j in range(len(lists)):
            if j + 1 < len(lists):
                b_lists = list(pixelart[lists[j] : lists[j + 1]])
                for y in range(len(b_lists)):
                    if b_lists[y] == "/":
                        b_lists[y] = "\\"
                    elif b_lists[y] == "\\":
                        b_lists[y] = "/"
                    makethiswork = makethiswork + (b_lists[y])
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


# For Store, Potion and money related stuff
class Currency:
    def __init__(self, money, potion, potioninbag):
        self.money = int(money)
        self.potion = int(potion)
        self.potioninbag = int(potioninbag)

    def pokemart(self):
        if self.potion > 0:
            print(
                f"""
Welcome to the Store,
Its your lucky day, our shipment just arrived so we have plenty in stock.
        
What would you like to buy today?
1. $1000 | Potion (S) | Recovers 1 health bar | In-Stock: {self.potion}
2. Leave        
            """
            )
            print(f"Your current money is: ${self.money} \n")
            ans = input("Option ")
            while not ans.isdigit() or not (1 <= int(ans) <= 2):
                print("Please type [number] and [enter] !")
                ans = input("Option ")
            option = int(ans)
            if option == 1:
                itemprice = 1000
                if self.money < itemprice:
                    print("Sorry, you dont have enough money to buy this.\n")
                    print("Please come another time!\n")
                else:
                    print("\nYou have selected %s" % ans)
                    multiplier = input("How many of it would you like? ")
                    while (not multiplier.isdigit()) or not (
                        1 <= int(multiplier) <= self.potion
                    ):
                        print("Please type [number] and [enter]!")
                        multiplier = input("How many of it would you like? (1 to 5) ")
                    m = int(multiplier)
                    if self.potion >= m:
                        itemprice = m * itemprice
                        print(f"That would be a total of ${itemprice} \n")
                        if self.money < itemprice:
                            print("Sorry, you dont have enough money to buy this.\n")
                            print("Please come another time!\n")
                        else:
                            self.potion -= m
                            self.potioninbag += m
                            print(
                                f"You currently have {self.potioninbag} potions in your bag.\n"
                            )
                            self.money -= itemprice
                            T.slowtype(
                                """\n 
Thank you for shopping with us, 
Hope to see you again! 
                        """
                            )
                            self.checkmoney()
                    else:
                        print(
                            f"Sorry we only have {self.potion} potions in stock right now"
                        )
                        self.pokemart()
            else:
                pass
        else:
            print("\nSorry we ran out of potions!")
            print("Please come another time!\n")

    def gainmoney(self, moneytoadd):
        T.slowtype(f"You have gained: ${moneytoadd} \n")
        self.money += moneytoadd
        self.checkmoney()
        pass

    def checkmoney(self):
        T.slowtype(f"Your current money is: ${self.money} \n")
        pass


# Pokemon class
class Pokemon:
    def __init__(self, name, types, health, attackpoints):
        self.name = name
        self.types = types
        self.attackpoints = attackpoints
        self.health = health

    def attack(self):
        return self.attackpoints

    def damage_taken(self):
        self.health = self.health - self.attackpoints

    def checkdead(self):
        if self.health == 0:
            print("Your pokemon has fainted... ")
            print("Game Over")
        pass


# global variables
T = Typing()
C = Currency(0, 20, 0)
I = Images()
Addition = Pokemon("Addition", "easy", 5, 1)
Subtraction = Pokemon("Subtraction", "easy", 5, 1)
Player = Pokemon("no name", "no type", 5, 1)

pokemon_fights = ["Addition", "Subtraction"]
difficulty_levels = ["Easy", "Medium", "Hard"]
pokemon_fight = None
difficulty = None

main_options = None


def main_menu():
    print(
        """
        Pokemons on the loose:
        [1]: Addition
        [2]: Subtraction

        For your adventures ahead:
        [3]: Pokemart
        --------------------------------------------
        If you want to exit the game, press [4]
        --------------------------------------------
        """
    )

    while True:
        try:
            global main_options
            main_options = int(input("Ready to start your adventure? "))
            if (main_options) == 1 or (main_options) == 2:
                global pokemon_fight
                pokemon_fight = pokemon_fights[main_options - 1]
                print(f"You have choosen {pokemon_fight} as your opponent!")
                break
            elif (main_options) == 3:
                C.pokemart()
                game_play()
                break
            elif (main_options) == 4:
                break
            else:
                print("I don't understand the input")
        except:
            print("I don't understand the input")

    if main_options == 1 or main_options == 2:
        print(
            """
            Difficulty levels:
            [1]: Easy 
            [2]: Medium
            [3]: Hard """
        )
        while True:
            try:
                difficulty_setting = int(input("What is your chosen difficulty?: "))
                global difficulty
                difficulty = difficulty_levels[difficulty_setting - 1]
                if (
                    difficulty_setting == 1
                    or difficulty_setting == 2
                    or difficulty_setting == 3
                ):
                    if difficulty_setting == 1:
                        print(f"You have chosen the {difficulty} level.")
                        break
                    elif difficulty_setting == 2:
                        print(f"You have chosen the {difficulty} level.")
                        break
                    elif difficulty_setting == 3:
                        print(f"You have chosen the {difficulty} level.")
                        break
                    else:
                        print("Choose from Level 1 to 3")
                        break
            except:
                continue
    if main_options == 4:
        end_game()


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


def options():
    while True:
        try:
            action = input(
                "What would you like to do?\n"
                "[1] Attack\n"
                "[2] Potion\n"
                "[3] Quit\n"
            )
            if action == "1":
                break
            elif action == "2":
                if C.potioninbag > 0:
                    if Player.health < 5:
                        Player.health += 1
                        print(f"Health added. Current health: {Player.health}")
                        break
                    else:
                        print("You already have max health!")
                else:
                    print(f"You currently have {C.potioninbag} potions in your bag")
            elif action == "3":
                game_play()
        except:
            print("Invalid input!")
            break
    pass


def solve_question():
    """
    Allows the user to input solution, and checks if user input is correct
    """
    loop1 = Player.health
    if pokemon_fight == "Addition":
        loop2 = Addition.health
    elif pokemon_fight == "Subtraction":
        loop2 = Subtraction.health

    while 0 < loop1 <= 5 and 0 < loop2 <= 5:
        two_numbers = random_generator(0, 1)

        options()

        if pokemon_fight == "Addition":
            start = time.time()
            correct_ans = two_numbers[0] + two_numbers[1]
            ans = input(f"Solve sum of {two_numbers[0]} and {two_numbers[1]}:")
            end = time.time()
            print("It took you", int(end - start), "seconds to attempt this problem!")
        elif pokemon_fight == "Subtraction":
            start = time.time()
            correct_ans = abs(two_numbers[0] - two_numbers[1])
            ans = input(
                f"Solve difference between {two_numbers[0]} and {two_numbers[1]}:"
            )
            end = time.time()
            print("It took you", int(end - start), "seconds to attempt this problem!")
        try:
            if int(ans) == correct_ans:
                if pokemon_fight == "Addition":
                    Addition.damage_taken()
                    # clear_screen()
                    print(
                        "Nice!\n"
                        "You inflicted 1 damage on enemy pokemon\n"
                        f"Enemy pokemon has {Addition.health} health left!\n"
                    )
                    print(f"Your pokemon has {Player.health} health left!")
                    loop2 = loop2 - 1
                elif pokemon_fight == "Subtraction":
                    Subtraction.damage_taken()
                    # clear_screen()
                    print(
                        "Nice!\n"
                        "You inflicted 1 damage on enemy pokemon\n"
                        f"Enemy pokemon has {Subtraction.health} health left!\n"
                    )
                    print(f"Your pokemon has {Player.health} health left!")
                    loop2 = loop2 - 1
            else:
                Player.damage_taken()
                # clear_screen()
                print(
                    "On no!\n"
                    "Your pokemon took 1 damage!\n"
                    f"Your pokemon has {Player.health} health left!\n"
                )
                if pokemon_fight == "Addition":
                    print(f"Enemy pokemon has {Addition.health} health left!")
                elif pokemon_fight == "Subtraction":
                    print(f"Enemy pokemon has {Subtraction.health} health left!")
                loop1 = loop1 - 1

        except ValueError:
            print("Please only type integers!")

    if Addition.health == 0:
        print("Victory. You defeated Addition!")
        if difficulty == "Easy":
            moneytoadd = 1000 * 1
        elif difficulty == "Medium":
            moneytoadd = 1000 * 2
        elif difficulty == "Hard":
            moneytoadd = 1000 * 3
        C.gainmoney(moneytoadd)
        Addition.health = 5
        game_play()
    elif Subtraction.health == 0:
        print("Victory. You defeated Subtraction!")
        if difficulty == "Easy":
            moneytoadd = 1000 * 1
        elif difficulty == "Medium":
            moneytoadd = 1000 * 2
        elif difficulty == "Hard":
            moneytoadd = 1000 * 3
        C.gainmoney(moneytoadd)
        game_play()
        Subtraction.health = 5
    elif Player.health == 0:
        print("Further refine your math skills to defeat this opponent!")
        game_play()


def game_play():
    main_menu()
    solve_question()
    pass


def start_game():
    print("---Gotta Solve Em' All---")
    player_name = input("What is your name? ")
    while (
        player_name == ""
    ):  # Ensure that they enter an input with length of at least 1
        print("Please enter a valid name!")
        player_name = input("What is your name? ")
    print(
        f"""
        Welcome player {player_name}!
        Choose your starter Pokemon!
        [1] Pythagoras
        [2] Franklin
        [3] Euler
        """
    )
    starter_pokemon = ["Pythagoras", "Franklin", "Euler"]
    while True:
        try:
            choose_pokemon = int(input("Your starter pokemon is: "))
            if choose_pokemon == 1 or choose_pokemon == 2 or choose_pokemon == 3:
                chosen_pokemon = starter_pokemon[choose_pokemon - 1]
                Player.name = chosen_pokemon
                print(f"Hooray. {chosen_pokemon} is now your Pokemon!")
                break
            else:
                print("Choose amongst the 3 pokemons provided")
        except:
            print("Choose amongst the 3 pokemons provided")
    time.sleep(1)
    print(
        "------------------------------------------"
    )  # https://www.asciiart.eu/people/faces
    print(T.concatimage(I.chewie, I.chewietalk))
    time.sleep(1)
    N = 0
    while True:
        choice = input("Help the Professor?(Y/N): ")
        if choice == "Y" or choice == "y":
            print("Prof: Thank you so much!\n")
            game_play()
            break
        elif choice == "N" or choice == "n":
            N += 1
            if N == 1:
                print("Come on... Don't you want to help me? :(")
            elif N == 2:
                print("I'll give you bonus marks for M&A assessment later...")
            elif N == 3:
                print("Sigh...No adventures for you then...")
                break
        else:
            print("Wait, what? I don't understand you.")


def end_game():
    print("GAME ENDED")
    os.abort()


start_game()


import time, random, os, platform


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


Addition = Pokemon("Addition", "easy", 5, 1)
Subtraction = Pokemon("Subtraction", "easy", 5, 1)
Player = Pokemon("no name", "no type", 5, 1)

pokemon_fights = ["Addition", "Subtraction"]
difficulty_levels = ["Easy", "Medium", "Hard"]
pokemon_fight = None
difficulty = None


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
            catch = int(input("Which pokemon do you want to catch first? "))
            if catch == 1 or catch == 2:
                global pokemon_fight
                pokemon_fight = pokemon_fights[catch - 1]
                print(f"You have choosen {pokemon_fight} as your opponent!")
                break
            else:
                print("I don't understand the input")
        except:
            continue
    print(
        """
        Difficulty levels:
        [1]: Easy 
        [2]: Medium
        [3]: Hard
        """
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
        except:
            continue
    pass


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
                if Player.health < 5:
                    Player.health += 1
                    print(f"Health added. Current health: {Player.health}")
                    break
                else:
                    print("You already have max health!")
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
        two_numbers = random_generator(0, 1000)

        options()

        if pokemon_fight == "Addition":
            correct_ans = two_numbers[0] + two_numbers[1]
            ans = int(input(f"Solve sum of {two_numbers[0]} and {two_numbers[1]}:"))
        elif pokemon_fight == "Subtraction":
            correct_ans = abs(two_numbers[0] - two_numbers[1])
            ans = int(
                input(f"Solve difference of {two_numbers[0]} and {two_numbers[1]}:")
            )
        try:
            if ans == correct_ans:
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


def game_play():
    main_menu()
    solve_question()
    pass


def start_game():
    print("---Gotta Solve Em' All---")
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
            continue
    time.sleep(1)
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
            game_play()
            break

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


start_game()


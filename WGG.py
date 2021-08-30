import random

def getHint(hWord):
    hint = ""
    while hWord:
        pos = random.randrange(len(hWord))
        hint += hWord[pos]
        hWord = hWord[: pos] + hWord[(pos + 1):]
    return hint

#LIST OF ELEMENTS
wList = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
         "Sodium", "Magnesium","Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
         "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
         "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
         "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium","Indium", "Tin",
         "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
         "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium","Ytterbium",
         "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium","Platinum",
         "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon","Francium", "Radium",
         "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium",
         "Ensteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium",
         "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium","Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]


#STATEMENT
print("\n\t   ! : . Welcome To The WGG : Word Guessing Game . : !")
print("\t         : : : : : Guess Elements Name : : : : :")

#GAME LEVEL
turn = 0
level = 0
v = input("\t\t    *  *  *  Choose Game Mode  *  *  *\n\t\t\t  *  *  *   E   *  *  *\n\t\t\t  *  *  *   M   *  *  * \n\t\t\t  *  *  *   H   *  *  *\n\nSELECT MODE: ")
if (v == "e"):
    print("\n\t\t\t ! : . E A S Y . : !")
    turn = 10
    level = 25
elif (v == "m"):
    print("\n\t\t\t! : . M E D I U M . : !")
    turn = 7
    level = 35
elif (v == "h"):
    print("\n\t\t\t ! : . H A R D . : !")
    turn = 3
    level = 50
else:
    while not v or v != "e" and v != "m" and v != "h":
        print("Wrong Entry")
        v = input("SELECT MODE: ")
        if (v == "e"):
            print("\n\t\t\t ! : . E A S Y . : !")
            turn = 10
            level = 25
            break
        elif (v == "m"):
            print("\n\t\t\t! : . M E D I U M . : !")
            turn = 7
            level = 35
            break
        elif (v == "h"):
            print("\n\t\t\t ! : . H A R D . : !")
            turn = 3
            level = 50
            break



print(f"\n\t\t\tThis is {level} Levels Game\n\t\t\tAnd, You Hava {turn} Lives\n\n")
v=""
guess = ""
count = 0

for i in range(1, level+1):
    word = random.choice(wList)
    word = word.lower()
    hint = "Level - " + str(i) + ":\t" + getHint(word)
    print(hint)
    while(turn > 0):
        guess = input("Your Guess:\t")
        guess = guess.lower()
        if not guess:
            print("Hey! You Can't Ran Off, Guess The Element")
        elif(guess == word):
            count = count + 1
            if (i == level):
                print(f"\n* * * AWESOME * * *\nYou Have Successfully Completed All {count} Levels")
                break
            else:
                print("\nCORRECT\n")
                break
        elif(guess != word):
            turn = turn - 1
            if (turn == 0):
                print(f"\nINCORRECT\n\n\t\t\t    * * * G A M E  O V E R * * *")
                break
            elif(turn != 0):
                print(f"\nINCORRECT\n\n* * * {turn} lives left * * *\n")
                print(hint)

    if(turn == 0):
        print(f"\n\n\t! ! ! : : : * * * The correct Element is: {word.capitalize()} * * * : : : ! ! !\n"
              f"\t     * * * - - - You Finihshed at Level {count} out of {level} - - - * * *")
        break

input("\n\nThanks For Playing!!!\nPress Enter Key For EXIT\t\t\t\t\t\t\t\t\t\t@shaan")

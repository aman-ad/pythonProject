import data
import random

import cv2 as cv
import numpy as np

# The Charaacter Model
class Character:
    strength = 10
    dexterity = 10
    constitution = 10
    intelligence = 10
    wisdom = 10
    charisma = 10

    race = "Human"
    c_class = "Fighter"
    firstname = "Jack"
    lastname = "Petty"
    weapon = ["Dagger"]
    armor = ["Cloth shirt"]
    skills = ["Insight"]
    abilities = ["Rage"]
    spells = ["None"]
    hp = 1
    gold = 0
    background = "outlander"
    saving_throws = []
    racial_traits = []

    age = 20
    size = "Large"

    languages = ["Common"]
    haircolor = "brown"
    hairtype = "Wavy"
    eyecolor = "brown"

    appearance = []
    traits = []
    mannerisms = []
    talents = []

    def __str__(self):
        return "A {} {} named {}.".format(self.race, self.c_class, self.firstname)


def RandStat():
    dice = []

    for i in range(4):
        dice.append(random.randrange(1,7))

    total = 0
    lowest = dice[0]

    # find the lowest value
    for num in dice:
        if num < lowest:
            lowest = num

    for num in dice:
        total += num

    return total - lowest

# The main part of our program.
def CreateNewCharacter():
    new_character = Character()

    races = []
    classes = []

    for race in data.races:
        races.append(race)

    for _class in data.classes:
        classes.append(_class)

    new_character.race = races[random.randrange(0,len(races))]
    new_character.c_class = classes[random.randrange(0,len(classes))]

    firstnames = []
    lastnames = []
    if new_character.race == 'Human':
        types = []

        for type in data.races['Human']['first names']:
            types.append(type)

        type = types[random.randrange(0,len(types))]

        for name in data.races[new_character.race]['first names'][type]:
            firstnames.append(name)

        for name in data.races[new_character.race]['last names'][type]:
            lastnames.append(name)

    elif new_character.race == "Half-Elf":
        types = []

        for type in data.races['Human']['first names']:
            types.append(type)

        type = types[random.randrange(0,len(types))]

        for name in data.races['Human']['first names'][type]:
            firstnames.append(name)

        for name in data.races['Elf']['first names']:
            firstnames.append(name)

        for name in data.races['Human']['last names'][type]:
            lastnames.append(name)

        for name in data.races['Elf']['last names']:
            lastnames.append(name)

    else:
        for name in data.races[new_character.race]['first names']:
            firstnames.append(name)

        if new_character.race == "Half-Orc":
            pass
        else:
            for name in data.races[new_character.race]['last names']:
                lastnames.append(name)

    new_character.firstname = firstnames[random.randrange(0,len(firstnames))]

    if new_character.race != "Half-Orc":
        new_character.lastname = lastnames[random.randrange(0,len(lastnames))]

    # roll the character stats
    new_character.strength = RandStat()
    new_character.dexterity = RandStat()
    new_character.constitution = RandStat()
    new_character.intelligence = RandStat()
    new_character.wisdom = RandStat()
    new_character.charisma = RandStat()

    weapons = []
    armors = []

    for weapon in data.classes[new_character.c_class]['weapons']:
        weapons.append(weapon)

    new_character.weapon = weapons[random.randrange(0,len(weapons))]

    for armor in data.classes[new_character.c_class]['armor']:
        armors.append(armor)

    new_character.armor = armors[random.randrange(0,len(armors))]

    new_character.skills = data.classes[new_character.c_class]['skills']

    if 'spells' in data.classes[new_character.c_class]:
        new_character.spells =  data.classes[new_character.c_class]['spells']

    new_character.abilities =  data.classes[new_character.c_class]['abilities']
    new_character.background = data.classes[new_character.c_class]['background']
    new_character.languages = ["Common"]
    new_character.languages += data.races[new_character.race]['languages']
    new_character.racial_traits = data.races[new_character.race]['traits']

    mannerisms = []
    for mannerism in data.mannerisms:
        mannerisms.append(mannerism)
    new_character.mannerisms = mannerisms[random.randrange(0,len(mannerisms))]

    traits = []
    for trait in data.traits:
        traits.append(trait)
    new_character.traits = traits[random.randrange(0,len(traits))]

    talents = []
    for talent in data.talents:
        talents.append(talent)
    new_character.talent = talents[random.randrange(0,len(talents))]

    appearances = []
    for appearance in data.appearance:
        appearances.append(appearance)
    new_character.appearance = appearances[random.randrange(0,len(appearances))]


    # There are some minor differences in how we'll present the data, depending
    # on the race involved. For instance, "An Elf" vs "A Human."
    if new_character.race == "Half-Orc":
        print("A {} {} named {}.".format(new_character.race, new_character.c_class, new_character.firstname))
    elif new_character.race == "Elf":
        print("An {} {} named {} {}.".format(new_character.race, new_character.c_class, new_character.firstname, new_character.lastname))
    else:
        print("A {} {} named {} {}.".format(new_character.race, new_character.c_class, new_character.firstname, new_character.lastname))

    print("Strength: {} Dexterity: {} Constitution: {} Intelligence: {} Wisdom: {} Charisma: {}".format(
        new_character.strength, new_character.dexterity,new_character.constitution,
        new_character.intelligence, new_character.wisdom, new_character.charisma))

    print("Background: " + new_character.background + ", Languages: " + str(new_character.languages))
    print("\nWeapon: " + new_character.weapon + ", Armor: " + new_character.armor)
    print("Skills: " + str(new_character.skills))
    print("Abilities: " + str(new_character.abilities))
    print("Spells: " + str(new_character.spells))
    print("Traits: " + str(new_character.racial_traits))

    print("\nMannerisms: " + str(new_character.mannerisms))
    print("Personality Traits: " + str(new_character.traits))
    print("Talents: " + str(new_character.talent))
    print("Appearance: " + str(new_character.appearance))
    print("\n")

def cartoon(name):
    image_loc=name+".png"
    img = cv.imread(image_loc)

    # Edges
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                   cv.THRESH_BINARY, 9, 9)

    # Cartoonization
    color = cv.bilateralFilter(img, 9, 250, 250)
    cartoon = cv.bitwise_and(color, color, mask=edges)

    # cv.imshow("Image", img)
    # cv.imshow("edges", edges)
    cv.imshow("Cartoon", cartoon)
    cv.waitKey(0)
    cv.destroyAllWindows()


# This is the entry point for the program
print("Welcome to the Random Character Generator.")

new_input = ""
characters=["Chris", "Kevin", "Gabor", "Per"]
for emp in characters:
    new_input = input("Create a new character for "+ emp+"?: ")


    new_input = new_input.lower()
    if new_input == "yes" or new_input == "y":
            print("Ok, let's make a character!\n")
            print("===============================================================")
            CreateNewCharacter()
            cartoon(emp)
    elif new_input == "no" or new_input == "n" or new_input == "quit":
            new_input = "quit"
            print("ok!")


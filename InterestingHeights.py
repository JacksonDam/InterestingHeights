import random

interest = {
    'Eiffel Tower': 1063,
    'Statue of Liberty': 305,
    'Empire State Building': 1250,
    'Burj Khalifa': 2717,
    'One World Trade Center': 1776,
    'CN Tower': 1815,
    'Golden Gate Bridge': 227,
    'Sydney Opera House': 167,
    'Big Ben': 316,
    'Taj Mahal': 73,
    'Leaning Tower of Pisa': 55,
    'Great Pyramid of Giza': 481,
    'London Eye': 135,
    'Arc de Triomphe': 50,
    'Space Needle': 605,
    'Mount Everest': 29029,
    'Mount Kilimanjaro': 19341,
    'Mount Fuji': 12388,
    'Mount McKinley': 20310,
    'Mount Rainier': 14411,
    'Mount Elbrus': 18510,
    'K2': 28251,
    'Mount Whitney': 14505,
    'Angel Falls': 3212,
    'Niagara Falls': 167,
    'Victoria Falls': 354,
    'Horseshoe Falls': 176,
    'Yosemite Falls': 2425,
    'Petronas Towers': 1483,
    'Shanghai Tower': 2073,
    'Taipei 101': 1667,
    'International Space Station': 357,
    'St. Basil’s Cathedral': 78,
    'an Ant': 0.0025,
    'a Grain of Sand': 0.00001,
    'a Dust particle': 0.0000001,
    'a Virus': 0.000000001,
    'a Bacteria': 0.0000002,
    'a Paramecium': 0.00005,
    'an Amoeba': 0.0003,
    'a Red Blood Cell': 0.000004,
    'a White Blood Cell': 0.000012,
    'a Mite': 0.00002,
    'a Mosquito': 0.0004,
    'a Flea': 0.00003,
    'a Housefly': 0.0001,
    'a Butterfly': 0.0004,
    'a Fruit Fly': 0.00003,
    'a Tick': 0.00004,
    'a Termite': 0.00004,
    'a Spider': 0.00002,
    'an Earthworm': 0.00005
}

def add_suffix(fraction):
    numerator, denominator = fraction.split('/')
    if int(denominator) % 10 == 1:
        suffix = 'st'
    elif int(denominator) % 10 == 2:
        suffix = 'nd'
    elif int(denominator) % 10 == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    return numerator + '/' + denominator + suffix

try:
    user_input = float(input("pls give me an height yes \n"))
except:
    print("Invalid input")
    exit()

random_choice = random.choice(list(interest.keys()))
random_height = interest[random_choice]

quot = "{:.1f}".format((user_input / random_height) * 100) + "%"
output = "DID YOU KNOW THAT " + str(user_input) + " FT " + "IS " + str(quot) + " THE HEIGHT OF"
if not "Mount" in random_choice and random_choice[0] != "a":
    output += " THE "
else:
    output += " "
print(output + random_choice.upper() + ". WOW!")
print("NEED SLEEP PLEASE HELP OK")

import random
from data import *

race_list = data["races"]
class_list = ['Bard', 'Mage', 'Merchant', 'Paladin', 'Ranger', 'Rogue', 'Warrior', 'Warlock']

random_race = choose_race()
race_name = random_race['name']
if race_name == 'Cursed':
  race_name = race_name + " " + random.choice(random_race)
first_letter = race_name[0:1].lower()
your_class = random.choice(class_list)

output_string = "You are "
if first_letter in ['a', 'e', 'i', 'o', 'u']:
  output_string = output_string + 'an'
else:
  output_string = output_string + 'a'

print (output_string, race_name, your_class)
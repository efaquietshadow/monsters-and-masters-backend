import random
from data import *

race_list = data["races"]
class_list = data["classes"]

random_race = choose_race()
race_name = random_race['name']
race_health = random_race['base-health']
base_skills = random_race["base-skills"]

is_cursed = random.randrange(1,18) == 1
if is_cursed:
  race_name = "Cursed " + race_name


first_letter = race_name[0:1].lower()

output_string = "You are "
if first_letter in ['a', 'e', 'i', 'o', 'u']:
  output_string = output_string + 'an'
else:
  output_string = output_string + 'a'

random_class = choose_class()
class_name = random_class["name"]


print (output_string, race_name, class_name)
if is_cursed:
  cursed_percent = random.randrange(1,100)
  print("your curse is at", cursed_percent, "%")
print ("base health:", race_health, "\nbase skills:", base_skills)
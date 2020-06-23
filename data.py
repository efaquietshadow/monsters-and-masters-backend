import random

data = {
    "races": {
        "centaur": {
            "name": "Centaur"
        },
        "cursed": {
            "name": "Cursed"
        },
        "dragonkin": {
            "name": "Dragonkin"
        },
        "dwarf": {
            "name": "Dwarf"
        },
        "elemental": {
            "name": "Elemental"
        },
        "elf": {
            "name": "Elf"
        },
        "fae": {
            "name": "Elf"
        },
        "giant": {
            "name": "Giant"
        },
        "goblin": {
            "name": "Goblin"
        },
        "hafling": {
            "name": "Hafling"
        },
        "human": {
            "name": "Human"
        },
        "ignisaka": {
            "name": "Ignisaka"
        },
        "oliforon": {
            "name": "Oliforon"
        },
        "shapeshifter": {
            "name": "Shapeshifter"
        },
        "siren": {
            "name": "Siren"
        },
        "taur": {
            "name": "Taur"
        },
        "vampire": {
            "name": "Vampire"
        },
        "zombie": {
            "name": "Zombie"
        }
    }
}



def choose_race():
    return data["races"][random.choice(list(data["races"].keys()))]
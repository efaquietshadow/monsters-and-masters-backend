import random

data = {
    "races": {
        "dragonkin": {
            "name": "Dragonkin",
            "base-health": 30,
              "base-skills": {
                "str": 2,
                "con": 1,
                "spe": 2,
                "ste": 0,
                "dex": 1,
                "int": 1,
                "cha": 0
            }
        },
        "dwarf": {
            "name": "Dwarf",
            "base-health": 34,
            "base-skills": {
                "str": 3,
                "con": 3,
                "spe": 0,
                "ste": 0,
                "dex": 0,
                "int": 0,
                "cha": 1
            }
        },
        "elemental": {
            "name": "Elemental",
            "base-health": 27,
            "sub-race": ["water", "earth", "air", "fire", "dark", "light"],
            "base-skills": {
                "str": 1,
                "con": 1,
                "spe": 1,
                "ste": 1,
                "dex": 1,
                "int": 1,
                "cha": 1
            }
        },
        "elf": {
            "name": "Elf",
            "base-health": 27,
            "base-skills": {
                "str": 1,
                "con": 1,
                "spe": 1,
                "ste": 0,
                "dex": 1,
                "int": 1,
                "cha": 2
            }
        },
        "fae": {
            "name": "Fae",
            "base-health": 21,
            "base-skills": {
                "str": -2,
                "con": 0,
                "spe": 3,
                "ste": 0,
                "dex": 1,
                "int": 1,
                "cha": 3
            }
        },
        "giant": {
            "name": "Giant",
            "base-health": 42,
            "base-skills": {
                "str": 5,
                "con": 3,
                "spe": 0,
                "ste": 0,
                "dex": -1,
                "int": -1,
                "cha": 1
            }
        },
        "goblin": {
            "name": "Goblin",
            "base-health": 21,
            "base-skills": {
                "str": 0,
                "con": 0,
                "spe": 2,
                "ste": 1,
                "dex": 2,
                "int": 1,
                "cha": 1
            }
        },
        "half-ling": {
            "name": "Half-ling",
            "base-health": 25,
            "base-skills": {
                "str": 0,
                "con": 1,
                "spe": 1,
                "ste": 2,
                "dex": 2,
                "int": 1,
                "cha": 0
            }
        },
        "human": {
            "name": "Human",
            "base-health": 30,
            # make randomized base skills == 7
            "base-skills": {
                "str": 1,
                "con": 1,
                "spe": 1,
                "ste": 1,
                "dex": 1,
                "int": 1,
                "cha": 1
            }
        },
        "ignisaka": {
            "name": "Ignisaka",
            "base-health": 30,
            "base-skills": {
                "str": 2,
                "con": 1,
                "spe": 1,
                "ste": 0,
                "dex": 2,
                "int": 0,
                "cha": 1
            }
        },
        "oliforon": {
            "name": "Oliforon",
            "base-health": 30,
            # add can modify with base animal
            "base-skills": {
                "str": 2,
                "con": 1,
                "spe": 2,
                "ste": 1,
                "dex": 1,
                "int": 0,
                "cha": 0
            }
        },
        "shapeshifter": {
            "name": "Shapeshifter",
            "base-health": 26,
            "base-skills": {
                "str": 0,
                "con": 1,
                "spe": 0,
                "ste": 3,
                "dex": 1,
                "int": 1,
                "cha": 1
            }
        },
        "siren": {
            "name": "Siren",
            "base-health": 28,
            "base-skills": {
                "str": 0,
                "con": 1,
                "spe": 1,
                "ste": 1,
                "dex": 1,
                "int": 1,
                "cha": 2
            }
        },
        "taur": {
            "name": "Taur",
            "base-health": 29,
            "base-skills": {
                "str": 2,
                "con": 1,
                "spe": 1,
                "ste": 0,
                "dex": 1,
                "int": 1,
                "cha": 1
            }
        },
        "vampire": {
            "name": "Vampire",
            "base-health": 32,
            "base-skills": {
                "str": [1, 2],
                "con": 1,
                "spe": [1, 2],
                "ste": 2,
                "dex": 1,
                "int": 0,
                "cha": 0
            }
        },
        "zombie": {
            "name": "Zombie",
            "base-health": 32,
            "base-skills": {
                "str": 1,
                "con": 4,
                "spe": 0,
                "ste": 0,
                "dex": 1,
                "int": -1,
                "cha": -2
            }
        }
    },
    "classes": {
        "bard": {
            "name": "Bard"
        },
        "mage": {
            "name": "Mage"
        },
        "merchant": {
            "name": "Merchant"
        },
        "paladin": {
            "name": "Paladin"
        },
        "ranger": {
            "name": "Ranger"
        },
        "rogue": {
            "name": "Rogue"
        },
        "warrior": {
            "name": "Warrior"
        },
        "warlock": {
            "name": "Warlock"
        }
    }
}



def choose_race():
    return data["races"][random.choice(list(data["races"].keys()))]

def choose_class():
    return data["classes"][random.choice(list(data["classes"].keys()))]
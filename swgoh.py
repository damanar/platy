#defines Guild data
#contains a list of Players
#contains methods to add and retrieve Player information
class Guild:
#initialize with Guild name and Galactic Power, we do
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.players = list()
    
#call constructor for Player, we will
    def add_player(self, name, level):
        p = Player( name, level )
#add player to list, we will
        self.players.append(p)
        return p

#return a Player of Guild by name
    def get_player(self, name):
        p = {}
        for player in self.players:
            if player.name == name:
                p = player
        return p

#determine if a player is assigned in the Guild
    def exists_player(self, name):
        exists = False
        for player in self.players:
            #print(player.get_name())
            if name == player.name:
                exists = True
        return exists

#return guild roster for a specific character
    def get_roster(self, name, territory):
        c_roster = list()
        for player in self.players:
#need to move territory check out of basic guild functionality to make Guild class more parsimonious; it should be a function of platy
            if player.get_assignment( territory ) < 10:
                for character in player.characters:
                    if character.get_name() == name:
#need to move availability check to platy to make Guild class more partimonious; it should be a function of platy
                        if character.is_available():
                            #add Character of Player to return list. Including references to both Player and Character obj for manipulation as well as flat data for sorting
                            c_roster.append( {'character': character.get_name(),
                                    'player': player.name,
                                    'star': character.star,
                                    'level': character.level,
                                    'gear': character.gear,
                                    'power': character.power,
                                    'char_obj': character,
                                    'player_obj': player
                                })
        return c_roster

#defines player data
#contains flat data as well as a list of Characters
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
#array to define what territories this player has assigned characters to
        self.assignments = [0,0,0]#0 for ships, 1 for territory 1, 2 for territory 2
        self.characters = list()

#return number of characters assigned to given territory
    def get_assignment(self, territory):
        return self.assignments[territory]

#check for an existing Character assigned to Player
    def exists_character(self, name):
        exists = False
        for character in self.characters:
            #print(character.get_name())
            if character.name == name:
                exists = True
        return exists

#return list of assigned Characters
    def get_characters(self):
        return self.characters

#return Character by name
    def get_character(self, name):
        c = {}
        for character in self.characters:
            if character['name'] == name:
                c = character
        return c

#increment Characters assigned to given territory
    def assign_territory(self, territory):
        self.assignments[territory] += 1

#add a character to Player roster, calls Character constructor
    def add_character( self, name, star, level, gear, power ):
        c = Character( name, star, level, gear, power )
#add Character to Player list
        self.characters.append(c)
        return c
        
#Obj to hold Character data, contains flat data with getters and setters
class Character:
    def __init__( self, name, star, level, gear, power ):
        self.name = name
        self.star = star
        self.level = level
        self.gear = gear
        self.power = power
        self.available = True
        self.assigned = ''

#return Character name
    def get_name(self):
        return self.name

#return Character star
    def get_star(self):
        return self.star

#return Character level
    def get_level(self):
        return self.level

#return Character gear level
    def get_gear(self):
        return self.gear

#return Character power
    def get_power(self):
        return self.power
    
#return where this Character is assigned, for output, this is a string "territory # - platoon #
    def get_assigned(self):
        return self.assigned

#is this Character available for assignment
    def is_available(self):
        return self.available

#assign this character to a territory->platoon
    def assign(self, territory, platoon):
        self.available = False
        self.assigned = territory + ' - ' + platoon

#return Character as a dict
    def get_as_dict(self):
        return {    'name': self.name,
                    'star': self.star,
                    'level': self.level,
                    'gear': self.gear,
                    'power': self.power
                }

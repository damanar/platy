#defines Guild data
#contains a list of Players
#contains methods to add and retrieve Player information
class Guild:
#initialize with Guild name and Galactic Power, we do
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.players = []
        self.characters = dict()
        self.ships = dict()
    
#call constructor for Player, we will
    def add_player(self, name, level):
        p = Player( self, name, level )
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

#return a Player of Guild by name
    def get_character(self, name):
        c = {}
        for character in self.players:
            if player.name == name:
                p = player
        return p

#determine if a player is assigned in the Guild
    def exists_player(self, name):
        exists = False
        for player in self.players:
            if name == player.name:
                exists = True
        return exists

#defines player data
#contains flat data as well as a list of Characters
class Player:
    def __init__(self, guild, name, level):
        self.guild = guild
        self.name = name
        self.level = level
#array to define what territories this player has assigned characters to
        self.assignments = [0,0,0]#0 for ships, 1 for territory 1(middle), 2 for territory 2(bottom)
        self.characters = []

#return number of characters assigned to given territory
    def get_assignment(self, territory):
        return self.assignments[territory]

#check for an existing Character assigned to Player
    def exists_character(self, name):
        exists = False
        for character in self.characters:
            if character.name == name:
                exists = True
        return exists

#increment Characters assigned to given territory
    def assign_territory(self, territory):
        self.assignments[territory] += 1

#add a character to Player roster, calls Character constructor
    def add_character( self, name, star, level, gear, power ):
        c = Character( self, name, star, level, gear, power )
#add Character to Player list
        self.characters.append(c)
        if name not in self.guild.characters:
            self.guild.characters[name] = []
        self.guild.characters[name].append(c)
        return c
        
#Obj to hold Character data, contains flat data with getters and setters
class Character:
    def __init__( self, player, name, star, level, gear, power ):
        self.player = player
        self.name = name
        self.star = star
        self.level = level
        self.gear = gear
        self.power = power
        self.available = True
        self.assigned = ''

#assign this character to a territory->platoon
    def assign(self, territory, platoon):
        self.available = False
        self.assigned = territory + ' - ' + platoon

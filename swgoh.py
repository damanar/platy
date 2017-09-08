#defines guild data
class Guild:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.players = list()
    
    def add_player(self, name, level):
        p = Player( name, level )
        self.players.append(p)
        return p

    def get_players(self):
        return self.players

    def get_player(self, name):
        p = {}
        for player in self.players:
            if player.get_name() == name:
                p = player
        return p

    def exists_player(self, name):
        exists = False
        for player in self.players:
            #print(player.get_name())
            if name == player.get_name():
                exists = True
        return exists

    def get_roster(self, name, territory):
        c_roster = list()
        for player in self.players:
            if player.get_assignment( territory ) <= 10:
                for character in player.characters:
                    if character.get_name() == name:
                        if character.is_available():
                            c_roster.append( {'character': character.get_name(),
                                    'player': player.get_name(),
                                    'star': character.get_star(),
                                    'level': character.get_level(),
                                    'gear': character.get_gear(),
                                    'power': character.get_power(),
                                    'char_obj': character,
                                    'player_obj': player
                                })
        return c_roster

#defines player data
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.assignments = [0,0,0]#0 for ships, 1 for territory 1, 2 for territory 2
        self.characters = list()

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_assignment(self, territory):
        return self.assignments[territory]

    def exists_character(self, name):
        exists = False
        for character in self.characters:
            #print(character.get_name())
            if character.get_name() == name:
                exists = True
        return exists

    def get_characters(self):
        return self.characters

    def get_character(self, name):
        c = {}
        for character in self.characters:
            if character['name'] == name:
                c = character
        return c

    def assign_territory(self, territory):
        self.assignments[territory] += 1

    def add_character( self, name, star, level, gear, power ):
        c = Character( name, star, level, gear, power )
        self.characters.append(c)
        return c
        
class Character:
    def __init__( self, name, star, level, gear, power ):
        self.name = name
        self.star = star
        self.level = level
        self.gear = gear
        self.power = power
        self.available = True
        self.assigned = ''

    def get_name(self):
        return self.name

    def get_star(self):
        return self.star

    def get_level(self):
        return self.level

    def get_gear(self):
        return self.gear

    def get_power(self):
        return self.power
    
    def get_assigned(self):
        return self.assigned

    def is_available(self):
        return self.available

    def assign(self, territory, platoon):
        self.available = False
        self.assigned = territory + ' - ' + platoon

    def get_as_dict(self):
        return {    'name': self.name,
                    'star': self.star,
                    'level': self.level,
                    'gear': self.gear,
                    'power': self.power
                }

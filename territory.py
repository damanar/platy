#defines a platoon, should contain 15 characters, but there is currently no validation on this
class Platoon:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def get_characters(self):
        return self.characters

    def get_char(self, iterant):
        return self.characters[iterant]
    
    def print_me(self):
        stringy = ''
        for char in self.characters:
            stringy += "\t" + char
        print( stringy )

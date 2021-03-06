##Script to automate platoon assignments based on guild members' rosters
##Requires csv input, for now, so as not to burden swgoh.gg

import sys
import csv
from swgoh import Guild
from swgoh import Player
from swgoh import Character
from territory import Platoon

roster_file = 'guild_list.csv'#requires "Player Name, Star Rating, Character Name, Character Level, Gear Level, Guild Name"
platoon_file = 'platoon_list.csv'#requires "Character Name, Character Name, ..." 15 per row/platoon; 6 rows per territory, no separation between territories. The script will automatically count the first 6 rows as territory 1 and 7 -12 as territory 2
#roster_list = []#no longer used
platoon_list = []#holding our platoon classes, 6 for P1, 12 for P2+
territory_list = []#holding our platoon classes, 6 for P1, 12 for P2+
max_assign = 10#Maximum number of characters a player can assign to a territory
unavailable_player = Player( {}, "Unavailable", 0 )
unavailable = Character( unavailable_player, "Unavailable", 0, 0, 0, 0 )

#basically just a group of constants to provide star requirements when provided with phase number defined by p1, p2...
class Requirements:
    def __init__(self):
        self.stars = { 'p1': 2, 'p2': 3, 'p3': 4, 'p4': 5, 'p5': 6, 'p6': 7 }

phase = sys.argv.pop(1)#grab phase argument
g = Guild('My Guild', 0)#Class to store Guild character roster, guild name is dummy data since it is unused
r = Requirements()#set of constants based on star rating

with open(platoon_file, 'rU') as csvfile:
#Parsing platoon_list.csv, grabbing characters and adding them to a new platoon class
    rows = csv.reader( csvfile )
    for row in rows:
        p = Platoon()
        for cell in row:
            p.add_character( cell )

        platoon_list.append( p )#add our platoon obj to our growing list

with open(roster_file, 'rU') as csvfile:
#Parsing guild_list.csv to build our Character and Player objs and add them to our Guild obj
    #rows = csv.DictReader( csvfile, fieldnames=['player', 'plevel', 'char', 'power', 'star', 'level', 'gear'] )#pulling in as a dict for readability
    rows = csv.DictReader( csvfile )#pulling in as a dict for readability
    for row in rows:
        p = {}#Holder for Player obj
        c = {}#Holder for Character obj
        if int(row['plevel']) >= 65:
            p = g.add_player( row['player'], row['plevel'] )#creates our Player obj under our Guild obj
        else:
            continue

        if int(row['star']) >= r.stars[phase]:#we only want to add characters that meet our star requirement for the phase
            p = g.get_player(row['player'])
            p.add_character( row['char'], int(row['star']), row['level'], row['gear'], row['power'] )#create our Character obj under our Player

######################## OUTPUT ########################
######################## OUTPUT ########################
######################## OUTPUT ########################

territory = 1#territory counter, will increment every 6 platoons
i = 1#platoon counter, will increment with each platoon

for platoon in platoon_list:
    print( "territory ", territory, " :: ", "platoon ", i, "-" )#platoon header
    #platoon.print_me()
    for char in platoon.characters:
        s_char = unavailable#placeholder for the character we want
        if char not in g.characters:
            print("\t", char, "\tUnavailable")
            continue

        clist = g.characters[ char ]
        #Trying to sort for the least power character in the guild that meets the requirements; will sort on power when we add them to the guild_list.csv
        c_sorted = sorted( clist, key=lambda k: k.power )
        #c_sorted = sorted( clist, key=lambda k: (k.star,k.gear,k.level) )
        for c in c_sorted:
            #print( c.name, "\t", c.player.name, "\t", c.star )
            if c.available:
                #print( "Assigning: ", c.name, ", ", c.player.name, ", ", c.power, sep="" )
                s_char = c
                c.available = False
                break

#increment player's assignment to the current territory, each player can only assign 10 characters to each territory
        if s_char.name != "Unavailable":
            s_char.player.assign_territory( territory )
#remove Player->Character from the available roster and assign it to the platoon. Probably should make Territory class for better OO
            s_char.assign("territory " + str(territory), "platoon " + str(i))

#print this character assignment
        print( "\t", char, "\t", s_char.player.name )

#incrementations
    i += 1
    if i > 6:#after 6 platoons move to the next territory
        territory += 1
        i = 1

print('*****************************************************')
#alternate output by player instead of by platoon, does not display Unattainable platoons. Future: add unattainable platoons at the end.
p_sorted = sorted( g.players, key=lambda k: (k.name) )
for player in p_sorted:
    for char in player.characters:
        if char.available is not True:
            print( player.name, "\t", char.assigned, "\t", char.name )

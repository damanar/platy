# platy
Quick and dirty python script to assign platoons in Territory Battles for Star Wars: Galaxy of Heroes

Currently using csv files for input as swgoh is having bandwidth issues and I don't want to overburden them with yet another tool scraping their site.

Example csv files included in the repo, but guild_list.csv should be setup like:
Player Name, Character Star level, Character Name, Character Level, Character Guild Level, Guild Name

These will change in the future as I intend to pull Character Power and Prioritize based on that stat.

platoon_list.csv should just be a list of each character with one platoon per line. Names of characters must match the character names in guild_list.csv

I will make all of this more user friendly in the future, but just getting what I can out there if others would like to leverage.

## Usage
Python version 3.6 is required and I have only tested on mac Sierra.

`python3 platy p1`

"p1" stands for phase 1 and sets the star requirement for the platoon assignments.

Currently the script outputs in 2 formats, sequentially, by platoon and then by player:

### platoon:
platoon  5 -
	 Cassian Andor ::  Kaiphooon shu
	 Garazeb &quot;Zeb&quot; Orrelios ::  JoshBFZ
	 Bistan ::  JoshBFZ
	 Bodhi Rook :: UNAVAILABLE
	 K-2SO ::  LyonHart
	 Cassian Andor ::  Peanut Butter
	 Pao :: UNAVAILABLE
	 Stormtrooper Han ::  Yamz
	 Hera Syndulla ::  JoshBFZ
	 Ezra Bridger ::  Daddy Dunc
	 Jyn Erso ::  Pandatron
	 Pao :: UNAVAILABLE
	 K-2SO ::  Bayne
	 Cassian Andor ::  Silverkakari
	 Bodhi Rook :: UNAVAILABLE

### player:
damanar :: territory 1 - platoon 1 :: Jawa
damanar :: territory 1 - platoon 6 :: Clone Sergeant - Phase I
DrAdamBomb :: territory 1 - platoon 6 :: Plo Koon
DrAdamBomb :: territory 1 - platoon 3 :: CT-5555 &quot;Fives&quot;
Studley Curmudgeon :: territory 1 - platoon 2 :: Baze Malbus
Studley Curmudgeon :: territory 1 - platoon 3 :: Jawa Scavenger

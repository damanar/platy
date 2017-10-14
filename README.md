# platy
Quick and dirty python script to assign platoons in Territory Battles for Star Wars: Galaxy of Heroes

Currently using csv files for input as swgoh is having bandwidth issues and I don't want to overburden them with yet another tool scraping their site.

## Example csv files included in the repo:
__guild_list.csv__:
player,plevel,char,power

These can be in any order but must be named correctly.

__platoon_list.csv__ should just be a list of each character with one platoon per line. Names of characters must match the character names in guild_list.csv. No separation between territories. Phase 1 should have 6 rows, Phase 2-6  should have 12

I will make all of this more user friendly in the future, but just getting what I can out there if others would like to leverage.

## Usage
Python version 3.6 is required and I have only tested on mac Sierra.

`python3 platy p1`

"p1" stands for phase 1 and sets the star requirement for the platoon assignments.

Currently the script outputs in 2 formats, sequentially, by platoon and then by player:

### platoon:
territory  1  ::  platoon  1 -

	 eeth-koth 	 Tazi

	 obi-wan-kenobi-old-ben 	 Bayne

	 stormtrooper-han 	 Peanut butter

	 garazeb-zeb-orrelios 	 kaiphoon shu

	 ugnaught 	 Delmon Ciiid'r

	 clone-sergeant-phase-i 	 PhunbKul

	 jawa-engineer 	 inyouendoh

	 kit-fisto 	 Skillinge

	 plo-koon 	 Peanut butter

	 mace-windu 	 TempleJax

	 finn 	 Vader000007

	 luke-skywalker-farmboy 	 Mor'du

	 lando-calrissian 	 AzureMatterSnake 11am est

	 jedi-consular 	 PandaTron3000

	 sabine-wren 	 Gerry Ferry

### player:
Ace 	 territory 1 - platoon 4 	 wedge-antilles

Ace 	 territory 1 - platoon 2 	 luke-skywalker-farmboy

Ace 	 territory 2 - platoon 3 	 princess-leia

AzureMatterSnake 11am est 	 territory 2 - platoon 5 	 kanan-jarrus

AzureMatterSnake 11am est 	 territory 2 - platoon 4 	 sabine-wren

AzureMatterSnake 11am est 	 territory 1 - platoon 2 	 biggs-darklighter

AzureMatterSnake 11am est 	 territory 1 - platoon 1 	 lando-calrissian

AzureMatterSnake 11am est 	 territory 2 - platoon 6 	 jedi-knight-anakin

AzureMatterSnake 11am est 	 territory 2 - platoon 1 	 clone-wars-chewbacca

AzureMatterSnake 11am est 	 territory 1 - platoon 5 	 stormtrooper-han

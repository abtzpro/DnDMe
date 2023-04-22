
DnDMe is an attempt to create a means to play D&amp;D with a party of players. DnDMe is mostly python based.


With the "Map-Maker", you can take any birds-eye top down bitmap image of an island, etc, and convert it into a D&D map sized appropriately for a D&D map.

With the "charactermaker", you can create your own D&D character and stats will be distributed according to the class etc chosen, keeping within the scope of your chosen class. Your stats and character are then saved as binary and accessed later with the python pickle module.

"Grid-Maker" loads the image output from the "Map-Maker" script and creates a new image with a white background that is slightly larger than the original image to accommodate the grid. It then pastes the original image onto the new image, and uses the Pillow library to draw the grid lines, letters, and numbers. (This grid will be your way of tracking where your player character is on the map) Finally, it saves the new image with the grid as a separate file.

"Dice.py" gives a user a full set of DnD dice and allows a user the ability to choose which dice to roll, and how many. Then prints the results and the total. 

"NPC.py" In this script, the NPC class is defined, which takes in various attributes such as name, level, stats, armor class, hit points, and damage. The attack method is also defined, which allows an NPC to attack a target, rolling a hit roll and damage roll, and subtracting the target's hit points based on the damage roll if the hit roll is successful.

"Multiplayer.py" Allows users the ability to play DnDMe in a multiplayer manner. 

"RandomEncounter.py" script defines two lists - one for events and one for encounter types - and three functions. The first function randomly selects an event from the events list, the second function randomly selects an encounter type from the encounter_types list, and the third function generates a random encounter based on the chosen encounter type. Finally, the script tests the functions by printing out a random event and encounter. You can modify the script to include more events and encounter types, or to generate more complex encounters based on the chosen encounter type.

DnDMe is Developed by abtzpro, Adam R, and Hello Security


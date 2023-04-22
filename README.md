
DnDMe is an attempt to create a means to play D&amp;D with a party of players. DnDMe is mostly python based.


With the "Map-Maker", you can take any birds-eye top down bitmap image of an island, etc, and convert it into a D&D map sized appropriately for a D&D map.

With the "charactermaker", you can create your own D&D character and stats will be distributed according to the class etc chosen, keeping within the scope of your chosen class.

"Grid-Maker" loads the image output from the "Map-Maker" script and creates a new image with a white background that is slightly larger than the original image to accommodate the grid. It then pastes the original image onto the new image, and uses the Pillow library to draw the grid lines, letters, and numbers. (This grid will be your way of tracking where your player character is on the map) Finally, it saves the new image with the grid as a separate file.

"Dice.py" gives a user a full set of DnD dice and allows a user the ability to choose which dice to roll, and how many. Then prints the results and the total. 

DnDMe is Developed by abtzpro, Adam R, and Hello Security

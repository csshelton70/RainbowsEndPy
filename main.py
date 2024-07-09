#//TODO: Find out how to create a requirements type file that other devs can use to isntall required libraries

""" Main entry point for the program """
import argparse
import game
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
logger = logging.getLogger(__name__)
logger.info("--Starting--")
_game = game.Game()

parser = argparse.ArgumentParser()
if ( _game.exists() == False ):
    parser.add_argument("-ng","--newgame",action="store_true", help="Starts a new game if there is not one in progress")

parser.add_argument("-pt","--processturn",action="store_true", help="process the next turn of the game")
parser.add_argument("-i","--info",action="store_true", help="display information about the game")
# --adduser <username>
parser.add_argument("-au","--adduser", help="Only available before the game beings.  Add a new user to the list")
#//TODO: Add an arguement for loglevel, default to info, and use logger.setLevel() to change it


logger.debug("  Parsing Arguments")
args = parser.parse_args()

if (( _game.exists() == False) and (args.newgame == True)):
    logger.debug("  Creating a game")

    game1 = game.Game()
    game1.create_new_game();
elif ( args.processturn == True):
    logger.debug("  Processing turns")

    x="x"
elif ( args.info == True ):
    logger.debug("  Displaying Info")

    x="x"
elif ( args.adduser != None ):
    logger.debug("  Adding a user")

    x=args.adduser
else:
    x="x"

logger.info("--Done--")
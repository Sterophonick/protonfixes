""" Game fix for Duck Game
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Changes the proton argument from the launcher to the game
    """

    # Replace launcher with game exe in proton arguments
    util.append_argument('-linux')
    
    #Force real XNA libraries so the menus render correctly
    util.set_environment('WINE_MONO_OVERRIDES','Microsoft.Xna.Framework.*,Gac=y')

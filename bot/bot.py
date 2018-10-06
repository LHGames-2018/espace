from helper import *
import sys

class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
#        print(len(gameMap.tiles),file=sys.stderr)

            #print('',file=sys.stderr)
#        print(str(gameMap.tiles),  file=sys.stderr)
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        self.visual(gameMap)
        return create_move_action(Point(-1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def visual(self, gameMap):
        toprint = []
        for line in gameMap.tiles:
            visualline = []
            for tile in line:
                t = str(tile.TileContent)
                t = t.replace('TileContent.Empty', ' ')
                t = t.replace('TileContent.Wall', '#')
                t = t.replace('TileContent.House', '^')
                t = t.replace('TileContent.Lava', 'X')
                t = t.replace('TileContent.Resource', '*')
                t = t.replace('TileContent.Player', '1')
                print("t:",t, file=sys.stderr)
                visualline.append(t)
            toprint.append(visualline)
        toprint = [*zip(*toprint)]
        for vline in toprint:
            print(''.join(vline),file=sys.stderr)

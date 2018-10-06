from helper import *
from state.machine import StateMachine
import state
import sys

class Bot:
    def __init__(self):
        self.state_machine = StateMachine(initial_state=state.HuntPlayerState())

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo
        print(playerInfo.json(), file=sys.stderr)

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        self.visual(gameMap)
        parsedGameMap = self.parseMap(gameMap)
        action = None
        while not action:
            action = self.state_machine.run({'PlayerInfo': self.PlayerInfo, 'gameMap': gameMap, 'parsedGameMap': parsedGameMap, 'visiblePlayers': visiblePlayers})

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return action

    def parseMap(self, gameMap):
        dictMap = {}
        for line in gameMap.tiles:
            for tile in line:
                dictMap[(tile.Position.x, tile.Position.y)] = tile.TileContent
        return dictMap


    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def visual(self, gameMap):
        #prints map in cmdline on bot server
        toprint = []
        for line in gameMap.tiles:
            visualline = []
            for tile in line:
                t = str(tile.TileContent)
                t = t.replace('TileContent.Player', '1')
                t = t.replace('TileContent.Empty', '_')
                t = t.replace('TileContent.Wall', '#')
                t = t.replace('TileContent.House', '^')
                t = t.replace('TileContent.Lava', 'X')
                t = t.replace('TileContent.Resource', '*')
                #print("t:",t, file=sys.stderr)
                visualline.append(t)
            toprint.append(visualline)
        toprint = [*zip(*toprint)]
        for vline in toprint:
            print(''.join(vline),file=sys.stderr)

    def findTargets(self, mapmatrix, me):
        #returns points of interest
        resources = []
        enemies = []
        shops = []
        for row in mapmatrix.tiles:
            for tile in row:
                if tile.TileContent==TileContent.Resource:
                    resources.append(tile)
                elif tile.TileContent==TileContent.Player and tile.Position != self.PlayerInfo.Position:
                    enemies.append(tile)
                elif tile.TileContent==TileContent.Shop:
                    shops.append(tile)
                else:
                    continue
        return [resources, enemies, shops]

    def manhattanDistance(self, tile_init, tile_dest):
        return abs(tile_dest.Position.x - tile_init.Position.x) + abs(tile_dest.Position.y - tile_init.Position.y)

    def manhattanDistancePoint(self, point_init, point_dest):
        return abs(point_init.x - point_dest.x) + abs(point_init.y - point_dest.y)

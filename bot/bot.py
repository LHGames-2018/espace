from helper import *
from helper.Astar import aStar
import sys

class Bot:
    def __init__(self):
        self.local = True
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
        if self.local:
            self.visual(gameMap)
        targets = self.findTargets(gameMap, self.PlayerInfo)
        neighbors = [(1,0), (-1, 0), (0,1), (0,-1)]
        target = (targets[0][0].Position.x, targets[0][0].Position.y)
        dists = []
        dictMap = {}
        for line in gameMap.tiles:
            for tile in line:
                dictMap[(tile.Position.x, tile.Position.y)] = tile.TileContent
        current_pos = (self.PlayerInfo.Position.x, self.PlayerInfo.Position.y)
        weightDict = {
        TileContent.Empty : 1,
        TileContent.Wall : -1,
        TileContent.House : 1,
        TileContent.Lava : -1,
        TileContent.Resource : 1,
        TileContent.Player : -1
        }
        current_dist = self.manhattanDistancePoint(self.PlayerInfo.Position, (target[0],target[1]))
#        print(dir(aStar), file=sys.stderr)
        nextMove = aStar(dictMap, current_pos, target, weightDict)
#        for neighbor in neighbors:
#            dists.append()
#        for resource in targets[0]:
#            print(resource, self.manhattanDistance(resource, self.PlayerInfo), file=sys.stderr)
#        resource1 = targets[0][0]
        return create_move_action(Point(nextMove[0], nextMove[1]))

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
                t = t.replace('TileContent.Empty', ' ')
                t = t.replace('TileContent.Wall', '#')
                t = t.replace('TileContent.House', '^')
                t = t.replace('TileContent.Lava', 'X')
                t = t.replace('TileContent.Resource', '*')
                t = t.replace('TileContent.Player', '1')
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
        return abs(point_init.x - point_dest.y) + abs(point_init.x - point.dest.y)

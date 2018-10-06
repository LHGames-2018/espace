from helper import *
from helper.AStar import aStar as a_star


#game_state = { PlayerInfo, gameMap, parsedGameMap, visiblePlayers }

def get_my_position(game_state):
    return game_state['PlayerInfo'].Position


def get_resources(game_state):
    resources = []
    for point in game_state['parsedGameMap']:
        if game_state['parsedGameMap'][point] == tile.TileContent.Resource:
            resources.append(Point(point[0], point[1]))
    return resources

def get_enemies(game_state):
    my_pos = get_my_position(game_state)
    enemies = []
    for point in game_state['parsedGameMap']:
        if game_state['parsedGameMap'][point] == tile.TileContent.Player and point != my_pos.to_tuple():
            enemies.append(Point(point[0], point[1]))
    return enemies

def get_next_move(my_pos, next_pos):
    return Point(next_pos.x - my_pos.x, next_pos.y - my_pos.y)

def get_current_hp_count(game_state):
    return game_state['PlayerInfo'].Health

def get_closest_resource(game_state):
    my_pos = get_my_position(game_state)
    resources = get_resources(game_state)

    # finds the position of the closest resource
    paths = [a_star(game_state['parsedGameMap'], my_pos, res, canWalkOnResources=True) for res in resources]
    paths = list(filter(lambda x: x != None, paths))
    paths.sort()

    if len(paths) >= 1:
        return paths[0]
    else:
        return -1, Point(-1, 0)

def get_closest_enemy(game_state):
    my_pos = get_my_position(game_state)
    enemies = get_enemies(game_state)

    # finds the position of the closest resource
    paths = [a_star(game_state['parsedGameMap'], my_pos, res) for res in enemies]
    paths = list(filter(lambda x: x != None, paths))
    paths.sort()

    if len(paths) >= 1:
        return paths[0]
    else:
        return -1, Point(-1, 0)

def get_home(game_state):
    poids, next_move = a_star(game_state['parsedGameMap'], get_my_position(game_state), game_state['PlayerInfo'].HouseLocation)
    return poids, next_move

def get_neighbours(game_state):
    p = get_my_position(game_state)
    return [Point(p.x + d[0], p.y + d[1]) for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]]

def inventory_is_full(game_state):
    return game_state['PlayerInfo'].CarriedResources >= game_state['PlayerInfo'].CarryingCapacity
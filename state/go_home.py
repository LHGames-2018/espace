from state.machine import BaseState
from helper import *
import state

class GoHomeState(BaseState):

    def action(self, game_state):
        
        my_pos = game_state_helper.get_my_position(game_state)
        poids, next_move = game_state_helper.get_home(game_state)
        
        if not next_move:
            vector = game_state['PlayerInfo'].HouseLocation - my_pos
            if abs(vector.x) > abs(vector.y):
                next_move = Point(-1 if vector.x < 0 else 1, 0)
            else:
                next_move = Point(0, -1 if vector.y < 0 else 1)

        if poids == 0:
            return state.GatherResourcesState(), None

        print(my_pos, next_move, file=__import__('sys').stderr)
        
        tile_content = game_state['parsedGameMap'][(my_pos + next_move).to_tuple()]
        action = create_move_action(tile_content, next_move)

        return None, action
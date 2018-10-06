from state.machine import BaseState
from helper import *
import state

class GoHomeState(BaseState):

    def action(self, game_state):
        
        my_pos = game_state_helper.get_my_position(game_state)
        poids, next_move = game_state_helper.get_home(game_state)

        if poids == 0:
            return state.GatherResourcesState(), None
            
        next_move = Point.from_tuple(next_move)

        tile_content = game_state['parsedGameMap'][(my_pos + next_move).to_tuple()]
        action = create_move_action(tile_content, next_move)

        return None, action
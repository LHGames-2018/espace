from state.machine import BaseState
from helper import *
import state

class HuntPlayerState(BaseState):

    def action(self, game_state):

        #if game_state_helper.get_current_hp_count(game_state) <= 5:
        #    return state.GoHomeState(), None

        my_pos = game_state_helper.get_my_position(game_state)

        # find closest resource
        poids, next_move = game_state_helper.get_closest_enemy(game_state)

        if poids == -1:
            return state.GatherResourcesState(), None

        tile_content = game_state['parsedGameMap'][(my_pos + next_move).to_tuple()]

        action = create_move_action(tile_content, next_move)


        if poids == 1: # if we're on top of the resource
            return state.AttackPlayerState(), None
        else:
            return None, action

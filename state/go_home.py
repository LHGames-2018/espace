from state.machine import BaseState
from helper import *
import state

class GoHomeState(BaseState):

    def action(self, game_state):
        
        poids, next_move = game_state_helper.get_home(game_state)

        if poids == 0:
            return state.GatherResourcesState(), None

        action = create_move_action(Point.from_tuple(next_move))

        return None, action
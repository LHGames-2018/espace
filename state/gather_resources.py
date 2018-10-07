from state.machine import BaseState
from helper import *
import state

class GatherResourcesState(BaseState):

    def action(self, game_state):

        if game_state_helper.inventory_is_full(game_state):
            #game_state_helper.get_current_hp_count(game_state) <= 5:
            return state.GoHomeState(), None

        neighbours = game_state_helper.get_neighbours(game_state)
        my_pos = game_state_helper.get_my_position(game_state)

        for neighbour in neighbours:
            if game_state['parsedGameMap'][neighbour.to_tuple()] == TileContent.Resource:
                return None, create_collect_action(game_state_helper.get_next_move(my_pos, neighbour))

        return state.GetToClosestResource(), None

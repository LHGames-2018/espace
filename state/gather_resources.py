from state.machine import BaseState
from helper import game_state_helper
import state

class GatherResourcesState(BaseState):

    def action(self, game_state):

        if game_state_helper.inventory_is_full() or game_state_helper.get_current_hp_count() <= 5:
            return state.GoHomeState(), None

        neighbours = game_state_helper.get_neighbours(game_state)

        for neighbour in neighbours:
            if game_state.gameMap.getTileAt(neighbour).content == 4:
                return None, create_collect_action(neighbour)

        return state.GetToClosestResource(), None
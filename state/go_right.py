import state
from helper import *

class GoRightState(state.BaseState):
    def __init__(self):
        self.__count = 0

    def action(self, game_state):
        action = create_move_action(Point(1,0))

        self.__count += 1

        if self.__count == 5:
            return state.GoLeftState(), action

        else:
            return None, action

    def __repr__(self):
        return 'Im going right'
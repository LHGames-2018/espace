from state import *
from helper import *

class GoLeftState(BaseState):
    def __init__(self):
        self.__count = 0

    def action(self, game_state):

        action = create_move_action(Point(0,1))

        if self.__count == 5:
            return GoRightState(), action

        else:
            return None, action

        self.__count += 1

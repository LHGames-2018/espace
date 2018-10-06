import state
from helper import *
import sys


class GoRightState(state.BaseState):
    def __init__(self):
        self.__count = 0

    def action(self, game_state):
        print(str(dir(state)), file=sys.stderr)
        action = create_move_action(Point(1,0))

        self.__count += 1

        if self.__count == 5:
            return GoLeftState(), action

        else:
            return None, action

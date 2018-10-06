from helper import *
from state.machine import StateMachine
from state import GetResourcesState, GoHomeState

class Bot:
    def __init__(self):
        self.state_machine = StateMachine(GetResourcesState())

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        action = self.state_machine.run()

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return action

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

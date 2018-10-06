

class StateMachine(object):
    def __init__(self, initial_state):
        self.state = initial_state

    def run(self, game_state):
        newState, action = self.state.action(game_state)

        if newState:
            self.state = newState

        return action

class BaseState(object):

    def action(self, game_state):
        pass

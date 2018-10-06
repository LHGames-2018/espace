from random import choice

class StateMachine(object):
    def __init__(self, initial_state):
        self.state = initial_state

    def run(self):
        newState, action = self.state.action()

        if newState:
            self.state = newState

        return action

class BaseState(object):

    def action(self):
        pass





class StateMachine(Object):
    def __init__(self, initial_state):
        self.state = initial_state

    def run(self):
        newState, action = self.state.action()

        if newState:
            self.state = newState

        return action

class State(Object):

    def action(self):
        pass


class GoHomeState(State):

    def action(self):
        pass

class GetResourcesState(State):

    def action(self):
        pass

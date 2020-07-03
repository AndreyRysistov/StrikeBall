class GameState:
    name = "state"
    allowed = []

    def __str__(self):
        return self.name

    def switch(self, state):
        """ Switch to new state """
        if state.name in self.allowed:
            self.__class__ = state
        else:
            pass

class Running(GameState):

    name = "running"
    allowed = ['pause', 'close']

class Close(GameState):
    name = "close"
    allowed = ['running']

class Pause(GameState):
    name = "pause"
    allowed = ['running', 'close']

class Error(GameState):
    name = "error"
    allowed = ['closed']

class GameState:
    """
    A class that implements the state of the game and changes it according to the State design pattern. The class is abstract and is used for inheriting other game state classes from it
    The class has the following methods:
        name - name of the state
        allowed-list of States that the class can go to from the source state
    The class has the following methods:
        switch-changes the game state to the new state passed in the method arguments
    """
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

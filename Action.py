class Action:
    pass


class TargetedAction(Action):
    def __init__(self, y, x):
        self.x = x
        self.y = y


class ActionOpen(TargetedAction):
    def __init__(self, y, x):
        super(ActionOpen, self).__init__(y=y, x=x)


class ActionFlag(TargetedAction):
    def __init__(self, y, x):
        super(ActionFlag, self).__init__(y=y, x=x)


class ActionNewGame(Action):
    pass


class ActionQuit(Action):
    pass

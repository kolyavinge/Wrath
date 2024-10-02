class EventManager:

    def __init__(self):
        self.handlers = {}

    def raiseEvent(self, event):
        if event in self.handlers:
            for handler in self.handlers[event]:
                handler()

    def attachToEvent(self, event, handler):
        if event in self.handlers:
            self.handlers[event].append(handler)
        else:
            self.handlers[event] = [handler]


def makeEventManager(resolver):
    return EventManager()

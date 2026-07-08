class EventPublisher:

    def __init__(self):
        self.listeners = []

    def register(self, listener):
        self.listeners.append(listener)

    def publish(self, event):
        for listener in self.listeners:
            listener.handleEvent(event)
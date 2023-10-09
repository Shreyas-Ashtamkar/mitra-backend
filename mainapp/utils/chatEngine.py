from enum import Enum

class MessageActions(Enum):
    INPUT   = 1
    OUTPUT  = 2
    EXECUTE = 3

INPUT = [2, 1]

class ChatMessage:
    def __init__(self, action="OUTPUT", message=""):
        self.action = action
        self.message = message

class ChatEngine:
    def __init__(self, client=1, currentStep=0):
        self.client = action
        self.currentStep = currentStep
        # Write to MONGO AND PULL DATA OUT

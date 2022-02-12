class Test:
    def __init__(self, test):
        self.test = test


class Dto:
    def __init__(self, note):
        self.note = note


class Body:
    def __init__(self, value, sampleWidth, sampleRate):
        self.value = value
        self.sampleRate = sampleRate
        self.sampleWidth = sampleWidth

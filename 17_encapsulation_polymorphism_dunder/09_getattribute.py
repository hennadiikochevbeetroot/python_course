class D:
    def __init__(self):
        self.test = 20
        self.test2 = 21

    def __getattribute__(self, name):
        if name == 'test':
            return 0.

        return super().__getattribute__(self, name)

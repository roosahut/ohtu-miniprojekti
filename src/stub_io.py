class StubIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def add_input(self, value):
        self.inputs.append(value)

    def read(self, prompt):
        if len(self.inputs) == 0:
            return ''
        return self.inputs.pop(0)

    def write(self, value):
        self.outputs.append(value)

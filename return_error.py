from runtime_error import RuntimeError


class ReturnError(RuntimeError):
    def __init__(self, value):
        super().__init__(None, None)
        self.value = value

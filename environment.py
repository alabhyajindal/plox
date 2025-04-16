from runtime_error import RuntimeError


class Environment:
    values = {}

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        raise RuntimeError(name, f"Undefined variable {name.lexeme}.")

    def assign(self, name, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return

        raise RuntimeError(name, f"Undefined variable {name.lexeme}.")

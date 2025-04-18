from runtime_error import RuntimeError


class Environment:
    def __init__(self, enclosing=None):
        self.values = {}
        self.enclosing: Environment = enclosing

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise RuntimeError(name, f"Undefined variable {name.lexeme}.")

    def assign(self, name, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return

        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return

        raise RuntimeError(name, f"Undefined variable {name.lexeme}.")

    def get_at(self, name, depth):
        environment = self.ancestor(depth)
        if environment is not None:
            return environment.values.get(name.lexeme)
        return None

    def assign_at(self, name, value, depth):
        environment = self.ancestor(depth)
        if environment is not None:
            environment.values[name.lexeme] = value
        else:
            self.assign(name, value)

    def ancestor(self, depth):
        environment = self
        for _ in range(depth):
            if environment is not None:
                environment = environment.enclosing
            else:
                return None
        return environment

from lox_callable import LoxCallable
from environment import Environment


class LoxFunction(LoxCallable):
    def __init__(self, declaration):
        self.declaration = declaration

    def arity(self):
        return len(self.declaration.params)

    def __str__(self):
        return f"<fn {self.declaration.name.lexeme}>"

    def call(self, interpreter, arguments):
        environment = Environment(interpreter.globals)
        for i in range(len(self.declaration.params)):
            environment.define(self.declaration.params[i].lexeme, arguments[i])

        interpreter.execute_block(self.declaration.body, environment)
        return None

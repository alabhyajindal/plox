from dataclasses import dataclass
from lox_token import Token
from expr import Expr


@dataclass
class Stmt:
    pass


@dataclass
class ExpressionStmt:
    expression: Expr


@dataclass
class PrintStmt:
    expression: Expr


@dataclass
class VariableStmt:
    name: Token
    initializer: Expr

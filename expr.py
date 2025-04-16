from dataclasses import dataclass
from lox_token import Token
from typing import Any


@dataclass
class Expr():
    pass


@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr


@dataclass
class Grouping(Expr):
    expression: Expr


@dataclass
class Literal():
    value: Any


@dataclass
class Unary(Expr):
    operator: Token
    right: Expr


@dataclass
class VariableExpr:
    name: Token

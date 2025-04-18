from dataclasses import dataclass
from lox_token import Token
from typing import List, Any


@dataclass
class Expr:
    pass


@dataclass
class AssignExpr(Expr):
    name: Token
    value: Expr


@dataclass
class BinaryExpr(Expr):
    left: Expr
    operator: Token
    right: Expr


@dataclass
class CallExpr(Expr):
    callee: Expr
    paren: Token
    arguments: List[Expr]


@dataclass
class GroupingExpr(Expr):
    expression: Expr


@dataclass
class LiteralExpr(Expr):
    value: Any


@dataclass
class LogicalExpr(Expr):
    left: Expr
    operator: Token
    right: Expr


@dataclass
class UnaryExpr(Expr):
    operator: Token
    right: Expr


@dataclass
class VariableExpr(Expr):
    name: Token

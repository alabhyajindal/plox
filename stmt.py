from dataclasses import dataclass
from typing import List, Optional, Union
from lox_token import Token
from expr import Expr


@dataclass
class Stmt:
    pass


@dataclass
class BlockStmt(Stmt):
    statements: List[Stmt]


@dataclass
class ExpressionStmt(Stmt):
    expression: Expr


@dataclass
class PrintStmt(Stmt):
    expression: Expr


@dataclass
class VariableStmt(Stmt):
    name: Token
    initializer: Optional[Expr]

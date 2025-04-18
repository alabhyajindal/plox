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
class FunctionStmt(Stmt):
    name: Token
    params: List[Token]
    body: List[Stmt]


@dataclass
class IfStmt(Stmt):
    condition: Expr
    then_branch: Stmt
    else_branch: Stmt


@dataclass
class PrintStmt(Stmt):
    expression: Expr


@dataclass
class VariableStmt(Stmt):
    name: Token
    initializer: Optional[Expr]


@dataclass
class WhileStmt(Stmt):
    condition: Expr
    body: Stmt

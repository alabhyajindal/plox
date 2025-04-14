from dataclasses import dataclass
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

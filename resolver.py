from enum import Enum
from stmt import *
from expr import *


class Resolver:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.scopes = []

    def resolve(self, statements):
        if isinstance(statements, list):
            for statement in statements:
                self.resolve(statement)
        else:
            self.resolve_stmt(statements)

    def resolve_stmt(self, stmt):
        match stmt:
            case BlockStmt():
                self.block_stmt(stmt)

    def block_stmt(self, stmt):
        self.begin_scope()
        self.resolve(stmt.statements)
        self.end_scope()

    def var_stmt(self, stmt):
        self.declare(stmt.name)
        if stmt.initializer is not None:
            self.resolve_expr(stmt.initializer)
        self.define(stmt.name)

    def declare(self, name):
        if not self.scopes:
            return
        scope = self.scopes[-1]

    def begin_scope(self):
        self.scopes.append({})

    def end_scope(self):
        self.scopes.pop()


class Resolver:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.scopes = []
        self.current_function = FunctionType.NONE

    def resolve(self, statements):
        if isinstance(statements, list):
            for statement in statements:
                self.resolve(statement)
        else:
            self.resolve_stmt(statements)

    def resolve_stmt(self, stmt):
        match stmt:
            case BlockStmt():
                self.block_stmt(stmt)
            case VarStmt():
                self.var_stmt(stmt)
            case FunctionStmt():
                self.function_stmt(stmt)
            case ExpressionStmt():
                self.expression_stmt(stmt)
            case IfStmt():
                self.if_stmt(stmt)
            case PrintStmt():
                self.print_stmt(stmt)
            case ReturnStmt():
                self.return_stmt(stmt)
            case WhileStmt():
                self.while_stmt(stmt)

    def resolve_expr(self, expr):
        match expr:
            case AssignExpr():
                self.assign_expr(expr)
            case BinaryExpr():
                self.binary_expr(expr)
            case CallExpr():
                self.call_expr(expr)
            case GroupingExpr():
                self.grouping_expr(expr)
            case LiteralExpr():
                self.literal_expr(expr)
            case LogicalExpr():
                self.logical_expr(expr)
            case UnaryExpr():
                self.unary_expr(expr)
            case VariableExpr():
                self.variable_expr(expr)

    def begin_scope(self):
        self.scopes.append({})

    def end_scope(self):
        self.scopes.pop()

    def block_stmt(self, stmt):
        self.begin_scope()
        self.resolve(stmt.statements)
        self.end_scope()

    def var_stmt(self, stmt):
        self.declare(stmt.name)
        if stmt.initializer is not None:
            self.resolve_expr(stmt.initializer)
        self.define(stmt.name)

    def declare(self, name):
        if not self.scopes:
            return
        scope = self.scopes[-1]  # Peek at the current scope
        if name.lexeme in scope:
            ErrorReporter.error(
                name.line, f"Already a variable with this name in this scope.")
        scope[name.lexeme] = False

    def define(self, name):
        if not self.scopes:
            return
        self.scopes[-1][name.lexeme] = True

    def variable_expr(self, expr):
        if self.scopes and self.scopes[-1].get(expr.name.lexeme) == False:
            ErrorReporter.error(
                expr.name.line, "Can't read local variable in its own initializer.")

        self.resolve_local(expr, expr.name)

    def resolve_local(self, expr, name):
        for i in range(len(self.scopes) - 1, -1, -1):
            if name.lexeme in self.scopes[i]:
                self.interpreter.resolve(expr, len(self.scopes) - 1 - i)
                return

    def assign_expr(self, expr):
        self.resolve_expr(expr.value)
        self.resolve_local(expr, expr.name)

    def function_stmt(self, stmt):
        self.declare(stmt.name)
        self.define(stmt.name)
        self.resolve_function(stmt, FunctionType.FUNCTION)

    def resolve_function(self, function, type):
        enclosing_function = self.current_function
        self.current_function = type

        self.begin_scope()
        for param in function.params:
            self.declare(param)
            self.define(param)
        self.resolve(function.body)
        self.end_scope()

        self.current_function = enclosing_function

    def expression_stmt(self, stmt):
        self.resolve_expr(stmt.expression)

    def if_stmt(self, stmt):
        self.resolve_expr(stmt.condition)
        self.resolve(stmt.then_branch)
        if stmt.else_branch is not None:
            self.resolve(stmt.else_branch)

    def print_stmt(self, stmt):
        self.resolve_expr(stmt.expression)

    def return_stmt(self, stmt):
        if self.current_function == FunctionType.NONE:
            ErrorReporter.error(stmt.keyword.line,
                                "Can't return from top-level code.")
        if stmt.value is not None:
            self.resolve_expr(stmt.value)

    def while_stmt(self, stmt):
        self.resolve_expr(stmt.condition)
        self.resolve(stmt.body)

    def binary_expr(self, expr):
        self.resolve_expr(expr.left)
        self.resolve_expr(expr.right)

    def call_expr(self, expr):
        self.resolve_expr(expr.callee)
        for argument in expr.arguments:
            self.resolve_expr(argument)

    def grouping_expr(self, expr):
        self.resolve_expr(expr.expression)

    def literal_expr(self, expr):
        pass

    def logical_expr(self, expr):
        self.resolve_expr(expr.left)
        self.resolve_expr(expr.right)

    def unary_expr(self, expr):
        self.resolve_expr(expr.right)


class FunctionType(Enum):
    NONE = 0
    FUNCTION = 1


class Resolver:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.scopes = []
        self.current_function = FunctionType.NONE

    def resolve(self, statements):
        if isinstance(statements, list):
            for statement in statements:
                self.resolve(statement)
        else:
            self.resolve_stmt(statements)

    def resolve_stmt(self, stmt):
        match stmt:
            case BlockStmt():
                self.block_stmt(stmt)
            case VariableStmt():
                self.var_stmt(stmt)
            case FunctionStmt():
                self.function_stmt(stmt)
            case ExpressionStmt():
                self.expression_stmt(stmt)
            case IfStmt():
                self.if_stmt(stmt)
            case PrintStmt():
                self.print_stmt(stmt)
            case ReturnStmt():
                self.return_stmt(stmt)
            case WhileStmt():
                self.while_stmt(stmt)

    def resolve_expr(self, expr):
        match expr:
            case AssignExpr():
                self.assign_expr(expr)
            case BinaryExpr():
                self.binary_expr(expr)
            case CallExpr():
                self.call_expr(expr)
            case GroupingExpr():
                self.grouping_expr(expr)
            case LiteralExpr():
                self.literal_expr(expr)
            case LogicalExpr():
                self.logical_expr(expr)
            case UnaryExpr():
                self.unary_expr(expr)
            case VariableExpr():
                self.variable_expr(expr)

    def begin_scope(self):
        self.scopes.append({})

    def end_scope(self):
        self.scopes.pop()

    def block_stmt(self, stmt):
        self.begin_scope()
        self.resolve(stmt.statements)
        self.end_scope()

    def var_stmt(self, stmt):
        self.declare(stmt.name)
        if stmt.initializer is not None:
            self.resolve_expr(stmt.initializer)
        self.define(stmt.name)

    def declare(self, name):
        if not self.scopes:
            return
        scope = self.scopes[-1]  # Peek at the current scope
        if name.lexeme in scope:
            ErrorReporter.error(
                name.line, f"Already a variable with this name in this scope.")
        scope[name.lexeme] = False

    def define(self, name):
        if not self.scopes:
            return
        self.scopes[-1][name.lexeme] = True

    def variable_expr(self, expr):
        if self.scopes and self.scopes[-1].get(expr.name.lexeme) == False:
            ErrorReporter.error(
                expr.name.line, "Can't read local variable in its own initializer.")

        self.resolve_local(expr, expr.name)

    def resolve_local(self, expr, name):
        for i in range(len(self.scopes) - 1, -1, -1):
            if name.lexeme in self.scopes[i]:
                self.interpreter.resolve(expr, len(self.scopes) - 1 - i)
                return

    def assign_expr(self, expr):
        self.resolve_expr(expr.value)
        self.resolve_local(expr, expr.name)

    def function_stmt(self, stmt):
        self.declare(stmt.name)
        self.define(stmt.name)
        self.resolve_function(stmt, FunctionType.FUNCTION)

    def resolve_function(self, function, type):
        enclosing_function = self.current_function
        self.current_function = type

        self.begin_scope()
        for param in function.params:
            self.declare(param)
            self.define(param)
        self.resolve(function.body)
        self.end_scope()

        self.current_function = enclosing_function

    def expression_stmt(self, stmt):
        self.resolve_expr(stmt.expression)

    def if_stmt(self, stmt):
        self.resolve_expr(stmt.condition)
        self.resolve(stmt.then_branch)
        if stmt.else_branch is not None:
            self.resolve(stmt.else_branch)

    def print_stmt(self, stmt):
        self.resolve_expr(stmt.expression)

    def return_stmt(self, stmt):
        if self.current_function == FunctionType.NONE:
            ErrorReporter.error(stmt.keyword.line,
                                "Can't return from top-level code.")
        if stmt.value is not None:
            self.resolve_expr(stmt.value)

    def while_stmt(self, stmt):
        self.resolve_expr(stmt.condition)
        self.resolve(stmt.body)

    def binary_expr(self, expr):
        self.resolve_expr(expr.left)
        self.resolve_expr(expr.right)

    def call_expr(self, expr):
        self.resolve_expr(expr.callee)
        for argument in expr.arguments:
            self.resolve_expr(argument)

    def grouping_expr(self, expr):
        self.resolve_expr(expr.expression)

    def literal_expr(self, expr):
        pass

    def logical_expr(self, expr):
        self.resolve_expr(expr.left)
        self.resolve_expr(expr.right)

    def unary_expr(self, expr):
        self.resolve_expr(expr.right)


class FunctionType(Enum):
    NONE = 0
    FUNCTION = 1

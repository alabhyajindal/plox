from expr import *
from token_type import TokenType


class AstPrinter:
    def print(self, expr: Expr) -> str:
        return self.evaluate(expr)

    def evaluate(self, expr: Expr) -> str:
        match expr:
            case BinaryExpr(left, operator, right):
                return self.parenthesize(operator.lexeme, left, right)

            case GroupingExpr(expression):
                return self.parenthesize("group", expression)

            case LiteralExpr(value):
                if value is None:
                    return "nil"
                return str(value)

            case UnaryExpr(operator, right):
                return self.parenthesize(operator.lexeme, right)

            case _:
                raise RuntimeError(f"Unknown expression type: {type(expr)}")

    def parenthesize(self, name: str, *exprs: Expr) -> str:
        result = f"({name}"

        for expr in exprs:
            result += f" {self.evaluate(expr)}"

        result += ")"

        return result


# Testing the AST printer
def main():
    expression = BinaryExpr(
        UnaryExpr(
            Token(TokenType.MINUS, "-", None, 1),
            LiteralExpr(123)
        ),
        Token(TokenType.STAR, "*", None, 1),
        GroupingExpr(
            LiteralExpr(45.67)
        )
    )

    print(AstPrinter().print(expression))


if __name__ == "__main__":
    main()

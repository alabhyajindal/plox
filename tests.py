from lox import Lox
from scanner import Scanner
from parser import Parser
from interpreter import Interpreter
from token_type import TokenType
from lox_token import Token
from expr import *


def main():
    test_scanner()
    test_parser()


def test_scanner():
    source = '"here"400)for foobar *'
    expected_tokens = [
        Token(TokenType.STRING, '"here"', "here", 1),
        Token(TokenType.NUMBER, "400", 400.0, 1),
        Token(TokenType.RIGHT_PAREN, ")", None, 1),
        Token(TokenType.FOR, "for", None, 1),
        Token(TokenType.IDENTIFIER, "foobar", None, 1),
        Token(TokenType.STAR, "*", None, 1),
        Token(TokenType.EOF, "", None, 1)
    ]

    scanner = Scanner(source)
    tokens = scanner.scan_tokens()

    assert len(tokens) == len(expected_tokens)

    for i, (actual, expected) in enumerate(zip(tokens, expected_tokens)):
        assert actual == expected, f"Expected {expected}, got {actual}"


def test_parser():
    source = '5 + 2 * 3'
    expected_ast = BinaryExpr(left=LiteralExpr(5.0), operator=Token(
        TokenType.PLUS, '+', None, 1), right=BinaryExpr(left=LiteralExpr(2.0), operator=Token(TokenType.STAR, '*', None, 1), right=LiteralExpr(3.0)))

    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    ast = parser.parse()
    assert ast == expected_ast, f"Expected:\n{expected_ast}, got:\n{ast}"


def test_expr_eval():
    source = '5 + 2 * 3'
    expected_value = 11

    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    parser = Parser(tokens)
    expr = parser.parse()

    interpreter = Interpreter()
    # interpreter doesn't return a value, can modify it after completing stmt eval
    interpreter.interpret(expr)


if __name__ == "__main__":
    main()

from lox import Lox
from scanner import Scanner
from token_type import TokenType
from lox_token import Token


def main():
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


if __name__ == "__main__":
    main()

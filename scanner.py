from token import Token
from token_type import TokenType

class Scanner:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
    
        return self.tokens

    def scan_token(self):
        c = self.advance()
        match c:
            case '(': self.add_token(TokenType.LEFT_PAREN)

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current+=1
        return self.source(self.current)

    def add_token(self, type, literal=None):
        text = self.source[self.start:self.current]
        tokens.append(Token(type, text, literal, self.line))
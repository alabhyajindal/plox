from token_type import TokenType


class ErrorReporter:
    had_error = False
    had_runtime_error = False

    @staticmethod
    def line_error(line, message):
        ErrorReporter.report(line, '', message)

    @staticmethod
    def token_error(token, message):
        from token_type import TokenType
        if token.type == TokenType.EOF:
            ErrorReporter.report(token.line, ' at end', message)
        else:
            ErrorReporter.report(token.line, f" at '{token.lexeme}'", message)

    @staticmethod
    def report(line, where, message):
        print(f'[line {line}] Error{where}: {message}')
        ErrorReporter.had_error = True

    @staticmethod
    def runtime_error(error):
        print(f'{error.message} \n[line {error.token.line}]')
        ErrorReporter.had_runtime_error = True

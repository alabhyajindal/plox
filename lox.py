import sys
from scanner import Scanner
from parser import Parser
from interpreter import Interpreter
from error_reporter import ErrorReporter


class Lox:
    interpreter = Interpreter()

    def run(self, source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        parser = Parser(tokens)
        statements = parser.parse()

        if ErrorReporter.had_error:
            return

        self.interpreter.interpret(statements)

    def run_file(self, path):
        with open(path, 'r') as file:
            source = file.read()
        self.run(source)
        if ErrorReporter.had_error:
            sys.exit(65)
        if ErrorReporter.had_runtime_error:
            sys.exit(70)

    def run_prompt(self):
        try:
            while True:
                print('> ', end='')
                line = input()
                if not line:
                    break
                self.run(line)
                ErrorReporter.had_error = False
        except EOFError:
            print()

    def main(self):
        if len(sys.argv) == 1:
            self.run_prompt()
        elif len(sys.argv) == 2:
            path = sys.argv[1]
            self.run_file(path)
        else:
            print('Usage: plox [script]')
            sys.exit(64)


if __name__ == '__main__':
    lox = Lox()
    lox.main()

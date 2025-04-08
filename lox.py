import sys

class Lox:
    had_error = False

    def run(self, source):
        from scanner import Scanner
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)


    def run_file(self, path):
        with open(path, 'r') as file:
            source = file.read()
        self.run(source)
        if Lox.had_error: sys.exit(65)


    def run_prompt(self):
        try:
            while True:
                print('> ', end='')
                line = input()
                if not line:
                    break
                self.run(line)
                Lox.had_error = False
        except EOFError:
            print()

    @staticmethod
    def error(line, message):
        Lox.report(line, '', message)

    @staticmethod
    def report(line, where, message):
        print(f'[line {line}] Error{where}: {message}')
        Lox.had_error = True

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

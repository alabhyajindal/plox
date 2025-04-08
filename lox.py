import sys
from scanner import Scanner


def run(source):
    scanner = Scanner(source)
    tokens = scanner.scan_tokens()
    for token in tokens:
        print(token)


def run_file(path):
    with open(path, 'r') as file:
        source = file.read()
    run(source)


def run_prompt():
    try:
        while True:
            print("> ", end="")
            line = input()
            if not line:
                break
            run(line)
    except EOFError:
        print()


def main():
    if len(sys.argv) == 1:
        run_prompt()
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        run_file(path)
    else:
        print("Usage: plox [script]")
        sys.exit(64)


if __name__ == "__main__":
    main()

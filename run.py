import importlib
import sys

def main(day):
    module = f"puzzles.day_{day}"
    puzzle = importlib.import_module(module)
    if hasattr(puzzle, "__main__"):
        puzzle.__main__()
    else:
        if hasattr(puzzle, 'main'):
            puzzle.main()
        else:
            print(f"No main function found in {module}")
            sys.exit(1)


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        print("Usage: python run.py <day>")
        sys.exit(1)

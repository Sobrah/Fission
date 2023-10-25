import fission
import helpers
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: project.py URL")

    try:
        # Depends On User System
        sys.setrecursionlimit(10000)
        fission.Trigger(sys.argv[1])
    except Exception as error:
        print(helpers.paint("Error: ", "red", "italic"), *error.args)


if __name__ == "__main__":
    main()

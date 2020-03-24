import argparse
from solver import Board


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", help="set input path in txt, must be rectangular n x m board, first line is 'n m' separated by space, then followed by n lines: fill the number separated by space or 0 if empty cell (must have exactly 1 empty cell)")
    return parser.parse_args()


def get_config():
    args = get_args()
    filename = args.input if args.input else input("Input filename: ")
    with open(filename, "r") as f:
        config = f.readlines()
    return config


if __name__ == "__main__":
    config = get_config()
    B = Board(config)
    print("==== Initial matrix ====")
    B.nodes[0].print()
    print()

    if B.solvable(output=True):
        B.solve()
    else:
        print("Puzzle is unsolvable!")

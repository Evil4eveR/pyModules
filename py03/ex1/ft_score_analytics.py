import sys
from builtins import ValueError


def score_error(nam) -> None:
    print("No scores provided. Usage: python3 "
          + f"{nam} <score1> <score2> ...")


def main() -> None:
    print("=== Player Score Analytics ===")
    if (len(sys.argv) < 2):
        score_error(sys.argv[0])
        return
    score = []
    errors = []
    for arg in sys.argv[1:]:
        try:
            score.append(int(arg))
        except ValueError:
            errors.append(arg)
    for er in errors:
        print(f"Invalid parameter: '{er}'")
    if (len(score) == 0):
        score_error(sys.argv[0])
        return
    print(f"Scores processed:{score}")
    print(f"Total players: {len(score)}")
    print(f"Total score: {sum(score)}")
    print(f"Average score: {sum(score)/len(score)}")
    print(f"High score: {max(score)}")
    print(f"Low score: {min(score)}")
    print(f"Score range: {max(score)-min(score)}")


if __name__ == "__main__":
    main()

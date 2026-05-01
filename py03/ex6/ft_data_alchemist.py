#!/usr/bin/env python3
import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = [
        "Alice", "bob", "Charlie", "henry",
        "dylan", "Emma", "frank", "Grace"
    ]
    capitalized = [name.capitalize() for name in players]
    capitalized_only = [name for name in players if name[0].isupper()]
    print(f"\nInitial list of players:{players}")
    print(f"\nNew list with all names capitalized: {capitalized}")
    print(f"\nNew list of capitalized names only: {capitalized_only}")
    score_dict = {name: random.randint(100, 1000) for name in capitalized}
    # for pl in capitalized:
    #     random_score = random.randint(100,900)
    #     score_dic.update({pl:random_score})
    print(f"\nScore dict:{score_dict}")
    score_average = round(sum(score_dict.values())/len(score_dict.values()), 2)
    print(f"Score average is {score_average}")
    high_dict = {name: score for name, score in score_dict.items()
                 if score > score_average}
    # for ky,val in score_dict.items():
    #     if (val > score_average):
    #         last_dic[ky] = val
    print(f"High scores: {high_dict}")


if __name__ == "__main__":
    main()

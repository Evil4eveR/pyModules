import typing
import random


def gen_event() -> typing.Generator[tuple, None, None]:
    players = [
    "Alice", "Bob", "Charlie", "Henry",
    "Dylan", "Emma", "Frank", "Grace"
    ]
    actions = [
    "sleep", "eat", "run", "play", "write",
    "move", "swim", "jump", "read", "dance"
    ]
    name = random.choice(players)
    action = random.choice(actions)
    yield (name, action)


def consume_event():
    pass

def main():
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        ev = next(gen_event())
        print(f"Event {i}: Player {ev[0]} did action {ev[1]}")
    tuple_list = []
    for i in range(10):
        tuple_list.append(next(gen_event()))
    print(f"Built list of 10 events: {tuple_list}")


if __name__ == "__main__":
    main()
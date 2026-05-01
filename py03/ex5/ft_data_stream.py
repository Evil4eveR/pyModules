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
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(evnt: list) -> typing.Generator[tuple, None, None]:
    while evnt:
        index = random.randrange(len(evnt))
        ev = evnt.pop(index)
        yield (ev)


def main():
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        ev = next(gen_event())
        print(f"Event {i}: Player {ev[0]} did action {ev[1]}")
    generator = gen_event()
    tuple_list = [next(generator) for _ in range(10)]
    print(f"Built list of 10 events: {tuple_list}")
    for event in consume_event(tuple_list):
        print(f"Got event from list :{event}")
        print(f"Remains in list: {tuple_list}")


if __name__ == "__main__":
    main()

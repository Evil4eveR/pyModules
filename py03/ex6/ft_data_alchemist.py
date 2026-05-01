#!/usr/bin/env python3
"""
Data stream processor using generators.
"""

import random
from typing import Generator, List, Tuple

# Constants for players and actions (based on exercise example)
PLAYERS: List[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: List[str] = [
    "run", "eat", "sleep", "grab",
    "move", "climb", "swim", "release", "use"
]


def gen_event() -> Generator[Tuple[str, str], None, None]:
    """
    Endless generator that yields a random (player, action) tuple.
    """
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(event_list: List[Tuple[str, str]]) -> Generator[Tuple[str, str], None, None]:
    """
    Randomly pick and remove one element from event_list, yield it,
    and repeat until the list is empty.
    """
    while event_list:
        # Randomly select an index and pop it (avoids remove() ambiguity)
        idx = random.randrange(len(event_list))
        event = event_list.pop(idx)
        yield event


def main() -> None:
    """Main entry point: runs the required steps."""
    print("=== Game Data Stream Processor ===")

    # ---- 1. Generate and display 1000 events ----
    event_stream = gen_event()
    for i in range(1000):
        player, action = next(event_stream)
        print(f"Event {i}: Player {player} did action {action}")

    # ---- 2. Build a list of 10 fresh events ----
    ten_events: List[Tuple[str, str]] = [next(gen_event()) for _ in range(10)]
    print("\nBuilt list of 10 events:", ten_events)

    # ---- 3. Consume the list randomly using the generator ----
    for event in consume_event(ten_events):
        print("\nGot event from list:", event)
        print("Remains in list:", ten_events)


if __name__ == "__main__":
    main()
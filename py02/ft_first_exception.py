#!/usr/bin/env python3
from builtins import ValueError


def input_temperature(temp_str: str) -> int | None:
    try:
        return int(temp_str)
    except ValueError:
        print("Caught input_temperature error: invalid literal for int() "
              f"with base 10: '{temp_str}'")
        return None


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    inputs = ["25", "abc"]
    for inp in inputs:
        print(f"\nInput data is '{inp}'")
        res = input_temperature(inp)
        if res is not None:
            print(f"Temperature is now {inp}°C")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

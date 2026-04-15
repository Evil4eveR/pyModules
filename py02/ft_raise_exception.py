#!/usr/bin/env python3
from builtins import ValueError


def input_temperature(temp_str: str) -> int | None:
    try:
        if int(temp_str) > 40:
            print(f"Caught input_temperature error: {temp_str}°C "
                  "is too hot for plants (max 40°C)")
            return None
        elif int(temp_str) < 0:
            print(f"Caught input_temperature error: {temp_str}°C "
                  "is too cold for plants (min 0°C)")
            return None
        else:
            return int(temp_str)
    except ValueError:
        print("Caught input_temperature error: invalid literal for int() "
              f"with base 10: '{temp_str}'")
        return None


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    inputs = ["25", "abc", "100", "-50"]
    for inp in inputs:
        print(f"\nInput data is '{inp}'")
        res = input_temperature(inp)
        if res is not None:
            print(f"Temperature is now {res}°C")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

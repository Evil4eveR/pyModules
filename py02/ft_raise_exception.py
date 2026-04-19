#!/usr/bin/env python3
from builtins import ValueError


def input_temperature(temp_str: str) -> int | None:
    try:
        temp: int = int(temp_str)
    except ValueError:
        print("Caught input_temperature error: invalid literal for int() "
              f"with base 10: '{temp_str}'")
        return None

    if temp > 40:
        raise ValueError(f"Caught input_temperature error: {temp}°C "
                         "is too hot for plants (max 40°C)")
    if temp < 0:
        raise ValueError(f"Caught input_temperature error: {temp}°C "
                         "is too cold for plants (min 0°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    inputs = ["25", "abc", "100", "-50"]
    for inp in inputs:
        print(f"\nInput data is '{inp}'")
        try:
            res = input_temperature(inp)
            if res is not None:
                print(f"Temperature is now {res}°C")
        except ValueError as e:
            print(e)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

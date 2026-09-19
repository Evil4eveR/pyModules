import operator
from collections.abc import Callable
from functools import reduce, partial
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    result: int = 0
    if not spells:
        return result
    if operation == 'add':
        result = reduce(operator.add, spells)
    elif operation == 'multiply':
        result = reduce(operator.mul, spells)
    elif operation == 'max':
        result = reduce(max, spells)
    elif operation == 'min':
        result = reduce(min, spells)
    else:
        raise ValueError("Unknown operation")
    return result


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:

    light_version = partial(base_enchantment, power=50, element="Light")
    earth_version = partial(base_enchantment, power=50, element="Earth")
    storm_version = partial(base_enchantment, power=50, element="Storm")

    return {"Light": light_version,
            "Earth": earth_version,
            "Storm": storm_version
            }

# def memoized_fibonacci(n: int) -> int:
#     pass


# def spell_dispatcher() -> Callable[[Any], str]:
#     pass


def main() -> None:
    spell_powers = [24, 10, 44, 10, 36, 30]
    operations = ['add', 'multiply', 'max', 'min', 'divation']
    print("Testing spell reducer...")
    try:
        for op in operations:
            print(op, end=": ")
            print(spell_reducer(spell_powers, op))
    except Exception as e:
        print(e)
    print("\nTesting partial enchanter")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} {target} with {power} power"

    enchants = partial_enchanter(base_enchantment)
    print(enchants["Light"](target="Sword"))
    print(enchants["Earth"](target="Shield"))
    print(enchants["Storm"](target="Staff"))
    print()
    fibonacci_tests = [15, 9, 12]


if __name__ == "__main__":
    main()

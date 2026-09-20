import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
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
        result = reduce(lambda a, b: a if a > b else b, spells)
    elif operation == 'min':
        result = reduce(lambda a, b: a if a < b else b, spells)
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


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return (memoized_fibonacci(n-1) + memoized_fibonacci(n-2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(arg: Any) -> str:
        return "Unknown spell type"

    @spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @spell.register(list)
    def _(arg: list[Any]) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return spell


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

    print("\nTesting memoized fibonacci...")
    fibonacci_tests = [0, 1, 10, 15]
    for fib in fibonacci_tests:
        print(f"Fib({fib}: {memoized_fibonacci(fib)}")
    print(memoized_fibonacci.cache_info())

    print("\nTesting spell dispatcher...")
    test = spell_dispatcher()
    print(test(42))
    print(test('fireball'))
    print(test(['firball', 42, 10.5, {"fr": "bonjour", "en": "morning"}]))
    print(test({"fr": "bonjour", "en": "morning"}))


if __name__ == "__main__":
    main()

from collections.abc import Callable


def mage_counter() -> Callable:
    cnt = 0

    def count() -> int:
        nonlocal cnt
        cnt += 1
        return cnt
    return count


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulator(add_power: int) -> int:
        nonlocal total
        total += add_power
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(name: str) -> str:
        return enchantment_type + " " + name
    return enchantment


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: object) -> None:
        vault[key] = value

    def recall(key: str) -> object:
        if key not in vault:
            return "Memory not found"
        return vault[key]
    return {'store': store, 'recall': recall}


def main() -> None:
    print("\nTesting mage counter...")
    a = mage_counter()
    b = mage_counter()
    print(f"counter_a call 1: {a()}")
    print(f"counter_a call 2: {a()}")
    print(f"counter_b call 1: {b()}")
    print(f"counter_a call 3: {a()}")

    print("\nTesting spell accumulator...")
    c = spell_accumulator(100)
    print(f"Base 100, add 20: {c(20)}")
    print(f"Base 100, add 30: {c(30)}")

    print('\nTesting enchantment factory...')
    d = enchantment_factory("Flaming")
    print(d("Sword"))
    e = enchantment_factory("Frozen")
    print(e("shield"))

    print("\nTesting memory vault...")
    f = memory_vault()
    print("Store 'secret' = 42")
    f['store']('secret', 42)
    print(f"Recall 'secret': {f['recall']('secret')}")
    print(f"Recall 'unknown': {f['recall']('unknown')}")


if __name__ == "__main__":
    main()

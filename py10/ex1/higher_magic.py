from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        spell = list(map(lambda s: s(target, power), spells))
        return spell
    return sequence


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def lightning(target: str, power: int) -> str:
        return f"Lightning strikes {target} for {power} damage"

    print("Testing spell combiner...")
    comb = spell_combiner(fireball, heal)
    test1 = comb("Dragon", 55)
    print(f"Combined spell result: {test1[0]}, {test1[1]}")
    print("\nTesting spell amplifier...")
    amp = power_amplifier(fireball, 3)
    test2 = amp('Dragon', 10)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {test2}")
    print("\nTesting conditional caster...")
    is_powerful = lambda trg, pwd: pwd > 10  # noqa : E731
    cond = conditional_caster(is_powerful, fireball)
    test3 = cond('Dragon', 40)
    print(f"Conditional result: {test3}")
    print("\nTesting spell sequence...")
    seq = spell_sequence([fireball, heal, lightning])
    test4 = seq('Dragon', 40)
    print(f"Sequence result: {test4}")


if __name__ == "__main__":
    main()

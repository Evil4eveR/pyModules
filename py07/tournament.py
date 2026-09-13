from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, DefensiveStrategy, AggressiveStrategy  # noqa: 501


def battle(creatures: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    n = len(creatures)
    print(f"{len(creatures)} opponents involved")
    participants = [(factory.create_base(), strategy) for factory, strategy in creatures]  # noqa: 501
    for i in range(n):
        for j in range(i+1, n):
            print("\n* Battle *")
            p1 = participants[i]
            p2 = participants[j]
            print(p1[0].describe())
            print("vs.")
            print(p2[0].describe())
            print("now fight!")
            try:
                p1[1].act(p1[0])
                p2[1].act(p2[0])
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
    print()


def main() -> None:
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(FlameFactory(), NormalStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])  # noqa: 501
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(FlameFactory(), AggressiveStrategy()), (HealingCreatureFactory(), DefensiveStrategy())])  # noqa: 501
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(AquaFactory(), NormalStrategy()),
            (HealingCreatureFactory(), DefensiveStrategy()),
            (TransformCreatureFactory(), AggressiveStrategy())
            ])


if __name__ == "__main__":
    main()

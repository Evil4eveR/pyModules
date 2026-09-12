#!/usr/bin/python3
from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factone: FlameFactory, facttow: AquaFactory) -> None:
    print("Testing battle")
    f1 = factone.create_base()
    f2 = facttow.create_base()
    print(f1.describe())
    print(" vs.")
    print(f2.describe())
    print(" fight!")
    print(f1.attack())
    print(f2.attack())


def main() -> None:
    test_factory(FlameFactory())
    print()
    test_factory(AquaFactory())
    print()
    test_battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()

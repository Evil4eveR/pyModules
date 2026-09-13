from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test(factory: CreatureFactory) -> None:
    print("Testing factory")
    b = factory.create_base()
    print(b.describe())
    print(b.attack())
    e = factory.create_evolved()
    print(e.describe())
    print(e.attack())
    print()


def battle(fac1: CreatureFactory, fac2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = fac1.create_base()
    c2 = fac2.create_base()
    print(c1.describe())
    print(" vs")
    print(c2.describe())
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    test(FlameFactory())
    test(AquaFactory())
    battle(FlameFactory(), AquaFactory())


if __name__ == "__main__":
    main()

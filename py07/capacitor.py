from ex0 import CreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def heal_test(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    b = factory.create_base()
    print(b.describe())
    print(b.attack())
    if isinstance(b, HealCapability):
        print(b.heal())
    print(" evolved:")
    e = factory.create_evolved()
    print(e.describe())
    print(e.attack())
    if isinstance(e, HealCapability):
        print(e.heal())


def transform_test(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    b = factory.create_base()
    print(b.describe())
    print(b.attack())
    if isinstance(b, TransformCapability):
        print(b.transform())
    print(b.attack())
    if isinstance(b, TransformCapability):
        print(b.revert())
    print(" evolved:")
    e = factory.create_evolved()
    print(e.describe())
    print(e.attack())
    if isinstance(e, TransformCapability):
        print(e.transform())
    print(e.attack())
    if isinstance(e, TransformCapability):
        print(e.revert())


def main() -> None:
    heal_test(HealingCreatureFactory())
    print()
    transform_test(TransformCreatureFactory())


if __name__ == "__main__":
    main()

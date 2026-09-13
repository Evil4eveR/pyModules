from abc import ABC, abstractmethod
from ex0 import Creature
from ex1.capabilities import HealCapability, TransformCapability


class BattleStrategy(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature):
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            assert isinstance(creature, TransformCapability)
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise Exception(f"Invalid Creature '{creature.name}' for this aggressive strategy")  # noqa: E501


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            assert isinstance(creature, HealCapability)
            print(creature.attack())
            print(creature.heal())
        else:
            raise Exception(f"Invalid Creature '{creature.name}' for this Defensive strategy")  # noqa: E501

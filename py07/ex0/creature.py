from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, c_type) -> None:
        self.name: str = name
        self.ctype: str = c_type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self.ctype} type Creature"

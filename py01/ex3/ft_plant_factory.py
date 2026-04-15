#!/usr/bin/env python3
import random as rnd


class Plant:
    name: str
    height: float
    p_age: int

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.p_age = age

    def __str__(self) -> str:
        return (
            f"{self.name.capitalize()}: {self.height:.1f}cm, "
            f"{self.p_age} days old"
        )

    def show(self) -> None:
        print(self.__str__())

    def age(self) -> None:
        self.p_age += 1

    def grow(self) -> None:
        self.age()
        self.height += rnd.uniform(0.1, 1.0)
        self.height = round(self.height, 1)


class FactoryPlant:
    plants: list[Plant]

    def __init__(self):
        self.plants = []

    def create(self, name: str, height: float, age: int) -> None:
        p = Plant(name, height, age)
        print("Created: " + str(p))
        self.plants += [p]


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    factory = FactoryPlant()
    factory.create("rose", 25, 30)
    factory.create("oak", 200, 365)
    factory.create("cactus", 5, 90)
    factory.create("sunflower", 80, 45)
    factory.create("fern", 15, 120)

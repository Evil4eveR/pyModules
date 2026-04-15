#!/usr/bin/env python3


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
        self.height += 0.8
        self.height = round(self.height, 1)


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    init_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for no in range(1, 8):
        print(f"=== Day {no} ===")
        rose.grow()
        rose.show()
    growth = rose.height - init_height
    print(f"Growth this week:{growth:.1f}cm")

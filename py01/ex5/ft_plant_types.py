#!/usr/bin/env python3


class Plant:
    name: str
    height: float = 0
    p_age: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height if height > 0 else 0
        self.p_age = age if age > 0 else 0

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.p_age} days old"

    def show(self) -> None:
        print(self)


class Flower(Plant):
    color: str

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def show(self) -> None:
        super().show()
        print(" Color:", self.color)

    def get_kind(self) -> None:
        print("=== Flower")
        self.show()
        print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully")

    def action(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.show()
        self.bloom()


class Tree(Plant):
    trunk_diameter: float

    def __init__(self, name: str, height: float, age: int, tr_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = tr_diameter

    def get_kind(self) -> None:
        print("=== Tree")
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def action(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self.produce_shade()


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: int

    def __init__(
            self,
            name: str,
            height: float,
            age: int,
            n_value: int,
            h_season: str
    ):
        super().__init__(name, height, age)
        self.nutritional_value = n_value
        self.harvest_season = h_season

    def show(self) -> None:
        super().show()
        print(" Harvest season:", self.harvest_season.capitalize())
        print(" Nutritional value:", self.nutritional_value)

    def get_kind(self) -> None:
        print("=== Vegetable")
        self.show()

    def produce_shade(self, age: int) -> None:
        self.p_age += age
        self.harvest_season = "May" if self.p_age > 30 else self.harvest_season
        self.nutritional_value += 20 if self.p_age >= 30 else 0
        self.show()

    def action(self) -> None:
        age = 20
        print(f"[make {self.name} grow and age for {age} days]")
        self.produce_shade(age)


def newline() -> None:
    print("")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    f = Flower("rose", 15, 10, "red")
    f.get_kind()
    f.action()
    newline()
    t = Tree("oak", 200, 365, 5)
    t.get_kind()
    t.action()
    newline()
    v = Vegetable("tomato", 5, 10, 0, "april")
    v.get_kind()
    v.action()

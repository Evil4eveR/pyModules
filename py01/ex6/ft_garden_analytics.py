#!/usr/bin/env python3


class Plant:
    name: str
    height: float = 0
    p_age: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height if height > 0 else 0
        self.p_age = age if age > 0 else 0
        self._stats = self._Stats(0, 0, 0, self.name)

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.p_age} days old"

    def show(self) -> None:
        self._stats.show_state += 1
        print(self)

    def age(self) -> None:
        self.p_age += 20
        self._stats.age_state += 1

    def grow(self) -> None:
        self._stats.grow_state += 1
        self.height += 8
        self.height = round(self.height, 1)

    @staticmethod
    def check_age(ag: int) -> None:
        print(f"Is {ag} days more than a year? -> {ag > 365}")

    @classmethod
    def anonymous(cls) -> None:
        print("=== Anonymous")
        anonymous = cls("Unknown plant", 0, 0)
        anonymous.show()
        anonymous._stats.state_print()

    class _Stats:
        grow_state: int
        age_state: int
        show_state: int
        name: str

        def __init__(self, grow: int, age: int, show: int, name: str) -> None:
            self.grow_state = grow
            self.age_state = age
            self.show_state = show
            self.name = name

        def state_print(self) -> None:
            print(f"[statistics for {self.name}]")
            print(f"Stats: {self.grow_state} grow, " +
                  f"{self.age_state} age, {self.show_state} show")


class Flower(Plant):
    color: str
    bloomed: bool

    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def get_kind(self) -> None:
        print("=== Flower")
        self.show()
        self._stats.state_print()

    def show(self) -> None:
        super().show()
        print(" Color:", self.color)
        if self.bloomed:
            print(f"{self.name} is blooming beautifully")
        else:
            print(f" {self.name} has not bloomed yet")

    def grow(self) -> None:
        self.bloomed = True
        super().grow()

    def action(self) -> None:
        print(f"[asking the {self.name} to grow and bloom]")
        self.grow()
        self.show()
        self._stats.state_print()


class Tree(Plant):
    trunk_diameter: float
    shade_cnt: int

    def __init__(self, name: str, height: float, age: int, tr_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = tr_diameter
        self.shade_cnt = 0

    def get_kind(self) -> None:
        print("=== Tree")
        self.show()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")
        self._stats.state_print()
        print(self.shade_cnt, "shade")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )
        self.shade_cnt += 1

    def action(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        self.produce_shade()
        self._stats.state_print()
        print(self.shade_cnt, "shade")


class Seed(Flower):
    seeds: int

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def get_kind(self) -> None:
        print("=== Seed")
        self.show()

    def show(self) -> None:
        super().show()
        print(" Seeds:", self.seeds)

    def action(self) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        self.grow()
        self.height = 110
        self.age()
        self.seeds += 42
        self.show()
        self._stats.state_print()


def newline() -> None:
    print("")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    newline()
    f = Flower("Rose", 15, 10, "red")
    f.get_kind()
    f.action()
    newline()
    t = Tree("Oak", 200, 365, 5)
    t.get_kind()
    t.action()
    newline()
    s = Seed("Sunflower", 80, 45, "yellow")
    s.get_kind()
    s.action()
    newline()
    Plant.anonymous()

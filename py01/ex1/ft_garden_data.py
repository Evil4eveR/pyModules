#!/usr/bin/env python3
class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(
            f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"
        )


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("rose", 25, 30).show()
    Plant("sunflower", 80, 45).show()
    Plant("cactus", 15, 120).show()

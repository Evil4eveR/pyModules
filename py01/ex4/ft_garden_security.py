#!/usr/bin/env python3

class Plant:
    __name: str
    __height: float = 0
    __p_age: int = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name = name.capitalize()
        self.__height = height if height > 0 else 0
        self.__p_age = age if age > 0 else 0

    def __str__(self) -> str:
        return (
            f"{self.__name}: {self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )

    def get_height(self) -> float:
        return (self.__height)

    def get_age(self) -> int:
        return (self.__p_age)

    def set_height(self, height: float) -> None:
        if (height > 0):
            self.__height = height
            self.ft_success("Height")
            return
        self.ft_error("Height")

    def set_age(self, age: int) -> None:
        if (age > 0):
            self.__p_age = age
            self.ft_success("Age")
            return
        self.ft_error("Age")

    def show(self) -> None:
        print("Plant created:", self.__str__())

    def ft_error(self, attributes) -> None:
        print(f"{self.__name}: Error, {attributes} can't be negative")
        print(f"{attributes} update rejected")

    def ft_success(self, attributes) -> None:
        if (attributes == "Height"):
            print(f"Height updated: {self.get_height():.1f}cm")
        elif (attributes == "Age"):
            print(f"Age updated: {self.get_age()} days")


def newline() -> None:
    print("")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant = Plant("rose", 15, 10)
    plant.show()
    newline()
    plant.set_height(25)
    plant.set_age(30)
    newline()
    plant.set_height(-5)
    plant.set_age(-30)
    newline()
    print(f"Current status: {plant}")

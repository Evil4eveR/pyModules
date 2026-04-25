import math


def get_player_pos() -> tuple:
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        lst = coords.split(",")
        if len(lst) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(lst[0])
            y = float(lst[1])
            z = float(lst[2])
            return (x, y, z)
        except ValueError as e:
            err_prmtr = None
            for l1 in lst:
                try:
                    float(l1)
                except ValueError:
                    err_prmtr = l1
                    break
            print(f"Error on parameter '{err_prmtr}' : {e}")


def distance_3d(p1: tuple, p2: tuple) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={round(first[0], 1)}, Y={round(first[1], 1)},"
          + f" Z={round(first[2], 1)}")
    print(f"Distance to center:{distance_3d((0, 0, 0), first):.4f}")
    print("Get a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates:"
          + f" {distance_3d(first, second):.4f}")


if __name__ == "__main__":
    main()

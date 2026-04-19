#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

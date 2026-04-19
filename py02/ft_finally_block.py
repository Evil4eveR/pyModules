#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, messge="Unknown plant error"):
        super().__init__(messge)


def water_plant(plant_name) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("\nTesting Valide plants...")
    print("Opening watering system")
    try:
        plants = ["Tomato", "Lettuce", "Carrots"]
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")
    print("\nTesting invalid plants...")
    try:
        plants = ["Tomato", "lettuce", "Carrots"]
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()

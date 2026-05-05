#!/usr/bin/env python3


class PlantError(Exception):
    def __init__(self, msg: str = ("Unknown plant error")) -> None:
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


valid_list = ("Tomato", "Lettuce", "Carrots")
invalid_list = ("Tomato", "lettuce")


def test_watering_system(valid_list: tuple[str, ...]) -> None:

    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in valid_list:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    finally:
        print("Closing watering system\n")

    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in invalid_list:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print("... ending tests and returning to main")
    finally:
        print("Closing watering system\n")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system(valid_list)
    print("Cleanup always happens, even with errors!")

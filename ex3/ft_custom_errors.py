#!/usr/bin/env python3


class GardenError(Exception):
    def __init__(self, msg: str = ("Unknown plant error")) -> None:
        self.msg = msg
        super().__init__(self.msg)


class PlantError(GardenError):
    def __init__(self, msg: str = ("Unknown plant error")) -> None:
        super().__init__(msg)


class WaterError(GardenError):
    def __init__(self, msg: str = ("Unknown plant error")) -> None:
        super().__init__(msg)


def perror(name: str, wilt: bool) -> None:
    if wilt:
        raise PlantError(f"The {name} plant is wilting!")


def werror(water: int) -> None:
    if water < 8:
        raise WaterError("Not enough water in the tank!")


if __name__ == '__main__':
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        perror("tomato", True)
    except PlantError as error:
        print(f"Caught PlantError: {error}\n")

    print("Testing WaterError")
    try:
        werror(7)
    except WaterError as error:
        print(f"Caught WaterError: {error}\n")

    print("Testing catching all garden errors...")
    try:
        perror("tomato", True)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        werror(5)
    except GardenError as error:
        print(f"Caught GardenError: {error}\n")

    print("All custom error types work correctly!")

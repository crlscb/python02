#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    list = ["25", "abc"]

    for temp in list:
        print(f"Input data is '{temp}'")

        try:
            print(f"Temperature is now {input_temperature(temp)}ºC\n")

        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")

    print("All test completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()

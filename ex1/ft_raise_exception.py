#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int >= 40:
        raise ValueError(f"{temp_int}ºC is too hot for plants (max 40ºC)")
    elif temp_int <= 0:
        raise ValueError(f"{temp_int}ºC is too cold for plants (min 0ºC)")
    else:
        return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Cheker ===\n")

    list = ["25", "abc", "100", "-50"]

    for temp in list:
        print(f"Input data is '{temp}'")

        try:
            print(f"Temperature is now' {input_temperature(temp)}ºC\n")

        except ValueError as error:
            print(f"Caught input_temperature error: {error}\n")

    print("All tests completed - program didn't crash!")


if __name__ == '__main__':
    test_temperature()

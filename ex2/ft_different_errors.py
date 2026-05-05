#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    print(f"Testing operations {operation_number}...")
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        int("abc" + 2)
    else:
        return


def test_error_types() -> None:
    try:
        garden_operations(0)
    except ValueError as error:
        print(f"Caught ValueErrro: {error}")
    try:
        garden_operations(1)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    try:
        garden_operations(2)
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    try:
        garden_operations(3)
    except (ValueError, TypeError) as error:
        print(f"Caught TypeError: {error}")
    try:
        garden_operations(4)
    except Exception as error:
        print(f"Other error {error}")
    print("Operation completed successfully\n")


if __name__ == "__main__":
    test_error_types()
    print("All error types successfully!")

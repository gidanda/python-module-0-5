def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp_int = int(temp_str)
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()

    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")

    print()

    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except Exception as error:
        print(f"Caught input_temperature error: {error}")

    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
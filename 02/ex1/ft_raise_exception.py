def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp_int = int(temp_str)
    
    if temp_int > 40:
        raise ValueError(
            f"{temp_int}°C is too hot for plants (max 40°C)"
        )
    
    if temp_int < 0:
        raise ValueError(
            f"{temp_int}°C is too cold for plants (min 0°C)"
        )
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print()

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Input data is '{value}'")
        try:
            temperature = input_temperature(value)
            print(f"Temperature is now {temperature}°C")
        except Exception as error:
            print(f"Caught input_temperature error: {error}")
        print()

    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    test_temperature()
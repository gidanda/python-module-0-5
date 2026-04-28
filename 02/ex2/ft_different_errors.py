def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "plant" + 3
    else:
        return
    
def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    i = 0
    while i < 5:
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
        i += 1

    print()

    print("Testing multiple error catch...")
    try:
        garden_operations(0)
    except (
        ValueError,
        ZeroDivisionError,
        FileNotFoundError,
        TypeError,
    ) as error:
        print(f"Caught one of multiple error types: {error}")
    print("All error types tested successfully!")

if __name__ == '__main__':
    test_error_types()
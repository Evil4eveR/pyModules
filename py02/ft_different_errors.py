#!/usr/bin/env python3
from builtins import ValueError


def garden_operations(operation_number) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42/0
    elif operation_number == 2:
        open("non_existent_file.txt", "r")
    elif operation_number == 3:
        "42" + 42
    else:
        print("Operation completed successfully!")
        return None


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError:
            print("Caught ValueError: invalid literal for int() "
                  + "with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: [Errno 2] No such file "
                  + "or directory: '/non/existent/file'")
        except TypeError:
            print("Caught TypeError: can only concatenate str "
                  + "(not \"int\") to str")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

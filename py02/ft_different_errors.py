#!/usr/bin/env python3
from builtins import ValueError

def garden_operations(operation_number) -> Exception:
    try:
        if (operation_number == 0):
            return ValueError
        elif (operation_number == 1):
            return ZeroDivisionError
        elif (operation_number == 2):
            return FileNotFoundError
        elif (operation_number == 3):
            return TypeError    
        else:
            return
        

def test_error_types() -> None:
    


if __name__ == "__main__":
    test_error_types()
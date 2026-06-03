import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"testing create_fire: {alchemy.create_air()}")
    print("Now show that not all functions can be reached")
    print("This raise an exception!")
    print(f"Testing create_fire: {alchemy.create_earth()}")

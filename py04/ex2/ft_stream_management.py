import sys


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    if (len(sys.argv) < 2):
        print(f"Usage: {sys.argv[0]} <file>")
        return None
    try:
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        with open(filename, "r") as f:
            print("---")
            data = f.read()
            print(data)
            print("---")
        print(f"File '{filename}' closed.")
        print("\nTransform data")
        print("---")
        transform_data = data.strip().split("\n")
        for line in transform_data:
            print(line + "#")    
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_file = sys.stdin.readline().strip()
        print(f"Saving data to '{new_file}'")
        if (new_file):
            with open(new_file, "w") as f:
                for line in transform_data:
                    f.write(line + "#" + "\n")
            print(f"Data saved in file '{new_file}'.")
        else:
            print("Data not saved.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()

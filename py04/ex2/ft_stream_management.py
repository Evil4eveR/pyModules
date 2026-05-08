import sys


def main() -> None:
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    if (len(sys.argv) < 2):
        print(f"Usage: {sys.argv[0]} <file>")
        return None
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename, "r")
        print("---")
        data = f.read()
        print(data)
        print("---")
        f.close()
        print(f"File '{filename}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}", file=sys.stderr)
        return
    transform_data = data.split("\n")
    print("\nTransform data:")
    print("---")
    for line in transform_data:
        if line:
            print(line + "#")
    print("---")
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_file = sys.stdin.readline().strip()
    if (new_file):
        print(f"Saving data to '{new_file}'")
        try:
            f = open(new_file, "w")
            for line in transform_data:
                if line:
                    f.write(line + "#" + "\n")
            f.close()
            print(f"Data saved in file '{new_file}'.")
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{new_file}': {e}", file=sys.stderr)
            print("Data not saved.")
            return
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()

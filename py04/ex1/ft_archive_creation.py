import sys


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return None
    print("=== Cyber Archives Recovery ===")
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        transform_data = ""
        f = open(filename, "r")
        print("---")
        for line in f:
            print(line.strip())
            transform_data += line.strip()+"#\n"
        print("---")
        print(f"File '{filename}' closed.")
        print("\nTransform data:")
        print("---")
        print(transform_data.strip())
        print("---")
        f.close()
        save = input("Enter new file name (or empty):").strip()
        if (save):
            print(f"Saving data to '{save}'")
            newfile = open(save, "w")
            newfile.write(transform_data.strip())
            newfile.close()
            print(f"Data saved in file '{save}'.")
        else:
            print("Not saving data.")
            return
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()

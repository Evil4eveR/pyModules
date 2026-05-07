import sys


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return None
    print("=== Cyber Archives Recovery ===")
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename)
        content = f.read()
        print(f"---\n{content}\n---")
        f.close()
        print(f"File '{filename}' closed.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()

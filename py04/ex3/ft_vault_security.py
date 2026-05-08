def secure_archive(filename: str, action: str = "read", content: str = ""
                   ) -> tuple[bool, str]:
    try:
        if (action == "read"):
            with open(filename, "r") as f:
                content = f.read()
                return (True, content)
        elif (action == "write"):
            with open(filename, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        else:
            return (False, "action Error")
    except Exception as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")
    tests = [
        "Using 'secure_archive' to read from a nonexistent file:",
        "Using 'secure_archive' to read from an inaccessible file:",
        "Using 'secure_archive' to read from a regular file:",
        "Using 'secure_archive' to write previous content to a new file:"
    ]
    filesname = ["nonexistent", "inaccessible.txt", "y.txt", "newfile.txt"]
    for i in range(len(filesname)):
        if (i < 3):
            print(f"\n{tests[i]}")
            print(secure_archive(filesname[i], "read"))
        else:
            print(f"\n{tests[i]}")
            success, content = secure_archive(filesname[2], "read")
            if success:
                print(secure_archive(filesname[i], "write", content))
            else:
                print("Content not written to file")


if __name__ == "__main__":
    main()

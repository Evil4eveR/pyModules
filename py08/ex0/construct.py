import os
import sys
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    is_venv = is_in_venv()
    current_py = sys.executable
    if is_venv:
        env_path = sys.prefix
        env_name = os.path.basename(env_path)
        site_pack = site.getsitepackages()[0]
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {current_py}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(site_pack)
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current_py}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == "__main__":
    main()

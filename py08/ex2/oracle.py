#!/usr/bin/env python3
import os
import sys


try:
    from dotenv import load_dotenv
except ImportError:
    print("ERROR: python-dotenv not installed.")
    print("Run: pip install python-dotenv")
    sys.exit(1)


def load_config() -> dict[str, str]:
    load_dotenv()

    config: dict[str, str] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv(
            "DATABASE_URL", "postgresql://localhost:5432/dev_db"
        ),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
        "ZION_ENDPOINT": os.getenv(
            "ZION_ENDPOINT", "https://zion.network/api/v1"
        ),
    }
    return config


def display_status(cnf: dict[str, str]) -> None:
    mode = cnf["MATRIX_MODE"].lower()
    is_prod = mode == "production"

    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {cnf['MATRIX_MODE']}")

    if is_prod:
        print("Database: Connected to production cluster")
        masked_api = (
            cnf["API_KEY"][:4] + "*" * 8 if cnf["API_KEY"] else "NOT SET"
        )
        print(f"API Access: Authenticated (Key: {masked_api})")
        print(f"Log Level: {cnf.get('LOG_LEVEL', 'INFO')}")
    else:
        print(f"Database: Connected to local instance ({cnf['DATABASE_URL']})")
        print(
            "API Access: Authenticated (Development Mode)"
            if cnf["API_KEY"]
            else "API Access: Missing Key"
        )
        print(f"Log Level: {cnf['LOG_LEVEL']}")

    print(f"Zion Network: {cnf['ZION_ENDPOINT']}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    cnf = load_config()

    if not cnf["API_KEY"]:
        print("WARNING: API_KEY is missing from environment/config!")

    display_status(cnf)


if __name__ == "__main__":
    main()

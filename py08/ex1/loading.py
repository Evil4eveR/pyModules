import sys
import importlib.metadata
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "requests": "Network access ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> bool:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    all_installed = True
    for pkg, desc in REQUIRED_PACKAGES.items():
        try:
            version = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - {desc}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {pkg} - Not installed!")
            all_installed = False

    if not all_installed:
        print("\nERROR: Missing dependencies detected!")
        print("To install using pip, run:")
        print("  pip install -r requirements.txt")
        print("To install using Poetry, run:")
        print("  poetry install")
        return False

    return True


def run_matrix_analysis() -> None:
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    np.random.seed(42)
    signal = np.random.normal(loc=0, scale=1, size=1000)
    noise = np.random.uniform(low=-0.5, high=0.5, size=1000)
    matrix_stream = signal + noise

    df = pd.DataFrame({"Stream_ID": np.arange(1000), "Data_Signal": matrix_stream})  # noqa:501
    df["Rolling_Mean"] = df["Data_Signal"].rolling(window=20).mean()

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.plot(df["Stream_ID"], df["Data_Signal"], alpha=0.4, label="Raw Matrix Signal")  # noqa:501
    plt.plot(df["Stream_ID"], df["Rolling_Mean"], color="red", label="Filtered Stream")  # noqa:501
    plt.title("Matrix Data Stream Analysis")
    plt.xlabel("Data Points")
    plt.ylabel("Signal Amplitude")
    plt.legend()
    plt.grid(True)

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    if not check_dependencies():
        sys.exit(1)
    run_matrix_analysis()


if __name__ == "__main__":
    main()

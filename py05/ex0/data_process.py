from abc import ABC, abstractmethod
from typing import Any, Sequence


class DataProcessor(ABC):
    def __init__(self):
        self.ingested = []
        self.rank = 1
        super().__init__()

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not len(self.ingested):
            raise Exception("Got exception: data empty")
        return self.ingested.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        numtup = (int, float)
        if isinstance(data, numtup):
            return True
        elif isinstance(data, list):
            if not len(data):
                return False
            return all(isinstance(d, numtup) for d in data)
        return False

    def ingest(self, data: int | float | Sequence[int | float]) -> None:
        numtup = (int, float)
        if not self.validate(data):
            raise Exception("Got exception: Improper numeric data")
        elif isinstance(data, numtup):
            self.ingested.append((self.rank, str(data)))
            self.rank += 1
        elif isinstance(data, list):
            for dat in data:
                self.ingested.append((self.rank, str(dat)))
                self.rank += 1


class TextProcessor(DataProcessor):
    def __init__(self):
       super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            if not len(data):
                return False
            return all(isinstance(dat, str) for dat in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Got exception: Improper Text data")
        if isinstance(data, str):
            self.ingested.append((self.rank, data))
            self.rank += 1
        elif isinstance(data, list):
            for dat in data:
                self.ingested.append((self.rank, dat))
                self.rank += 1


class LogProcessor(DataProcessor):
    pass


def main() -> None:
    print("\nTesting Numeric Processor...")
    np = NumericProcessor()
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate("Hello")}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except Exception as e:
        print(e)
    testnum = [1, 2, 3, 5, 4]
    print(f"Processing data:{testnum}")
    try:
        np.ingest(testnum)
    except Exception as e:
        print(e)
    print("Extracting 3 values...")
    for i in range(3):
        print(f"Numeric value {i}: {np.output()[1]}")
    print("\nTesting Text Processor...")
    tp = TextProcessor()
    print(f"Trying to validate input '42': {tp.validate(42)}")
    teststr = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {teststr}")
    try:
        tp.ingest(teststr)
    except Exception as e:
        print(e)
    print("Extracting 1 value...")
    for i in range(1):
        print(f"Numeric value {i}: {tp.output()[1]}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    main()

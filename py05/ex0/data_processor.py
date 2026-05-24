from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.ingested = []
        self.rank = 1
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    
    def output(self) -> tuple[int, str]:
        if not len(self.ingested):
            raise Exception("Got exception: No data to output")
        return self.ingested.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        nmtype = (int, float)
        if isinstance(data,nmtype):
            return True
        elif isinstance(data, list):
            if not len(data):
                return False
            return all(isinstance(x,nmtype) for x in data)
        return False

    def ingest(self, data: int | float | list[float | int]) -> None:
        if not self.validate(data):
            raise Exception ("Got exception: Improper numeric data")
        else:
            print("Processing data:", data)
            if isinstance (data, (int, float)):
                self.ingested.append((self.rank, str(data)))
                self.rank+=1
            else:
                for d in data:
                    self.ingested.append((self.rank, str(d)))
                    self.rank+=1

class TextProcessor(DataProcessor):
    pass


class LogProcessor(DataProcessor):
    pass


def numptest() -> None:
    print("Testing Numeric Processor...")
    np = NumericProcessor()
    test = np.validate(42)
    print(f"Trying to validate input '{42}': {test}")
    test = np.validate("Hello")
    print(f"Trying to validate input '{"Hello"}': {test}")
    try:
        print(f"Test invalid ingestion of string '{"foo"}' without prior validation:")
        np.ingest("foo")
    except Exception as e:
        print(e)
    input = [1, 8, 3, 4, 5]
    np.ingest(input)
    print("Extracting 3 values...")
    for i in range(3):
        tpl = np.output()
        print((f"Numeric value {i}: {tpl[1]}"))

def main():
    print("=== Code Nexus - Data Processor ===\n")
    numptest()

if __name__ == "__main__":
    main()




from abc import ABC, abstractmethod
from typing import Any
import typing


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.ingested: list[tuple[int, str]] = []
        self.rank = 1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def _store(self, value: str):
        self.ingested.append((self.rank, value))
        self.rank += 1

    def output(self) -> tuple[int, str]:
        if not self.ingested:
            raise ValueError("Got exception: data empty")
        return self.ingested.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        numtup = (int, float)
        if isinstance(data, numtup):
            return True
        elif isinstance(data, list):
            return all(isinstance(d, numtup) for d in data)
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        numtup = (int, float)
        if not self.validate(data):
            raise ValueError("Got exception: Improper numeric data")
        elif isinstance(data, numtup):
            self._store(str(data))
        elif isinstance(data, list):
            for dat in data:
                self._store(str(dat))


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(dat, str) for dat in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper Text data")
        if isinstance(data, str):
            self._store(data)
        elif isinstance(data, list):
            for dat in data:
                self._store(dat)


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str):
                    return False
                if not isinstance(v, str):
                    return False
            return True
        elif isinstance(data, list):
            return all(isinstance(itm, dict) and
                       all(isinstance(k, str) and isinstance(v, str)
                           for k, v in itm.items())
                       for itm in data)
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Got exception: Improper Log data")
        if isinstance(data, dict):
            dic_str = (f"{data['log_level']}: {data['log_message']}")
            self._store(dic_str)
        if isinstance(data, list):
            for dat in data:
                dic_str = (f"{dat['log_level']}: {dat['log_message']}")
                self._store(dic_str)


class DataStream():
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        if not len(self.processors):
            print("No processor found, no data")
            return
        for st in stream:
            processed = False
            for pro in self.processors:
                if (pro.validate(st)):
                    pro.ingest(st)
                    processed = True
                    break
            if not processed:
                print("DataStream error - Can't process " +
                      f"element in stream: {st}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return
        for pro in self.processors:
            dpcnt = pro.rank - 1
            remaining = len(pro.ingested)
            print(f"{pro.__class__.__name__}: total {dpcnt} items " +
                  f"processed,remaining {remaining} on processor")


def testing() -> None:
    print("== DataStream statistics ==")
    ds = DataStream()
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    ds.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    ds.register_processor(np)
    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING',
               'log_message': 'Telnet access! Use ssh instead'},
              {'log_level': 'INFO',
               'log_message': 'User wil isconnected'}],
             42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch}")
    ds.process_stream(batch)
    print("== DataStream statistics ==")
    ds.print_processors_stats()
    print("\nRegistering other data processors")
    ds.register_processor(tp)
    ds.register_processor(lp)
    print("Send the same batch again")
    print("== DataStream statistics ==")
    ds.process_stream(batch)
    ds.print_processors_stats()
    print("\nConsume some elements from the data processors:"
          " Numeric 3, Text 2, Log 1")
    print("== DataStream statistics ==")
    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    lp.output()
    ds.print_processors_stats()


def main() -> None:
    print("\nInitialize Data Stream...")
    testing()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    main()

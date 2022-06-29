"""
Utilities for debugging Rust programs.

"""

import gdb
import typing


class Vector:
    """
    Wrapper for easy processing of vectors.

    """

    def __init__(self, vector: gdb.Value) -> None:
        """
        Initialize a :class:`.Vector`.

        """

        self.vector = vector

    def __len__(self) -> int:
        return int(self.vector["len"])

    def __iter__(self) -> typing.Iterator[gdb.Value]:
        pointer = self._start_pointer()
        for _ in range(len(self)):
            yield pointer.referenced_value()
            pointer += 1

    def __reversed__(self) -> typing.Iterator[gdb.Value]:
        pointer = self._start_pointer() + len(self) - 1
        for _ in range(len(self)):
            yield pointer.referenced_value()
            pointer -= 1

    def __getitem__(self, index: int) -> gdb.Value:
        if index >= len(self) or index < -len(self):
            raise IndexError("Index out of range.")
        if index < 0:
            index += len(self)

        pointer = self._start_pointer() + index
        return pointer.referenced_value()

    def _start_pointer(self) -> gdb.Value:
        return self.vector["buf"]["ptr"]["pointer"]

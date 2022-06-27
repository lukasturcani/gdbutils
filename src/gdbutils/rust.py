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
        start = self.vector["buf"]["ptr"]["pointer"]
        for _ in len(self):
            yield start.reference_value()
            start += 1

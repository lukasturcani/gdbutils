import gdb
import typing


def vector_data(
    vector: gdb.Value,
) -> typing.Iterator[gdb.Value]:

    vector_size = int(vector["len"])
    start = vector["buf"]["ptr"]["pointer"]
    for _ in range(vector_size):
        yield start.referenced_value()
        start += 1

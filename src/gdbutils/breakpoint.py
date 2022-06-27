"""
Breakpoint utilities.

"""

import gdb
import typing


def reset(
    spec: str,
    breakpoint: typing.Callable[[str], gdb.Breakpoint],
) -> None:
    """
    Set a breakpoint, deleting the previous one at the same position.

    """

    try:
        gdb.execute(f"clear {spec}")
    except gdb.error:
        pass
    breakpoint(spec)

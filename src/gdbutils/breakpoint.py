import gdb
import typing


def reset_breakpoint(
    spec: str,
    breakpoint: typing.Callable[[str], gdb.Breakpoint],
) -> None:

    try:
        gdb.execute(f"clear {spec}")
    except gdb.error:
        pass
    breakpoint(spec)

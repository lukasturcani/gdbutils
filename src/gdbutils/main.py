"""
Run GDB commands.

"""

import importlib

import gdbutils._main

importlib.reload(gdbutils._main)
gdbutils._main.main()

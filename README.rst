========
gdbutils
========

Utilties for the GDB Python API.


Installation
============

The gdbutils library should be importable by GDB within the Python
sessions it launches. One way to do this is to add the path to gdbutils
to GDB in the ``.gdbinit`` script:

.. code-block:: python

    python
    import os
    sys.path.append("path/to/gdbutils/src")
    end


Usage
=====

First create the file ``src/gdbutils/_main.py``. This file is excluded
from source control by the repo, as you are expected to edit it while
debugging. It should define a ``main()`` function:

.. code-block:: python

    # src/gdbutils/_main.py

    def main() -> None:
        # Code you want GDB to run goes here.
        ...

The ``main()`` function should contain the code you want GDB to execute
during debugging.

Next, once GDB is launched, run the following command:

.. code-block:: python

    (gdb) python import gdbutils.main;import importlib;importlib.reload(gdbutils.main)

This will import the ``gdbutils.main`` script. The use of
``importlib.reload()`` means that changes to
``src/gdbutils/_main.py`` made while GDB was open will be propagated,
as Python normally caches module imports. Importing the
``gdbutils.main`` module will run the ``main()`` function defined in
your ``src/gdbutils/_main.py`` file.

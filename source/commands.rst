----------------------
Command line options
----------------------

*Themis* usage is done via Linux command line as follows

.. code-block:: none

   themis [RUNTYPE] [GRID]


[RUNTYPE] options are:

.. code-block:: none

   --run

to start a new calculation

.. code-block:: none 

   --rerun

to calculate properties from interaction energies obtined previously. In this case, an
``energy.bin`` file will be read if these energy values were obtained whit *themis* or an
``energy.log`` file will be read if these energy values were obtained externally. Whit the
former is useful to obtain thermodynamic properties using a different temperature from a
previous calculation, the latter is useful to obtain thermodynamics properties using quantum
chemistry interaction energies.


[GRID] options are:

.. code-block:: none

   --shell <radius>

indicates that translation moves will be performed on a spherical shell around the reference
molecule (generated on the run). The real argument ``<radius>`` is the scaling factor for the
radius (in Angstrom).

.. code-block:: none

   --user <file.xyz>

indicates that translation moves will be performed on an user-defined grid read from
``<file.xyz>``. It must be aligned with molecule 1 and can be generated using the ``sas_grid``
utility (found in the ``utils/`` folder).


Other valid options are ``--help``, ``--citation``, ``--license`` and ``--plot``.

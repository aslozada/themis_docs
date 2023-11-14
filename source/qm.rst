-----------------------------
Using QM interaction energies
-----------------------------

Calculations using *Themis* + *MOPAC* were performed for the bipheny dimers (please see *Themis* main
reference for more details) in multiple steps. For each intermolecular distance:

*i.* Write *MOPAC* input files for all valid configuration using the following ``INPUT`` options along
with the following coordinate files ``conf1.xyz`` and ``conf2.xyz`` for P-Biphenyl

.. code-block:: none

   translation_factor : 3
   rot1_factor : 4
   rot2_factor : 36
   rot2_range : 360.0
   temperature : 300.0
   potential : none
   ref_mol1 : 23
   rot_ref_mol2 : 1
   shortest_distance : 1.2
   write_xtc : no
   lowset_strucutures : 10
   write_frames : MOP
   mopac_job : MOP PM7 iscf output threads=1 shift=1.0 itry=150
   cutoff_distance : 0.0




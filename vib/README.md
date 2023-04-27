# Part 2: Vibrational analysis of the transition state

The transition state (TS) is a first-order saddle-point on the multi-dimensional
potential energy surface (PES). In other words, it is a maximum along the reaction
path and a minimum in all other directions. This means that a vibrational analysis
of the TS should yield exactly one imaginary vibrational mode. This technique is
frequently used to verify that a TS was really found.

## Task 2.1 – Fixing the input files and submitting the calculation

1. Move to the `sscc-qc-inter/vib/` directory, copy the TS structure and
   wave function restart there and edit the input files (replace `TODO`):
   * Fix coordinate and wavefunction restart filenames
   * The initial density guess (`SCF_GUESS`) is made based on `RESTART`
   * The wave-function file from earlier calculation (`WFN_NAME`) should be `enol-neb-BAND5-RESTART.wfn`
   * Coordinates-file from earlier calculation (`XYZ_NAME`) should be `enol-neb-pos-Replica_nr_5-1.xyz`
   * `RUN_TYPE` should be `VIBRATIONAL_ANALYSIS`

   ```bash
   $ cd ../vib
   $ cp ../neb/enol-neb-BAND5-RESTART.wfn .
   $ cp ../neb/enol-neb-pos-Replica_nr_5-1.xyz .
   $ grep TODO *.in*  # fix all matches
   ```

2. Submit the job and, after a few minutes, inspect the produced `.mol` file:

   ```bash
   $ sbatch cp2k.sh
   $ less enol-vib-VIBRATIONS-1.mol
   ```

3. Is there only one imaginary (negative) frequency? How many vibrational modes
   are there in total? Why?
   * Hint: Think about degrees of freedom

**Continue the hands-on with [Part 3](../hybrid/README.md).**

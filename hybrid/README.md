# Part 3: Re-converging the NEB minimum energy profile using the PBE0 hybrid functional

Due to self-interaction error and resulting electron overdelocalization, reaction
barriers are underestimated by semilocal exchange–correlation functionals such as
PBE. Hybrid functional that include a fraction of exact Hartree–Fock (HF) exchange
can mitigate this. We will now re-converge the energies of the NEB images optimized
at the PBE level using the hybrid PBE0 functional.

## Task 3.1 – Fixing the input files and submitting the calculation

1. Move to the `sscc-qc-inter/hybrid/` directory and edit the input files:
   * We will now only run single-point energy calculations, so `RUN_TYPE` should
     be `ENERGY`
   * PBE0 replaces 25% of the PBE exchange with exact HF exchange

   ```bash
   $ cd ../hybrid
   $ cp ../neb/*1.xyz .
   $ cp ../neb/*.wfn .
   $ grep TODO *.in*  # fix all matches
   ```

2. To run all images efficiently at the same time, we will use the `FARMING`
   program of CP2K
   * The farming method is actually used "under the hood" also in the NEB and
     normal mode calculations
   * The input files `hybrid-*.inp` for each image are now specified in the master
     `farming.inp` input. We again request one Mahti node so each image will be
     allocated 16 cores.
3. Submit the job as usual with `sbatch cp2k.sh`

## Task 3.2 – Analysis

1. Once the job has finished (should only take about a minute), extract and plot
   the PBE0 energy profile for the proton transfer (in meV):

   ```bash
   $ grep "ENERGY|" *.out | awk '{print $10}' > energy.txt
   $ module load gnuplot
   $ gnuplot
   gnuplot> y0=system("head -1 energy.txt")
   gnuplot> plot "energy.txt" using (27211.38*($1-y0)) with linespoints
   ```

2. Did the barrier height improve compared to the PBE results?
3. Calculate the equilibrium constant for the reaction based on:
   
   $$K\approx\exp(-\Delta E/k_\mathrm{B}T)$$

4. NMR results suggest that there should be a 76%–24% split between the enol
   forms. Does your results agree with this?

**Continue the hands-on with [Part 4](../aimd/README.md).**

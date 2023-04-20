# Part 4: *Ab initio* molecular dynamics simulation of 2-formylcyclohexanone in aqueous solution

Standard classical MD simulations are unable to describe chemical reactions such
as proton transfer. In *ab initio* molecular dynamics (AIMD) simulations the forces
are calculated at each time step from first principles instead of a parametrized
empirical force field. Atoms are thus free to move however they please, making bond
making and breaking possible. AIMD simulations are very heavy and can typically be
run only for about ~100 ps. It is therefore typically not possible to observe
chemical reactions without applying some external bias on the system. However,
in the present case the proton transfer barrier is so low (about the size of the 
thermal energy) that we can see and sample it.

## Task 4.1 – Solvating the enol system

1. Move to the `sscc-qc-inter/aimd/` directory and solvate the enol molecule:
   * We will use GROMACS for this, and since GROMACS does not understand `.xyz`
     files, we need to first convert it into another format, e.g. `.gro`. Use
     Open Babel for the conversion:

   ```bash
   $ cd ../aimd
   $ module load openbabel
   $ obabel enol.xyz -O enol.gro
   $ module load gromacs-env
   $ gmx_mpi solvate -cp enol.gro -cs spc216.gro -o enol-solv.gro -box 1.5 1.5 1.5
   $ obabel enol-solv.gro -O enol-solv.xyz
   ```

2. Have a look at the solvated system:

   ```bash
   $ module load gpaw
   $ ase gui enol-solv.xyz
   ```

## Task 4.2 – Fixing the input files and submitting the calculation

1. Edit the input files and submit the job:
   * `RUN_TYPE` should be `MD`
   * We'll simulate in the `NVT` ensemble (number of particles, volume and
     temperature are kept constant) using a timestep of `0.5` femtoseconds
   * PBE has a tendency to "overstructure" water (it is too ice-like). To mitigate
     this, we'll use an increased simulation temperature of `348.15` K
   * Now the system is periodic, so make sure the Poisson solver is set to
     `PERIODIC`

   ```bash
   $ grep TODO *.in*  # fix all matches
   $ sbatch cp2k.sh
   ```

1. You can monitor the temperature and potential energy with Gnuplot:

   ```bash
   $ module load gnuplot
   $ gnuplot
   gnuplot> plot "enol-aimd-1.ener" using 2:4 with linespoints
   gnuplot> plot "enol-aimd-1.ener" using 2:5 with linespoints
   ```

## Task 4.3 – Analysis

1. The simulation will be run only for 1000 steps (0.5 ps), which is way too
   little for any meaningful results. Still, the calculation will take more
   than an hour.
2. Instead of waiting, download a ready 50 ps trajectory which has been simulated
   using the exactly same input settings:

   ```bash
   $ wget https://a3s.fi/CSC_training/enol-aimd-nowater.xyz
   ```

3. Note that the water molecules have been removed from this trajectory in order
   to decrease the file size.
4. Use the `energy.py` Python script to analyze the proton transfer energy profile:
   * Have a look at the script, `less energy.py`
   * We define a _reaction coordinate_ to quantify the progression of the reaction
     as $q=d_\mathrm{O_a H}-d_\mathrm{O_b H}$ where $d_{ij}$ is the distance between
     atoms $i$ and $j$.
   * The free energy is then

     $$A(q)=-k_\mathrm{B}T\ln P(q)$$

     where $P(q)$ is the probability density of $q$.

   ```bash
   $ module load gpaw
   $ python3 energy.py enol-aimd-nowater.xyz
   ```

5. What can you say about the free energy profile? Does the reaction free energy
   and barrier differ from the static vacuum phase NEB results? Why (not)?

## Conclusions

The aim of this hands-on exercise was to introduce CP2K and different ways to
study simple low-barrier chemical reactions with NEB and AIMD. While this
exercise should serve as a realistic example of how to work with CP2K, there
are multiple aspects which could be improved on, especially if you intend to run
production-type simulations. Can you think of what could have been done better?

# Part 1: Nudged elastic band (NEB) calculations at PBE level of theory

The nudged elastic band method is a technique for finding the minimum energy
path between two equilibrium structures. A discrete string of replicas (images)
of the system that connect the initial (IS) and final states (FS) is created
and optimized. A harmonic potential is included between each image in order to
keep the string continuous and images equidistant.

## Task 1 – The CP2K input structure

1. Navigate to the `./sscc-qc-inter/neb/` directory and inspect the files:
   
   ```bash
   $ cd sscc-qc-inter/neb/
   $ ls
   cp2k.sh  dft.inc  enol-fs.xyz  enol-is.xyz  neb.inp  README.md	solution  subsys.inc
   $ less neb.inp
   ```

2. The general form of the CP2K input syntax is as follows:
   
   ```
   &SECTION1  ! this is a comment
     KEYWORD1 VALUE1
     &SECTION2
       KEYWORD2 VALUE2 VALUE3  # this is also a comment
     &END SECTION2
   &END SECTION1
   ```

3. In addition, there are `@SET` and `@INCLUDE` directives for assigning variables
   and including files into the `.inp` input file, respectively. Study the input
   sections and keywords with the help of the CP2K input reference available
   [here](https://manual.cp2k.org).
4. Visualize the `enol-is.xyz` and `enol-fs.xyz` geometries using ASE GUI, which
   is provided in the GPAW module:

   ```bash
   $ module load gpaw
   $ ase gui enol-*
   ```

5. The main input file `neb.inp` contains the high-level `&GLOBAL`, `&FORCE_EVAL`
   and `&MOTION` sections. The subsections `&DFT` and `&SUBSYS` and specified in
   the files `dft.inc` and `subsys.inc` an included under the `&FORCE_EVAL` section
   using the `$INCLUDE` syntax.

# Task 2 – Fixing the input files and submitting the calculation

1. Replace all occurrences of `TODO` in the input/include files based on that:
   * We will perform a run of type `BAND` with `8` replicas (images)
   * We will use the PBE exchange–correlation functional
   * The simulation cell is cubic with side length 15 Å2
2. Hint: to find all `TODO`s, try `grep TODO *.in*`
3. Once you've fixed the input files, have a look at the batch job script 
   (it's quite simple) and then submit the calculation with:
   
   ```bash
   $ less cp2k.sh
   $ sbatch cp2k.sh
   ```

4. In the batch script we request one Mahti nodes (128 cores), meaning that each
   of the 8 replicas will be processed using 16 CPU cores. We run 20 NEB iterations,
   so the calculation should only take about 10 minutes.
5. A bunch of output files are produced
   * `*.out` are various output files
   * `*.wfn` are wavefunction restart files
   * `*.xyz` are coordinate files
   * `*.ener` contains the energies for each image and NEB iteration

# Task 3 – Analysis

1. Create and view a movie of the optimized minimum energy path:
   
   ```bash
   $ for i in {1..8} ; do tail -n 21 "enol-neb-pos-Replica_nr_${i}-1.xyz" >> movie.xyz ; done
   $ module load gpaw
   $ ase gui movie.xyz
   ```

2. Extract and plot the minimum energy profile of the proton transfer (in meV):
   
   ```bash
   $ grep "i =" movie.xyz | awk '{print $6}' > energy.txt
   $ module load gnuplot
   $ gnuplot
   gnuplot> y0=system("head -1 energy.txt")
   gnuplot> plot "energy.txt" using (27211.38*($1-y0)) with linespoints
   ```

3. What can you say about the reaction barrier height? What about the reaction
   energy?
   * Hint: The thermal energy at room temperature is about $k_\mathrm{B}T\approx25$ meV

Continue the hands-on with [Part 2](../vib/README.md)
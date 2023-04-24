# CSC Spring School on Computational Chemistry – Intermediate quantum chemistry hands-on

This exercise explores the proton transfer step associated with the interconversion
of the two enol forms of 2-formylcyclohexanone using DFT simulations. The
calculations are done using the [CP2K](https://www.cp2k.org/) software package
and visualization/analyses with [ASE](https://wiki.fysik.dtu.dk/ase/index.html)
and [Gnuplot](http://www.gnuplot.info/).

This exercise consists of the following parts:

* [Part 1](neb/README.md): Nudged elastic band (NEB) calculations at PBE level
  of theory
* [Part 2](vib/README.md): Vibrational analysis of the transition state
* [Part 3](hybrid/README.md): Re-converging the NEB minimum energy profile
  using the PBE0 hybrid functional
* [Part 4](aimd/README.md): *Ab initio* molecular dynamics simulation of
  2-formylcyclohexanone in aqueous solution

## Part 0: Preparations

This exercise is run on the Mahti supercomputer. Login and clone this repository
to a suitable directory under `/scratch`:

```bash
$ ssh -X <username>@mahti.csc.fi
$ mkdir -p /scratch/project_2006657/$USER
$ cd /scratch/project_2006657/$USER
$ git clone https://github.com/csc-training/sscc-qc-inter.git
```

Some parts of this exercise will use different Python packages for visualization,
anlysis and plotting. To use these, modify your path by running:

```bash
$ export PATH="/projappl/project_2006657/sscc-2023-python/bin:$PATH"
```

**Now, start the actual hands-on with [Part 1](neb/README.md).**

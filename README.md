# CSC Spring School on Computational Chemistry – Intermediate-level hands-on

This hands-on explores proton transfer associated with the interconversion of the
two enol forms of 2-formylcyclohexanone using DFT simulations. The simulations
will be done using the [CP2K](https://www.cp2k.org/) software package and
visualization/analyses with [ASE](https://wiki.fysik.dtu.dk/ase/index.html) and
[Gnuplot](http://www.gnuplot.info/).

The hands-on consists of the following parts:

* Part 1: Nudged elastic band (NEB) calculations at PBE level of theory
* Part 2: Vibrational analysis of the transition state
* Part 3: Re-converging the NEB minimum energy profile using the PBE0 hybrid
  functional
* Part 4: *Ab initio* molecular dynamics simulation of 2-formylcyclohexanone in
  aqueous solution

## Part 0: Preparations

This hands-on is run on Mahti. Login and clone this repository to a suitable
directory under `/scratch`:

```bash
$ ssh -X <username>@mahti.csc.fi
$ mkdir -p /scratch/project_2006657/$USER
$ cd /scratch/project_2006657/$USER
$ git clone https://github.com/csc-training/sscc-qc-inter.git
```

Start the hands-on with [Part 1](neb/README.md).

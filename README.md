# CSC Spring School on Computational Chemistry – CP2K hands-on (intermediate)

These notebooks explore the proton transfer step associated with the
interconversion of the two enol forms of 2-formylcyclohexanone based on DFT
calculations. Specifically, the [CP2K](https://www.cp2k.org/) software package
is used together with various Python tools for analysis and visualization.

The hands-on consists of the following parts:

* [Part 1](Part-1-NEB/Part-1-NEB.ipynb): Nudged elastic band (NEB) calculations
  at PBE level of theory
* [Part 2](Part-2-NMA/Part-2-NMA.ipynb): Vibrational analysis of the transition
  state
* [Part 3](Part-3-Hybrid/Part-3-Hybrid.ipynb): Re-converging the NEB minimum
  energy profile using the PBE0 hybrid functional
* [Part 4](Part-4-AIMD/Part-4-AIMD.ipynb): *Ab initio* molecular dynamics
  simulation of 2-formylcyclohexanone in aqueous solution

## How to run

The notebooks are run using Puhti web interface, and they rely on CSC's
`cp2k/2024.1` module and a [custom Python environment](def.yml).

1. Go to <https://www.puhti.csc.fi>
2. Select *Jupyter for courses*
3. Reservation: *sscc_thu_small* (applicable during the school)
4. Project: *project_2013760*
5. Course module: *sscc-2024-cp2k*
6. Partition: *small* (default resource settings)
7. Launch!

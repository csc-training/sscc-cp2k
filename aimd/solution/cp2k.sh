#!/bin/bash -l
#SBATCH --time=01:30:00
#SBATCH --partition=medium
#SBATCH --ntasks-per-node=128
#SBATCH --nodes=1
#SBATCH --account=project_2006657

module purge
module load gcc/9.4.0 openmpi/4.1.2 cp2k/2023.1

srun cp2k.psmp aimd.inp

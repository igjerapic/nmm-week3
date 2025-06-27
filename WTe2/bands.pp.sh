#!/bin/bash
#SBATCH -J WTe2_bands
#SBATCH -o %j.out
#SBATCH -p parallel
#SBATCH -N 1
#SBATCH -n 12
#SBATCH -t 00:10:00

module load QuantumESPRESSO/7.1-foss-2022a
srun bands.x < WTe2.pp.in > WTe2.pp.out

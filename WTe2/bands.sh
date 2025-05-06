#!/bin/bash
#SBATCH -J QE_WTe2
#SBATCH -o %j.out
#SBATCH -p parallel
#SBATCH -N 1
#SBATCH -n 12
#SBATCH -t 00:30:00

module load QuantumESPRESSO/7.1-foss-2022a
srun pw.x < WTe2.bands.in > WTe2.bands.out

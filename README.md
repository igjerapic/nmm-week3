# Tutorial 3
This week, we will calculate properties of two-dimensional (2D) materials, graphene and monolayer WTe2, as well as a heterostructure made of these 2D materials.

## Assignment 1

We will start with the DFT calculation of monolayer WTe2. 

### Instructions

1a. Copy the file wte2.scf.in as well as the fully relativistic pseudopotentials (marked as 'rel') for both elements to your working directories. This material consists of heavy elements and it is a topological insulator so the spin-orbit interaction is switched on in the input file. Open the structure using XCrysDen or the online visualizer. What is the Bravais lattice? Does the structure make sense? Do you understand how the supercell is constructed? Try to display multiple unit cells along the z-direction. What is the distance between the monolayers?

Now, prepare the job script similar to the previously used 'quantum.qsub'. Note that your calculations will be much longer due to the number of electrons and spin-orbit coupling. You will have to adjust your file. You can try first setting time to a few minutes, and check how long each electronic step takes. Estimate your calculation time, change the job script and rerun the calculation.

1b. Based on the knowledge from the last week, prepare and run the band structure calculation. What high-symmetry k-points are relevant for the rectangular Brillouin zone? Does your band structure resemble the one provided on the slides? What is the difference? Can you think of the possible reason for the discrepancy?

## Assignment 2

Last week, we have explored the properties of graphite. Now, we will calculate graphene. The typical approach of creating two-dimensional material is to exfoliate the bulk structure. 

### Instructions

2a. Look once again at the WTe2 supercell, and try to create a graphene supercell using the graphite structure from the previous week. Open your file in XCrysden or using the online tool and inspect what you made. Does it make sense? Run the self-consistent field calculation with or without spin-orbit coupling - note that carbon atoms are light so the influence of spin-orbit coupling will be negligible. 

2b. Calculate the band structure along the M-G-K-M direction. How does it differ from graphite? Does it agree with the literature? 

## Assignment 3

In this exercise, you will analyze the file prepared for the calculation Gr/WTe2 heterostructure. This is not a typical step for computational research, as usually you do not have such files. Based on this analysis, you will prepare the heterostructure yourself. 

### Instructions

3a. Copy the file 'wte2-gr.relax.in' and the corresponding pseudopotentials to your working directory. Inspect carefully the file and open it in XCrysden. What can you say about the structure? Is the supercell hexagonal or rectangular? What can you say about the twisting angle? How many graphene unit cells can you see?

3b. Once you understand how the heterostructure is constructed, use your own files for graphene and WTe2 monolayers, and try to create the heterostructure yourself. You can write your own code that creates (i) first the supercell of one material using the basic unit cell, and (ii) stacks the second monolayer with an adjusted lattice constant on top of it. Alternatively, several online tools can help you create heterostructures. You can use any of them if they do the job.

## Assignment 4

Now, we will relax the heterostructure. 

### Instructions

4a. If you did not manage to create a heterostructure in the previous exercise, use the file that we prepared for you. You need to use the parameter 'relax', as you will be only relaxing the atomic positions and not the lattice constants. Do not forget about van der Waals interaction. Do not include spin-orbit coupling, as it does not affect the positions. 

The challenge of this exercise is to make the calculation finish on the cluster. The job may run for several hours, so try first running a short calculation that will give you an indication of how long it can take. Since it is a relaxation calculation, it is not a major problem if the calculation stops in the middle. If this happens, simply copy the latest coordinates from the output file, paste them to the input file, and rerun the calculation. 

Visualize the result. Have the atoms moved a lot? Note: XCrysden allows one to visualize relaxation as animation. 

4b. This exercise is optional.
If you have time, run also the self-consistent calculation using the relaxed coordinates and the band structure. What can you say about BZ of the supercell? Which k-line do you choose for the band structure calculation?

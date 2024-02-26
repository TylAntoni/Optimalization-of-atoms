# Geometry of atoms and its optimalization in XYZ coordinations

This code is designed to give easier solution for optimalization of chemical compounds in XYZ coordinations. 

The input file has the initial geometry of subjected compound. It need to contain in first line the sum of atoms in compound. It creates a matrix to further mathematical work, 

When initial geometry is created the code creates 6N new compunds where every compound has deviation in every atom for 0.02 Angstrom. 

So in the end we obtain `6N + 1` geometries where N is a number of atoms. 

For every displacement it creates separeted folder with files for easier searching and ordering of new compunds calling them by numbers where number `100` is initial geometry without displacement in any atom.

In this case we putting obtained failes to optimalization method to obtain dipole moments for every geometry. 


In the end the code is using simply equatation for first and second derivative and our output is report with total energy of sugested geometry.


This code has 2 switches

- --prepare - is preparing `6N+1` files with geometries
- --analyze - is calculating derivatives with previously optimalized values of dipole moment every geometry
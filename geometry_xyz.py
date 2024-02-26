#!/usr/bin/env python3

import os,string,sys,re
from pathlib import Path


def prepare_files():
 dir_parent=os.getcwd()
 xyz_file_name = input("Please provide name of .xyz file :  ")
 xyz_file = open(xyz_file_name,"r")
 no_atoms = int(xyz_file.readline())
 dummy = xyz_file.readline()
 atom = []
 x = []
 y = []
 z = []
 i=0
 while i < no_atoms:
   temp_a = xyz_file.readline()
   temp_b = temp_a.split()
   atom.append(temp_b[0])
   x.append(float(temp_b[1]))
   y.append(float(temp_b[2]))
   z.append(float(temp_b[3]))
   i+=1
 xyz_file.close()

 # we first open unit 100 and print there initial geometry (undisplaced)

 fno=100
 directory=str(fno)
 Path(directory).mkdir(parents=True, exist_ok=True)
 xyz_file_name = os.path.join(directory, 'geom.xyz')
 with open(xyz_file_name,"w") as xyz_file:
   # xyz_file.write(str(no_atoms))
   # xyz_file.write("\n\n")
   i=0
   while i < no_atoms:
     xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[i])),'{:>15}'.format(str((x[i]))),'{:>15}'.format(str(y[i])),'{:>15}'.format(str(z[i]))))
     i+=1
   xyz_file.write("\n")
   xyz_file.close()
   os.chdir(dir_parent+'/'+directory)
   os.system('cp ../templates/*inp .')
   os.chdir(dir_parent)
   fno=fno+1

 delta=0.01  # displacement

 # positive displacements x+delta

 i=0
 while i < no_atoms:
   j=0
   directory=str(fno)
   Path(directory).mkdir(parents=True, exist_ok=True)
   xyz_file_name = os.path.join(directory, 'geom.xyz')
   with open(xyz_file_name,"w") as xyz_file:
     # xyz_file.write(str(no_atoms))
     # xyz_file.write("\n\n")
     while j < no_atoms:
       if j == i:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[i])),'{:>15}'.format(str(((x[i]+delta)))),'{:>15}'.format(str(y[i])),'{:>15}'.format(str(z[i]))))
       else:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[j])),'{:>15}'.format(str((x[j]))),'{:>15}'.format(str(y[j])),'{:>15}'.format(str(z[j]))))
       j+=1
     xyz_file.write("\n")
   xyz_file.close()
   os.chdir(dir_parent+'/'+directory)
   os.system('cp ../templates/*inp .')
   os.chdir(dir_parent)
   fno=fno+1
   i+=1

# negative displacements x-delta

 i=0
 while i < no_atoms:
   j=0
   directory=str(fno)
   Path(directory).mkdir(parents=True, exist_ok=True)
   xyz_file_name = os.path.join(directory, 'geom.xyz')
   with open(xyz_file_name,"w") as xyz_file:
     # xyz_file.write(str(no_atoms))
     # xyz_file.write("\n\n")
     while j < no_atoms:
       if j == i:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[i])),'{:>15}'.format(str(((x[i]-delta)))),'{:>15}'.format(str(y[i])),'{:>15}'.format(str(z[i]))))
       else:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[j])),'{:>15}'.format(str((x[j]))),'{:>15}'.format(str(y[j])),'{:>15}'.format(str(z[j]))))
       j+=1
     xyz_file.write("\n")
   xyz_file.close()
   os.chdir(dir_parent+'/'+directory)
   os.system('cp ../templates/*inp .')
   os.chdir(dir_parent)
   fno=fno+1
   i+=1

 # positive displacements y+delta

 i=0
 while i < no_atoms:
   j=0
   directory=str(fno)
   Path(directory).mkdir(parents=True, exist_ok=True)
   xyz_file_name = os.path.join(directory, 'geom.xyz')
   with open(xyz_file_name,"w") as xyz_file:
     # xyz_file.write(str(no_atoms))
     # xyz_file.write("\n\n")
     while j < no_atoms:
       if j == i:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[i])),'{:>15}'.format(str(((x[i])))),'{:>15}'.format(str((y[i]+delta))),'{:>15}'.format(str(z[i]))))
       else:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[j])),'{:>15}'.format(str((x[j]))),'{:>15}'.format(str(y[j])),'{:>15}'.format(str(z[j]))))
       j+=1
     xyz_file.write("\n")
   xyz_file.close()
   os.chdir(dir_parent+'/'+directory)
   os.system('cp ../templates/*inp .')
   os.chdir(dir_parent)
   fno=fno+1
   i+=1


 # positive displacements y-delta

 i=0
 while i < no_atoms:
   j=0
   directory=str(fno)
   Path(directory).mkdir(parents=True, exist_ok=True)
   xyz_file_name = os.path.join(directory, 'geom.xyz')
   with open(xyz_file_name,"w") as xyz_file:
     # xyz_file.write(str(no_atoms))
     # xyz_file.write("\n\n")
     while j < no_atoms:
       if j == i:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[i])),'{:>15}'.format(str(((x[i])))),'{:>15}'.format(str((y[i]-delta))),'{:>15}'.format(str(z[i]))))
       else:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[j])),'{:>15}'.format(str((x[j]))),'{:>15}'.format(str(y[j])),'{:>15}'.format(str(z[j]))))
       j+=1
     xyz_file.write("\n")
   xyz_file.close()
   os.chdir(dir_parent+'/'+directory)
   os.system('cp ../templates/*inp .')
   os.chdir(dir_parent)
   fno=fno+1
   i+=1
 # positive displacements z+delta

 i=0
 while i < no_atoms:
   j=0
   directory=str(fno)
   Path(directory).mkdir(parents=True, exist_ok=True)
   xyz_file_name = os.path.join(directory, 'geom.xyz')
   with open(xyz_file_name,"w") as xyz_file:
     # xyz_file.write(str(no_atoms))
     # xyz_file.write("\n\n")
     while j < no_atoms:
       if j == i:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[i])),'{:>15}'.format(str(((x[i])))),'{:>15}'.format(str((y[i]))),'{:>15}'.format(str(z[i]+delta))))
       else:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[j])),'{:>15}'.format(str((x[j]))),'{:>15}'.format(str(y[j])),'{:>15}'.format(str(z[j]))))
       j+=1
     xyz_file.write("\n")
   xyz_file.close()
   os.chdir(dir_parent+'/'+directory)
   os.system('cp ../templates/*inp .')
   os.chdir(dir_parent)
   fno=fno+1
   i+=1

 # positive displacements z-delta

 i=0
 while i < no_atoms:
   j=0
   directory=str(fno)
   Path(directory).mkdir(parents=True, exist_ok=True)
   xyz_file_name = os.path.join(directory, 'geom.xyz')
   with open(xyz_file_name,"w") as xyz_file:
    # xyz_file.write(str(no_atoms))
    # xyz_file.write("\n\n")
     while j < no_atoms:
       if j == i:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[i])),'{:>15}'.format(str(((x[i])))),'{:>15}'.format(str((y[i]))),'{:>15}'.format(str(z[i]-delta))))
       else:
         xyz_file.write("%s  %s  %s  %s \n" % ('{:<3}'.format(str(atom[j])),'{:>15}'.format(str((x[j]))),'{:>15}'.format(str(y[j])),'{:>15}'.format(str(z[j]))))
       j+=1
     xyz_file.write("\n")
   xyz_file.close()
   os.chdir(dir_parent+'/'+directory)
   os.system('cp ../templates/*inp .')
   os.chdir(dir_parent)
   fno=fno+1
   i+=1

def analyze_data():
 xyz_file_name = input("Please provide name of .xyz file :  ")
 xyz_file = open(xyz_file_name, "r")
 no_atoms = int(xyz_file.readline())
 x_p_fdir = 101
 x_p_limit = 101 + no_atoms
 x_m_limit = 101 + no_atoms * 2
 x_m_fdir = 101 + no_atoms
 y_p_fdir = 101 + no_atoms * 2
 y_p_limit = 101 + no_atoms * 3
 y_m_limit = 101 + no_atoms * 4
 y_m_fdir = 101 + no_atoms * 3
 z_p_fdir = 101 + no_atoms * 4
 z_p_limit = 101 + no_atoms * 5
 z_m_limit = 101 + no_atoms * 6
 z_m_fdir = 101 + no_atoms * 5
 dir_parent = os.getcwd()
 x_p_str = []
 while x_p_fdir < x_p_limit:
  print(f'Dipole moments for file {x_p_fdir} are:')
  directory_x_p = str(x_p_fdir)
  os.chdir(dir_parent+'/'+directory_x_p)
  fchk_x_p =  open("x_p.fchk", "r")
  fchk_content_x_p = fchk_x_p.read()
  try:
   x_p_dip_1 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_x_p, re.M).group(1))
   y_p_dip_1 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_x_p, re.M).group(2))
   z_p_dip_1 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_x_p, re.M).group(3))
   x_p_str.append(x_p_dip_1)
   print('      X               Y               Z')
   print(f'{x_p_dip_1}  {y_p_dip_1}  {z_p_dip_1}')
   print('\n')
  except:
   pass
  fchk_x_p.close()
  x_p_fdir=x_p_fdir+1
 x_p = [float(x) for x in x_p_str]
 #print(x_p)
 os.chdir(dir_parent)
 x_m_str = []
 while x_m_fdir < x_m_limit:
  print(f'Dipole moments for file {x_m_fdir} are:')
  directory_x_m = str(x_m_fdir)
  os.chdir(dir_parent+'/'+directory_x_m)
  fchk_x_m = open("x_m.fchk", "r")
  fchk_content_x_m = fchk_x_m.read()
  try:
   x_m_dip_1 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_x_m, re.M).group(1))
   y_m_dip_1 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_x_m, re.M).group(2))
   z_m_dip_1 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_x_m, re.M).group(3))
   x_m_str.append(x_m_dip_1)
   print('      X                     Y               Z')
   print(f'{x_m_dip_1}  {y_m_dip_1}  {z_m_dip_1}')
   print('\n')
  except:
   pass
  fchk_x_m.close()
  x_m_fdir = x_m_fdir + 1
 x_m = [float(x) for x in x_m_str]
 #print(x_m)
 os.chdir(dir_parent)
 y_p_str = []
 while y_p_fdir < y_p_limit:
  print(f'Dipole moments for file {y_p_fdir} are:')
  directory_y_p = str(y_p_fdir)
  os.chdir(dir_parent+'/'+directory_y_p)
  fchk_y_p =  open("y_p.fchk", "r")
  fchk_content_y_p = fchk_y_p.read()
  try:
   x_p_dip_2 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_y_p, re.M).group(1))
   y_p_dip_2 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_y_p, re.M).group(2))
   z_p_dip_2 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_y_p, re.M).group(3))
   y_p_str.append(y_p_dip_2)
   print('      X               Y               Z')
   print(f'{x_p_dip_2}  {y_p_dip_2}  {z_p_dip_2}')
   print('\n')
  except:
   pass
  fchk_y_p.close()
  y_p_fdir = y_p_fdir + 1
 y_p = [float(x) for x in y_p_str]
 #print(y_p)
 os.chdir(dir_parent)
 y_m_str = []
 while y_m_fdir < y_m_limit:
  print(f'Dipole moments for file {y_m_fdir} are:')
  directory_y_m = str(y_m_fdir)
  os.chdir(dir_parent+'/'+directory_y_m)
  fchk_y_m = open("y_m.fchk", "r")
  fchk_content_y_m = fchk_y_m.read()
  try:
   x_m_dip_2 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_y_m, re.M).group(1))
   y_m_dip_2 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_y_m, re.M).group(2))
   z_m_dip_2 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_y_m, re.M).group(3))
   y_m_str.append(y_m_dip_2)
   print('      X               Y               Z')
   print(f'{x_m_dip_2}  {y_m_dip_2}  {z_m_dip_2}')
   print('\n')
  except:
   pass
  fchk_y_m.close()
  y_m_fdir = y_m_fdir + 1
 y_m = [float(x) for x in y_m_str]
 #print(y_m)
 os.chdir(dir_parent)
 z_p_str = []
 while z_p_fdir < z_p_limit:
  print(f'Dipole moments for file {z_p_fdir} are:')
  directory_z_p = str(z_p_fdir)
  os.chdir(dir_parent+'/'+directory_z_p)
  fchk_z_p =  open("z_p.fchk", "r")
  fchk_content_z_p = fchk_z_p.read()
  try:
   x_p_dip_3 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_z_p, re.M).group(1))
   y_p_dip_3 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_z_p, re.M).group(2))
   z_p_dip_3 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_z_p, re.M).group(3))
   z_p_str.append(z_p_dip_3)
   print('      X               Y               Z')
   print(f'{x_p_dip_3}  {y_p_dip_3}  {z_p_dip_3}')
   print('\n')
  except:
   pass
  fchk_z_p.close()
  z_p_fdir = z_p_fdir + 1
 z_p = [float(x) for x in z_p_str]
 #print(z_p)
 os.chdir(dir_parent)
 z_m_str = []
 while z_m_fdir < z_m_limit:
  print(f'Dipole moments for file {z_m_fdir} are:')
  directory_z_m = str(z_m_fdir)
  os.chdir(dir_parent+'/'+directory_z_m)
  fchk_z_m = open("z_m.fchk", "r")
  fchk_content_z_m = fchk_z_m.read()
  try:
   x_m_dip_3 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_z_m, re.M).group(1))
   y_m_dip_3 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_z_m, re.M).group(2))
   z_m_dip_3 = (re.search(r"^Dipole Moment\s+R\s+N=\s+\d+\n\s+(.*?)\s+(.*?)\s+(.*?)\s", fchk_content_z_m, re.M).group(3))
   z_m_str.append(z_m_dip_3)
   print('      X               Y               Z')
   print(f'{x_m_dip_3}  {y_m_dip_3}  {z_m_dip_3}')
   print('\n')
  except:
   pass
  fchk_z_m.close()
  z_m_fdir = z_m_fdir + 1
 z_m = [float(x) for x in z_m_str]
 #print(z_m)
 os.chdir(dir_parent)

 i = 0
 delta = 0.01
 x_start = 101
 x_end = x_start + no_atoms
 y_start = x_start + no_atoms*2
 y_end = x_start + no_atoms*3
 z_start = x_start + no_atoms*4
 z_end = x_start + no_atoms*5
 for j in range(len(x_p)):
  print(f'Derivative of file {x_start} and {x_end} is:')
  s = (x_p[i]-x_m[i])/(-2*delta)
  print(s)
  i = i + 1
  x_start = x_start + 1
  x_end = x_start + no_atoms
 i = 0
 for j in range(len(y_p)):
  print(f'Derivative of file {y_start} and {y_end} is:')
  s = (y_p[i]-y_m[i])/(-2*delta)
  print(s)
  i = i + 1
  y_start = y_start + 1
  y_end = y_end + 1
 i = 0
 for j in range(len(z_p)):
  print(f'Derivative of file {z_start} and {z_end} is:')
  s = (z_p[i]-z_m[i])/(-2*delta)
  print(s)
  i = i + 1
  z_start = z_start + 1
  z_end = z_end + 1

if ( len(sys.argv) < 2  ):
 sys.exit("usage: IR.py --prepare --analyze")

if sys.argv[1] == '--prepare':
 prepare_files()

if sys.argv[1] == '--analyze':
 analyze_data()


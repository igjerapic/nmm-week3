#!/usr/bin/env python3
from scripts.bands import *
import os
import xml.etree.ElementTree as ET

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))
plt.style.use(PARENT_DIR + '/scripts/default.mplstyle')

def get_fermiEnergy_DOS(dos_file):
    # reading first line
    with open(dos_file, 'r') as f:
        first_line = f.readline()
    print(first_line)
    fermiEnergy = float(first_line.split()[-2])
    return fermiEnergy

def get_fermiEnergy(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find all <fermi_energy> tags
    for elem in root.iter('fermi_energy'):
        try:
            fermi_energy = float(elem.text)
            return fermi_energy
            #print("Found Fermi energy:", fermi_energy)
        except (ValueError, TypeError):
            print("Invalid Fermi energy value:", elem.text)
            break

#structure="WTe2"
structure="graphene"

main_dir = PARENT_DIR + f"/{structure}/Bands/"
bandsfile = main_dir + f"{structure}.dat.gnu"
xml_file = main_dir + f"{structure}.xml"


symmetryfile = main_dir + f"{structure}.pp.out"

fermi = get_fermiEnergy(xml_file)
bool_shift_efermi= True
fig, ax = plt.subplots()

path  = ['G','Y','S','X', "G"] if structure == "WTe2" else ["M", "G", "K", "M"] 

#bndplot(datafile,fermi,symmetryfile,ax)
bndplot(bandsfile, fermi, symmetryfile, ax, shift_fermi=True,\
color='black',linestyle='solid',name_k_points=path)
if structure == "WTe2":
    plt.ylim((-1, 1))
else:
    plt.ylim((-19.48469, 2.1740899999999996)) # matches with graphite from week2
plt.xlabel("Wavevector")
plt.tight_layout()
fig_file = "ass1_bands.png" if structure == "WTe2" else "ass2_bands.png"
fig.savefig(PARENT_DIR + f"/report/figs/{fig_file}", dpi=300)
plt.show()

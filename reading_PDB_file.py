#import Biopython
import Bio

#Import the PDBparser class from Bio.PDB
from Bio.PDB import PDBParser

#specify the PDB file
pdb_filename = "pdbfile.pdb"

#create a PDBParser object
parser = PDBParser()

#parse the PDB file and get the structure
"""The 'get_structure' method of the PDBParser object is used to parse the specified PDB file and obtain a
hierarchical representation of the structure."""

structure = parser.get_structure("pdbfile", pdb_filename)

#Iterate through the structure
for model in structure:
    #iterate through the models
    for chain in model:
       #iterate through the chains
       for residue in chain:
           #print info about each residue
           print(residue) 

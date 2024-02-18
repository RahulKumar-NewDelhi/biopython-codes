#import Biopython
import Bio

#import necessary modules
"""The ProtParam class which is a part of Biopythons seqUtils module provides tools for analyzing biological sequnces,
including protein sequences."""

from Bio.SeqUtils import ProtParam
from Bio.Seq import Seq

#Define a protien sequence
protein_sequence = Seq("VRPSEFYRTEREAMPGEHQFDIGPQETPKWCKKTLAGTYPVYCKPTMV")

#create a protein analysis object
protein_analysis = ProtParam.ProteinAnalysis(str(protein_sequence))

#Calculate the amino acid composition
"""The 'get_amino_acids_percent' method of the protein analysis object calculates the percentage
composition of each amino acids in the protein sequences."""

aa_composition = protein_analysis.get_amino_acids_percent()

#print the amino acid composition
print(aa_composition)
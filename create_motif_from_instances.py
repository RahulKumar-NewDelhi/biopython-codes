#import Biopython
import Bio

#import the necessary module
from Bio import motifs

#Define instances sequences
instances = ["ACGT", "ATGC", "AGCT", "CGTA"]

#create a motif from instances
motif = motifs.create(instances)

#print the motif
print("Motif:")
print(motif)
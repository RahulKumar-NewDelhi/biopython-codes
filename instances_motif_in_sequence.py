#import Biopython and necessary modules
import Bio
from Bio.Seq import Seq
from Bio import motifs

#Define the Sequence
sequence = Seq("ATCGATCGATCGAGCT")

#Define the motif
motif = motifs.create([Seq("ATCG")])

#Search for instances  of the motif in the sequence
instances = list(motif.instances.search(sequence))

#print the positions where the motif is found
print("Motif found at positions", instances)

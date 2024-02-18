#import the necessary module
from Bio import motifs

#Define instances(sequences)
instances = ["ACGT", "ATGC", "AGCT", "CGTA"]

#create a motif from instances
motif = motifs.create(instances)

#Access the position-specific Scoring Matrix(PSSSM)
pssm = motif.pssm
print(pssm)
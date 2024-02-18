#import Biopython and necessary modules
import Bio
from Bio import SeqIO
import numpy as np
import pandas as pd

#Read sequences from a FASTA file using Biopython
fasta_file = "sequences.fasta"
records = list(SeqIO.parse(fasta_file, "fasta"))

#Extract sequence data into a Numpy array
sequences_array = np.array([list(str(record.seq)) for record in records])

#Create a pandas Dataframe from the NumPy array
df = pd.DataFrame(sequences_array, index=[record.id for record in records])

#Display the pandas Dataframe
print("Pandas Dataframe:")
print(df)

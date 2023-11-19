#Import Biopython
import Bio

#Import necessary modules
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import Align

#create a simple alignment
alignment_data = ["ATAGTGGTACGT","ATGCGTTTGG-T","AC-GTGTCGTAT"]

#create a multiple sequence alignment object
alignment = Align.MultipleSeqAlignment([SeqRecord(Seq(seq))for seq in alignment_data])
print("Original Alignment:")
print(alignment)

#Slice the alignment
start_position = 1
end_position = 5

sliced_alignment = alignment[:,start_position:end_position]

#print the sliced alignment
print("\nSliced Alignment:")
print(sliced_alignment)

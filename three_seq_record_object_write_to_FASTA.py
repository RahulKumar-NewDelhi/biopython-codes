#Import Biopython
import Bio

#Import necessary modules from Biopython
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

#Create three SeqRecords objects
"""Three SeqRecord objects are created, each with unique sequence(Seq), identifier(id), and description"""

seq_record1 = SeqRecord(Seq("ATCGTGTACTAGGCATGAACGTA"), id="seq1", description="First sequence")
seq_record2 = SeqRecord(Seq("GCTAGCTAATGTGATTATATGGC"), id="seq2", description="Second sequence")
seq_record3 = SeqRecord(Seq("TTAAGCGTAATGTCGCTGTATAA"), id="seq3", description="Third sequence")

# Combine SeqRecord objects into a list

seq_record = [seq_record1, seq_record2, seq_record3]

# Specify the output file name and format
output_file = "output.fasta"
output_format = "fasta"

# Write SeqRecord objects to the output file in FASTA format
"""The 'SeqIO.write' function is used to write the seq_records
list to the specified output file ("output.fasta") in FASTA format. """

with open(output_file, "w") as output_handle:
    SeqIO.write(seq_record, output_handle, output_format)

#Print a success message to indicate that the SeqRecord objects have been successfully written
print(f"SeqRecord objects written to {output_file} in {output_format} format.")

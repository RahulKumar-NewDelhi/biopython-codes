#Import Biopython
import Bio

#Import necessary modules
from Bio import Align
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#create two sequences for alignment
sequence1 = Seq("ACGTGACCTGGGAGGATGCTTTG")
sequence2 = Seq("AGGTTACCTTGGAAGGAGAAGGA")

#create SeqRecord object for the sequences
seq_record1 = SeqRecord(sequence1, id="seq1", description="Sequence1")
seq_record2 = SeqRecord(sequence2, id="seq2", description="sequence2")

#Reverse complement the second sequence
reverse_complement_seq2 = seq_record2.seq.reverse_complement()
seq_record2_reverse = SeqRecord(reverse_complement_seq2, id="seq2_reverse", description="Sequence2(Reverse)")

#create a list of SeqRecord objects
seq_records = [seq_record1, seq_record2_reverse]

#create a MultipleSeqAlignment object
alignment = Align.MultipleSeqAlignment(seq_records)

#Iterate over the alignment
for record in alignment:
    print(f"ID:{record.id}, Description:{record.description}")
    print(f"Sequence:{record.seq}")
    print("-")
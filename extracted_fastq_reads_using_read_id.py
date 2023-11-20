from Bio.SeqIO.QualityIO import FastqGeneralIterator
import itertools
from Bio import SeqIO

input_fastq_file = "/home/ngsa4/Documents/DATASET/variant-calling/Illumina/SO_11011_MYB49_OE_Line2_R1.fq"
read_ids_file = "/home/ngsa4/Documents/fastq_read_id.tsv"
output_file = "/home/ngsa4/Documents/extracted_reads.fastq"

wanted = set(line.rstrip("\n").split(None,1)[0] for line in open(read_ids_file))
print("Found %i unique identifiers in %s" % (len(wanted), read_ids_file))

count = 0
handle = open(output_file, "w")
for title, seq, qual in FastqGeneralIterator(open(input_fastq_file)) :
    if title.split(None,1)[0] in wanted:
        handle.write("@%s\n%s\n+\n%s\n" % (title, seq, qual))
        count += 1
handle.close()

print("Saved %i records from %s to %s" % (count, input_fastq_file, output_file))
if count < len(wanted):
    print("Warning %i IDs not found in %s" % (len(wanted)-count, input_fastq_file))

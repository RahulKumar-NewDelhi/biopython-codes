#import Biopython
import Bio
from Bio import SeqIO
from Bio import Entrez


#Import Biopython modules
"""# Import the SeqIO modules from Biopython for reading sequence files.
#Import the entrez module from Biopython, which provide access to the NCBI databases.
"""

#provide your email address for NCBI services
Entrez.email = "abc@gmail.com"

#specify the accession number of the nucleotide sequences
accession_number = "NM_001301716.1"

#fetch the sequence from the NCBI nucleotide database
handle = Entrez.efetch(db = "nucleotide", id = accession_number, rettype="gb", retmode="text")

"""Use the Entrez.efetch function to retrieve information from the NCBI nucleotide database. Parameters
include the database(db), the identifier(id), the return type(rettype), and the return mode (retmode).
In this case, it fetches the GenBank formattted data (rettype="gb") in plain text(retmode= "text")"""

#Read the GenBank-formatted data using SeqIO
record = SeqIO.read(handle, "genbank")

#print the sequence
print(record.seq)

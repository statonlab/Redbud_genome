"""
The script is used to extract congits from a given list of contig names
Usage: python extract_contig.py <input.fasta> <header_list.txt> <mapped.fasta> <unmapped.fasta>
"""


import sys
from Bio import SeqIO

fasta_file = sys.argv[1]
header_file = sys.argv[2]
result1_file = sys.argv[3]
result2_file = sys.argv[4]

contigs_list=[]
with open(header_file, "r") as contigs:
    for line in contigs:
        header = line.strip("\n")
        contigs_list.append(header)

wanted = set(contigs_list)
#print(contigs_list)
fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
with open(result1_file, "w") as f1, open(result2_file,"w") as f2:
    for seq in fasta_sequences:
        if seq.id in wanted:
            SeqIO.write([seq], f1, "fasta")
        else:
            SeqIO.write([seq], f2, "fasta")

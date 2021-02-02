"""
Created on Feb 2, 2021
Author: Jiali
This script is to take the minimap2 alignment output PAF file and calculate
the alignment rate, seperate the query reads to mapped or non-mapped files 
based on a given cutoff rate [0-1].

Usage:
python filter_paf.py <input.paf> --rate float 
"""
import argparse
parser = argparse.ArgumentParser(description="Extract reads from PAF file and split them into two files", usage="%(prog)s <input file> [--rate float]")
parser.add_argument("input", type=str, help="input PAF file")
parser.add_argument('--rate', action='store', type=float, required=True, help="alignment rate cutoff")
args = parser.parse_args()
PAFfile = args.input
mapped = 'aligned_read_headers.txt'
unmapped = 'unaligned_read_headers.txt'

# calculate mapping rate
def calRate(a,b):
    return float(a)/float(b)

if __name__ == "__main__":
    with open(PAFfile) as in_file, open(mapped, "w") as out1, open(unmapped ,"w") as out2:
        for line in in_file:
            content = line.split("\t")
            header = content[0]
            seq_length = content[1]
            alignment = content[9]
            mapping_rate = calRate(alignment, seq_length)
            if mapping_rate > args.rate:
                out1.write(header+"\n")
            else:
                out2.write(header+"\n")

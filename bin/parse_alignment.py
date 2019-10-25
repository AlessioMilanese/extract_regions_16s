# this script takes the output from cmalign and
# 1. selects only the alignment rows
# 2. transform space to "\t"

# note that if the fasta file had spaces, then they are removed in the alignmet

import sys

for line in sys.stdin:
    if not(line.startswith("#")):
        if not(line.startswith("//")):
            vals = line.rstrip().split(" ")
            if vals[0] != "":
                sys.stdout.write(vals[0]+"\t"+vals[-1]+"\n")              

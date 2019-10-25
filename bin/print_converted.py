# this script prints to stdout the file passed as input, changing T's into U's
# and adding at the beginning the reference sequence

import sys

reference_file = sys.argv[1]
fasta_file = sys.argv[2]

# print the reference file
o = open(reference_file,"r")
for i in o:
    sys.stdout.write(i)
o.close()
# print the fasta file where we change the T's to U's
o = open(fasta_file,"r")
for i in o:
    if i.startswith(">"):
        sys.stdout.write(i)
    else:
        sys.stdout.write(i.replace("T","U"))
o.close()

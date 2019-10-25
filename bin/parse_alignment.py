# this script takes the output from cmalign and
# 1. selects only the alignment rows
# 2. transform space to "\t"

# note that if the fasta file had spaces, then they are removed in the alignmet

import sys
import os
import tempfile
import shutil

file_alignment_name = sys.argv[1]
save_alignment = sys.argv[2]

# check if we need to save the alignment
if save_alignment == "True":
    al_temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w")
    os.chmod(al_temp_file.name, 0o644)


for line in sys.stdin:
    if not(line.startswith("#")):
        if not(line.startswith("//")):
            vals = line.rstrip().split(" ")
            if vals[0] != "":
                sys.stdout.write(vals[0]+"\t"+vals[-1]+"\n")
                # check if saving the intermediate alignment
                if save_alignment == "True":
                    al_temp_file.write(vals[0]+"\t"+vals[-1]+"\n")

# we exit if we dont need to save the temporary alignment
if save_alignment == "False":
    sys.exit(0)

# we arrive here if we save the alignment
try:
    al_temp_file.flush()
    os.fsync(al_temp_file.fileno())
    al_temp_file.close()
except:
    sys.stderr.write("Error when closing alignment file\n")

try:
    shutil.move(al_temp_file.name,file_alignment_name) #It is not atomic if the files are on different filsystems.
except:
    sys.stderr.write("Error when copying intermediate alignment to the final destination\n")

sys.exit(0)

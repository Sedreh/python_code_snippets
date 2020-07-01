################################# code for going through a directory and appending all files (combine fastas)


import os

DIR = '/home/is6/ASVs_comparison/16s_fastas'

oh = open('/home/is6/ASVs_comparison/16s_fastas/16s_database.fasta', 'w')
for f in os.listdir(DIR):
    fh = open(os.path.join(DIR, f))
    for line in fh:
        oh.write(line)
    fh.close()
oh.close()

#-----------------------------------


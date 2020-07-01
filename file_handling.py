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

#################################### 
# reading 16s_extracted file as dataframes
extracted_df = pd.read_csv("/home/is6/ASVs_comparison/modify1.csv", sep=',', header=None)
extracted_df.head()

extracted_df.columns = ['sseqid', 'None', 'species']
extracted_df = extracted_df.drop(extracted_df.index[0])


extracted_df = extracted_df.drop('None', 1)
extracted_df.head()


# merge final dataframe on 'sseqid' to 16s_extracted dataframe to get species name
final_data = pd.merge(extracted_df, N_data, on="sseqid")
final_data.head()

final_data.to_csv ("/home/is6/ASVs_comparison/16s_fastas/BLAST_results.csv", index = False)
#-----------------------------------

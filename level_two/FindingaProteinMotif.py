# I will be given a list of protein IDs, and for each ID I need to 
# 1) download fasta data by inserting the ID into http://www.uniprot.org/uniprot/{ID}.fasta
# 2) compose a list of all the fasta data
# 3) read it with my function 
# 4) for each, find the N{P}[ST]{P} motif and note down its location, if it exists 
# 5) return the ID of proteins where the motif exists and the list of locations

import requests
import time
from rosalind_utils.fasta import fastaParser
from pathlib import Path

idList = {}
with open("level_two/ProteinIDs.txt", 'r') as file:
    for protID in file:
        protID = protID.strip()
        idList[protID] = protID

        underscoreIdx = protID.find("_")
        if underscoreIdx != -1:
            idList[protID] = protID[ : underscoreIdx]

urlList = []
for id in idList.values():
    urlList.append(f"https://rest.uniprot.org/uniprotkb/{id}.fasta")

for url in urlList:
    response = requests.get(url)
    time.sleep(2)
    file_Path = 'level_two/experiment.txt'

    if response.status_code == 200:
        if url == urlList[0]:
            with open(file_Path, 'w') as file:
                file.write(response.content.decode())
            print('File downloaded successfully')
        else:
            with open(file_Path, 'a') as file:
                file.write(response.content.decode())
            # print('File downloaded successfully')    
    else:
        print('Failed to download file ')


parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "experiment.txt"
proteinsFasta = fastaParser(fasta_path)

proteinsWithMotif = {}
# the motif is N{P}[ST]{P}
for fastaName, protein in proteinsFasta.items():
    # extracting the ID from the fasta name
    nameID = fastaName[3:]
    nameID = nameID[:nameID.find('|')]
    for key, value in idList.items():
        if value == nameID:
            proteinsWithMotif[key] = []
            nameID = key
            
    proteinLength = len(protein)
    for idx in range(proteinLength):
        # -1 because the idx starts from 0, and 4 because the reading frame 
        # is 4 characters including the idx
        if proteinLength - 1 - 3 < idx: 
            break
        elif (protein[idx] == 'N' and \
              protein[idx + 1] != 'P' and \
              (protein[idx + 2] == 'S' or protein[idx + 2] == 'T') and \
              protein[idx + 3] != 'P'
        ):
            proteinsWithMotif[nameID].append(idx + 1) 
    if not proteinsWithMotif[nameID]:
        proteinsWithMotif.pop(nameID)

for key, value in proteinsWithMotif.items():
    print(key)
    print(" ".join(map(str, value)))
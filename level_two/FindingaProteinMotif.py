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

# idList = []
# with open("level_two/ProteinIDs.txt", 'r') as file:
#     for protID in file:
#         protID = protID.strip()
#         underscoreIdx = protID.find("_")
#         if underscoreIdx != -1:
#             protID = protID[ : underscoreIdx]
#         idList.append(protID)
# print(idList)

# urlList = []
# for id in idList:
#     urlList.append(f"https://rest.uniprot.org/uniprotkb/{id}.fasta")

# for url in urlList:
#     response = requests.get(url)
#     time.sleep(2)
#     file_Path = 'level_two/experiment.txt'

#     if response.status_code == 200:
#         if url == urlList[0]:
#             with open(file_Path, 'w') as file:
#                 file.write(response.content.decode())
#             print('File downloaded successfully')
#         else:
#             with open(file_Path, 'a') as file:
#                 file.write(response.content.decode())
#             print('File downloaded successfully')    
#     else:
#         print('Failed to download file ')


parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "experiment.txt"
proteinsFasta = fastaParser(fasta_path)

proteinsWithMotif = {}
# N{P}[ST]{P}
for fastaName, protein in proteinsFasta.items():
    # extracting the ID from the fasta name
    nameID = fastaName[3:]
    nameID = nameID[:nameID.find('|')]
    proteinsWithMotif[nameID] = []
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
# print(proteinsWithMotif)


{'sp|A2Z669|CSPLT_ORYSI CASP-like protein 5A2 OS=Oryza sativa subsp. indica OX=39946 GN=OsI_33147 PE=3 SV=1': [], 
 'sp|B5ZC00|SYG_UREU1 Glycine--tRNA ligase OS=Ureaplasma urealyticum serovar 10 (strain ATCC 33699 / Western) OX=565575 GN=glyQS PE=3 SV=1': [85, 118, 142, 306, 395], 
 'sp|P07204|TRBM_HUMAN Thrombomodulin OS=Homo sapiens OX=9606 GN=THBD PE=1 SV=2': [47, 115, 116, 382, 409], 
 'sp|P20840|SAG1_YEAST Alpha-agglutinin OS=Saccharomyces cerevisiae (strain ATCC 204508 / S288c) OX=559292 GN=SAG1 PE=1 SV=2': [79, 109, 135, 248, 306, 348, 364, 402, 485, 501, 614]}
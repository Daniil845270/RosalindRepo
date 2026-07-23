from rosalind_utils.fasta import fastaParser
from pathlib import Path

parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "Data.txt"
dnaStrands = fastaParser(fasta_path)

graphList = []

for name, strand in dnaStrands.items():
    for nameItr, strandItr in dnaStrands.items():
        if name != nameItr and strand[-3:] == strandItr[:3]:
            graphList.append([name, nameItr])

for nodePair in graphList:
    print(" ".join(nodePair))

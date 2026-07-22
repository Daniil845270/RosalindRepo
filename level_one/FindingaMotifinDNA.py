from rosalind_utils.fasta import multipleBigSequencesReader, returnAnswerAsFile
from pathlib import Path

def findStrings(bigString, subString):

    sequenceFound = 0
    subStringIndexes = []

    if bigString.find(subString, sequenceFound) == -1:
        return []
    
    while True:
        sequenceFound = bigString.find(subString, sequenceFound)
        if sequenceFound != -1:
            subStringIndexes.append(sequenceFound + 1)
            sequenceFound += 1
        else: 
            break
    return subStringIndexes

parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "Data.txt"
sequences = multipleBigSequencesReader(fasta_path)
bigString, subString = sequences[0], sequences[1]

subStringIndexes = findStrings(bigString, subString)

print(" ".join(map(str, subStringIndexes)))
from rosalind_utils.fasta import multipleBigSequencesReader
from pathlib import Path

parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "Data.txt"
sequences = multipleBigSequencesReader(fasta_path)
oneString, anotherString = sequences[0], sequences[1]
hamming = 0

for nucleotide in range(len(oneString)):
    if oneString[nucleotide] != anotherString[nucleotide]:
        hamming += 1

print(hamming)
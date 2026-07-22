from rosalind_utils.constants import CODON_TABLE
from rosalind_utils.fasta import bigSingleSequenceReader
from pathlib import Path
import math

parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "Data.txt"
proteinSequence = bigSingleSequenceReader(fasta_path)

options = []

for aaSeq in proteinSequence:
    aaOptions = 0
    for codonTable, aaTable in CODON_TABLE.items():
        if aaTable == aaSeq:
            aaOptions += 1
    options.append(aaOptions)

print((math.prod(options) * 3) % 1000000) # to account for the 3 stop codons

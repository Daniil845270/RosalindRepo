from rosalind_utils.fasta import bigSingleSequenceReader
from rosalind_utils.constants import MONOISOTOPIC_MASS_TABLE
from pathlib import Path

parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "Data.txt"
proteinSequence = bigSingleSequenceReader(fasta_path)

proteinWeight = 0
for aa in proteinSequence:
    proteinWeight += MONOISOTOPIC_MASS_TABLE[aa]

print(proteinWeight)
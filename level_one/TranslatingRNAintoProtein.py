from rosalind_utils.constants import CODON_TABLE
from rosalind_utils.fasta import bigSingleSequenceReader, returnAnswerAsFile
from pathlib import Path

parentDir = Path(__file__).resolve().parent
fasta_path = parentDir / "fastaData.txt"
rna = bigSingleSequenceReader(fasta_path)

cnt1 = 0
cnt2 = 3
stopCodons = ["UAA", "UAG", "UGA"]
protein = ""

stop = False
while stop == False:
    triplet = rna[cnt1:cnt2]
    if triplet in stopCodons:
        break
    protein += CODON_TABLE[triplet]
    cnt1 += 3
    cnt2 += 3

returnAnswerAsFile(parentDir / "Answer", protein)
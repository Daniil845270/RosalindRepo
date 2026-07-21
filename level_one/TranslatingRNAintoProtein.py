# from rosalind_utils.constants import CODON_TABLE
from rosalind_utils import constants

rna = str(input())

cnt1 = 0
cnt2 = 3
stopCodons = ["UAA", "UAG", "UGA"]
protein = ""

stop = False
while stop == False:
    triplet = rna[cnt1:cnt2]
    if triplet in stopCodons:
        break
    protein += constants.CODON_TABLE[triplet]
    cnt1 += 3
    cnt2 += 3


print(protein)
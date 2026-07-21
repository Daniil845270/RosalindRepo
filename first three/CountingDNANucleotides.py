sequence = str(input())
counter = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
}
allNucs = ['A', 'C', 'G', 'T']

for nucleotide in sequence:
    for nuc in allNucs:
        if nucleotide == nuc:
            counter[nucleotide] += 1

print(counter)
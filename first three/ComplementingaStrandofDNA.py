sequence = list(input())

for idx, nuc in enumerate(sequence):
    if nuc == 'A':
        sequence[idx] = 'T'
    elif nuc == 'T':
        sequence[idx] = 'A'
    elif nuc == 'C':
        sequence[idx] = 'G'
    elif nuc == 'G':
        sequence[idx] = 'C'

reversed = sequence[::-1] 

print()
print("".join(reversed)) 
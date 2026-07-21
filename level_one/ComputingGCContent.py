# this generic parser was created with chat gpt when asked "How to read FASTA files"
def fastaParser(documentName: str) -> dict: 
    content = {}
    current_id = None
    with open(documentName) as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                current_id = line[1:]
                content[current_id] = ""
            else:
                content[current_id] += line
    return content

sequences = fastaParser("fastaData.txt")
result = [None, -1] 

for name, sequence in sequences.items():
    gc = (sequence.count("G") + sequence.count("C")) * 100 / len(sequence)
    if gc > result[1]:
        result[0] = name
        result[1] = gc

for item in result:
    print(item)

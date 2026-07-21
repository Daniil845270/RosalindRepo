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
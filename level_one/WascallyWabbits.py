months, pairs = int(input()), int(input())

result: int
minusOne = 1
minusTwo = 1

if not (months == 1 or months == 2):
    for n in range(months - 2):
        result = minusTwo * pairs + minusOne
        minusTwo = minusOne
        minusOne = result
    print()
    print(result)
else: 
    print()
    print(1)


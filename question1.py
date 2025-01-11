import re

def extract_numbers(filenames):
    numbers = re.findall(r'\d', filenames)
    if len(numbers) == 1:
        return int(numbers[0]+ numbers[0])
    elif len(numbers) >= 2:
        return int(numbers[0]+numbers[-1])
    return 0

def calcul_total(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            total += extract_numbers(line.strip())
    return total


file_path = 'document.txt'
total = calcul_total(file_path)
print(f'The total sum is: {total}')
#nactu si radky
#nadefinuju hodnoty znaku do dict + var count 
#projedu kazdy radek a rozparsuju na pul 
#   - porovnam, ktery znak je 2x a prictu ho do promenne count
from string import ascii_lowercase, ascii_uppercase     #importing python library for EN ascii letters
letter = ascii_lowercase + ascii_uppercase              #define letter for each lower and upper cases
print(letter)

with open('input.txt') as file:                         #read given file and split it into lines
    lines = file.read().strip().split("\n")
    
count = 0

for line in lines:
    n = len(line)                                       #line length (how many letters)
    first_half = line[:(n//2)]                          #first half of line aka rucksack
    second_half = line[(n//2):]                         #second half of line aka rucksack
    
    for i, c in enumerate(letter):          
        if c in first_half and c in second_half:        #if they have common value in both two parts in rucksack
            count += letter.index(c) + 1                # +1, because indexing starts from 0 but we need "a" to have value "1", "b" to have "2" etc. 
            
print("Answer to part 1:", count)
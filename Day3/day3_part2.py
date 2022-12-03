from string import ascii_lowercase, ascii_uppercase     #importing python library for EN ascii letters
letter = ascii_lowercase + ascii_uppercase              #define letter for each lower and upper cases

with open('input.txt') as file:                         #read given file and split it into lines
    lines = file.read().strip().split("\n")
    
count = 0

for i in range(0, len(lines), 3):                                      
    group = lines[i:(i+3)]                              #set group for each three lines
    
    for i, c in enumerate(letter):          
        if all([c in line for line in group]):        
            count += letter.index(c) + 1                # +1, because indexing starts from 0 but we need "a" to have value "1", "b" to have "2" etc. 
            
print("Answer to part 2:", count)
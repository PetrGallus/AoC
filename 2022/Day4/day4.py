with open('input.txt') as file:                         #read given file and split it into lines
    lines = file.read().strip().split("\n")
    
count = 0
count2 = 0

for line in lines:
    elves = line.split(",")                                     #divide each line by , for each elve
    ranges = [list(map(int, elf.split("-"))) for elf in elves]  #create a list of ranges of each elf by "-" splitter
    
    begin1, end1 = ranges[0]
    begin2, end2 = ranges[1]
    
    if ((begin1 <= begin2) and (end1 >= end2)) or ((begin1 >= begin2) and (end1 <= end2)):
        count += 1
    
    if not ((end1 < begin2) or (begin1 > end2)):
        count2 += 1
        
print("Answer to part 1:", count)   
print("Answer to part 2:", count2)      


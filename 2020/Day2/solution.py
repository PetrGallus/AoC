sum1 = 0
sum2 = 0
with open('input.txt') as file:
    for line in file:
        parsed = line.split(" ")

        parsed1 = parsed[0]
        low = int(parsed1.split("-")[0])
        high = int(parsed1.split("-")[1])

        parsed2 = parsed[1]
        letter = parsed2[0]

        password = parsed[2]

        finds = 0

        for character in password:
            if character == letter:
                finds += 1
        if finds >= low and finds <= high:
            sum1 += 1  

        first = password[low-1]
        second = password[high-1]
        if (letter == first and letter != second) or (letter != first and letter == second):
            sum2 += 1        

print("Part 1: ",sum1)
print("Part 2: ",sum2)

name = input("Name: ")
with open("name.txt", 'w') as out_file:
    print(name, file=out_file)

with open("name.txt", 'r') as in_file:
    print(in_file.readline())

numbers = []
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        line.strip()
        numbers.append(int(line))
    result = numbers[0] + numbers[1]
    print(result)

numbers = []
total = 0
lines = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        line.strip()
        numbers.append(int(line))
        total += numbers[lines]
        lines += 1
    print(total)

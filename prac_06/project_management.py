FILENAME = "project.txt"
HEADER = "Name	Start Date	Priority	Cost Estimate	Completion Percentage"


def main():
    records = load_file(FILENAME)
    print(records)


def load_file(filename):
    records = []
    # filename = input("Filename: ")
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            parts[2] = int(parts[2])
            parts[3] = float(parts[3])
            parts[4] = int(parts[4])
            records.append(parts)
        return records


main()

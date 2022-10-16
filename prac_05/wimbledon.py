"""
CP1404 Practical 5
Game, Set, Match
Estimate: 20 minutes
Actual: 27 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Read, Process, and Display Wimbledon data"""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Read data into records list"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_records(records):
    """Process records into countries set and champion_to_count dictionary"""
    countries = set()
    champion_to_count = {}
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display results of Wimbledon records"""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(champion, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


main()

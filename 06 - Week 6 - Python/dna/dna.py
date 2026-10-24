import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    database = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            for key in row:
                if key != "name":
                    row[key] = int(row[key])
            database.append(row)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        sequence = file.read()

    # Find longest match of each STR in DNA sequence
    str_names = list(database[0].keys())[1:]
    counts = {}
    for s in str_names:
        counts[s] = longest_match(sequence, s)

    # Check database for matching profiles
    for person in database:
        if all(person[s] == counts[s] for s in str_names):
            print(person["name"])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    sub_len = len(subsequence)
    seq_len = len(sequence)

    for i in range(seq_len):
        count = 0
        while sequence[i + count * sub_len : i + (count + 1) * sub_len] == subsequence:
            count += 1
        longest_run = max(longest_run, count)

    return longest_run


if __name__ == "__main__":
    main()

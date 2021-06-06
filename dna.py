import csv
import sys

def count(sequence, dna_str):

    maximum = 0
    counter = 0
    i = 0

    while sequence[i:].find(dna_str) >= 0:

        while sequence[i:i+len(dna_str)] == dna_str:
            counter += 1
            i += len(dna_str)

        if counter > maximum:
            maximum = counter

        i = sequence[i:].find(dna_str)

    return str(maximum)

def main():

    file_sequence = open("{}".format(sys.argv[2]), "r")
    sequence = file_sequence.read()

    file_database = open("{}".format(sys.argv[1]), "r")
    database = csv.DictReader(file_database)

    for data in database:
        for key in list(data.keys()):
            valid = True
            if key != 'name':
                if data[key] != count(sequence, key):
                    valid = False
                    break
        if valid == True:
            print("{}".format(data["name"]))
            break

main()

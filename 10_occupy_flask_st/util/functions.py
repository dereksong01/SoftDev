import random
import csv

occupationDict = {}

def convertor():
    with open ('data/occupations.csv') as csvfile:
        # Why .DictReader()?
        # Idk. But if I try to use .reader(), my code breaks. Heh
        reader = csv.DictReader(csvfile) # reads file
        next(reader) # skips first line
        for line in reader: # iterates through the csv file
            if line['Job Class'] != "Total": # Total serves to be unnecessary info
                occupationDict[line['Job Class']] = float(line['Percentage'])
            else:
                total = float(line['Percentage'])
                return total
        
def randOcc():
    limit = random.uniform(0, convertor())

    # The purpose of limit was to serve as a credit, for a lack of a better word,
    # for the function to exhaust and when the credit is exhausted, it will land
    # on a key and thus, that key would be the randomly chosen occupation.
    for occPerc in occupationDict.keys():
        limit -= occupationDict[occPerc]
        if limit <= 0:
            return occPerc

# Team GudetamaV2 - Andrew Shao, Derek Song
# Soft Dev - PD8
# K#06 - StI/O: Divine your Destiny!
# 2018 - 09 - 13

import csv
import random

# python script
occupationDict = {}
with open ('occupations.csv') as csvfile:
    # Why .DictReader()?
    # Idk. But if I try to use .reader(), our code breaks. Heh
    reader = csv.DictReader(csvfile) # reads file
    next(reader) # skips first line
    for line in reader: # iterates through the csv file
        if line['Job Class'] != "Total": # Total serves to be unnecessary info
            occupationDict[line['Job Class']] = float(line['Percentage'])
        else:
            total = float(line['Percentage'])
        
# function that chooses occupation
def randOcc():
    limit = random.uniform(0, total)

    # The purpose of limit was to serve as a credit, for a lack of a better word,
    # for the function to exhaust and when the credit is exhausted, it will land
    # on a key and thus, that key would be the randomly chosen occupation.
    for occPerc in occupationDict.keys():
        limit -= occupationDict[occPerc]
        if limit <= 0:
            return occPerc

        
    

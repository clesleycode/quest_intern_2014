import csv
import StringIO as st

def search_titles(word):
    counter = 0
    with open('filename.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, quotechar = ' ',)
        for row in spamreader:
            mount = 0
            for x in row:
                if x.lower() == word.lower():
                    count = 1
                    if count == 1:
                       mount += 1
                else:
                   for word in x.replace('.','').replace("!", '').replace('"', '').replace("(",'').replace(")",'').lower().split():
                        if word == 'step':
                            count = 1
                            if count == 1:
                                mount += 1 
            if mount > 0:
                counter += 1
                print counter

import csv
import StringIO as st

def search_words(key):
    counter = 0
    with open('filename.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, quotechar = ' ',)
        for row in spamreader:
            mount = 0
            for x in row:
                for word in x.replace('.','').replace("!", '').replace("-", '').replace(":", '').replace('"', '').replace("(",'').replace(")",'').lower().split():
                    if word == key:
                        count = 1
                        if count == 1:
                            mount += 1
            if mount > 0:
                counter += 1
                print counter

def search_titles(key):
    counter = 0
    with open('filename.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, quotechar = ' ',)
        for row in spamreader:
            mount = 0
            for x in row:
                if x.lower() == key.lower():
                    count = 1
                    if count == 1:
                       mount += 1
            if mount > 0:
                counter += 1
                print counter

def search(key):
    counter = 0
    with open('filename.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, quotechar = ' ',)
        for row in spamreader:
            mount = 0
            for x in row:
                if x.lower() == key.lower():
                    count = 1
                    if count == 1:
                       mount += 1
                else:
                   for word in x.replace('.','').replace("!", '').replace('"', '').replace("-", '').replace(":", '').replace("(",'').replace(")",'').split():
                        if word == key or word == key:
                            count = 1
                            if count == 1:
                                mount += 1 
            if mount > 0:
                counter += 1
                print counter




    

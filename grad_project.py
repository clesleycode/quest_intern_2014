########################################################
# Lesley Cordero
# Quest Project 3
# Partner graduation rate of Quest Scholars, excluding transfers (Fall 08 and before)
########################################################

from xlrd import open_workbook,XL_CELL_TEXT
import csv

def graduation():
    book = open_workbook("graduation.xls")
    sheet = book.sheet_by_index(0)
    partners = [] # partner school appendage
    finalists = [] # scholars IDs
    scholars = []
    total = 0 # number of students
    gcount = 0 # graduated students
    bcount = 0 # blank cell students
    x = 0
    # Begins x index number at 0 since it counts number of students, not transitions
    for col in sheet.col(0):
        # iterates through first column and appends to list
        finalists.append(col)
    with open('partners.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, quotechar = ' ',)
    # Opens CSV file and iterates through all filled cells
        for row in spamreader:
            for it in row:
                item = "text:u'" + it + "'"
                # fixes format to compare to clearinghousedata
                partners.append(item)
                # appends each partner college to a list for comparison later on
    with open('IDs.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile, quotechar = ' ',)
        for row in spamreader:
            for it in row:
                item = "text:u'" + it + "_'"
                # Fixes ID format to match format of Clearinghouse data
                scholars.append(item)
                # Appends to list to compare to clearinghouse data
    for item in finalists:
        # Iterates through item of finalist IDs
        if x + 1 < len(finalists):
            # Proceed so long as the index number does not exceed the length of
            # the list.
            if str(finalists[x]) == str(finalists[x+1]):
                total = total
                # If the ID numbers remain the same, it is the same person so the
                # total count remains the same
            else:
                # Otherwise, it's a new person 
                if str(finalists[x]) in scholars:
                    if str(sheet.cell(x,2)) in partners:
                # since this is excluding transfer students, we have to check
                # to make sure that the student is both a Quest Scholar and still
                # attends a partner school
                        total = total + 1
                        # If they appear in these lists, increase the total by 1
                        if str(sheet.cell(x,1)) == "text:u'Y'":
                            # If the graduated? cell is equal to yes, then they graduated
                            # from somewhere
                            cell = str(sheet.cell(x,3))
                            cell = cell.split()
                            # To make sure the degree is a bachelor's, split the degree
                            # cell by whitespace
                            if cell[0] != "text:u'ASSOCIATE":
                                # Check first string- if not equal to associate,
                                # they graduated from a bachelor's or master's
                                gcount = gcount + 1
                                # therefore, increase the graduated count by 1.
        if x + 1 == len(finalists):
            # The following code is the same as the previous.
            if str(finalists[x]) in scholars:
                    if str(sheet.cell(x,2)) in partners:
                        total = total + 1
                        if str(sheet.cell(x,1)) == "text:u'Y'":
                            cell = str(sheet.cell(x,3))
                            cell = cell.split()
                            if cell[0] != "text:u'ASSOCIATE":
                                gcount = gcount + 1
        x = x + 1
        # Increases index to proceed to next student in excel file/list 
    print total
    print gcount
    print bcount
    # Prints the total number of students, followed by number graduated and blank cell count!
    



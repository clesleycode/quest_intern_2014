##########################
# Lesley Cordero
# Quest Project
##########################

from xlrd import open_workbook,XL_CELL_TEXT
import csv

def graduation():
    book = open_workbook("quest.xlsx")
    # opens excel
    sheet = book.sheet_by_index(0)
    book2 = open_workbook("partners.xlsx")
    sheet2 = book2.sheet_by_index(0)
    liss = []
    liss2 = []
    # create empty list to append cells
    tcount = 0
    # counts total number of quest scholars in excel file
    gcount = 0
    # counts number of quest scholars that graduated
    x = 0
    # set first index number to 0
    for col in sheet.col(0):
        # iterate through first column
        liss.append(col)
    for col2 in sheet2.col(0):           
        liss2.append(col2)
    for item in liss:
        # iterate through each item in list
        if x + 1 < len(liss):
            # if x + 1 is less than the length of list, proceed because
            # then program will not have run into empty cells
            if str(liss[x]) == str(liss[x+1]):
                # if cell values are equal, they are same person
                tcount = tcount 
                # since they are the same person, the total count doesnt change
            else:
                # otherwise, it's a new person
                if str(sheet.cell(x,2)) in str(liss2):
                    tcount = tcount + 1
                    # that means they went to one of our partners, so add to
                    # total count
                    if str(sheet.cell(x,1)) == "text:u'Y'":
                        gcount = gcount + 1
        if x + 1 == len(liss):
            # if x + 1 is less than the length of list, proceed because
            # then program will not have run into empty cells
            if str(sheet.cell(x,2)) in str(liss2):
                if str(sheet.cell(x,1)) == "text:u'Y'":
                    gcount = gcount + 1
        x = x + 1
    print tcount
    print gcount
    


        
    









    


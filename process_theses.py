import openpyxl
# Get spreadsheet from Box (not implemented)

# load spreadsheet
sheet = "bachelor's thesis precat worksheet.xlsx"
wb = openpyxl.load_workbook(sheet)


def make_245_c(author_statement):
    deslashed = deslash(author_statement)
    #trucased = trucase(deslashed)

    return deslashed

def deslash(str_):
    """Convert a string like by J. P. Anderson \ A. H. Boileau \ W. E. Dexter \ J. A. Yungclas."
    to one like "by J. P. Anderson, A. H. Boileau, W. E. Dexter, and J. A. Yungclas."
    """
    if (str_.count("\\") == 1):
        deslashed = str_.replace("\\", " and ")
    elif (str_.count("\\") > 1):
        temp = str_.replace("\\", ",").replace(" ,", ",")
        # Replace the last comma with an and
        deslashed = " and ".join(
            [temp[: temp.rfind(",") + 1], temp[temp.rfind(",") + 1 :]]
        )      
    else:
        deslashed = str_

    # Along the way extra spaces may have been introduced.
    # Make sure to reduce those down to one space.
    return deslashed.replace("  ", " ")



import openpyxl

import truecaser

truecaser_model_file = "resources/distributions.obj"
truecaser_model = truecaser.load_model(truecaser_model_file)

# Get spreadsheet from Box (not implemented)

# load spreadsheet
sheet = "bachelor's thesis precat worksheet.xlsx"
wb = openpyxl.load_workbook(sheet)


def make_245_c(author_statement):
    deslashed = deslash_author_statement(author_statement)
    truecased = truecase(deslashed)
    if truecased.startswith("By"):
        output = "".join(["by", truecased[2:]])
    else:
        output = truecased

    return output

def deslash_author_statement(str_):
    """Convert a string like by J. P. Anderson \ A. H. Boileau \ W. E. Dexter \ J. A. Yungclas."
    to one like "by J. P. Anderson, A. H. Boileau, W. E. Dexter, and J. A. Yungclas."
    """
    if (str_.count("\\") == 1):
        deslashed = str_.replace("\\", " and ")
    elif (str_.count("\\") > 1):
        temp = str_.replace("\\", ", ").replace(" ,", ",")
        # Replace the last comma with an and
        deslashed = " and ".join(
            [temp[: temp.rfind(",") + 1], temp[temp.rfind(",") + 1 :]]
        )      
    else:
        deslashed = str_

    # Along the way extra spaces may have been introduced.
    # Make sure to reduce those down to one space.
    return deslashed.replace("  ", " ").replace("  ", " ")


def deslash_title(str_):
    return str_.replace("\\", "").replace("  ", " ")


def truecase(str_):
    tokens = str_.split(" ")
    return " ".join(truecaser.get_true_case(tokens, "", truecaser_model))


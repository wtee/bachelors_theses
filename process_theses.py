import openpyxl

import truecaser
from fuzzywuzzy import fuzz

truecaser_model_file = "resources/distributions.obj"
truecaser_model = truecaser.load_model(truecaser_model_file)

# Get spreadsheet from Box (not implemented)

# load spreadsheet
sheet = "bachelor's thesis precat worksheet.xlsx"
wb = openpyxl.load_workbook(sheet)


def make_245_a(title):
    deslashed = deslash_title(title)
    if needs_truecase(deslashed, "title"):
        truecased = truecase(deslashed)
    else:
        truecased = deslashed
    styled = final_styling_for_title(truecased)

    return styled


def make_245_c(author_statement):
    deslashed = deslash_author_statement(author_statement)
    if needs_truecase(deslashed, "author"):
        truecased = truecase(deslashed)
    else:
        truecased = deslashed
    styled = final_styling_for_author(truecased)

    return styled


def deslash_author_statement(str_):
    """Convert a string like by J. P. Anderson \ A. H. Boileau \ W. E. Dexter \ J. A. Yungclas."
    to one like "by J. P. Anderson, A. H. Boileau, W. E. Dexter, and J. A. Yungclas."
    """
    if str_.count("\\") == 1:
        deslashed = str_.replace("\\", " and ")
    elif str_.count("\\") > 1:
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
    return " ".join(truecaser.get_true_case(tokens, "title", truecaser_model))


def needs_truecase(str_, type_):
    """Checks if a string needs to be truecased.

    Returns True or False depending on whether a string too closely resembles
    an all-caps version of the string.

    Parameters
    ----------
    str_ : str
        The string to check.
    type_ : str
        What type of string is being checked. Accepts "title" or "author".

    Returns
    -------
    bool
    """
    ratio = fuzz.ratio(str_, str_.upper())

    if type_ == "title":
        # "An Investigation of Industrial Housing" should return True.
        # "A study of the decomposition of green manures." should return
        # False.
        if ratio > 20:
            return_ = True
        else:
            return_ = False
    elif type_ == "author":
        # "by HERBERT CHARLES FLINT and WILLIAM FRANCIS LAGRANGE"
        # should return True.
        # "By A. A. Baustian, H. D. Susong, and E. Young" should
        # return False.
        if ratio > 60:
            return_ = True
        else:
            return_ = False

    return return_


def final_styling_for_title(str_):
    # remove final "." if needed; end with " /"
    styled_str = str_.rstrip(".")
    styled_str += " /"

    return styled_str


def final_styling_for_author(str_):
    # lowercase "By"; end with "."
    if str_.startswith("By"):
        styled_str = "by" + str_[2:]
    else:
        styled_str = str_

    if not styled_str.endswith("."):
        styled_str += "."

    return styled_str

#!/usr/bin/env python3

# There are more
SPECIAL_CHARS = {
    "%" : "\\%",
    "$" : "\\$",
    "{" : "\\{",
    "_" : "\\_",
    "|" : "\\textbar",
    ">" : "\\textgreater",
    "#" : "\\#",
    "&" : "\\&",
    "}" : "\\}",
    "\\": "\\textbackslash",
    "<" : "\\textless"
}

def latex_encode(string):
    """
    Encodes characters with special
    significance in latex
    """
    if not isinstance(string, str):
        raise Exception("latex_encode only accepts string parameters")

    encoded = ""
    for c in string:
        if c in SPECIAL_CHARS.keys():
            encoded += "{" + SPECIAL_CHARS[c] + "}"
        else:
            encoded += c

    return encoded

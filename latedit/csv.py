#!/usr/bin/env python3

import csv

def parse_csv(data, has_header=False):
    """
    Parses the CSV data into a list of dictionary objects
    Throws an exception if the CSV is badly formatted

    Arguments
    data -- a string containing the CSV data
    has_header -- parse the first row as a header or not
    """
    reader = csv.reader(data.splitlines())

    rows = list(reader)
    if len(rows) == 0:
        return []

    column_count = len(rows[0])
    header = []
    offset = 0
    if has_header:
        header = rows[0]
        # Skip first row if it's the header in the data
        offset = 1
    else:
        header = [ str(i) for i in range(0, column_count) ]

    ret = []
    for x in range(offset, len(rows)):
        row = rows[x]
        tmp = {}
        if len(row) != column_count:
            raise Exception(
                "Column count for row is not equal to the expected. " 
                "Expected '{}' columns, row at line '{}' has '{}' columns"
                .format(column_count, x, len(row)))
        for i in range(0, column_count):
            tmp[header[i]] = row[i]
        ret.append(tmp)

    return ret

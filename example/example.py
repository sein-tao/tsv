#!/usr/bin/env python

# add parent directory to path
import sys
sys.path.append("..")

# now the example code
import tsv
class bedFile(tsv.tsvFile):
    class Record(tsv.tsvRecord):
        _fields = ("chr", "start", "end")
        _fields_parser = {"chr": str, "start":int, "end": int}

with bedFile.open("out.bed", 'w') as out:
    for rec in bedFile.open("input.bed", 'r'):
        if  rec.end - rec.start <= 500:
            out.write(rec)

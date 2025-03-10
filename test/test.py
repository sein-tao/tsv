import tsv
class bedFile(tsv.tsvFile):
    class Record(tsv.tsvRecord):
        _fields = ("chr", "start", "end")
        _fields_parser = {"start":int, "end": int}

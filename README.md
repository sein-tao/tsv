NAME
-------
tsv : class for tsv files with named fields, especially for bioinfomatics use.

DESCRIPTION
-------
This module defines two class: tsvFile and tsvRecord, which serve as 
the superclass for derived tsv file types.

the subclasses of tsvFile should specify the Record attribute, 
which is typically a tsvRecord subclass.
To define a subclass of tsvRecord, you at least to specifiy \_fields,
the attribute names for Record columns.

The tsvFile also support file with header lines. The tsvRecord also support self-defined behavior for each filed. See document for details


EXAMPLE
-------
* define bed file 
```python
import tsv
class bedFile(tsv.tsvFile):
    class Record(tsv.tsvRecord):
        _fields = ("chr", "start", "end")
    	_fields_parser = {"chr": str, "start":int, "end": int}

```
* Read file, invoke fields and write file
```python
with bedFile.open("out.bed", 'w') as out:
    for rec in bedFile.open("input.bed", 'r'):
        if  rec.end - rec.start <= 500:
            out.write(rec)
```

REQUIREMENTS
-------
Python >= 2.6

AUTHORS
-------
Sein Tao

LISENSE
-------
This module is distributed under GNU GPL v2




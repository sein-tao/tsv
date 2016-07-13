Name
-------

tsv : class for tsv files with named fields, especially for bioinfomatics use.

tsv now is part of BioUtil_ module. code here may out of date.

.. _BioUtil: https://github.com/sein-tao/pyBioUtil

Description
-----------

This module defines two class: tsvFile and tsvRecord, which serve as 
the superclass for derived tsv file types.

the subclasses of tsvFile should specify the Record attribute, 
which is typically a tsvRecord subclass.
To define a subclass of tsvRecord, you at least to specifiy \_fields,
the attribute names for Record columns.

The tsvFile also support file with header lines. The tsvRecord also support self-defined behavior for each filed. See document for details


Example
--------
* define bed file
.. code-block:: python

    import tsv
    class bedFile(tsv.tsvFile):
        class Record(tsv.tsvRecord):
            _fields = ("chr", "start", "end")
            _fields_parser = {"start":int, "end": int}

* Read file, invoke fields and write file
.. code-block:: python

    with bedFile.open("out.bed", 'w') as out:
        for rec in bedFile.open("input.bed", 'r'):
            if  rec.end - rec.start <= 500:
                out.write(rec)

Requirements
------------
Python >= 2.6

Authors
--------
Sein Tao

Lisense
--------
GNU GPL v2




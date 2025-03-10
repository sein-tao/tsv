"""
xzopen - open (may) gzip/bz2 files
Sein Tao, <sein.tao@gmail.com>
2012-07-07 19:33:41 CST
2015-05-18
"""
# __debug = True
# if __debug: 
#     import sys
import builtins
def xzopen(file, *args, **kargs):
    try:
        if file.endswith('.gz') or file.endswith('.bgz'):
            # if __debug: sys.stderr.write(file + ":\tgz\n")
            import gzip
            return gzip.open(file, *args, **kargs)
        elif file.endswith('.bz2'):
            # if __debug: sys.stderr.write(file + ":\tbz2\n")
            import bz2
            return bz2.BZ2File(file, *args, **kargs)
        else:
            return builtins.open(file, *args, **kargs)
    except:
        raise



if __name__ == '__main__':
    pass






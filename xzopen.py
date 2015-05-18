"""
gzopen.pm - open (may) gzip/bz2 files
XU Yu, <xuyu@genomics.org.cn>
2012-07-07 19:33:41 CST
"""
# __debug = True
# if __debug: 
#     import sys
import __builtin__
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
            return __builtin__.open(file, *args, **kargs)
    except:
        raise

# deprecated, for compatibility
open = xzopen

if __name__ == '__main__':
    pass






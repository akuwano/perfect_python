import sys

def echo2(in_, out):

    for line in in_:
        out.write("{0} {1}".format(len(line), line))
        out.write("{0:04} {1}".format(len(line), line))
        out.write("{0:,} {1}".format(len(line) * 100000, line))

echo2(sys.stdin, sys.stdout)

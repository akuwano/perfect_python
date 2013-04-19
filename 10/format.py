import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __format__(self, spec):
        return ("({0.x:" + spec + "}, {0.y:" + spec + "})").format(self)

def echo2(line, out):
    out.write("{0} {1}\n".format(len(line), line))
    out.write("{0:04} {1}\n".format(len(line), line))
    out.write("{0:,} {1}\n".format(len(line) * 100000, line))

testdict = { 'x': 1, 'y':2 }
test = "({0[x]}, {0[y]})".format(testdict)
print(test)

testlist = [3, 4]
test = "({0[0]}, {0[1]})".format(testlist)
print(test)

echo2("TESTTESTTEST", sys.stdout)

p = Point(7, 8)
print(format(p))

# ERROR
testdict2 = { '200': 5, '201':6 }
test = "({0[200]}, {0[201]})".format(testdict2)
print(test)




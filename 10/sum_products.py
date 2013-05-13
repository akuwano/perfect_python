import sys
import argparse
import traceback
import logging

class ArgumentParse(object):
    """
    Parse Argument.

    """
    def __init__(self):
        try:
            parser = argparse.ArgumentParser(description='Command Description')
            parser.add_argument('-f', action="store", dest="file", \
                             help=u"読み込みファイル  defualt=testfile", \
                             default="testfile")
            self.optargs = parser.parse_args()
            self.checkopts()
        except Exception as e:
            print >>sys.stderr, "Argument Parse Error"
            print >>sys.stderr, str(e)
            exit(1)

    def checkopts(self):
        if not self.optargs.file:
            self.opt_messages.append("-f options is required.")
            exit(1)

def sum_products(filename):
    with open(filename) as f:
        results = {}
        for line in f:
            parts = line.split(",")
            title = parts[0]
            count = int(parts[1])
            last_count = results.get(title, 0)
            results[title] = last_count + count
    return results

def print_results(results):
    for key, value in sorted(results.items(), operator.itemgetter(1)):
        print(key, value)

def main():
    arguparse = ArgumentParse()
    results = sum_products(arguparse.optargs.file)
    print_results(results)

if __name__ == "__main__":
    main()


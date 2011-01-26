#!/usr/bin/env python
import optparse
import sys
import webbrowser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    parser = optparse.OptionParser(usage="usage: %prog [options]")
    parser.add_option('-a', '--asin', dest='asin')
    (options, args) = parser.parse_args(argv[1:])
    if options.asin is not None:
        webbrowser.get('firefox').open('http://www.amazon.com/gp/product/'+options.asin)
    else:
        parser.error('Please supply an ASIN with --asin')

if __name__ == '__main__':
    sys.exit(main())

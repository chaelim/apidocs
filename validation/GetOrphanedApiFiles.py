#
#
#
#
import os
import codecs
import re
from collections import defaultdict

################################################################################
#   Globals
################################################################################
ROOTDIR = 'v1.0'
api_file_names = {}

################################################################################
### __main__
################################################################################

if __name__ == '__main__':
    # Command line args
    import getopt
    import sys

    def usage (exitcode=1):
        from os.path import basename
        print('Usage:  %s [-h] [-r=<Root Folder>]\n\t-h: dispplay \n\tDefault Root Dir = %s' % \
            (basename(__file__).rsplit('.')[0], ROOTDIR), \
            file=sys.stderr)
        sys.exit(exitcode)

    try:
        opts, args = \
            getopt.getopt(              \
                sys.argv[1:], "hr:dv",     \
                ["help", "delete", "verbose"]     \
            )
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    verbose = False
    delete = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-r", "--root"):
            ROOTDIR = a
        elif o in ("-d", "--delete"):
            delete = true
        else:
            assert False, "unhandled option"

    API_DIR = os.path.abspath(''.join([ '../', ROOTDIR, '/api']))
    RESOURCE_DIR = os.path.abspath(''.join([ '../', ROOTDIR, '/resources']))

    print('* API Folder: %s' % API_DIR)
    print('* Resource Folder: %s\n' % RESOURCE_DIR)
    #
    #
    #
    for dirpath, dirnames, files in os.walk(API_DIR):
        for name in files:
            if name.endswith('.md'):
                api_file_names[name] = 0

    for root, dirs, files in os.walk(RESOURCE_DIR):
        for name in files:
            with codecs.open(os.path.join(root, name), 'r', encoding='utf8') as f:
                lines = f.readlines()
                for line in lines:
                    s = re.search('\(\.\.\/api\/([^\)]+)\)', line)
                    if s:
                        if s.group(1) in api_file_names:
                            api_file_names[s.group(1)] += 1
                        else:
                            print('ERROR: Broken link in file \"%s\" : %s' % (name, s.group(1)))

    orphaned_file_count = 0
    for k, v in api_file_names.items():
        if v == 0:
            orphaned_file_count += 1
            print("ERROR: Orphaned file \"%s\"" % k)

    print('\nTotal orphaned Api file count: %d' % orphaned_file_count)
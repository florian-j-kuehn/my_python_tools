#!/usr/local/bin/python3.6


"""
 Create new python file with minimum requirements.
 Created by Florian Kuehn.

 While creating the directory we try to catch an exception if something is
 wrong. Errors for already existing files are suppressed.

 Things to add:
    - main function to make use of docopt
"""


from docopt import docopt
import sys
import os
import errno
import time



NAME = 'Path and file creator'
VERSION = '0.0.1'
VERSIONSTR = '{} v. {}'.format(NAME, VERSION)
SCRIPT = os.path.split(os.path.abspath(sys.argv[0]))[1]
SCRIPTDIR = os.path.abspath(sys.path[0])

USAGESTR = """{versionstr}
    Usage:
        {script} [-h | -v]
        {script} -r

    Options:
        -h,--help     : Show this help message.
        -r,--raw      : Show raw bytes repr() instead of trying to decode.
        -v,--version  : Show version.
""".format(script=SCRIPT, versionstr=VERSIONSTR)
#docopt(USAGESTR, version=VERSIONSTR)


# Get (f)filename from cmdline.
f_name = input('Input filename: ')
f_file = f_name + '.py'


# (d)Directory commands.
d_name = input('Input new dir: ')


# Create directory if needed. Throw error exception.
# Wait two seconds before creation.
try:
    print('Creating directory {}'.format(d_name))
    os.makedirs(d_name)
except OSError as exception:
    if exception.errno == errno.EEXIST:
        sys.exit('There was an error creating the file.')
        raise


# Open file and write SHEBANG to it. Also print absolute file (p)path for new file.
with open(os.path.join(d_name, f_file), 'w') as f:
    f.write('#!/usr/local/bin/python3.6\n\n\n# Created by Florian Kuehn.')
    print('File created ...' + os.path.abspath(os.path.join(d_name, f_file)))

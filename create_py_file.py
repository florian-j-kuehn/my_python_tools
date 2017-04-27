#!/usr/local/bin/python3.6


"""
 Create new python file with SHEBANG.
 Created by Florian Kuehn.

 While creating the directory we try to catch an exception if something is
 wrong. Errors for already existing files are suppressed.

 Things to add:
    - main function to make use of docopt - done
    - add docopt and main def stuff to file creation
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

    Options:
        -h,--help     : Show this help message.
        -v,--version  : Show version.
""".format(script=SCRIPT, versionstr=VERSIONSTR)



# Header text starts here
h = """
#!/usr/local/bin/python3.6


\"\"\"
Create new python file with SHEBANG.
Created by Florian Kuehn.

\"\"\"


from docopt import docopt


NAME = 'xy'
VERSION = '0.0.1'
VERSIONSTR = '{} v. {}'.format(NAME, VERSION)
SCRIPT = os.path.split(os.path.abspath(sys.argv[0]))[1]
SCRIPTDIR = os.path.abspath(sys.path[0])
USAGESTR = \"\"\"{versionstr}
    Usage:
        {script} [-h | -v]


    Options:
        -h,--help     : Show this help message.
        -v,--version  : Show version.
\"\"\".format(script=SCRIPT, versionstr=VERSIONSTR)


def main(argd):
# Start Programming here
"""


# Create directory if needed. Throw error exception.
# Wait two seconds before creation.
def main(argd):
    # Get (f)filename from cmdline.
    f_name = input('Input filename: ')
    f_file = f_name + '.py'


    # (d)Directory commands.
    d_name = input('Input new dir: ')


    """ Main entry point, expects doctopt arg dict as argd """
    try:
        print('Creating directory {}'.format(d_name))
        os.makedirs(d_name)
    except OSError as exception:
        if exception.errno == errno.EEXIST:
            sys.exit('There was an error creating the file.')
            raise
    # Open file and write SHEBANG to it. Also print absolute file (p)path for new file.
    with open(os.path.join(d_name, f_file), 'w') as f:
        f.write(h)
        print('File created ...' + os.path.abspath(os.path.join(d_name, f_file)))


# Call the main function together with docstring if given.
if __name__ == '__main__':
    main(docopt(USAGESTR, version=VERSIONSTR))

#!/usr/local/bin/python3.6


"""
 Create new python file with minimum requirements.
 Created by Florian Kuehn.

 While creating the directory we try to catch an exception if something is
 wrong. Errors for already existing files are suppressed.
"""


import sys
import os
import errno
import time


# Get (f)filename from cmdline.
f_name = input('Input filename: ')
f_extension = '.py'
f_file = f_name + f_extension


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


# Open file and write SHEBANG to it. Also print absolute file path for new file.
with open(os.path.join(d_name, f_file), 'w') as f:
    t = '#!/usr/local/bin/pydon3.6\n\n\n# Created by Florian Kuehn.'
    f.write(t)
    p_new = os.path.join(d_name, f_file)
    print('File created ...' + os.path.abspath(p_new))

#!/usr/local/bin/python3.6

# Create new python file with minimum requirements.
# Created by Florian Kuehn.


# Import modules.
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
# Wait three seconds between check and creation.
if not os.path.exists(d_name):
    print('Wait ...')
    time.sleep(2)
    try:
        print('Creating directory {}'.format(d_name))
        os.makedirs(d_name)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise


# Open file and write SHEBANG to it. Also print absolute file path to new file.
with open(os.path.join(d_name, f_file), 'w') as f:
    t = '#!/usr/local/bin/pydon3.6\n\n\n# Created by Florian Kuehn.'
    f.write(t)
    # f.write('#!/usr/local/bin/python3.6')
    p_new = os.path.join(d_name, f_file)
    print('Just created ...' + os.path.abspath(p_new))

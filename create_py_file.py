#!/usr/local/bin/python3.6

# Create new python file with minimum requirements.
# Created by Florian Kuehn.


import sys
import os
import errno 


# Get (f)filename from cmdline.
f_name = input('Input filename: ')
f_extension = '.py'
f_file = f_name + f_extension


# (d)Directory commands.
d_name = input('Input new dir: ')


# Create directory if needed.
if not os.path.exists(d_name):
    print('Creating directory {}'.format(d_name))
    try:
        os.makedirs(d_name)
    except OSError as error:
        if error.errno != errno.EEXIST:
            raise


# Opening file.
with open(os.path.join(d_name, f_file), 'w') as f:
    f.write('#!/usr/local/bin/python3.6')
    print('Just created {}'.format(f_file))

#!/usr/bin/env python
import subprocess

import glob


def upload():

    for filename in glob.iglob('build/**/spotlight-*.tar.bz2', recursive=True):
        print('Uploading {}...'.format(filename))
        subprocess.check_call(['anaconda',
                               'upload',
                               '--force',
                               filename])


if __name__ == '__main__':
    upload()

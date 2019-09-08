#!/usr/bin/env python
import os
import shutil
import subprocess


def make_build_dir():

    if os.path.exists('./build'):
        shutil.rmtree('./build')

    os.mkdir('build')
    os.mkdir('build/linux-64')


def get_package_name(python):

    command = ['conda',
               'build',
               '--channel',
               'pytorch',
               '--py',
               python,
               '--output',
               'recipe']

    print(' '.join(command))
    return (subprocess.check_output(command, env=os.environ)
            .decode('utf-8').replace('\n', ''))


def build(python):

    command = ['conda',
               'build',
               '--channel',
               'pytorch',
               '--py',
               python,
               'recipe']

    print(' '.join(command))
    subprocess.check_call(' '.join(command), shell=True)


def convert(name):

    command = ['conda',
               'convert',
               '--platform',
               'all',
               '-o',
               './build',
               name]

    shutil.copy(name, './build/linux-64')

    print(' '.join(command))
    subprocess.check_call(command, env=os.environ)


if __name__ == '__main__':

    make_build_dir()

    for python in ('2.7', '3.6', '3.7'):

        build(python)
        package_name = get_package_name(python)
        convert(package_name)

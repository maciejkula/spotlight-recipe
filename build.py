import os
import subprocess


def make_build_dir():

    if not os.path.exists('build'):
        os.mkdir('build')


def get_package_name(python):

    command = ['conda',
               'build',
               #'--croot',
               #'build',
               '--py',
               python,
               '--output',
               '.']

    return subprocess.check_output(command).decode('utf-8')


def build(python):

    command = ['conda',
               'build',
               #'--croot',
               #'build',
               '--py',
               python,
               '.']

    subprocess.check_call(command)


if __name__ == '__main__':

    make_build_dir()

    for python in ('2.7'):#, '3.5', '3.6'):
        out_name = get_package_name(python)
        build(python)

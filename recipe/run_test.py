import subprocess


import spotlight


VERSION = getattr(spotlight, '__version__', 'v0.1.6')


def run_tests():

    clone = ['git',
             'clone',
             'https://github.com/maciejkula/spotlight.git']
    subprocess.check_call(clone)

    checkout = 'cd spotlight && git checkout tags/{}'.format(VERSION)
    subprocess.check_call(checkout, shell=True)

    move = 'mv spotlight/tests tests/ && rm -rf spotlight'
    subprocess.check_call(move, shell=True)

    subprocess.check_call(['py.test', '-v', 'tests/'])

    subprocess.check_call('rm -rf tests/', shell=True)


run_tests()

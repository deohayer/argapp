'''
Wrapper for argparse and argcomplete.

Compatible with Python versions 3.6 - 3.11.
'''

import sys


class Arg:
    '''
    '''

    @property
    def name(self) -> 'str':
        '''
        '''

    @name.setter
    def name(self, v: 'str | None') -> 'None':
        ...

    @property
    def lopt(self) -> 'str':
        '''
        '''

    @lopt.setter
    def lopt(self, v: 'str | None') -> 'None':
        ...


class App:
    '''
    '''


class ArgHelper:
    '''
    '''


class AppHelper:
    '''
    '''


class Completer:
    '''
    '''


class CompleterNone:
    '''
    '''


class CompleterList:
    '''
    '''


class CompleterPath:
    '''
    '''


class CallError:
    '''
    '''


def main(
    app: 'App',
    argv: 'list[str]' = sys.argv,
) -> 'None':
    '''
    '''

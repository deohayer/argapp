import sys


class Arg:
    ...


class App:
    ...


class ArgHelper:
    ...


class AppHelper:
    ...


class Completer:
    ...


class CompleterNone:
    ...


class CompleterList:
    ...


class CompleterPath:
    ...


class CallError:
    ...


def main(
    app: 'App',
    argv: 'list[str]' = sys.argv,
) -> 'None':
    ...

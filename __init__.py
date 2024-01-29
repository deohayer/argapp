import sys


class Arg:
    @property
    def name(self) -> 'str':
        ...

    @name.setter
    def name(self, v: 'str | None') -> 'None':
        ...

    @property
    def lopt(self) -> 'str':
        ...

    @lopt.setter
    def lopt(self, v: 'str | None') -> 'None':
        ...

    @property
    def sopt(self) -> 'str':
        ...

    @sopt.setter
    def sopt(self, v: 'str | None') -> 'None':
        ...

    @property
    def help(self) -> 'str':
        ...

    @help.setter
    def help(self, v: 'str | None') -> 'None':
        ...

    @property
    def helper(self) -> 'ArgHelper':
        ...

    @helper.setter
    def helper(self, v: 'ArgHelper | None') -> 'None':
        ...

    @property
    def type(self) -> 'type':
        ...

    @type.setter
    def type(self, v: 'type | None') -> 'None':
        ...

    @property
    def count(self) -> 'int | str':
        ...

    @count.setter
    def count(self, v: 'int | str | None') -> 'None':
        ...

    @property
    def default(self) -> 'object | list | None':
        ...

    @default.setter
    def default(self, v: 'object | list | None') -> 'None':
        ...

    @property
    def choices(self) -> 'dict':
        ...

    @choices.setter
    def choices(self, v: 'dict | None') -> 'None':
        ...

    @property
    def restrict(self) -> 'bool':
        ...

    @restrict.setter
    def restrict(self, v: 'bool | None') -> 'None':
        ...

    @property
    def suppress(self) -> 'bool':
        ...

    @suppress.setter
    def suppress(self, v: 'bool | None') -> 'None':
        ...

    @property
    def required(self) -> 'bool':
        ...

    @required.setter
    def required(self, v: 'bool | None') -> 'None':
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

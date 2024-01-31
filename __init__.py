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

    @property
    def append(self) -> 'bool':
        ...

    @append.setter
    def append(self, v: 'bool | None') -> 'None':
        ...

    @property
    def completer(self) -> 'Completer':
        ...

    @completer.setter
    def completer(self, v: 'Completer | None') -> 'None':
        ...

    @property
    def optional(self) -> 'bool':
        ...

    @property
    def positional(self) -> 'bool':
        ...

    @property
    def flag(self) -> 'bool':
        ...

    @property
    def single(self) -> 'bool':
        ...

    @property
    def multiple(self) -> 'bool':
        ...

    def __init__(
        self,
        name: 'str | None' = None,
        lopt: 'str | None' = None,
        sopt: 'str | None' = None,
        help: 'str | None' = None,
        helper: 'ArgHelper | None' = None,
        type: 'type | None' = None,
        count: 'int | str | None' = None,
        default: 'object | list | None' = None,
        choices: 'dict | None' = None,
        restrict: 'bool | None' = None,
        suppress: 'bool | None' = None,
        required: 'bool | None' = None,
        append: 'bool | None' = None,
        completer: 'Completer | None' = None,
    ) -> 'None':
        ...

    def __call__(
        self,
        v: 'bool | int | str | list | list[list] | None',
    ) -> 'bool | int | object | list | list[list] | None':
        ...


class App:
    @property
    def name(self) -> 'str':
        ...

    @name.setter
    def name(self, v: 'str | None') -> 'None':
        ...

    @property
    def help(self) -> 'str':
        ...

    @help.setter
    def help(self, v: 'str | None') -> 'None':
        ...

    @property
    def prolog(self) -> 'str':
        ...

    @prolog.setter
    def prolog(self, v: 'str | None') -> 'None':
        ...

    @property
    def epilog(self) -> 'str':
        ...

    @epilog.setter
    def epilog(self, v: 'str | None') -> 'None':
        ...

    @property
    def helper(self) -> 'AppHelper':
        ...

    @helper.setter
    def helper(self, v: 'AppHelper | None') -> 'None':
        ...

    @property
    def args(self) -> 'list[Arg]':
        ...

    @property
    def apps(self) -> 'list[App]':
        ...

    def __init__(
        self,
        name: 'str | None' = None,
        help: 'str | None' = None,
        epilog: 'str | None' = None,
        prolog: 'str | None' = None,
        helper: 'AppHelper | None' = None,
    ) -> 'None':
        ...

    def __call__(
        self,
        args: 'dict[Arg]',
        apps: 'list[App]',
    ) -> 'None':
        ...


class ArgHelper:
    @property
    def choices(self) -> 'bool':
        ...

    @choices.setter
    def choices(self, v: 'bool | None') -> 'None':
        ...

    @property
    def default(self) -> 'bool':
        ...

    @default.setter
    def default(self, v: 'bool | None') -> 'None':
        ...

    def text_help(self, arg: 'Arg') -> 'str':
        ...

    def text_usage(self, arg: 'Arg') -> 'str':
        ...

    def __init__(
        self,
        choices: 'bool | None' = None,
        default: 'bool | None' = None,
    ) -> 'None':
        ...


class AppHelper:
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

    def text_help(
        self,
        apps: 'list[App]',
        name: 'str',
    ) -> 'str':
        ...

    def text_usage(
        self,
        apps: 'list[App]',
        name: 'str',
    ) -> 'str':
        ...

    def section_prolog(
        self,
        title: 'str',
        app: 'App',
    ) -> 'str':
        ...

    def section_epilog(
        self,
        title: 'str',
        app: 'App',
    ) -> 'str':
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

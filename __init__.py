import sys


class Arg:
    @property
    def name(self) -> 'str':
        return self.__name

    @name.setter
    def name(self, v: 'str | None') -> 'None':
        # Validate.
        _raise_t(v, (str, type(None)), 'Arg.name')
        # Set.
        self.___name = v or ''
        self.__name = self.___name or self.lopt.upper() or self.sopt.upper()

    @property
    def lopt(self) -> 'str':
        return self.__lopt

    @lopt.setter
    def lopt(self, v: 'str | None') -> 'None':
        # Validate.
        _raise_t(v, (str, type(None)), 'Arg.lopt')
        # Set.
        self.__lopt = v or ''
        self.name = self.___name

    @property
    def sopt(self) -> 'str':
        return self.__sopt

    @sopt.setter
    def sopt(self, v: 'str | None') -> 'None':
        # Validate.
        _raise_t(v, (str, type(None)), 'Arg.sopt')
        _raise_v(v,
                 v is None or len(v) < 2,
                 'Arg.sopt',
                 'Must not exceed one character.')
        # Set.
        self.__sopt = v or ''
        self.name = self.___name

    @property
    def help(self) -> 'str':
        return self.__help

    @help.setter
    def help(self, v: 'str | None') -> 'None':
        # Validate.
        _raise_t(v, (str, type(None)), 'Arg.help')
        # Set.
        self.__help = v or ''

    @property
    def helper(self) -> 'ArgHelper':
        return self.__helper

    @helper.setter
    def helper(self, v: 'ArgHelper | None') -> 'None':
        # Validate.
        _raise_t(v, (ArgHelper, type(None)), 'Arg.helper')
        # Set.
        self.__helper = v or ArgHelper()

    @property
    def type(self) -> 'type':
        return self.__type

    @type.setter
    def type(self, v: 'type | None') -> 'None':
        self.__type = v

    @property
    def count(self) -> 'int | str':
        return self.__count

    @count.setter
    def count(self, v: 'int | str | None') -> 'None':
        # Validate.
        V = 'Arg.count'
        _raise_t(v, (int, str, type(None)), V)
        if self.optional:
            if isinstance(v, int):
                M = f'Must be non-negative for optional.'
                _raise_v(v, v >= 0, V, M)
            if isinstance(v, str):
                M = f'Must be "?", "*" or "+" for optional.'
                _raise_v(v, v in ['?', '*', '+'], V, M)
        if self.positional:
            if isinstance(v, int):
                M = f'Must be positive for positional.'
                _raise_v(v, v > 0, V, M)
            if isinstance(v, str):
                M = f'Must be "?", "*", "+" or "~" for positional.'
                _raise_v(v, v in ['?', '*', '+', '~'], V, M)
        if isinstance(self.default, list):
            l = len(self.default)
            if v == '+':
                M = f'Must allow zero values, self.default is empty.'
                _raise_v(v, l != 0, V, M)
            if isinstance(v, int):
                M = f'Must match the number of values in self.default: {l}.'
                _raise_v(v, v == l, V, M)
        # Set.
        self.___count = v
        self.__count = self.___count
        if self.__count is None:
            self.__count = '*' if isinstance(self.default, list) else 1

    @property
    def default(self) -> 'object | list | None':
        return self.__default

    @default.setter
    def default(self, v: 'object | list | None') -> 'None':
        self.__default = v
        self.count = self.___count

    @property
    def choices(self) -> 'dict':
        return self.__choices

    @choices.setter
    def choices(self, v: 'dict | None') -> 'None':
        self.__choices = v

    @property
    def restrict(self) -> 'bool':
        return self.__restrict

    @restrict.setter
    def restrict(self, v: 'bool | None') -> 'None':
        # Validate.
        _raise_t(v, (bool, type(None)), 'Arg.restrict')
        # Set.
        self.__restrict = True if v is None else v

    @property
    def suppress(self) -> 'bool':
        return self.__suppress

    @suppress.setter
    def suppress(self, v: 'bool | None') -> 'None':
        self.__suppress = v

    @property
    def required(self) -> 'bool':
        return self.__required

    @required.setter
    def required(self, v: 'bool | None') -> 'None':
        self.__required = v

    @property
    def append(self) -> 'bool':
        return self.__append

    @append.setter
    def append(self, v: 'bool | None') -> 'None':
        self.__append = v

    @property
    def completer(self) -> 'Completer':
        return self.__completer

    @completer.setter
    def completer(self, v: 'Completer | None') -> 'None':
        self.__completer = v

    @property
    def optional(self) -> 'bool':
        return bool(self.sopt or self.lopt)

    @property
    def positional(self) -> 'bool':
        return not self.optional

    @property
    def flag(self) -> 'bool':
        return self.count == 0

    @property
    def single(self) -> 'bool':
        return self.count == 1 or self.count == '?'

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
        # Actual value.
        self.___name: 'str | None' = None
        # No lopt.
        # No sopt.
        # No help.
        # No helper.
        self.___type: 'type | None' = None
        self.___count: 'int | str | None' = None
        self.___default: 'object | list | None' = None
        self.___choices: 'dict | None' = None
        # No restrict.
        self.___suppress: 'bool | None' = None
        self.___required: 'bool | None' = None
        self.___append: 'bool | None' = None
        self.___completer: 'Completer | None' = None
        # Cached value.
        self.__name: 'str' = ''
        self.__lopt: 'str' = ''
        self.__sopt: 'str' = ''
        self.__help: 'str' = ''
        self.__helper: 'ArgHelper' = ArgHelper()
        self.__type: 'type' = str
        self.__count: 'int | str' = 1
        self.__default: 'object | list | None' = None
        self.__choices: 'dict' = {}
        self.__restrict: 'bool' = True
        self.__suppress: 'bool' = False
        self.__required: 'bool' = True
        self.__append: 'bool' = False
        self.__completer: 'Completer' = CompleterPath()
        # Set the fields.
        self.name = name
        self.lopt = lopt
        self.sopt = sopt
        self.help = help
        self.helper = helper
        self.type = type
        self.count = count
        self.default = default
        self.choices = choices
        self.restrict = restrict
        self.suppress = suppress
        self.required = required
        self.append = append
        self.completer = completer

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

    def section_apps(
        self,
        title: 'str',
        apps: 'list[App]',
    ) -> 'str':
        ...

    def section_args(
        self,
        title: 'str',
        apps: 'list[Arg]',
    ) -> 'str':
        ...

    def __init__(
        self,
        lopt: 'str | None' = 'help',
        sopt: 'str | None' = 'h',
        help: 'str | None' = 'Show the help text and exit.',
    ) -> 'None':
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
    @property
    def text(self) -> 'str':
        ...

    @text.setter
    def text(self, v: 'str | None') -> 'None':
        ...

    @property
    def code(self) -> 'int':
        ...

    @code.setter
    def code(self, v: 'int | None') -> 'None':
        ...

    def __init__(
        self,
        text: 'str | None' = None,
        code: 'int | None' = None,
    ) -> 'None':
        ...


def main(
    app: 'App',
    argv: 'list[str]' = sys.argv,
) -> 'None':
    ...


def _str(o: 'object') -> 'str':
    if isinstance(o, str):
        return f'"{o}"'
    if isinstance(o, type):
        return 'None' if o is type(None) else o.__name__
    return str(o)


def _raise_t(
    o: 'object',
    t: 'type | tuple[type]',
    v: 'str',
) -> 'None':
    if isinstance(t, type):
        t = (t,)
    if isinstance(o, t):
        return
    types = ', '.join(_str(x) for x in t)
    raise TypeError(
        f'{v}: Invalid type: {type(o).__name__}. Must be: {types}.')


def _raise_v(
    o: 'object',
    c: 'bool',
    v: 'str',
    m: 'str',
) -> 'None':
    if c:
        return
    raise ValueError(f'{v}: Invalid value: {_str(o)}. {m}')

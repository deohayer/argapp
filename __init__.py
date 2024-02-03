import sys
from typing import Iterable


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
        self.suppress = self.__suppress
        self.required = self.__required
        self.append = self.__append

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
        self.suppress = self.__suppress
        self.required = self.__required
        self.append = self.__append

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
        # Validate.
        V = 'Arg.type'
        _raise_t(v, (type, type(None)), V)
        if v is not None:
            M = f'Must match self.default:'
            if isinstance(self.default, list) and self.default:
                M = f'{M} {_str(type(self.default[0]))}.'
                _raise_v(v, isinstance(self.default[0], v), V, M)
            elif not isinstance(self.default, list) and self.default is not None:
                M = f'{M} {_str(type(self.default))}.'
                _raise_v(v, isinstance(self.default, v), V, M)
        # Set.
        self.___type = v
        self.__type = self.___type
        if self.flag:
            self.__type = bool
        elif self.__type is None:
            if isinstance(self.default, list) and self.default:
                self.__type = type(self.default[0])
            elif not isinstance(self.default, list) and self.default is not None:
                self.__type = type(self.default)
            else:
                self.__type = str
        if self.___completer is None:
            self.completer = None

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
        v = self.__count
        self.__count = self.___count
        if self.__count is None:
            self.__count = '*' if isinstance(self.default, list) else 1
        if self.___type is None:
            self.type = None
        if self.___default is None and self.__count is not v:
            self.default = None

    @property
    def default(self) -> 'object | list | None':
        return self.__default

    @default.setter
    def default(self, v: 'object | list | None') -> 'None':
        # Validate.
        V = 'Arg.default'
        if isinstance(v, Iterable) and not isinstance(v, str):
            v = [x for x in v]
        if self.___type is not None:
            if isinstance(v, list):
                for i in range(len(v)):
                    _raise_t(v[i], self.type, f'{V}[{i}]')
            else:
                _raise_t(v, (self.type, type(None)), V)
        if self.___count is not None:
            if isinstance(v, list):
                if self.single:
                    raise TypeError(
                        f'{V}: Invalid type: list. Must be: object, None.')
                if isinstance(self.count, int):
                    M = f'Must match self.count: {self.count}.'
                    O = Exception(f'len() is {len(v)}')
                    _raise_v(O, len(v) == self.count, V, M)
                elif self.count == '+':
                    M = 'Must have at least one item, self.count is "+".'
                    _raise_v(v, bool(v), V, M)
            elif self.multiple:
                _raise_t(v, (list, type(None)), V)
        # Set.
        self.___default = v
        self.__default = self.___default
        if self.__default is None:
            if self.flag:
                self.__default = False
            elif self.___count in ['*', '~']:
                self.__default = []
        if self.___count is None:
            self.count = None
        if self.___type is None:
            self.type = None

    @property
    def choices(self) -> 'dict[str, str]':
        return self.__choices

    @choices.setter
    def choices(self, v: 'list | dict | None') -> 'None':
        # Validate.
        _raise_t(v, (Iterable, type(None)), 'Arg.choices')
        # Set.
        self.__choices = {}
        if isinstance(v, dict):
            self.__choices = {str(x): str(y) for x, y in v.items()}
        elif v:
            self.__choices = {str(x): '' for x in v}
        if self.___completer is None:
            self.completer = None

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
        # Validate.
        _raise_t(v, (bool, type(None)), 'Arg.suppress')
        # Set.
        self.__suppress = False if self.positional else bool(v)

    @property
    def required(self) -> 'bool':
        return self.__required

    @required.setter
    def required(self, v: 'bool | None') -> 'None':
        # Validate.
        _raise_t(v, (bool, type(None)), 'Arg.required')
        # Set.
        self.__required = self.positional or bool(v)

    @property
    def append(self) -> 'bool':
        return self.__append

    @append.setter
    def append(self, v: 'bool | None') -> 'None':
        # Validate.
        _raise_t(v, (bool, type(None)), 'Arg.append')
        # Set.
        self.__append = False if self.positional else bool(v)

    @property
    def completer(self) -> 'Completer':
        return self.__completer

    @completer.setter
    def completer(self, v: 'Completer | None') -> 'None':
        # Validate.
        _raise_t(v, (Completer, type(None)), 'Arg.completer')
        # Set.
        self.___completer = v
        self.__completer = self.___completer
        if self.__completer is None:
            if self.choices:
                self.__completer = CompleterList(self.choices)
            elif issubclass(self.type, str):
                self.__completer = CompleterPath()
            else:
                self.__completer = CompleterNone()

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
        return not (self.flag or self.single)

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
        # No choices.
        # No restrict.
        # No suppress.
        # No required.
        # No append.
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
        self.__choices: 'dict[str, str]' = {}
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
        if self.flag:
            if not self.append:
                return self.__call___bool(v)
            else:
                return self.__call___int(v)
        if self.single:
            if not self.append:
                return self.__call___str(v)
            else:
                return self.__call___list(v)
        if self.multiple:
            if not self.append:
                return self.__call___list_str(v)

    def __call___bool(self, v: 'bool') -> 'bool':
        return not self.default if v else self.default

    def __call___int(self, v: 'int') -> 'int':
        return v

    def __call___str(self, v: 'str | None') -> 'object | None':
        if self.restrict and self.choices:
            if v is not None and v not in self.choices:
                raise CallError(
                    f'Invalid value of argument {self.__strname()}: {v}. '
                    f'Must be one of:{self.__strchoices()}',
                    1)
        return self.default if v is None else self.type(v)

    def __call___list(self, v: 'list[str | None]') -> 'list[object | None]':
        if self.restrict and self.choices:
            for i in range(len(v)):
                if v[i] is not None and v[i] not in self.choices:
                    raise CallError(
                        f'Invalid value of argument {self.__strname()}[{i}]: {v[i]}. '
                        f'Must be one of:{self.__strchoices()}',
                        1)
        return [self.default if x is None else self.type(x) for x in v]

    def __call___list_str(self, v: 'list[str] | None') -> 'list[object] | None':
        if self.restrict and self.choices and v is not None:
            for i in range(len(v)):
                if v[i] not in self.choices:
                    raise CallError(
                        f'Invalid value of argument {self.__strname()}[{i}]: {v[i]}. '
                        f'Must be one of:{self.__strchoices()}',
                        1)
        return self.default if v is None else [self.type(x) for x in v]

    def __strname(self) -> 'str':
        if self.lopt:
            return f'--{self.lopt}'
        if self.sopt:
            return f'-{self.sopt}'
        return self.name

    def __strchoices(self) -> 'str':
        return '\n * ' + '\n * '.join(self.choices)


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


class CompleterNone(Completer):
    ...


class CompleterList(Completer):
    def __init__(self, v: 'Iterable') -> 'None':
        pass


class CompleterPath(Completer):
    ...


class CallError(RuntimeError):
    @property
    def text(self) -> 'str':
        return self.__text

    @text.setter
    def text(self, v: 'str | None') -> 'None':
        self.__text = v

    @property
    def code(self) -> 'int':
        return self.__code

    @code.setter
    def code(self, v: 'int | None') -> 'None':
        self.__code = v

    def __init__(
        self,
        text: 'str | None' = None,
        code: 'int | None' = None,
    ) -> 'None':
        self.__text = text
        self.__code = code


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
    if o is Iterable:
        return 'Iterable'
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

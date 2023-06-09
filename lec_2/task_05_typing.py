"""
Модуль typing
Для указания типа переменной можно использовать модуль typing. Они содержать
как готовые типы данных, так и обобщенные. В таблице представлен доступные на
текущий момент типы, разделённые по группам. Назначение большинства из них
понятно по названиям. А с некоторыми вы никогда не столкнётесь.

Примитивы супер специального типа:
Annotated,
Any,
Callable,
ClassVar,
Final,
ForwardRef,
Generic,
Literal,
Optional,
Protocol,
Tuple,
Type,
TypeVar,
Union

Абсолютные типы из collections.abc
AbstractSet,
ByteString,
Container,
ContextManager,
Hashable,
ItemsView,
Iterable,
Iterator,
KeysView,
Mapping,
MappingView,
MutableMapping,
MutableSequence,
MutableSet,
Sequence,
Sized,
ValuesView,
Awaitable,
AsyncIterator,
AsyncIterable,
Coroutine,
Collection,
AsyncGenerator,
AsyncContextManager

Структурные проверки, протоколы
Reversible,
SupportsAbs,
SupportsBytes,
SupportsComplex,
SupportsFloat,
SupportsIndex,
SupportsInt,
SupportsRound

Коллекция конкретных типов
ChainMap,
Counter,
Deque,
Dict,
DefaultDict,
List,
OrderedDict,
Set,
FrozenSet,
NamedTuple,
TypedDict,
Generator

Другие конкретные типы
BinaryIO,
IO,
Match,
Pattern,
TextIO

Одноразовые вещи
AnyStr,
cast,
final,
get_args,
get_origin,
get_type_hints,
NewType,
no_type_check,
no_type_check
_decorator,
NoReturn,
overload,
runtime_check
able,
Text,
TYPE_CHECKING

Ещё раз напомню, что программа будет работать без указания типа. Более того, в
процессе исполнения Python игнорирует аннотации. Если переменная получит
значение неподходящего типа, ошибку это не вызовет. Указание типов служит для
повышения читаемости кода и более быстрой отладки.
Если вы будете работать в команде, которая придерживается аннотации, вы знаете
где искать. Далее на курсе мы будем использовать указание типа там, где это
уместно. Но не будет делать аннотацию обязательной.
"""
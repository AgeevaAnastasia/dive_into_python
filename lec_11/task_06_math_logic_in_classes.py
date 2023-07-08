"""
Математика и логика в классах

Под математикой стоит понимать переопределение дандер методов, которые
позволяют производить операции сложения, вычитания, умножения и т.п. с
использованием математических символов. Что касается логики, речь идёт о
логических операциях “и”, “или” и т.п. над объектами.

Рассмотрим возможности Python в таблице.


Операция    Основной метод                  Right метод                     In place метод
в Python
+           __add__(self, other)            __radd__(self, other)           __iadd__(self, other)
-           __sub__(self, other)            __rsub__(self, other)           __isub__(self, other)
*           __mul__(self, other)            __rmul__(self, other)           __imul__(self, other)
@           __matmul__(self, other)         __rmatmul__(self, other)        __imatmul__(self, other)
/           __truediv__(self, other)        __rtruediv__(self, other)       __itruediv__(self, other)
//          __floordiv__(self, other)       __rfloordiv__(self, other)      __ifloordiv__(self, other)
%           __mod__(self, other)            __rmod__(self, other)           __imod__(self, other)
divmod()    __divmod__(self, other)         __rdivmod__(self, other)        __idivmod__(self, other)
**, pow()   __pow__(self, other[,modulo])   __rpow__(self, other[,modulo])  __ipow__(self, other[,modulo])
<<          __lshift__(self, other)         __rlshift__(self, other)        __ilshift__(self, other)
>>          __rshift__(self, other)         __rrshift__(self, other)        __irshift__(self, other)
&           __and__(self, other)            __rand__(self, other)           __iand__(self, other)
^           __xor__(self, other)            __rxor__(self, other)           __ixor__(self, other)
|           __or__(self, other)             __ror__(self, other)            __ior__(self, other)


Переопределение перечисленных в таблице методов позволяет использовать
указанные в первом столбце операции для вычисления результата. Рассмотрим
некоторые из них на примерах.

"""
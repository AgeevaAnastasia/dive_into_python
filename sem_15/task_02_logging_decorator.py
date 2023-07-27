"""На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.

Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.

"""
import logging

FORMAT = '{levelname:<8} - {asctime}: \n{msg}'

logging.basicConfig(format=FORMAT, style='{', filename='log1.log', filemode='a', encoding='utf-8', level=logging.INFO)

logger = logging.getLogger(__name__)


def deco(func):
    def wrapper(a, b=0, c=0):
        result = func(a, b, c)
        logger.info(f'функция {func.__name__}():'
                    f'\nкоэффициент a = {a} \nкоэффициент b = {b} \nкоэффициент c = {c} '
                    f'\nкорни: {result}\n')

    return wrapper


@deco
def quadratic_equation(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return 'no roots'
    if d == 0:
        x = -b / (2 * a)
        return f'{x = }'

    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return f'{x1 = }, {x2 = }'


if __name__ == '__main__':
    quadratic_equation(4, 13, 3)

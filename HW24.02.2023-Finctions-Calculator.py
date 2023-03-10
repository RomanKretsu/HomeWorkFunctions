# Calculator
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”.
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def fplus():
    return a + c


def fminus():
    return a - c


def fmultiply():
    return a * c


def fdividing():
    return a / c


def fexponentiation():
    return a ** c


while ZeroDivisionError or Exception:  # зацикливаем программу, пока не введется кодовый символ (в нашем случае '0')
    try:
        print('*********************************************************************************')
        print('Программа "Калькулятор" ')
        print('Вводить необходимо только числа и знаки +, -, *, /, **.')
        print('При вводе "0" как первое значение или действие - означает "Выход из программы"')
        print('При вводе "0" как второе значение - означает "Ошибка! Деление на ноль!"')
        print('*********************************************************************************')
        a = input('Введите первое число:  ')
        if a == '0':  # создаем условие для выхода из программы через break
            print('Ноль. Программа завершена')
            break

        b = input('Введите действие:  ')
        if b == '0':  # создаем условие для выхода из программы через break
            print('Ноль. Программа завершена')
            break
        if b == '+' or b == '-' or b == '*' or b == '/' or b == '**':
            print('Действие:  ', b)

        c = input('Введите второе число:  ')
        if b == '/' and c == '0':  # создаем условие для действий при делении на ноль
            print('Деление на ноль!')
        elif b != '/' and c == '0':  # создаем условие для выхода из программы через break
            print('Ноль. Программа завершена')
            break

        a = float(a)
        c = float(c)

        if b == '+':
            fplus()
            print('Сложение: ', a, '+', c, '=', fplus())
            print('Ответ:  ', fplus())

        elif b == '-':
            fminus()
            print('Вычитание: ', a, '-', c, '=', fminus())
            print('Ответ:  ', fminus())

        elif b == '*':
            fmultiply()
            print('Умножение: ', a, '*', c, '=', fmultiply())
            print('Ответ:  ', fmultiply())

        elif b == '/':
            fdividing()
            print('Деление: ', a, '/', c, '=', fdividing())
            print('Ответ:  ', fdividing())

        elif b == '**':
            fexponentiation()
            print('Возведение в степень: ', a, '**', c, '=', fexponentiation())
            print('Ответ:  ', fexponentiation())


    except ZeroDivisionError:
        print('Ошибка! Деление на ноль! Сделайте корректный ввод значений! ')  # исключаем вывод ошибки "Деление на ноль"
    except Exception:
        print('Некорректный ввод значений или команд. Вводить необходимо только числа и знаки +, -, *, /, ** . '
              'Сделайте корректный ввод значений и команд.')
        # исключаем вывод ошибки, в случае ввода текста

    else:
        print('*********************************************************************************')
        print('Вводить необходимо только числа и знаки +, -, *, /, ** ')

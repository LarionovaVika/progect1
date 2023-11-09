print('Здравствуйте!')
print('Обозначение знаков:')
print('"+" - сложение')
print('"-" - вычитание')
print('"*" - умножение')
print('"/" - вещественное деление')
print('"//" - целочисленное деление')
print('"%" - взятие остатка')
print('"**" - возведение в степень')
print('"** (1 / 2)" - квадратный корень числа')
print('"^" - переводить из любой системы счисления в десятичную("y" является системой счисления "x")')
print('"@" - анализ числа')
x = input('Введите число ')
while '1' not in x and '2' not in x and '3' not in x and '4' not in x and '5' not in x and\
              '6' not in x and '7' not in x and '8' not in x and '9' not in x and '0' not in x:
    print('Нужно ввести число.')
    x = input('Введите число ')
c = input('Напиши знак действия ')
while c != '*' and c != '/' and c != '//' and c != '+' and c != '-' and c != '**' and c != '%' and\
              c != '** (1 / 2)' and c != '^' and c != '@':
    print('Можно писать только знаки: +, -, /, //, *, **, %, ** (1 / 2), ^, @.')
    c = input('Напиши знак действия ')
if c != '** (1 / 2)' and c != '@':
    y = input('Введите число ')
    while '1' not in y and '2' not in y and '3' not in y and '4' not in y and '5' not in y and\
                  '6' not in y and '7' not in y and '8' not in y and '9' not in y and '0' not in y:
        print('Нужно ввести число.')
        y = input('Введите число ')
    y = int(y)
x = int(x)
a = 'да'
while a != 'нет' and a != 'Нет':
    if c == '*':
        print(x * y)
    elif c == '/':
        if y != 0:
            print(x / y)
        elif y == 0:
            print('Нельзя!')
    elif c == '//':
        if y != 0:
            print(x // y)
        elif y == 0:
            print('Нельзя!')
    elif c == '+':
        print(x + y)
    elif c == '-':
        print(x - y)
    elif c == '**':
        print(x ** y)
    elif c == '%':
        print(x % y)
    elif c == '** (1 / 2)':
        print(x ** (1 / 2))
    elif c == '^':
        q = int(str(x), int(y))
        print(int(q))
    elif c == '@':
        print('Количество разрядов в числе:')
        print(len(str(x)))
        print('Сколько каких цифр есть в числе:')
        b = x
        w = 0
        t = 0
        h = 0
        u = 0
        f = 0
        l = 0
        e = 0
        g = 0
        n = 0
        z = 0
        while b != 0:
            s = b % 10
            if s == 1:
                w = w + 1
            elif s == 2:
                t = t + 1
            elif s == 3:
                h = h + 1
            elif s == 4:
                u = u + 1
            elif s == 5:
                f = f + 1
            elif s == 6:
                l = l + 1
            elif s == 7:
                e = e + 1
            elif s == 8:
                g = g + 1
            elif s == 9:
                n = n + 1
            elif s == 0:
                z = z + 1
            b = b // 10
        b = x
        if b == 0:
            z = z + 1
        if w != 0:
            print('1 -', w, 'раз(а).')
        if t != 0:
            print('2 -', t, 'раз(а).')
        if h != 0:
            print('3 -', h, 'раз(а).')
        if u != 0:
            print('4 -', u, 'раз(а).')
        if f != 0:
            print('5 -', f, 'раз(а).')
        if l != 0:
            print('6 -', l, 'раз(а).')
        if e != 0:
            print('7 -', e, 'раз(а).')
        if g != 0:
            print('8 -', g, 'раз(а).')
        if n != 0:
            print('9 -', n, 'раз(а).')
        if z != 0:
            print('0 -', z, 'раз(а).')
        if x // 2 == 0:
            print('Чётное.')
        elif x // 2 == 1:
            print('Не чётное.')
        print('Вывод суммы цифр числа:')
        m = 0
        d = x
        while d != 0:
            m = m + (d % 10)
            d = d // 10
        print(m)
        p = 1
        k = 0
        if x != 0:
            while x != p:
                if x % p == 0:
                    k = k + 1
                p = p + 1
            if x == 1:
                print('Простое.')
            elif k == 1:
                print('Простое.')
            elif k != 1:
                p = 1
                print('Делители числа:')
                while x // p != 1:
                    if x % p == 0:
                        print(p)
                    p = p + 1
                print(x)
        elif x == 0:
            print('Делителями являются все числа.')
        j = x ** (1 / 2)
        print('Является ли число полным квадратом?')
        if round(j) ** 2 == x:
            print('Да.')
            print('Является квадратом числа:')
            print(round(j))
        elif round(j) ** 2 != x:
            print('Нет.')
        j = x ** (1 / 3)
        print('Является ли число полным кубом?')
        if round(j) ** 3 == x:
            print('Да.')
            print('Является кубом числа:')
            print(round(j))
        elif round(j) ** 3 != x:
            print('Нет.')
    print('Желаете ли вы выполнить еще действие?')
    a = input()
    while a != 'нет' and a != 'Нет' and a != 'да' and a != 'Да':
        print('Ответ может быть только "Да"("да") или "Нет"("нет")')
        a = input('Введите "Да"("да") или "Нет"("нет") ')
    if a == 'да' or a == 'Да':        
        x = input('Введите число ')
        while '1' not in x and '2' not in x and '3' not in x and '4' not in x and '5' not in x and\
                      '6' not in x and '7' not in x and '8' not in x and '9' not in x and '0' not in x:
            print('Нужно ввести число.')
            x = input('Введите число ')
        c = input('Напиши знак действия ')
        while c != '*' and c != '/' and c != '//' and c != '+' and c != '-' and c != '**' and\
                      c != '%' and c != '** (1 / 2)' and c != '^' and c != '@':
            print('Можно писать только знаки: +, -, /, //, *, **, %, ** (1 / 2), ^, @.')
            c = input('Напиши знак действия ')
        if c != '** (1 / 2)' and c != '@':
            y = input('Введите число ')
            while '1' not in y and '2' not in y and '3' not in y and '4' not in y and '5' not in y and\
                          '6' not in y and '7' not in y and '8' not in y and '9' not in y and '0' not in y:
                print('Нужно ввести число.')
                y = input('Введите число ')
            y = int(y)
    x = int(x)
print('До свидания!')

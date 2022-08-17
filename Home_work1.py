duration = int(input('Введите время :'))
if duration < 0:
    print('Необходимо положительное число!')
    duration = int(input('Введите время :'))
if 0 < duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    m = duration // 60
    s = duration % 60
    print(m, 'мин', s, 'сек')
elif 3600 <= duration < 86400:
    h = duration // 3600
    ostatok = duration % 3600
    m = ostatok // 60
    s = ostatok % 60
    print(h, 'час', m, 'мин', s, 'сек')
else:
    day = duration // 86400
    ostatok = duration % 86400
    h = ostatok // 3600
    ost2 = ostatok % 3600
    m = ost2 // 60
    s = ost2 % 60
    print(day, 'дн', h, 'час', m, 'мин', s, 'сек')

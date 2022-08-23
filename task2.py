p = int(input('Введите число от 1 до 100: '))
for p in range(1, 101):
        if p == 1:
            print(f"{p} процент")
        elif 1 < p < 5:
            print(f"{p} процента")
        else:
            print(f"{p} процентов")

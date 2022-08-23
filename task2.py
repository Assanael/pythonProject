p = int(input('Введите число от 1 до 100: '))
for p in range(1, 101):
        if p % 10 == 1 and p % 100 != 11:
            print(f"{p} процент")
        elif 1 < p % 10 < 5 and not 11 < p % 100 < 15:
            print(f"{p} процента")
        else:
            print(f"{p} процентов")

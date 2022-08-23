my_list = kyb_list = []
for x in range(1, 1001, 2):
    my_list.append(x ** 3)
print(my_list)


def sumkub():
    itog = 0
    for i in my_list:
        a = str(i)
        sum = 0
        for j in range(0, len(a)):
            sum = sum + int(a[j])
        if sum % 7 == 0:
            itog += i
    print(itog)


def sumkub17():
    itog = 0
    for i in my_list:
        a = str(i)
        sum = 0
        for j in range(0, len(a)):
            sum = sum + int(a[j] + '17')
        if sum % 7 == 0:
            itog += i
    print(itog)

def test(variable):
    a = []
    spisok = list(variable.replace(' ', ''))
    slovar = set(spisok)
    for i in slovar:
        a.append(variable.count(i))
    b = list(slovar)
    if len(a) == len(b):
        for _ in range(len(a)):
            return f'| {b[_]} | {a[_]: <{3}} |'
    else:
        return " Не получилось"

print(test(input('Введите строку:')))

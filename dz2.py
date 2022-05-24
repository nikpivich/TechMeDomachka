def test(variable):
    number = variable.replace(',', '.')
    if number.count(".") <=1 and number.count("-") <= 1:
        if "-" or "" in number[0:]:
            a = number.replace('-', '')
            if (a.replace('.', '').isdigit()) is True:
                if float(number) > 0:
                    return 'Положительное'
                elif float(number) < 0:
                    return 'Отрицательное'
                else:
                    return 'нуль'
            else:
                return "Нужно число"
        else:
            return "Нужно число"
    else:
        return "Нужно число"


print(test(input('Ввидите число')))

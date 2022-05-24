oooero = {
    'control': {
        'general_director': {  # Управление: гнеральный деректор, его помощник, секретарь
            'name': 'Timur',
            'age': '40',
            'salary': '6000'
        },
        'assistant_general_manager': {
            'name': 'Oliver',
            'age': '38',
            'salary': '5700'
        },
        'secretary': {
            'name': 'Jack',
            'age': '38',
            'salary': '4200'
        }
    },
    'personnel_management': {  # Управление персоналом: начальник и 3 сотрудника
        'head_department': {
            'name': 'Harry',
            'age': '29',
            'salary': '5000'
        },
        'employee1': {
            'name': 'Jacob',
            'age': '25',
            'salary': '4000'
        },
        'employee2': {
            'name': 'Charley',
            'age': '26',
            'salary': '4000'
        },
        'employee3': {
            'name': 'Thomas',
            'age': '25',
            'salary': '4000'
        }
    },
    'development_department': {  # Отдел разработки: начальник и 6 сотрудников
        'head_department': {
            'name': 'George',
            'age': '27',
            'salary': '5500'
        },
        'employee1': {
            'name': 'Jacob',
            'age': '26',
            'salary': '4500'
        },
        'employee2': {
            'name': 'Oscar',
            'age': '22',
            'salary': '4500'
        },
        'employee3': {
            'name': 'Jack',
            'age': '22',
            'salary': '4500'
        },
        'employee4': {
            'name': 'Noah',
            'age': '24',
            'salary': '4500'
        },
        'employee5': {
            'name': 'Liam',
            'age': '27',
            'salary': '4500'
        },
        'employee6': {
            'name': 'Ethan ',
            'age': '25',
            'salary': '4500'
        },
    },
    'operation_department': {  # Отдел эксплуатации: начальник и 5 сотрудников
        'head_department': {
            'name': 'Alexander',
            'age': '30',
            'salary': '4800'
        },
        'employee1': {
            'name': 'Alister',
            'age': '26',
            'salary': '4200'
        },
        'employee2': {
            'name': 'Fergus',
            'age': '22',
            'salary': '4200'
        },
        'employee3': {
            'name': 'Crispin ',
            'age': '22',
            'salary': '4200'
        },
        'employee4': {
            'name': 'Paul',
            'age': '24',
            'salary': '4200'
        },
        'employee5': {
            'name': 'Mark',
            'age': '27',
            'salary': '4200'
        },
    },
    'testing_department': {  # Отдел тестировки: начальник и 4 сотрудника
        'head_department': {
            'name': 'Rosy',
            'age': '30',
            'salary': '4200'
        },
        'employee1': {
            'name': 'Jenny',
            'age': '26',
            'salary': '4000'
        },
        'employee2': {
            'name': 'Barbie',
            'age': '22',
            'salary': '4000'
        },
        'employee3': {
            'name': 'Annie ',
            'age': '22',
            'salary': '4000'
        },
        'employee4': {
            'name': 'Liza',
            'age': '24',
            'salary': '4000'
        },
    },
    'sales_department': {  # Отдел продаж: Начальник и 5 сотрудников
        'head_department': {
            'name': 'Jack ',
            'age': '30',
            'salary': '4200'
        },
        'employee1': {
            'name': 'Jacob ',
            'age': '26',
            'salary': '3800'
        },
        'employee2': {
            'name': 'Fergus',
            'age': '22',
            'salary': '3800'
        },
        'employee3': {
            'name': 'Thomas  ',
            'age': '22',
            'salary': '3800'
        },
        'employee4': {
            'name': 'Oscar ',
            'age': '24',
            'salary': '3800'
        },
        'employee5': {
            'name': 'Mark',
            'age': '27',
            'salary': '3800'
        },
    },
    'cleanliness_department': {  # Отдел клининга и 2 рабочих
        'employee1': {
            'name': 'Anastasia ',
            'age': '52',
            'salary': '1000'
        },
        'employee2': {
            'name': 'Olga',
            'age': '47',
            'salary': '1000'
        }
    }
}
new_department = {  # Новый отдел с сотрудниками для добавления
    'security': {
        'name': 'Oleg',
        'age': '47',
        'salary': '2000'
    }
}

oooero |= new_department  # Добавление нового отдела
print(oooero)

remote_department = oooero.pop('testing_department')  # удаление отдела тестировки
print(remote_department)

new_employee1 = {
    'trainee': {  # Добавление 1 сотрудника в отдел
        'name': 'Natacha',
        'age': '22',
        'salary': '1500'
    }
}
new_employee2 = {
    'trainee': {  # Добавление 1 сотрудника в отдел
        'name': 'Polina',
        'age': '23',
        'salary': '1500'
    }
}
new_employee3 = {
    'trainee': {  # Добавление 1 сотрудника в отдел
        'name': 'Nikita',
        'age': '21',
        'salary': '1500'
    }
}
new_employee4 = {
    'trainee': {  # Добавление 1 сотрудника в отдел
        'name': 'Alla',
        'age': '22',
        'salary': '1500'
    }
}
new_employee5 = {
    'trainee': {  # Добавление 1 сотрудника в отдел
        'name': 'Zoi',
        'age': '19',
        'salary': '1500'
    }
}
oooero['personnel_management'].update(new_employee1)
oooero['development_department'].update(new_employee2)
oooero['operation_department'].update(new_employee3)
oooero['sales_department'].update(new_employee5)
print(oooero)

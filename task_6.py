types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

# функция удаления дублей
# ХОЧУ ЗАЧЁТ
def delete(ticket):
    for i in ticket.values():
        for lis in i:
            for key, value in ticket.items():
                if lis in value:
                    value.remove(lis)
                    ticket[key] = value



# функция объединения
def combine(type, ticket):
    new = {}
    for key, value in type.items():
        new[value] =ticket[key]
    return new


print(combine(types, tickets))
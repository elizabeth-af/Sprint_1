world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}
country = 'Италия'

# задание 1
world_champions[2022] = 'Аргентина'

# задание 2
for key, value in world_champions.items():
    print(key, '-', value)

# задание 3
if country in world_champions.values():
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')
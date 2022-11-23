dict = {
    'city': 'Москва',
    'temperature': '20'
}

# Выведите на экран значение ключа city
print(dict['city'])
# Уменьшите значение "temperature" на 5
dict['temperature'] = 5
print(dict['temperature'])
# Выведите на экран весь словарь
print(dict)
# Проверьте, есть ли в словаре ключ country
def key_in_dict(key, dict):
    return key in dict
result = key_in_dict('country', dict)
print(result)
# Добавьте в словарь элемент date со значением "27.05.2019"
dict['date'] = "27.05.2019"
print(dict)
print('длинна словаря', len(dict))


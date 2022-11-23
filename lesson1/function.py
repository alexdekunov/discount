def get_summ(one, two, delimiter='&'):
    return str(one) + delimiter + str(two)

# print(get_summ("Ler", "torr"))

# resoult = get_summ('Learn', 'python')  # в переменную и на экран
# print(resoult)
# print(resoult.upper())  # всё заглавными

''' Задание 2'''

def format_price(price):
    price = int(price)
    return f"Цена: {price} руб."

tru = format_price(56.24)
print(tru)
# Цена: 56 руб.








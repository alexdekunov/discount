#price = 100
#discount = 5

def discounted (price, discount, max_discount=20):
    price = abs(price) # абсолютное число возвращает
    discount = abs(discount) # абсолютное число возвращает
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('максимальная скидка не должна быть больше 100')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

print(f'Возможная цена: {discounted(100, 5)}')
print(f'Возможная цена: {discounted(100, 50)}')
print(discounted(100, 15, max_discount=90))
print(discounted(100, 5, max_discount=60))

#product = {'name': 'Samsung', 'price': 5000, 'discount': 5}
#product['with_discount'] = discounted(product['price'], product['discount'])
#print(product)

#discounted(100, 50)
#discounted(100, 500)
#discounted(-100, 50)
#discounted(100, -50)
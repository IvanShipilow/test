class shop():
    """магазин"""
    def __init__(self, names, numbers):
     """Св-ва магазина"""
     self.names = names
     self.numbers = numbers

def optoin(self):
    print('название магазина' + self.names + 'под номером' + self.numbers)
shop1 = shop('Пятёрочка', 5)
shop2 = shop('магнит', 12)

print(shop1.names , shop1.numbers)
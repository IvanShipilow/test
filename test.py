age = int(input('сколько тебе лет?'))
if (age >= 23):
    print('тебе можно входить')
elif (age >=18) and (age < 23):
    print('тебе можно с ограничиным временем')
else:
    print('тебе сюда нельзя')

x = int(input('Введите 1 число: '))
y = int(input('Введите 2 число: ')) 
def sum(a,b):
    return a + b
print(sum(x,y))    
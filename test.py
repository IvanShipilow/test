age = int(input('сколько тебе лет?'))
if (age >= 23):
    print('тебе можно входить')
elif (age >=18) and (age < 23):
    print('тебе можно с ограничиным временем')
else:
    print('тебе сюда нельзя')
# функции 
x = int(input('Введите 1 число: '))
y = int(input('Введите 2 число: ')) 
def sum(a,b):
    return a + b
print(sum(x,y))  
print('\n')  
# циклы
name = 'цикл фор!'
for i in name:
    print(i)
print('\n')
for k in range(1,6):
    print(name)

print('\n')
i=1
while i<=10:
    if i != 5:
      print(i)
    i+=1    
print(type(i))

tuple = ('dasf', 45 , 54 , 56,)
print(tuple)
print('\n')
lack ={"яблоко": 'красное', 'лимон': 'жёлтый'}
for i in lack.keys():
    print(i)
print('\n')
for l in lack.values():
    print(l)
print('\n')
for f in lack.items():
    print(f)
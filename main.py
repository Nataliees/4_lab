#4.1)  Напишите функцию, которая проверяет, делится ли введенное число на 3, или нет.
#4.2) Напишите программу деления числа 100 на введенное пользователем число. Деление реализуйте с помощью функции.
# Предусмотрите возможные исключения (ValueError, возникающее в случае, если пользователь введет не число, а строку, и
# ZeroDivisionError – если будет введено число 0 и остальные).
#4.3) Напишите функцию, которая возвращает True, если введенная пользователем дата является магической, и False в
# обратном случае. Магической считается дата, в которой произведение дня и месяца равно двум последним цифрам года,
# например: 02.11.2022.
#4.4) "Счастливым" называют билет с номером, в котором сумма первой половины цифр равна сумме второй половины цифр.
# Номера могут быть произвольной длины, с единственным условием, что количество цифр всегда чётно, например: 33 или
# 2341 и так далее.
#Билет с номером 385916 — счастливый, так как 3 + 8 + 5 == 9 + 1 + 6. Билет с номером 231002 не является счастливым,
# так как 2 + 3 + 1 != 0 + 0 + 2
#Реализуйте функцию, проверяющую является ли номер счастливым (номер — всегда строка).

def one():
    try:
        count=int(input('введите число '))
    except ValueError:
        print('введено не число')
    else:
        if(count%3==0):
            print('делится')
        else:
            print('не делится')

def two():
    try:
        a = int(input('введите число '))
        b = 100 / a
    except ValueError:
        print('введено не число ')
    except ZeroDivisionError:
        print('на 0 не делится ')
    else:
        print('ответ: ', b)

def three():
    datee = input('введите дату ')
    d = datee.split(".")
    a = int(d[0])
    b = int(d[1])
    c = int(d[2])%100
    if(a*b==c):
        print('дата магическая ')
    else:
        print('дата не магическая ')

def four():
    ticket = input('Введите номер билета ')
    dlina = len(ticket)
    h=int(dlina/2)
    ticket=int(ticket)
    a=0
    for i in range (h):
        a+=ticket%10
        ticket=int(ticket/10)
    b=0
    for i in range(h):
        b += ticket % 10
        ticket = int(ticket / 10)
    if(a==b):
        print('Билет счастливый ')
    else:
        print('Билет не является счастливым ')
four()

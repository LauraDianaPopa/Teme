#1.Funcție care să calculeze și să returneze suma a două numere
from typing import Set, Any, Type


# def adunare():
#     numar1 = int (input ('Introduceti un numar: '))
#     numar2 = int (input ('Introduceti al doile numar: '))
#     suma = numar1 + numar2
#     return suma
# y = adunare()
# print(f'Suma numerelor introduse este: {y}')

#Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar.

# def is_even_2(numar):
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
# argument_numar= int(input('Introduceti un numar par: '))
# y = is_even_2(argument_numar)
# print(y)

#Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)

# def nume():
#     nume_prenume = input('Introduceti numele complet: ')
#     numar_caractere = len(nume_prenume)
#     return numar_caractere
# y = nume()
# print(f'Numele tau are {y} caractere!')

#Funcție care returnează aria dreptunghiului:

# def arie():
#     lungime_dreptunghi = int(input('Introduceti lungimea dreptunghiului: '))
#     latime_dreptunghi = int(input('Introduceti latimea dreptunghiului: '))
#     arie_dreptunghi = lungime_dreptunghi * latime_dreptunghi
#     return arie_dreptunghi
# y = arie()
# print(f'Aria dreptunghiului este: {y}')

#Funcție care returnează aria cercului.

# def aria():
#     raza_cercului = int( input('Introduceti raza cercului: '))
#     pi = 3.14
#     aria_cercului = raza_cercului* raza_cercului * pi
#     return aria_cercului
# y = aria()
# print(f'Aria cercului este: {y}')

#Funcție care returnează True dacă un caracter x se găsește într-un string dat și False dacă nu găsește.

# def propozitie_1():
#     prop = str ('In iarna aceasta nu este anuntata zapada prea curand!')
#     if cuvant in prop:
#         return True
#     else:
#         return False
# cuvant = str (input('Introduceti un cuvant: '))
# y = propozitie_1()
# print(y)

# Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
# ● Nr de caractere upper case exte y

# def string_litere_mari_si_mici(string):
#     lower_case = 0
#     upper_case = 0
#     for char in string:
#         if char.islower():
#             lower_case = lower_case + 1
#         elif char.isupper():
#             upper_case = upper_case + 1
#     print(f'Numarul de caractere lower case este: {lower_case}')
#     print(f'Numarul de caractere upper case este: {upper_case}')
#
# string_litere_mari_si_mici('MultuMesC')


# Funcție care primește o LISTA de numere și returnează o LISTA doar cu
#numerele pozitive

# def lista_numere(lista):
#     lista_numere_pozitive = []
#     for numar in lista:
#         if numar > 0:
#             lista_numere_pozitive.append(numar)
#     return print(lista_numere_pozitive)
#
# lista_numere([-1, 0, 1, 2, -4, 7])
#
# Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
# ● Primul număr x este mai mare decat al doilea nr y
# ● Al doilea nr y este mai mare decat primul nr x
# ● Numerele sunt egale.

# def numere():
#     x = int(input('Introduceti primul numar: '))
#     y = int(input('Introduceti al doilea numar: '))
#     if x > y:
#         print(f'Primul numar este mai mare ca al doilea!')
#     elif x < y:
#         print(f'Al doilea numar este mai mare decat primul!')
#     else:
#         print(f'Numerele sunt egale!')
# numere()


# Funcție care primește un număr și un set de numere.
# ● Printeaza ‘am adaugat numărul nou în set’ + returnează True
# ● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
# returnează False

# def add_number_to_set(number, number_set):
#     if number in number_set:
#         print(f'Nu am adaugat numărul {number} în set. Acesta există deja')
#         return False
#     else:
#         number_set.add(number)
#         print(f'Am adaugat numărul {number} în set')
#         return True
#
# print(add_number_to_set(8, {6, 5, 4}))

#Funcție care primește o lună din an și returnează câte zile are acea luna

# def an():
#     luna = input('Introduceti o luna: ')
#     if luna in ('Ianuarie', 'Martie', 'Mai', 'Iulie', 'August', 'Octombrie', 'Decembrie'):
#         return 31
#     elif luna in ('Aprilie', 'Iunie', 'Septembrie', 'Noiembrie'):
#         return 30
#     else:
#         return 28
# y= an()
# print(y)

#  Funcție calculator care să returneze 4 valori. Suma, diferența, înmulțirea, împărțirea a două numere.
# În final vei putea face:
# a, b, c, d = calculator(10, 2)
# ● print("Suma: ", a)
# ● print("Diferenta: ", b)
# ● print("Inmultirea: ", c)
# ● print("Impartirea: ", d)

# def calculator():
#     a = int(input ('Introduceti primul numar: '))
#     b = int(input ('Introduceti al doilea numar: '))
#     suma = a + b
#     diferenta = a - b
#     produs = a * b
#     cat = a / b
#     print(f' Suma :{suma}, Diferenta: {diferenta}, Inmultire:{produs}, Impartire:{cat}')
# y = calculator()
# print(y)

# Funcție care primește o lista de cifre (adică doar 0-9)
# Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returnează un DICT care ne spune de câte ori apare fiecare cifră
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

# def functie_dict():
#     dictionar = {}
#     lista = [1, 3, 1, 6, 9, 7, 7, 5, 5]
#     for i in range(0, 10):
#         contor = 0
#         for j in range(0, len(lista)):
#             if i == lista[j]:
#                 contor += 1
#                 dictionar.update({i: contor})
#             else:
#                 dictionar.update({i: contor})
#     return dictionar
# a = functie_dict()
# print(a)

#Funcție care primește 3 numere.Returnează valoarea maximă dintre ele.

# def maxim_numere():
#     x = input('Introduceti primul numar: ')
#     y = input('Introduceti al doilea numar: ')
#     z = input('Introduceti al treilea numar: ')
#     if x > y > z:
#         return print(f'Primult numar este cel mai mare: {x}')
#     elif y>x>z :
#         return print(f'Al doilea numar este cel mai mare: {y}')
#     else:
#         return print(f'Al treilea numar este cel mai mare: {z}')
# a = maxim_numere()
# print(a)

#Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr
#Exemplu: daca dam nr 3. Suma va fi 6 (0+1+2+3)

# def suma():
#     x = int(input('Introduceti un numar: '))
#     suma = 0
#     for i in range(x + 1):
#         suma += i
#     return suma
# a = suma()
# print(a)

# Funcție care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune
# Exemplu:
# list1 = [1, 1, 2, 3]list2 = [2, 2, 3, 4]
# Răspuns: {2, 3}

# def numere_comune(list1,list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     return set1.intersection(set2)
# print(numere_comune([1, 1, 2, 3],[2, 2, 3, 4]))

# Funcție care să aplice o reducere de preț
# Dacă produsul costa 100 lei și aplicăm reducere de 10%.
# Pretul va fi 90 . Tratați cazurile în care reducerea e invalida. De exemplu o reducere de 110% e invalidă.

# def reducere_pret(pret_intreg):
#     reducere = 100 - int(input('Introduceti reducerea: '))
#     pret_redus = pret_intreg / 100 * reducere
#     while reducere < 0:
#         print('suma invalida')
#         break
#     else:
#         return pret_redus
#
# print(reducere_pret(100))

#  Funcție care să afișeze data și ora curentă din ro
# (bonus: afișați și data și ora curentă din China)

# import datetime
# def afiseaza_data_ora_curenta():
#     data_ora_curenta = datetime.datetime.now()
#     print(data_ora_curenta.strftime("%d/%m/%Y %H:%M:%S"))
# afiseaza_data_ora_curenta()

#Funcție care să afișeze câte zile mai sunt până la ziua ta / sau până la Crăciun dacă nu vrei să ne zici cand e ziua ta :)
import datetime
def zile():
    data_curenta = datetime.datetime.now()
    data_ziua_mea = datetime.datetime(2023, 6, 9)
    data_craciun = datetime.datetime(2023, 12, 25)
    zile_ramase_craciun = (data_craciun - data_curenta).days
    zile_ramase_ziua_mea = (data_ziua_mea - data_curenta).days
    print(f'Mai sunt {zile_ramase_craciun} zile pana la Craciun')
    print(f'Mai sunt {zile_ramase_ziua_mea} zile pana la ziua mea!')

zile()

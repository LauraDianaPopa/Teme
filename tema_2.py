# if else functioneaza ca o conditie ce trebuie indeplinita, daca nu se indeplineste conditia de la if atunci se trece la conditia else si se inchide

# x = input('Scrie un numar: ')
# if int (x) >= 0:
#     print(f'Numarul introdus este un numar natural!')
# else:
#     print(f'Numarul introdus nu este un numar natural')

# x = input ('Scrie un numar: ')
# if int (x) > 0:
#     print(f'Numarul introdus este pozitiv!')
# elif int (x) <0:
#     print(f'Numarul introdus este negativ!')
# else:
#     print(f'Numarul introdus este neutru!')

# x = input('Introduceti un numar cuprins in intervalul -2 si 13! ')
# if -2<= int(x) <= 13:
#     print(f'Numarul introdus este cuprins in intervalul -2 si 13!')
# else:
#     print(f'Numarul introdus NU este cuprins in intervalul -2 si 13!')

# x = input('Introduceti un numar!')
# y = input('Introduceti alt numar!')
# x = int(x)
# y = int(y)
# if abs (x - y)<5:
#     print(f'Diferenta dintre numerele introduse este mai mica decat 5!')
# else:
#     print(f'Diferenta dintre numerele introduse este mai mare decat 5')


# x = input('Introduceti un numar! ')
# if not 5<= int(x) <=27:
#     print(f'Numarul introdus nu este cuprins in intervalul 5-27')
# else:
#     print(f'Numarul introdus este cuprins in intervalul 5-27!')

# x = input ('Introduceti un numar! ')
# y = input('Introduceti alt numar! ')
# if int(x) == int(y):
#     print(f'Numerele introduse sunt egale!')
# elif int(x)< int(y):
#     print(f'Numarul introdus prima data este mai mic decat numarul introdus a doua oara!')
# else:
#     print(f'Numarul introdus prima data este mai mare decat numarul introdus a doua oara!')

# print(f'x,y,z sunt laturile unui triunghi!')
# x = int (input('Introduceti valoarea primei laturi a triunghiului: '))
# y = int (input('Introduceti valoarea celei de-a doua laturi: '))
# z = int (input('Introduceti valoarea celei de-a treia laturi: '))
# if x == y != z or y == z != x or z == x != y:
#     print(f'Triunghiul este isoscel!')
# elif x == y == z:
#     print(f'Triunghiul este echilateral!')
# else:
#     print(f'Triunghiul este oarecare!')
#
# litera = str( input('Introduceti o litera: '))
# if litera.upper().lower() =='a':
#     print(f'Litera introdusa este o vocala!')
# elif litera.upper().lower()=='e':
#     print(f'Litera introdusa este o vocala!')
# elif litera.upper().lower()=='i':
#     print(f'Litera introdusa este o vocala!')
# elif litera.upper().lower()=='o':
#     print(f'Litera introdusa este o vocala!')
# elif litera.upper().lower()=='u':
#     print(f'Litera introdusa este o vocala!')
# else:
#     print(f'Litera introdusa este o consoana!')

# nota = int(input('Introduceti nota: '))
# if nota>=9:
#     print(f'Nota in sistem american este: A ')
# elif 9>nota>=8:
#     print(f'Nota in sistem american este: B')
# elif 8>nota>=7:
#     print(f'Nota in sistem american este: C ')
# elif 7>nota>=6:
#     print(f'Nota in sistem american este: D')
# elif 6>nota>=4:
#     print(f'Nota in sistem american este: E ')

# x = int(input('Introduceti un numar: '))
# if len(x)>=4:
#     print(f'Numarul introdus are minim 4 cifre!')
# else:
#     print(f'Numarul introdus nu are minim 4 cifre!')

# x =input('Introduceti un numar: ')
# if len(x) == 6:
#     print(f'Numarul introdus are 6 cifre!')
# else:
#     print(f'Numarul introdus nu are 6 cifre!')

# x = int(input('Introduceti un numar: '))
# if x%2 == 0:
#     print(f'Numarul introdus este par!')
# else:
#     print(f'Numarul introdus este impar!')

# x = int(input('Introduceti valoarea lui x: '))
# y = int(input('Introduceti valoarea lui y: '))
# z = int(input('Introduceti valoarea lui z: '))
# if x>y>z:
#     print (f'Valoarea atribuita lui x este cea mai mare!')
# elif y>x>z:
#     print (f'Valoarea atribuita lui y este cea mai mare!')
# else:
#     print(f'Valoarea atribuita lui z este cea mai mare!')

# a = int(input('Introduceti valoarea unui unghi: '))
# b = int(input('Introduceti valoarea celui de-al doilea unghi: '))
# c = int(input('Introduceti valoarea ceiu de al treilea unghi:' ))
# if  a + b + c == 180 :
#     print(f'Triunghiul este valid!' )
# else:
#     print(f'Triunghiul este invalid!')

# prop = 'Coral is either the stupidest animal or the smartest rock'
# y = int(input('Introduceti un numar: '))
# y=len (prop[-1:0])
# x=len (prop[::-1])
# prop_noua = x-y
# if  prop_noua == x -y:
#     print (f'Noua propozitie este: {prop_noua}')
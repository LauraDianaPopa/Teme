# variabila = locul (cutiuta) din memorie care tine date;
# String;
# Culoare = "rosie";
# print(type( "culoare" ))

# Int
# ani = '31' ;
# ani = int (ani);
# print(type (ani))

# Float
# pret_floare = 15.600;
# print(f'O floare poate sa ajunga sa coste si {pret_floare} lei')

# pret_floare = round(15.600);
# print(type(pret_floare))

# Bool
# casatorita = True;
# print (f'Sunt casatorita? {casatorita}')

# Float
# pret_floare = 15.600;
# print(type(pret_floare))

# Bool
# casatorita = True;
# print (type(casatorita))


# nume_prenume = 'Popa Laura-Diana';
# print(f'Numele meu complet are {len(nume_prenume)} caractere!')

# lungime = '18'
# lungime = int(lungime);
# latime = '10';
# latime = int(latime);
# print(f'Aria dreptunghiului este {lungime * latime}');

# Propozitie = "Coral is either the stupidest animal or the smartest rock";
# print(f'Propozitia de mai sus foloseste cuvantul the de {(Propozitie.count (" the "))} ori')

# Propozitie = 'Coral is either the stupidest animal or the smartest rock'
# print(f'{Propozitie.replace("the" , "THE")}')

# Propozitie = 'Coral is either the stupidest animal or the smartest rock'
# assert Propozitie.isdigit() is True , 'Propozitia nu contine doar cifre'

# cuvant = input ('Scrie un cuvant:')
# assert (str(cuvant) == str(cuvant)[::-1])
# print(f'Cuvant palindrom')
# else:
#  print("Cuvantul nu este palindrom")

# nume = input ("Numele meu este:")
# prenume = input ("Prenumele meu este:")
# print(f'Numele meu complet are {len(nume)+len(prenume)} caractere!')

# Propozitie = ("Coral is either the stupidest animal or the smartest rock")
# assert Propozitie == int (Propozitie)
# print(f'Propozitia contine numere')
# assert Propozitie == str ('Propozitie')
# print (f'Propozitia nu are numere!')

# sir = input('Introduceti un numar impar de caractere:')
# a = len(sir)
# print (f'Numarul introdus de caractere este:{a}')
# if int(a % 2) != 0:
#   m = int(a/ 2 + 1)
#  b = ['m']
# print (f'Mijlocul sirului de caractere introdus este:{b}')
# else:
#   print (f' Numarul sirului de caractere introdus nu este impar ')


# propozitie =input ('Scrie doua cuvinte:' , )
# n , m = propozitie.split(' ')
# print(f'Primul cuvant este: {n}')
# print(f'Al doilea cuvant este:{m}')

# text = input('Scrie un string format din doua cuvinte: ')
# prima_litera = text [0]
# text_modificat = text[0] + text[1:len(text)-1].replace(text[0],text[0].upper()) + text[len(text)-1]
# print(f'Stringul modificat este: {text_modificat}')

USER = str(input('User-ul este: '))
PAROLA = str(input('Tasteaza parola: '))
PAROLA_ASCUNSA= '*' * len(PAROLA)
print(f'Parola pentru user-ul {USER} este {PAROLA_ASCUNSA} si are {len(PAROLA)} caractere!')
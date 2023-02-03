# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#for i in range (0, len(masini)):
 #   print(f'Masina mea preferata este: {masini[i]}')

# i = 0
# while i <len(masini):
#     print(f'Masina mea preferata este: {masini[i]}')
#     i+=1
#
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i in (masini):
#     print(f'Masina mea preferata este: {i}')


masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for marca in range(len(masini)):
#   if marca in range(1,len(masini)-1):
#     masini[marca] = masini[marca].upper()
# else:
#   print(masini)

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for marca in range (len(masini)):
#     if masini[marca] == 'Mercedes':
#         print(f'Am gasit masina dorita de dumneavoastra!{masini[marca]}')
#     else:
#         print(f'Am gasit masina {masini[marca]}. Mai cautam')

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for marca in range (len(masini)):
#     if masini[marca] == 'Trabant' or masini[marca] == 'Lăstun':
#         marca =+1
#         continue
#     print(f' S-ar putea sa va placa masina: {masini[marca]}')

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
# marca_veche = ['Lăstun', 'Trabant']
# for marca in masini:
#     if marca in marca_veche:
#         continue
#     masini_vechi.append(marca)
#     masini.append('Tesla')
#     print(f'Modelele vechi sunt: {marca_veche}')
#     break
# print(f'Modele noi: {masini}')

# pret_masini = { 'Dacia': 6800, 'Lăstun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000 }
# buget = 15000
# for masina, pret in pret_masini.items():
#   if pret <= buget:
#     print(f"Pentru un buget de sub {buget} euro puteți alege mașina {masina} la pretul de {pret} euro")
#
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# i = 0
# for numar in numere:
#   if numar == 3:
#     i += 1
# print(f"Numărul 3 apare de {i} ori în listă.")
#
# suma = 0
# for numar in numere:
#   suma += numar
#
# print(f"Suma elementelor din listă este: {suma}.")

# maxim = numere[0]
# for numar in numere:
#   if numar > maxim:
#     maxim = numar
# print(f"Cel mai mare număr din listă este: {maxim}.")

# for i, numar in enumerate(numere):
#   if numar > 0:
#     numere[i] = -numar
# print(f"Noua listă este: {numere}.")


# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar > 0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
# print(f'Lista cu numere pare este: {numere_pare}')
# print(f'Lista cu numere impare este: {numere_impare}')
# print(f'Lista cu numere pozitive este: {numere_pozitive}')
# print(f'Lista cu numere negative este: {numere_negative}')


# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# for i in range(len(alte_numere)):
#     for j in range(i + 1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
# print(alte_numere)

# import random
#
# numar_secret = random.randint(1, 30)
# numar_ghicit = None
# while numar_ghicit is None:
#     nr = int(input('Introdu un numar: '))
#     if nr > numar_secret:
#         print('Numarul secret este mai mic')
#     elif nr < numar_secret:
#         print('Numarul secret este mai mare')
#     else:
#         print('Felicitari, ai gasit numarul!')
#         break

# nr = int(input("Scrie un numar: "))
# i = 1
# while i <= nr:
#     print(' ')
#     for j in range(i):
#         j = i
#         print(j, end='')
#         j = j + 1
#     i = i + 1


tastatura_telefon = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f'Cifra curenta este {tastatura_telefon[i][j]}')

# sau cu for each
for row in tastatura_telefon:
    for column in row:
        print(f'FOR EACH: Cifra curenta este {column}')


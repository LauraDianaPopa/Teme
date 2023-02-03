# gama = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
# # print(gama)
# # print(gama[::-1])
# # print(gama[0:-1])
# print(gama.count("do"))

# lista1 = [3,1,0,2]
# lista2 = [6,5,4]
# lista3 = lista1 + lista2
# print(lista3)
# lista3.remove(lista3[2])
# print(lista3)
# # if len(lista3) == 0:
# #     print(f'Lista este goala')
# # else:
# #     print(f'Lista nu este goala')
# lista3.clear()
# print(f'{lista3} nu are elemente')
# if len(lista3) == 0:
#     print(f'Lista este goala')
# else:
#     print(f'Lista nu este goala')

#Dictionare

# dict1 = {'Ana':8, 'Gigel':10, 'Dorel':5}
# print(dict1.keys())
# print(f'Ana are nota: {dict1["Ana"] }')
# print(f'Gigel are nota: {dict1["Gigel"] }')
# print(f'Dorel are nota: {dict1["Dorel"] }')
# dict1['Dorel']=6
# print(f'Dorel are nota: {dict1["Dorel"] }')
# dict1.pop('Gigel')
# print(dict1)
# dict1.update({'Ionica':9})
# print(dict1)

#Seturi
# zile_sapt = { 'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata','duminica'}
#print(zile_sapt)
#zile_sapt.update('luni')
#print(zile_sapt)
# if weekend.issubset(zile_sapt):
#     print(True)
# else:
#     print(False)

# print(zile_sapt.difference(weekend))
# print(weekend.difference(zile_sapt))

# print(zile_sapt.intersection(weekend))

lista_jucatori_teren = ['Adrian','Gica','Ciprian','Emilian','Marius']
lista_jucatori_rezerva = ['Ion','Gabriel','Mihai','George','Octavian']
lista_jucatori_scosi = []
Schimbari_efectuate = str(input('Doriti sa faceti o schimbare? '))
raspuns_corect = str('Da')
assert Schimbari_efectuate == raspuns_corect, 'NU se doresc schimbari pe teren'
SCHIMBARI_MAX = 3
while len(lista_jucatori_scosi) <= 2:
    schimbare1 = input('Ce jucator doriti sa schimbati? ')
    int(len(lista_jucatori_scosi)) == int(len(lista_jucatori_scosi)) + 1
    if schimbare1 in lista_jucatori_teren:
        print(f"Jucatorul {schimbare1} exista pe teren")
        primul_jucator_iesit = lista_jucatori_teren.remove(schimbare1)
        print(f'Noua lista cu jucatorii de pe teren este: {lista_jucatori_teren}')
        lista_jucatori_scosi == lista_jucatori_scosi.append(schimbare1)
        print(f'{schimbare1} a fost mutat in lista jucatori scosi, noua lista de jucatori scosi este {lista_jucatori_scosi}')
        schimbare1in = input ('Ce jucator doriti sa intre pe teren din rezerva? ')
        if schimbare1in in lista_jucatori_rezerva:
            print(f'Jucatorul {schimbare1in} este in rezerva ')
            primul_jucator_rezerva = lista_jucatori_rezerva.remove(schimbare1in)
            print(f'Noua lista cu jucatorii de rezerva este {lista_jucatori_rezerva}')
            lista_jucatori_teren == lista_jucatori_teren.append(schimbare1in)
            print(f'Noua lista cu jucatorii de pe teren este: {lista_jucatori_teren}')
        else:
            print(f"Jucatorul {schimbare1in} nu exista in lista cu jucatorii de rezerva")
    else:
        print(f"Jucatorul {schimbare1} nu exista pe teren")
print('A fost atins numarul maxim de schimbari')




# Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

# class Cerc():
#
#     def __init__ (self, culoare, raza):
#         self.culoare = culoare
#         self.raza = 20
#
#     def descriere_cerc(self):
#         print(self.culoare, self.raza)
#
#     def aria(self, aria_cercului):
#         if self.raza == 20:
#             aria_cercului = 3.14 * self.raza * self.raza
#         print(f'Aria cercului este: {aria_cercului}')
#
#     def diametrul (self, diametrul_cercului):
#         if self.raza ==20:
#             diametrul_cercului = 2 * self.raza
#             print(f'Diametrul cercului este: {diametrul_cercului}')
#
#     def circumferinta (self, circumferinta_cerc):
#         if self.raza == 20:
#             circumferinta_cerc = self.raza * 3.14 *2
#             print(f' Circumferinta cercului este: {circumferinta_cerc}')
#
# cerc_test = Cerc('Rosie', 20)
# cerc_test.descriere_cerc()
# cerc_test.aria(20)
# cerc_test.diametrul(20)
# cerc_test.circumferinta(20)

# Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pentru toate atributele
# Metode:
# ● descrie()
# ● aria()
# ● perimetrul()
# ● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
# Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
#
# class Dreptunghi():
#     def __init__(self, lungime, latime, culoare):
#         self.lungime = lungime
#         self.latime = latime
#         self.culoare = culoare
#     def descriere (self):
#         print(self.lungime, self.latime, self.culoare)
#
#     def aria(self):
#         aria = self.lungime * self.latime
#         print(f'Aria dreptunghiului este: {aria}')
#
#     def perimetrul(self):
#         perimetrul = 2 * self.latime + 2 * self.lungime
#         print(f'Perimetrul dreptunghiului este: {perimetrul}')
#
#     def schimba_culoare(self,noua_coloare):
#         self.culoare = noua_culoare
#
#
# dreptunghi_calcul = Dreptunghi(40, 20, 'Rosie')
# dreptunghi_calcul.descriere()
# dreptunghi_calcul.aria()
# dreptunghi_calcul.perimetrul()

'''
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''
from datetime import date

from pip._internal.utils.misc import tabulate

# class Angajat():
#     def __init__(self, nume, prenume, salariu):
#         self.nume = nume
#         self.prenume = prenume
#         self.salariu = salariu
#
#     def descriere(self):
#         print(f'Numele angajatului este: {self.nume}')
#         print(f'Prenumele angajatului este: {self.prenume}')
#         print(f'Salariul angajatului este: {self.salariu}')
#
#     def nume_complet(self):
#         print(f'Numele complet al angajatului este: {self.nume} {self.prenume}')
#
#     def salariu_lunar(self):
#         print(f'Salariu lunar a angajatului {self.nume} {self.prenume} este {self.salariu} lei')
#
#     def salariu_anual(self):
#         salariu_anual = 12 * self.salariu
#         print(f'Salariul anual al angajatului este de {salariu_anual}')
#
#     def marire_salariu(self, marire):
#         self.salariu = self.salariu + (marire / 100 * self.salariu)
#         print(f'Marire de salar de 20%, angajatul are noul salar de: {self.salariu}')
#
#
# angajat = Angajat('Popa', 'Vasile', 2000)
# angajat.descriere()
# angajat.nume_complet()
# angajat.salariu_lunar()
# angajat.salariu_anual()
# angajat.marire_salariu(30)

'''
Clasa Cont 
Atribute: iban, titular_cont, sold 
Constructor pentru toate atributele 
Metode: 
● afisare_sold() - Titularul x are în contul y suma de n lei 
● debitare_cont(suma) 
● creditare_cont(suma) 
'''

# class Cont():
#     def __init__(self, iban, titular_cont, sold):
#         self.iban = iban
#         self.titular_cont = titular_cont
#         self.sold = sold
#
#     def afisare(self):
#         print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
#
#     def debitare_cont(self, suma):
#         if suma <= self.sold:
#             self.sold -= suma
#             print(f'Mai aveti {self.sold} lei in cont')
#         else:
#             print('Fonduri insuficiente')
#
#     def creditare_cont(self,suma):
#         self.sold += suma
#         print(f'Suma dumneavoastra din cont este: { self.sold}')
#
# cont = Cont( 'ROBTRCRTxxxxxx' , 'Popa Vasile', 2500)
# cont.afisare()
# cont.debitare_cont(200)
# cont.creditare_cont(300)

'''
Clasa Factura 
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc 
Constructor: toate atributele, fara serie 
Metode: 
● schimbă_cantitatea(cantitate) 
● schimbă_prețul(pret) 
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți 
Factura seria x numar y 
Data: generați automat data de azi 
Produs | cantitate | preț bucată | Total 
Telefon | 7 | 700 | 49000 
Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/ 
'''
# class Factura():
#     serie = 5231
#     def __init__(self, numar, nume_produs, cantitate, pret_buc):
#         self.numar = numar
#         self.nume_produs = nume_produs
#         self.cantitate = cantitate
#         self.pret_buc = pret_buc
#
#     def schimba_cantitatea(self, cantitate):
#         self.cantitate = cantitate
#         print(self.cantitate)
#
#     def schimba_pretul(self, pret):
#         self.pret = pret
#         print(self.pret)
#
#     def schimba_nume_produs(self, nume):
#         self.nume = nume
#         print(self.nume)
#
#     def calc_total(self):
#         return self.pret_buc * self.cantitate
#
#     def genereaza_factura(self):
#         print([[self.nume_produs, self.cantitate, self.pret_buc, self.calc_total(), date.today()]])
#
#
# factura = Factura( 1, 'Oua', 50, 0.9)
# factura.schimba_cantitatea(30)
# factura.schimba_pretul(1.2)
# factura.schimba_nume_produs('Bomboane')
# factura.genereaza_factura()
#
'''
Clasa Masina 
Atribute: marca, model, viteza maxima, viteza_actuala, culoare, 
culori_disponibile (set), inmatriculata (bool) 
Culoare = gri - toate mașinile cand ies din fabrica sunt gri 
Viteza_actuală = 0 - toate mașinile stau pe loc când ies din fabrica 
Culori disponibile = alegeți voi 5-7 culori 
Marca = alegeți voi - fabrica produce o singură marca dar mai multe modele 
Inmatriculata = False 
Constructor: model, viteza_maxima 
Metode: 
● descrie() - se vor printa toate atributele, în afară de culori_disponibile 
● înmatriculare() - va schimba atributul înmatriculată în True 
● vopsește(culoare) - se va vopsi mașina în noua culoare DOAR dacă noua 
culoare e în opțiunea de culori disponibile, altfel afișați o eroare 
● accelerează(viteza) - se va accelera la o anumită viteza, dacă viteza e 
negativă-eroare, daca viteza e mai mare decat viteza_max - masina va 
accelera până la viteza maximă 
● franeaza() - mașina se va opri și va avea viteza 0 
'''
# class Masina():
#     culoare = 'gri'
#     viteza_actuala = 0
#     culori_disponibile = ['albastru', 'verde', 'rosu', 'galben', 'violet', 'alb', 'negru']
#     marca = 'Skoda'
#     inmatriculata = False
#
#     def __init__(self, model, viteza_maxima):
#         self.model = model
#         self.viteza_maxima = viteza_maxima
#
#     def descriere(self):
#         print(f'Masina este de culoare {self.culoare}, are marca {self.marca} si modelul {self.model}, are viteza {self.viteza_actuala} km/h dar poate ajunge pana la viteza {self.viteza_maxima} km/h si este inmatriculata {self.inmatriculata}')
#
#     def inmatriculare(self):
#         self.inmatriculata = True
#         return self.inmatriculata
#
#     def culoare_noua(self,culoare_noua):
#         if culoare_noua in self.culori_disponibile:
#             self.culoare = culoare_noua
#             print(f'Noua culoare a masinii este: {self.culoare}')
#         else:
#             print(f'Nu avem aceasta culoare!')
#
#     def accelereaza(self, viteza):
#         if viteza < 0:
#             print(f'Viteza Negativa - EROARE!')
#         elif viteza >= self.viteza_maxima:
#             self.viteza_actuala = self.viteza_maxima
#             print(f'Viteza a depasit viteza maxima!')
#         else:
#             viteza < self.viteza_maxima
#             print(f'Masina s-a accelerat cu viteza {viteza}')
#
#     def franeaza(self):
#         self.viteza_actuala = 0
#         print(f'Masina s-a oprit!')
#
# masina = Masina('Fabia', 150)
# masina.descriere()
# masina.culoare_noua('magenta')
# masina.accelereaza(260)
# masina.franeaza()

'''
 Clasa TodoList 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea) 
La început nu avem taskuri, dict e gol și nu avem nevoie de constructor 
Metode:
● adauga_task(nume, descriere) - se va adauga in dict 
● finalizează_task(nume) - se va sterge din dict 
● afișează_todo_list() - doar cheile 
● afișează_detalii_suplimentare(nume_task) - în funcție de numele taskului, 
printăm detalii suplimentare. 
○ Dacă taskul nu e în todo list, întrebam utilizatorul dacă vrea să-l 
adauge. 
○ Dacă acesta răspunde nu - la revedere 
○ Dacă răspunde da - îi cerem detalii task și salvăm nume+detalii în 
dict
'''
class ToDoList():
    dict = {}
    def adauga_task(self, nume, descriere):
        self.dict[nume] = descriere
        print(f'Am adaugat task-ul cu succes! {self.dict}')

    def finalizeaza_task(self, nume):
        del self.dict[nume]
        print(f'Am finalizat task-ul!')

    def afiseaza_todo_list(self):
        print(f'Task-urile din todolist sunt: {self.dict.keys()}')

    def afiseaza_detalii_suplimentare(self, nume):
        if nume in self.dict:
            print(f'Detalii pt taskul {nume}: {self.dict[nume]}')
        else:
            print('Nu am gasit taskul dorit')
            raspuns = input('Vrei sa adaugi task-ul in lista?')
            if raspuns.lower() == 'da':
                descriere = input('Introdu descrierea pentru noul task: ')
                self.dict[nume] = descriere
                print('Am adaugat taskul cu succes')
            elif raspuns.lower() == 'nu':
                print('La revedere!')


lista = ToDoList()
lista.adauga_task('Tema', 'Matematica' )
lista.finalizeaza_task('Tema')
lista.afiseaza_todo_list()
lista.afiseaza_detalii_suplimentare('Tema')


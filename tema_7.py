'''
ABSTRACTION
Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
'''
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    @classmethod
    def descrie(cls):
        print('Cel mai probabil are colturi!')

'''
INHERITANCE 
Clasa Pătrat - moștenește FormaGeometrica constructor pentru latură
'''
class Patrat(FormaGeometrica):

    def init (self, latura):
        self.latura = latura

    def aria(self):
        self.aria = self.latura * self.latura
        return self.aria

forma= Patrat(15)
print(forma.latura)

'''
ENCAPSULATION 
latura este proprietate privată
Implementează getter, setter, deleter pentru latură Implementează metoda cerută de interfață 
(opțional, doar dacă ai ales să implementezi metoda abstractă aria)
'''
class Forma(FormaGeometrica):

    def latura(self):
        return self.latura

    def get_latura(self):
        return self.latura

    def set_latura(self,val):
     self.latura = val

    def delete_latura(self):
         self.latura = None

'''
Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria)
'''
class Cerc(FormaGeometrica):
    def raza(self):
        return self.raza

    def get_raza(self):
        print(f'Raza cercului este: {self.raza}')
        return self.raza

    def set_raza(self, raza):
        print(f'Noua valoarea a razei este: {raza}')
        self.raza = raza

    def delete_raza(self):
        print(f'Am sters valoarea razei')
        self.raza = 0

    def aria(self):
        aria_cercului = self.PI * self.raza * self.raza
        return aria_cercului

'''
Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
'''
def descrie(self):
    print(f'Eu nu am colturi')



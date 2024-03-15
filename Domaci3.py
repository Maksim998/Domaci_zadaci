#Zadatak1

def get_word_ends_with_letter(sentences, letter):

    lista=[]
    
    sentences=sentences.split('.')[:-1]


    for i in sentences:
        lista_pom = []
        i = i.strip()
        
        rijeci=i.split(' ')
        
        for j in rijeci:
            if j[-1].isalpha() != True:
                j=j[:-1]
            if j[-1] == letter:
                lista_pom.append(j)
        lista_pom.append(len(lista_pom))
        lista.append(tuple(lista_pom))

    return lista


string="Print only the words that end with the chosen letter in those sentences. Example can contains one or more sentences."
print(get_word_ends_with_letter(string,'s'))


#Zadatak2

def najveci_proizvod_sekvence(lista):

    i=0
    proizvod=0
    sekvenca=[]
    sekvenca_pom=[]
    proizvod_pom=1
    while i<len(lista)-1:
        
        proizvod_pom=lista[i]
        sekvenca_pom=[lista[i]]

        while i+1<len(lista) and lista[i+1] == lista[i]:
            proizvod_pom*=lista[i+1]
            sekvenca_pom.append(lista[i+1])
            i+=1

        else:
            if proizvod_pom>proizvod:
                proizvod = proizvod_pom
                sekvenca = sekvenca_pom[:]
            i+=1

    return sekvenca, proizvod

print(najveci_proizvod_sekvence([1,2,5,5,5,2,2,4,4,10,10,10,10,10]))


#Zadatak3

def najduzi_testerasti_niz(lista):

    i = 0
    podniz = []
    podniz_pom = []

    while i < len(lista) - 1:
        if lista[i] != lista[i+1]:
            podniz_pom = [lista[i], lista[i+1]]
            i += 1

            while i< len(lista) - 1 and ((lista[i] -lista[i-1] > 0 and lista[i+1] - lista[i] < 0) or (lista[i] -lista[i-1] < 0 and lista[i+1] - lista[i] > 0)):
                podniz_pom.append(lista[i+1])
                i += 1
            else:
                if len(podniz_pom) >= len(podniz) and len(podniz_pom) > 2:
                    podniz = podniz_pom.copy()
                    i += 1
        else:
            i+=1
    return podniz

print(najduzi_testerasti_niz([1,2,1,1,-1,5,2,7,4,8,1,1,1,1,5,5,5,5,2,1,2,100,5,6,7,8,9,10]))


#Zadatak4

def poklapanje_susjednih_karaktera(string):

    return sum([1 for i in range(len(string)-1) if string[i]==string[i+1]])
    
print(poklapanje_susjednih_karaktera('aabaaac'))


#Zadatak5

def the_worst_podcast(podcasts):

    the_worst = {}
    pom = float('inf')
    for i in podcasts:

        if (n:=i['br_pozitivni']/i['br_negativni'])< pom:
            
            pom = n
            the_worst = i['naziv']

    return the_worst

podcasts=[{'naziv':'Español para principiantes', 'br_pozitivni':1000,'br_negativni':10},
{'naziv':'Philophize This!', 'br_pozitivni':500,'br_negativni': 30}, 
{'naziv':'Science VS. ','br_pozitivni':600,'br_negativni': 45}]

print(the_worst_podcast(podcasts))


#Zadatak6

class Televizor():

    def __init__(self, tekuci_kanal = None, naziv_tekuceg_kanala = '', kanali=[], jacina_tona = None):

        self.tekuci_kanal = tekuci_kanal
        self.naziv_tekuceg_kanala = naziv_tekuceg_kanala
        self.kanali = kanali
        self.jacnina_tona = jacina_tona

    def set_ton(self, vrijednost):

        if vrijednost > 10:
            print('Jacina tona prevazilazi maksimalnu dozvoljenu')
        elif vrijednost < 0:
            print('Vrijednost ne moze biti manja od 0')
        else:
            self.jacnina_tona = vrijednost

    def get_ton(self):
        print(self.jacnina_tona)

    def add_kanal(self, kanal):
        self.kanali.append(kanal)

    def get_tekuci_kanal(self):
        print(self.tekuci_kanal, self.naziv_tekuceg_kanala)

    def get_kanali(self):
     
        print(self.kanali)

    def set_tekuci_kanal(self,broj):
        if broj>len(self.kanali)-1 or broj<1:
            print('Kanal sa ovim brojem ne postoji')
        else:
            self.naziv_tekuceg_kanala = self.kanali[broj-1]
            self.tekuci_kanal = broj

    def obrisi_kanal(self, kanal):
        self.kanali.remove(kanal)

    def pojacaj_ton(self):
        self.jacnina_tona += 1

    def ime_kanala(self, broj):

        if broj<1 or broj>len(self.kanali):
            print('Ne postoji kanal sa tim brojem.')
        else:
            print(self.kanali[broj-1])



televizor=Televizor()

televizor.get_kanali()
televizor.add_kanal('SportKlub')
televizor.add_kanal('ArenaSport')
televizor.add_kanal('EuroSport')
televizor.get_kanali()

televizor.set_tekuci_kanal(1)
televizor.get_tekuci_kanal()

televizor.set_ton(5)
televizor.get_ton()
televizor.obrisi_kanal('SportKlub')
televizor.get_kanali()
televizor.pojacaj_ton()
televizor.get_ton()
televizor.ime_kanala(2)


#Zadatak7

class Book():
    def __init__(self, naslov, autor, god_izdanja, br_kopija):
        self.naslov = naslov
        self.autor = autor
        self.god_izdanja = god_izdanja
        self.br_kopija = br_kopija
    
    def set_naslov(self, naslov):
        self.naslov = naslov

    def set_autor(self, autor):
        self.autor = autor

    def set_god_izdanja(self, god_izdanja):
        self.god_izdanja = god_izdanja

    def set_br_kopija(self, br_kopija):
        self.br_kopija = br_kopija

    def get_naslov(self):
       
        return self.naslov
    def get_autor(self):
       
        return self.autor

    def get_god_izdanja(self):
        
        return self.god_izdanja

    def get_br_kopija(self):
        return self.br_kopija

class Library(Book):
    def __init__(self):
        self.knjige=[]

    def dodaj_knjigu(self,knjiga):
        self.knjige.append(knjiga)

    def izbrisi_knjigu(self,naslov):
        for i in self.knjige:
            if self.get_naslov(i) == naslov:
                self.knjige.remove(i)

    def broj_knjiga(self):
        print(len(self.knjige))

    def pretraga_knjiga_autor(self,autor):

        for i in self.knjige:
            
            if i.get_autor() == autor:
                print(i.get_naslov())
                print(i.get_autor())
                print(i.get_god_izdanja())
                print(i.get_br_kopija())
        
    def prikaz_biblioteke(self):
        for i in self.knjige:
            print(i.get_naslov())
            print(i.get_autor())
            print(i.get_god_izdanja())

    def izmjena_knjige_naziv(self,naslov1,naslov2):
        for i in self.knjige:
            if i.get_naslov()==naslov1:
                i.set_naslov(naslov2)

    def izmjena_knjige_autor(self,naslov,autor):
        for i in self.knjige:
            if i.get_naslov()==naslov:
                i.set_autor(autor)

    def izmjena_knjige_god_izdanja(self,naslov,god_izdanja):
        for i in self.knjige:
            if i.get_naslov() == naslov:
                i.set_god_izdanja=god_izdanja
    
    def izmjena_knjige_br_kopija(self, naslov, br_kopija):
        for i in self.knjige:
            if i.get_naslov()==naslov:
                i.set_br_kopija=br_kopija
        
knjiga=Book('Harry Potter','J. K. Rawling',1995,1500)

print(knjiga.get_autor())
print(knjiga.get_br_kopija())

knjige=Library()
knjige.dodaj_knjigu(knjiga)
knjige.broj_knjiga()

knjige.pretraga_knjiga_autor('J. K. Rawling')

knjige.prikaz_biblioteke()

knjige.izmjena_knjige_naziv('Harry Potter','Harry Potter2')
knjige.pretraga_knjiga_autor('J. K. Rawling')


#Zadatak8

class Player():

    def __init__(self, x, y, width, height, health):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._health = health

    def set_x(self,x):
        self._x = x
    def set_y(self,y):
        self._y = y
    def set_width(self,width):
        self._width = width
    def set_height(self,height):
        self._height = height
    def set_health(self, health):
        if health > 100 or health < 0:
            print('Nije moguce dodijeliti ovu vrijednost')
        else:
            self._health = health

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height
    def get_health(self):
        return self._health

class Enemy(Player):

    def __init__(self, x, y, width, height, damage):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._damage = damage
        
    def set_x(self,x):
        self._x = x
    def set_y(self,y):
        self._y = y
    def set_width(self,width):
        self._width = width
    def set_height(self,height):
        self._height = height
    def set_damage(self, damage):
        if damage<0 or damage>100:
            print('Nije moguce postaviti damage na ovu vrijednost.')
        else:
            self._damage = damage

    def get_x(self):
        return self._x
    def get_y(self):
        return self._y
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height
    def get_damage(self):
        return self._damage



def check_collision(player, enemy):
    
    x_player = player.get_x()
    x1_player = x_player + player.get_width()/2
    x2_player = x_player - player.get_width()/2
    y_player = player.get_y()
    y1_player = y_player + player.get_width()/2
    y2_player = y_player - player.get_width()/2

    x_enemy = enemy.get_x()
    x1_enemy = x_enemy + enemy.get_width()/2
    x2_enemy = x_enemy - enemy.get_width()/2
    y_enemy = enemy.get_y()
    y1_enemy = y_enemy + enemy.get_width()/2
    y2_enemy = y_enemy - enemy.get_width()/2
   
   #Mislim da nije dobro definisan ovaj zadatak, pa je pojednostavljen
    return (x1_player >= x2_enemy and x2_player <= x1_enemy and
        y1_player >= y2_enemy and y2_player <= y1_enemy)
    
def decrease_health(player,enemy):

    if player.get_health()- enemy.get_damage()<0:
        player.set_health(0)
    else:
        player.set_health(player.get_health()- enemy.get_damage())
        
    return player


player = Player(1, 1, 10, 10, 50)
enemy1 = Enemy(10, 4, 20,20, 60)
enemy2 = Enemy(4,1, 20, 20, 20)


if check_collision(player,enemy1):
    player = decrease_health(player,enemy1)
    
    if player.get_health()==0:
        print('Player ima health 0 i izgubio je.')
    else:
        print(f'Player ima health {player.get_health()}')

else:
    print('Nije doslo do sudara')


#Zadatak9
    
import random

class Turnir():
    def __init__(self, naziv, broj_rundi):
        self.naziv = naziv
        self.lista_igraca = []
        self.broj_igraca = 0
        self.broj_rundi = broj_rundi

    def set_lista_igraca(self, lista_igraca):
        self.lista_igraca = lista_igraca[:]
        self.broj_igraca = len(self.lista_igraca)
    def set_naziv(self,naziv):
        self.naziv = naziv
    def set_broj_rundi(self, broj_rundi):
        if broj_rundi > 10 or broj_rundi < 0:
            print('Nije moguce unijeti ovaj broj rundi.')
        else:
            self.broj_rundi = broj_rundi
            
    def get_lista_igraca(self):
        return self.lista_igraca
    def get_broj_igraca(self):
        return self.broj_igraca
    def get_naziv(self):
        return self.naziv
    def get_broj_rundi(self):
        return self.broj_rundi
    def get_igrac(self,ime):
        for i in self.lista_igraca:
            if i[0]==ime:
                return i
                break
    
    def set_igrac_bodovi(self,ime, bodovi):
        for i in range(len(self.lista_igraca)):
            if self.lista_igraca[i][0]==ime:
                self.lista_igraca[i]=ime, bodovi
                break
    def dodaj_igraca(self, ime):
        self.lista_igraca.append((ime,0))
        self.broj_igraca+=1

    def ukloni_igraca(self,ime):
        for i in self.lista_igraca:
            if i[0] == ime:
                self.lista_igraca.remove(i)

    def najbolji_igrac(self):
        return max(self.lista_igraca, key=lambda x: x[1])
    
    def set_br_bodova(self, ime, bodovi):
        for i in range(len(self.lista_igraca)):
            if self.lista_igraca[i][0]==ime:
                self.lista_igraca[i]=ime,bodovi


def pokreni_rundu(turnir):

    turnir.set_broj_rundi(turnir.get_broj_rundi()+1)
   
    a=random.randint(0, turnir.get_broj_igraca()-1)

    b=random.randint(0, turnir.get_broj_igraca()-1)

    while a==b:
       b=random.randint(0, turnir.get_broj_igraca()-1)

    igrac1=turnir.get_lista_igraca()[a]
    igrac2=turnir.get_lista_igraca()[b]
    
    if igrac1[1] > igrac2[1]:
        pobjeda_igrac1 = 1.6*random.random()
        pobjeda_igrac2 = random.random()

    else:
        pobjeda_igrac2 = 1.6*random.random()
        pobjeda_igrac1 = random.random()


    pobjednik= igrac1 if pobjeda_igrac1>pobjeda_igrac2 else igrac2
    return pobjednik


turnir=Turnir('Turnir1', 2)
turnir.dodaj_igraca('Igrac1')
turnir.dodaj_igraca('Igrac2')

print(turnir.get_igrac('Igrac1'))
turnir.set_br_bodova('Igrac2',3)
print(turnir.get_igrac('Igrac1'))
print(turnir.get_broj_rundi())
print(pokreni_rundu(turnir))
print(turnir.get_broj_rundi())


#Zadatak10

class Color():
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    def set_blue(self, blue):
        if blue < 0 or blue > 255:
            print('Unijeta vrijednost izlazi iz dozvoljenog opsega.')
        else:
            self._blue = blue
    def set_red(self, red):
        if red < 0 or red > 255:
            print('Unijeta vrijednost izlazi iz dozvoljenog opsega.')
        else:
            self._red = red
    def set_green(self, green):
        if green < 0 or green > 255:
            print('Unijeta vrijednost izlazi iz dozvoljenog opsega.')
        else:
            self._green = green

    def get_green(self):
        return self._green
    def get_red(self):
        return self._red
    def get_blue(self):
        return self._blue    
    
    def add_red(self, change):

        if self._red+change < 0 or self._red+change > 255:
            print('Vrijednost nije moguce promijeniti jer izlazi iz opsega.')
        else:
            self._red += change
    
    def add_green(self, change):

        if self._green+change < 0 or self._green+change > 255:
            print('Vrijednost nije moguce promijeniti jer izlazi iz opsega.')
        else:
            self._green += change
    
    def add_blue(self, change):

        if self._blue+change < 0 or self._blue+change > 255:
            print('Vrijednost nije moguce promijeniti jer izlazi iz opsega.')
        else:
            self._blue += change

    def __lt__(color1, color2):
        return( color1._blue < color2._blue and color1._green < color2._green and color1._red < color2._red)

    def __eq__(color1, color2):
        return(color1._blue == color2._blue and color1._green == color2._green and color1._red == color2._red)
    
    def __str__(self):
        return(f"""blue: {self.get_blue()}
red: {self.get_red()}
green: {self.get_green()}""")

color1=Color(1,1,1)
color2=Color(1,1,1)

print(color1 < color2)
print(color1 == color2)
print(color1)


#Zadatak11

class ColorAlpha(Color):
    def __init__(self, red, green, blue, alpha):
        super().__init__(red,green,blue)
        self._alpha = alpha

    def get_alpha(self):
        return self._alpha
    
    def set_alpha(self,alpha):
        if alpha > 1 or alpha < 0:
            print('Vrijednost je van dozvoljenog opsega.')
        else:
            self._alpha = alpha

    def update_color_by_alpha(self):
        self.set_blue(self.get_blue() - self.get_blue()*self.get_alpha())
        self.set_red(self.get_red() - self.get_red()*self.get_alpha())
        self.set_green(self.get_green() - self.get_green()*self.get_alpha())

    def __str__(self):
        return(f"""blue: {self.get_blue()}
red: {self.get_red()}
green: {self.get_green()}
alpha: {self.get_alpha()}""")
    

coloralpha1 = ColorAlpha(200, 200, 200, 0.5)
coloralpha2 = ColorAlpha(300, 300, 300, 0.1)

coloralpha1.set_alpha(-1)
coloralpha1.set_alpha(0.4)
print(coloralpha1.get_alpha())

coloralpha1.update_color_by_alpha()
coloralpha2.update_color_by_alpha()

print(coloralpha1)
print(coloralpha1 < coloralpha2)
print(coloralpha1 == coloralpha2)


#Zadatak12

class Company():
    def __init__(self, name, area, balance, max_num_of_employees):
        self._name = name
        self._area = area
        self._employees = []
        self._balance = balance
        self._max_num_of_employees = max_num_of_employees 

    def get_name(self):
        return self._name
    def get_area(self):
        return self._area
    def get_balance(self):
        return self._balance
    def get_max_num_of_employees(self):
        return self._max_num_of_employees
    
    def set_name(self, name):
        self._name = name
    def set_area(self, area):
        self._area = area
    def set_balance(self, balance):
        if balance < 0:
            return('Nije moguce podesiti balance na ovu vrijednost.')
        else:
            self._balance = balance
    def set_max_num_of_employees(self, max_num_of_employees):
        if max_num_of_employees < 0:
            print('Nije moguce podesiti maksimalni broj zaposlenih na ovu vrijednost.')
        else:
            self._max_num_of_employees = max_num_of_employees

    def add_employee(self, employee):
        if self.get_max_num_of_employees() > len(self._employees):
            self._employees.append(employee)
        else:
            print('Nije moguce dodati novog zaposlenog jer je broj zaposlanih maksimalni moguci')

    def remove_employee(self, name, surname):
        for i in self._employees:
            if i['name'] == name and i['surname'] ==surname:
                self._employees.remove(i)
                break

    def __str__(self):

        return f"""name: {self.get_name()}
area: {self.get_area()}
balance : {self.get_balance()}
"""
    
    def can_pay_employees(self):

        sum_of_salaries=sum([x['salary'] for x in self._employees])

        return self._balance > sum_of_salaries
    
    def __gt__(company1, company2):

        return(len(company1._employees) > len(company2._employees))
    

kompanija1=Company('Kompanija1','Arena1',100000,100)
kompanija2=Company('Kompanija2','Arena2',200000,200)

kompanija1.add_employee({'name':'Ime11','surname':'Prezima11','salary':1000})
kompanija1.add_employee({'name':'Ime12','surname':'Prezima12','salary':1500})

kompanija2.add_employee({'name':'Ime21','surname':'Prezima21','salary':1000})


kompanija1.set_area('Nova lokacija')
kompanija1.set_balance(20000000)
kompanija1.set_max_num_of_employees(2)
kompanija1.set_name('Novo ime')
print(kompanija1.get_name())
print(kompanija1.get_area())
print(kompanija1.get_balance())
print(kompanija1.get_max_num_of_employees())

kompanija1.add_employee({'name':'Ime13','surname':'Prezima13','salary':1500})

kompanija1.remove_employee('Ime12','Prezima12')

print(kompanija1)

print(kompanija1.can_pay_employees())
print(kompanija1 > kompanija2)


#Zadatak13

class Student():
    def __init__(self, name, surname, year):
        self._ime = name
        self._prezime = surname
        self._godina = year
        self._predmeti = []

    def get_ime(self):
        return self._ime
    def get_prezime(self):
        return self._prezime
    def get_godina(self):
        return self._godina
    
    def set_ime(self, ime):
        self._ime = ime
    def set_prezime(self, prezime):
        self._prezime = prezime
    def set_godina(self, godina):
        if godina < 0 or godina > 8:
            print('Nije moguce postaviti ovu vrijednost za atribut godina')
        else:
            self._godina = godina

    def insert_subject(self, predmet):
        self._predmeti.append(predmet)
        print(self._predmeti)
    def remove_subject(self, predmet):

         self._predmeti = list(filter(lambda x: x['naziv'] != predmet, self._predmeti)).copy()
        

    def compute_average(self):

        ocjene ={'A': 10, 'B': 9, 'C': 8, 'D': 7, 'E': 6}
        suma = 0
        ukupno_kredita = 0
        for i in self._predmeti:
            if i['ocjena'] != 'F':
                suma += ocjene[i['ocjena']]*i['broj_kredita']
                ukupno_kredita += i['broj_kredita']
        
        return suma/ukupno_kredita
    
    def __str__(self):
        return f"""ime: {self.get_ime()}
prezime: {self.get_prezime()}
prosjek: {self.compute_average()}"""
    
student1 = Student('Ime1', 'Prezime1', 1)
student2 = Student('Ime2', 'Prezime2', 3)

student1.set_godina(5)
student1.set_ime('Maksim')
student1.set_prezime('Kontic')
print(student1.get_ime())
print(student1.get_prezime())
print(student1.get_godina())

student1.insert_subject({'naziv': 'matematika', 'ocjena':'A', 'broj_kredita':7})
student1.insert_subject({'naziv': 'programiranje', 'ocjena':'B', 'broj_kredita': 5})
student1.insert_subject({'naziv': 'programiranjeII', 'ocjena':'D', 'broj_kredita': 5})
student1.remove_subject('programiranje')
print(student1._predmeti)

print(student1)
print(student1.compute_average())


#Zadatak14

class Drzava():

    def __init__(self, name, population, border, cities):
        self.name = name
        self.population = population
        self.border = border.copy()
        self.cities = cities.copy()

    def get_name(self):
        return self.name
    def get_population(self):
        return self.population
    def get_border(self):
        return self.border
    def get_cities(self):
        return self.cities

    def set_name(self, name):
        self.name = name
    def set_population(self, population):
        self.population = population
    def set_border(self, border):
        self.border = border.copy()
    def set_cities(self, cities):
        self.cities = cities.copy()

    def add_in_border(self, country):
        self.border.append(country)

    def print_max_min_population(self):
        maks_pop = max(self.cities, key = lambda x: x['population'])
        min_pop = min(self.cities, key = lambda x: x['population'])

        print(maks_pop['name'], min_pop['name'])
    
    def __str__(self):
        return f'ime, {self.name}; broj stanovnika, {self.population}; gradovi, {self.cities}'


class Federacija(Drzava):

    def __init__(self, name, population, border, cities, countries):
        super().__init__(name, population, border, cities)
        self.countries = countries[:]

    def get_countries(self):
        return self.countries
    
    def set_countries(self, countries):
        self.countries = countries.copy()

    def __lt__(self, federacija2):

        return len(self.countries) < len(federacija2.countries)
    
    def __gt__(self, federacija2):
        return len(self.countries) > len(federacija2.countries)
    
    def __str__(self):
        return f'ime, {self.name}; broj drzava u federaciji, {len(self.countries)}; imena drzava, {self.countries}'


drzava1 = Drzava('Drzava1', 9000, ['Drzava2', 'Drzava3', 'Drzava4'],[{'name':'Grad1','population':50}, {'name':'Grad2','population':500}])
drzava1.print_max_min_population()

federacija1 = Federacija('Federacija1', 1000000, ['Drzava5', 'Drzava6', 'Drzava7', 'Drzava8', 'drzava9'],[{'name':'Grad5','population':5000}, {'name':'Grad6','population':10}, {'name':'Grad7','population':10000},
                                                                                                        {'name':'Grad8','population':100000}, {'name':'Grad9','population':1000}], ['Clanica1', 'Clanica2', 'Clanica3', 'Clanica4'])
federacija2 = Federacija('Federacija2', 1000000, ['Drzava1', 'Drzava2'],[{'name':'Grad99','population':500}, {'name':'Grad100','population':1000000}], ['Clanica A', 'Clanica B', ' Clanica C', 'Clanica D', 'Clanica E'])
federacija1.print_max_min_population()

drzava1.add_in_border('Drzava5')
federacija1.add_in_border('Drzava10')

print(drzava1.get_name())
print(drzava1.get_population())
print(drzava1.get_border())
print(drzava1.get_cities())
print(drzava1)

federacija1.set_name('Federacija_novo')
federacija1.set_population(1)
federacija1.set_cities([{'name':'Grad5 novo', 'population': 1200}, {'name': 'Grad6 novo', 'population':1500}])
print(federacija1.get_name())
print(federacija1.get_population())
print(federacija1.get_border())
print(federacija1.get_cities())
print(federacija1)

print(federacija1 > federacija2)
print(federacija1 < federacija2)


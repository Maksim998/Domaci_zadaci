#Zadatak1

from functools import reduce
lista=['flower', 'flow', 'flight']

najduzi_string = reduce(lambda x,y: x if len(x) > len(y) else y, lista)
print(najduzi_string)


#Zadatak2

def studenti_iznad_prosjeka(lista1,lista2):

    lista3 =list(filter(lambda x: x[1] >= 8.5, list(zip(lista1,lista2))))
    return lista3

lista1 = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7']
lista2 = [7.5, 9.5, 6.5, 10, 9, 7, 8.5]

print(studenti_iznad_prosjeka(lista1,lista2))


#Zadatak3

def funkcija(studenti):

    studenti1 = sorted(list(filter(lambda x: x['godine'] > 21 , studenti)), key = lambda x: x['prosek'])
    return studenti1


studenti=[{ 'ime': 'Ana', 'godine': 22, 'prosek': 9.1 },
          { 'ime': 'Marko', 'godine': 20, 'prosek': 10 },
          { 'ime': 'Janko', 'godine': 25, 'prosek': 10 },
          { 'ime': 'Milos', 'godine': 21, 'prosek': 6.5 },
          { 'ime': 'Stefan', 'godine': 26, 'prosek': 7.5 }]

print(funkcija(studenti))


#Zadatak4

from functools import reduce
def funkcija(lista):

    return(reduce(lambda x,y: x+y,list(map(lambda x: len(x.split(' ')), lista))))


lista = ["Hello, World!", "Python is cool", "Functional programming rocks"]
print(funkcija(lista))


#Zadatak5

from functools import reduce

def funkcija(lista):

    
    predmeti= set(map(lambda x: x[2], lista))
    proracun = lambda predmet: (predmet,reduce(lambda y,x: x[1]+y, filter(lambda x: x[2] == predmet, lista),0)/len(list(filter(lambda x: x[2] == predmet, lista))))
    average_grades = list(map(proracun, predmeti))

    print(average_grades)

lista =  [("Ana", 10, "Matematika"), ("Ana", 8, "Fizika"), ("Marko", 10, "Matematika"), ("Marko", 6, "Fizika")]
funkcija(lista)

#Zadatak6 

a=[1,2,7,4,23,1]

dif=list(map(lambda x,y: y-x, a[:-1],a[1:]))
print(dif)


#Zadatak7

from functools import reduce

def funkcija(lista):
     lista1 = reduce(lambda y, x: {**y, x: y.get(x, 0)+1} , lista, {})

     return lista1

lista = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
print(funkcija(lista))


#Zadatak8

with open('pravougaonici.txt', mode= 'r') as my_file:
    maks_p = 0
    for line in my_file:
        line = line.split(',')
        if int(line[0]) * int(line[1]) > maks_p:
            maks_p = int(line[0]) * int(line[1])

    print(maks_p)

    #maks_p = max(list(map(lambda x: int(x[0])*int(x[1]), map(lambda x: x.split(','), my_file.readlines()))))


#Zadatak9

def najvece_naselje(grad):

    with open('cities.txt', mode= 'r') as my_file:
       
        return(max(list(filter(lambda x: x[0] == grad, list(map(lambda x: x.split(','), my_file.readlines())))), key= lambda x: int(x[2]))[1])

        #max_pop = 0
        #max_pop_naselje = ''
        #for line in my_file:
            #line = line.split(',')
            #if line[0] == grad and int(line[2]) > max_pop:
               # max_pop = int(line[2])
                #max_pop_naselje = line[1]

    #return max_pop_naselje

print(najvece_naselje('Podgorica'))


#Zadatak10

def najmanji_grad(drzava):

    with open('population.txt', mode= 'r') as my_file:
       
        return(min(list(filter(lambda x: x[0] == drzava, list(map(lambda x: x.split(','), my_file.readlines())))), key= lambda x: int(x[2]))[1])


print(najmanji_grad('Poljska'))


#Zadatak11

def ukupna_pop(drzava):

    with open('population.txt', mode= 'r') as my_file:
        ukupno = 0

        for line in my_file:

            if (n:=line.split(','))[0] == drzava:
                ukupno += int(n[2])

        return ukupno
    
print(ukupna_pop('Poljska'))


#Zadatak12

with open('heksadecimalni brojevi.txt', mode= 'r') as my_file:
    suma = 0
    for line in my_file:
        if line[0:2] == '0x' and (n := int(line,16)) % 10 == 3:
            suma += n

print(suma)


#Zadatak13

def append_to_file(lista):

    with open('products.txt', 'w') as my_file:

        my_file.write('Naziv, Opis, Godina, Kolicina, Cijena \n')


        for i in lista:

            my_file.write(f'{i['naziv']}, {i['opis']}, {i['godina']}, {i['kolicina']}, {i['cijena']} \n')
    
        

def get_products_older_than(godina):
    izdvojeni=[]
    with open('products.txt', 'r') as my_file:
        my_file.readline()
        for line in my_file:
            line_pom=line.split(',')
            if int(line_pom[2]) > godina:
                izdvojeni.append(line.strip())
    
    return izdvojeni


def max_possible_revenue():
    revanue = 0
    with open('products.txt', 'r') as my_file:
        my_file.readline()
        for line in my_file:
            line_pom = line.split(',')
            revanue += int(line_pom[3]) * int(line_pom[4])

    return revanue
    

lista = [{'naziv': 'Televizor', 'opis': 'LG televizor 43inc', 'godina': 2019, 'kolicina': 10, 'cijena':
300}, {'naziv': 'Televizor', 'opis':'Samsung televizor 39inc', 'godina': 2017, 'kolicina': 5,
'cijena': 250}]

append_to_file(lista)

izdvojeni = get_products_older_than(2018)
print(izdvojeni)

print(max_possible_revenue())


#Zadatak14

def append_to_file(list_of_students):
    with open('students.txt','w') as my_file:
        
        for i in list_of_students:
            
            my_file.write(f'{i['ime']},{i['prezime']},{i['godina']},{i['prosjek']}\n')

def get_students_with_greater_grade(year, grade):
    students = []
    grades = {'A':(9.5,10),'B':(8.5,9.5),'C':(7.5,8.5),'D':(6.5,7.5), 'E':(6,6.5)}
    with open('students.txt','r') as my_file:
        
        for line in my_file:
            line_pom = line.split(',')
            
            if int(line_pom[2]) == year and float(line_pom[3]) >= grades[grade][0]:
                students.append({'ime':line_pom[0],'prezime':line_pom[1],'godina':int(line_pom[2]),'prosjek':float(line_pom[3])})
                
    return students

list_of_students = [{'ime': 'Marko', 'prezime':'Markovic', 'godina': 2, 'prosjek': 8.6 }, {'ime': 'Boris',
'prezime':'Boricic', 'godina': 3, 'prosjek': 7.9 }, {'ime': 'Novak', 'prezime': 'Novovic',
'godina': 3, 'prosjek': 6.9 }]

list_of_students1 = [{'ime': 'Stefan', 'prezime':'Stefanovic', 'godina': 2, 'prosjek': 9.2 }, {'ime': 'Janko',
'prezime':'Jankovic', 'godina': 5, 'prosjek': 6.6 }, {'ime': 'Petar', 'prezime': 'Petrovic',
'godina': 2, 'prosjek': 8.2 }]

append_to_file(list_of_students)
print(get_students_with_greater_grade(3,'C'))

append_to_file(list_of_students1)
print(get_students_with_greater_grade(2,'B'))


#Zadatak15

def validacija():
    with open('kreditne_kartice.txt','r') as my_file, open('kreditne_kartice_valid_or_invalid.txt','w') as my_file2:
        for line in my_file:
            line = line.strip()
            if len(line) == 16 and line.isdigit():
                line_pom = [int(digit) for digit in line]
                if len(line) == 16 and all(i.isdigit() for i in line):
                    line_pom = list(map(int, list(line)))

                    for i in range(len(line_pom)-2,-1,-2):
                        if line_pom[i] * 2 > 9:
                            line_pom [i] = (line_pom[i] * 2) % 10 + (line_pom[i]*2)//10
                        else:
                            line_pom[i] *= 2

                    if sum(line_pom)%10 == 0:
                        my_file2.write(f'{line} Valid\n')
                    else:
                        my_file2.write(f'{line} Invalid\n')

            else:
                my_file2.write(f'{line} Invalid\n')


validacija()


#Zadatak16

#Zadatak17

from time import time
import random

def decorator(func):

    def wrap_func(*arg, **kwarg):
        t1 = time()
        func(*arg,**kwarg)
        t2 = time()

        print(t2 - t1)

    return wrap_func


@decorator
def say_hello():
    print('hallooooo')


@decorator
def funkcija1():
    for i in range(1000000):
        j = i+100
        

@decorator
def funkcija2(x):
    a=[]
    for i in range(x):
        a.append(random.random())

@decorator
def funkcija3(x,y = 5):
    lista=[]
    for i in x:
        if i % y == 0:
            lista.append(i)

    #print(lista)


say_hello()
funkcija1()
funkcija2(150000)
funkcija3(list(range(15000000)))
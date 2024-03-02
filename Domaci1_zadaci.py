#Zadatak1

a=int(input('Duzina stranice a '))
b=int(input('Duzina stranice b '))

P=a*b
O=2*a+2*b

print(f'Povrsina je {P}, obim je {O}')


#Zadatak2

a=2
b=-5
c=2

x1=(-b+(b**2-4*a*c)**(1/2))/2/a
x2=(-b-(b**2-4*a*c)**(1/2))/2/a

print(x1,x2)


#Zadatak3

x1=int(input("Prvi broj"))
x2=int(input("Drugi broj"))

rezultat=x1**2-x2**2

print(rezultat)


#Zadatak4

a=int(input('Duzina terena '))
b=int(input('Sirina terena '))

pretrcano=4*(2*a+2*b)

print(pretrcano)


#Zadatak5

a=int(input('Duzina papira u mm'))
b=int(input('Sirina papira u mm'))

P=a*b/10/10

print(f'Povrsina papira u cm je {P}')


#Zadatak6

a=int(input('Prvi parametar '))
b=int(input('Drugi parametar '))
c=int(input('Treci parametar '))


Rezultat=a**2+b**2+c**2+2*a*b+2*a*c+2*b*c

print(f'Kvadrat trinom iznosi {Rezultat}')


#Zadatak7

vrijeme=float(input('Vrijeme voznje '))

kolicina=vrijeme//2

print(kolicina)


#Zadatak8

import math

r=float(input('Poluprecnik stoljnjaka '))

traka=2*r*math.pi

print(traka)


#Zadatak9
d=float(input('Duzina terena u m '))
s=float(input('Sirina terena u m '))
r=float(input('Rastojanje ograde od terena'))


rezultat=2*(d+2*r)+2*(d+2*r)

print(rezultat)


#Zadatak10

koordinate_dd=input('Koordinate donje desne ivice (forma x,y)')
koordinate_gl=input('Koordinate gornje lijeve ivice (forma x,y) ')

x_dd=int(koordinate_dd[0])
y_dd=int(koordinate_dd[2])

x_gl=int(koordinate_gl[0])
y_gl=int(koordinate_gl[2])


O=2*((x_dd-x_gl)+(y_gl-y_dd))
P=(x_dd-x_gl)*(y_gl-y_dd)

print(O)
print(P)


#Zadatak11

A=input('Koordinate tacke A forma (x,y)')
B=input('Koordinate tacke B forma (x,y)')

x1=float(A[0])
y1=float(A[2])

x2=float(B[0])
y2=float(B[2])

D=((x1-x2)**2+(y1-y2)**2)**0.5

print(f'Rastojanje je {D}')


#Zadatak12

godine=int(input('Miloseve godine: '))


god_rodjenja=2024-godine

print(f'Milos je rodjen {god_rodjenja}. godine')


#Zadatak13

G=(1,1)
K=(2,5)


Pozicija_blago=K[0]+2,K[1]-3

print(Pozicija_blago)

Vazdusno_rastojanje=((G[0]-Pozicija_blago[0])**2+(G[1]-Pozicija_blago[1])**2)**0.5
print(Vazdusno_rastojanje)

Ukupno_rastojanje=((G[0]-K[0])**2+(G[1]-K[1])**2)**0.5+((K[0]-Pozicija_blago[0])**2+(K[1]-Pozicija_blago[1])**2)**0.5
print(Ukupno_rastojanje)


#Zadatak14

velicina=float(input('Velicina stana '))
cijena_kvadrat=1200
fiksni_dio_cijene=1000

parking=int(input('Da li ima parking: ima-1, nema-0: '))
lokacija=int(input('Lokacija: zona 1-3, zona 2-2, zona 3-1: '))

cijena=(velicina+lokacija*5+parking*5*10)*cijena_kvadrat+fiksni_dio_cijene

print(cijena)


#Zadatak15

from math import sqrt


a=(1,1)
b=(3,1)
c=(2,2)

ab=sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
ac=sqrt((a[0]-c[0])**2+(a[1]-c[1])**2)
bc=sqrt((b[0]-c[0])**2+(b[1]-c[1])**2)

print(ab)
print(ac)
print(bc)

s=(ab+ac+bc)/2

P=sqrt(s*(s-ab)*(s-ac)*(s-bc))
print(P)


#Zadatak16

kilometri=int(input('Predjena kilometraza: '))

cijena_km=0.5
cijena_poc=1

cijena_voznje=cijena_poc+cijena_km*kilometri

print(cijena_voznje)


#Zadatak17

cijena=float(input('Cijena knjige: '))
popust=int(input('Popust: '))


nova_cijena=cijena-cijena*popust/100

print(f'Nova cijena knjige: {nova_cijena}')


#Zadatak18

cijena=float(input("Cijena Playstation 5 je :"))

#cijena1=cijena+cijena*10/100
cijena1=cijena*1.1

#cijena2=cijena1- cijena1*10/100
cijena2=cijena1*0.9

print(cijena2)


#Zadatak19

broj=495
suma=0

while broj>0:
    suma+=broj%10
    broj=broj//10

print(suma)


#Zadatak20

broj=222

suma=0
proizvod=1

while broj>0:
    suma+=broj%10
    proizvod*=broj%10
    broj//=10

kod=proizvod-suma

print(kod)


#Zadatak21

broj=2224

kod=broj%10*broj//1000-(broj%100//10)*(broj%1000//100)

print(kod)


#Zadatak22

N=80
K=30
p1=78.2
p2=89.3

p=((N-K)*p1+K*p2)/N

print(f'{p:.2f}')


#Zadatak23

a=float(input('Prvi parametar: '))
b=float(input('Drugi parametar: '))

p=(a+b)/2

print(p)


#Zadatak24

x=7
y=10

pom=x
x=y
y=pom

print(x,y)


#Zadatak25

duzina_cm=324

duzina_m=duzina_cm//100

print(duzina_m)


#Zadatak26

broj=int(input("Zadati broj: "))

sprat=broj%100//10

print(sprat)


#Zadatak27

broj=int(input('Cetvorocifreni broj: '))

suma=0
while broj>0:
    suma+=broj%10
    broj//=10

rezultat=suma**2

print(rezultat)


#Zadatak28

broj=int(input("Trocifreni broj: "))

broj_novo=broj%10*100+broj%100//10*10+broj//100

print(broj_novo)


#Zadatak29

x1 = float(input("X koordinata prve tacke: "))
y1 = float(input("Y koordinata druge tacke: "))
x2 = float(input("X koordinata druge tacke: "))
y2 = float(input("Y koordinata druge tacke: "))

tacka_susreta=(x1+x2)/2,(y1+y2)/2

print(f'Koordinate tacke susreta {tacka_susreta}')

from math import sqrt

predjeni_put=sqrt((tacka_susreta[0]-x1)**2+(tacka_susreta[1]-y1)**2)

print(f'Predjeni put: {predjeni_put}')


#Zadatak30

a,b=543,130

c=65

rjesenje=(a*b)//c**2

print(rjesenje)


#Zadatak31

from math import sqrt
d=50

odnos=16/9

#a=odnos*b
#d**2=(1+odnos**2)*b**2

b=sqrt(d**2/(1+odnos**2))

a=b*odnos

P=a*b

print(f""" 
Duzina: {a}
Sirina: {b}
Povrsina: {P}""")


#Zadatak32

broj=input('Sestocifreni broj: ')

a=int(broj[0])*int(broj[2])+2+int(broj[-1])
b=int(broj[1])+int(broj[3])*int(broj[-2])

print(a==b)


#Zadatak33

a=int(input('Duzina poljane: '))
b=int(input('Sirina poljane: '))
x=int(input('Stranica kvadrata: '))

p1=a*b
p2=x**2

broj=p1//p2

print(broj)


#Zadatak34

broj=123456

identifikacioni_broj=0

broj_pom=broj


while broj_pom>0:
    identifikacioni_broj+=broj_pom%10
    broj_pom//=10


identifikacioni_broj=identifikacioni_broj**2
identifikacioni_broj-=(broj%10000//1000)*(broj%1000//100)

print(identifikacioni_broj)


#Zadatak35

broj=54321

broj_pom=broj
k=0
suma=0

while broj_pom>0:
    k+=1
    suma+=broj_pom%10
    broj_pom//=10

rezultat=suma/k+broj%10

print(rezultat)
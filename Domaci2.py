#Zadatak1

broj=input('Generisani broj: ')

if int(broj)%10%2==0:
    print('Portal se otvara.')
else:
    print('Portal ostaje zatvoren.')


#Zadatak2
    
m=input('Milos je ubrao: ')
p=input('Petar je ubrao: ')

if int(m)>int(p):
    print('Milos je ubrao vise.')
else:
    print('Petar je ubrao vise.')


#Zadatak3
    
prisustvo=input('Student je prisustvovao:')
seminarski=input('Student je predao sve seminarske radove (0-Ne, 1-Da): ')

if int(prisustvo)>75 and int(seminarski)== 1:
    print('Student moze pristupiti ispitu.')
else:
    print('Student ne moze pristupiti ispitu')


#Zadaci4
    
vrijeme=input('Unesite vrijeme: ')

if int(vrijeme)<6 or (int(vrijeme)>13 and int(vrijeme)<17) or int(vrijeme)>22:
    print('Ne mogu se izvoditi bucniji radovi.')
else:
    print('Mogu se izvoditi bucniji radovi.')


#Zadatak5
    
a=float(input('Duzina prve stranice: '))
b=float(input('Duzina druge stranice: '))
c=float(input('Duzina trece stranice: '))

if a+b>c and a+c>b and b+c>a:
    print('Date stranice mogu konstruisati trougao.')
else:
    print('Date stranice ne mogu konstruisati trougao.')


#Zadatak6
    
x=input('X koordinata: ')
y=input('Y koordinata: ')

if int(y)==2*int(x)+5:
    print('Pcela se krece po zici.')
else:
    print('Pcela se ne krece po zici.')


#Zadatak7
    
mat1=int(input('Prvi takmicar matematika bodovi: '))
prog1=int(input('Prvi takmicar programiranje bodovi: '))

mat2=int(input('Drugi takmicar matematika bodovi: '))
prog2=int(input('Drugi takmicar programiranje bodovi: '))


if mat1 + prog1 == mat2 + prog2:
    if prog1>prog2:
        print('Pobijedio je prvi takmicar.')
    else:
        print('Pobijedio je drugi takmicar.')

elif mat1 + prog1 > mat2 + prog2:
    print('Pobijedio je prvi takmicar.')

else:
    print('Pobijedio je drugi takmicar.')


#Zadatak8
    
prosjek=float(input('Prosjek ucenika: '))

if prosjek==1:
    print('Ucenik ima nedovoljan uspjeh.')
elif prosjek >= 2 and prosjek < 2.5:
    print('Ucenik ima dovoljan uspjeh.')
elif prosjek >= 2.5 and prosjek < 3.5:
    print('Ucenik ima dobar uspjeh')
elif prosjek >= 3.5 and prosjek < 4.5:
    print('Ucenik ima vrlodobar uspjeh.')
else:
    print('Ucenik ima odlican upsjeh.')


#Zadatak9
    
gl_x_z=int(input('gl x koordinata zavjese: '))
gl_y_z=int(input('gl y koordinata zavjese: '))

dd_x_z=int(input('dd x koordinata zavjese: '))
dd_y_z=int(input('dd y koordinata zavjese: '))

gl_x_p=int(input('gl x koordinata prozora: '))
gl_y_p=int(input('gl y koordinata prozora: '))

dd_x_p=int(input('dd x koordinata prozora: '))
dd_y_p=int(input('dd y koordinata prozora: '))



if gl_x_z < gl_x_p and gl_y_z > gl_y_p and dd_x_z > dd_x_p and dd_y_z < dd_y_p:
    print('Zavjesa ce prekriti prozor.')
else:
    print('Zavjesa nece prekriti prozor.')


#Zadatak10
    
import math

x = float(input('X koordinata strelice: '))
y = float(input('Y koordinata strelice: '))

x_centar=float(input('X koordinata centra: '))
y_centar=float(input('Y koordinata centra: '))

r=float(input('Poluprecnik table: '))

if math.sqrt((x-x_centar)**2 + (y-y_centar)**2) < r:
    print('Strelica je pogodila pikado tablu.')
else:
    print('Strelica nije pogodila tablu.')


#Zadatak11
    
x_m=int(input('X koordinata mrava: '))
y_m=int(input('Y koordinata mrava: '))

gd_x=int(input('gd x koordinata stola: '))
gd_y=int(input('gd y koordinata stola: '))

dl_x=int(input('dl x koordinata stola: '))
dl_y=int(input('dl y koordinata stola: '))

if ((x_m==gd_x or x_m==dl_x) and y_m>=dl_y and y_m<=gd_y)  or ((y_m==dl_y or y_m==gd_y) and x_m>=dl_x and x_m<=gd_x):
    print('Mrav se krece po ivici stola.')
else:
    print('Mrav se ne krece po ivici stola.')


#Zadatak12
    
broj=int(input('Dvocifreni broj: '))

if broj//10 > broj%10:
    print(broj//10 - broj%10)

elif broj//10 < broj%10:
    print(broj//10 + broj%10)

else:
    print(print(broj//10 * broj%10))


#Zadatak13
    
import math

r1=float(input('Poluprecnik prvog stola: '))
r2=float(input('Poluprecnik drugog stola: '))

if r1>r2:
    print(math.pow(r1,2)*math.pi)
elif r2>r1:
    print(math.pow(r2,2)*math.pi)
else:
    print(f'Stolovi imaju istu povrsinu koja iznosi: {math.pow(r1,2)*math.pi}')


#Zadatak14
    
a=float(input('Cijena prvog proizvoda: '))
b=float(input('Cijena drugog prozivoda: '))
c=float(input('Cijena treceg prozivoda: '))


if a+b < a+c and a+b < b+c:
    print('a i b')
elif a+c < a+b and a+c < b+c:
    print('a i c')
elif c+b < a+b and c+b < a+c:
    print('c i b')          


#Zadatak15

godina=int(input('Godina: '))

if (godina % 4 ==0 and godina % 100 != 0) or godina % 400 ==0:
    print(f'Godina {godina} je prestupna.')
else:
    print(f'Godina {godina} nije prstupna.')


#Zadatak16

gl_x=int(input('gl x koordinata pravougaonika: '))
gl_y=int(input('gl y koordinata pravougaonika: '))

dd_x=int(input('dd x koordinata pravougaonika: '))
dd_y=int(input('dd y koordinata pravougaonika: '))

x_t=int(input('X koordinata tacke: '))
y_t=int(input('Y koordinata tacke:'))


if dd_x>=x_t>=gl_x and gl_y>=y_t>=dd_y:
    print('Tacka se nalazi unutar pravougaonika.')
else:
    print('Tacka se ne nalazi unutar pravougaonika.')


#Zadatak17
    
a=float(input('Duza stranica pravougaonika: '))
b=float(input('Kraca stranica pravougaonika: '))

if a//b >=2:
    print('Mogu se smjestiti bar dva kvadrata.')
else:
    print('Ne mogu se smjestiti.')


#Zadatak18
    
temp=int(input('Temperatura vode: '))

if 0 < temp < 100:
    print('Tecno')
elif temp < 0:
    print('Cvrsto')
else:
    print('Gasovito')


#Zadatak19
    
skol=float(input('Iznos skolarine: '))
pros=float(input('Prosjecna ocjena: '))
nagrada=int(input('Ima nagradu? '))

if nagrada==1 and pros<4.5:

        skol=skol*0.7

elif pros>=4.5:
    skol=skol*0.6
elif 4.5>pros>=3.5:
      skol=skol*0.8
elif 3.5>pros>=2.5:
      skol=skol*0.9

print(f'Skolarina ovog ucenika iznosi {skol}')


#Zadatak20

n=int(input('Broj: '))

if n%2==0:
    suma=0
    while n>0:
        if (m:=n%10)%2==0:
            suma+=m
        
        n//=10
    print(f'Broj je paran i algoritam vraca: {suma}')
else:
    proizvod=1

    while n>0:
        if (m:=n%10)%2==1:
            proizvod*=n%10

        n//=10
    print(f'Broj je neparan i algoritam vraca: {proizvod}')


#Zadatak21
    
from math import sqrt
x=int(input('Vrijednost x je: '))

if x <= -7:
    y = -2*x+7/2
elif -7<x<1:
    y = (x**2-3*x+5)/(x**2+2)
elif 1<=x<=8:
    y = sqrt(x**2+2*x+2)+sqrt(abs(3/2*x-4/7))
else:
    y=abs(3/x**2-11*x)

print(y)


#Zadatak22

x=int(input('X koordinata: '))
y=int(input('X koordinata: '))

if x>0 and y>0:
    print('Tacka pripada prvom kvadrantu')
elif x>0 and y<0:
    print('Tacka pripada cetvrtom kvadrantu.')
elif x<0 and y>0:
    print('Tacka pripada drugom kvadrantu.')
else:
    print('Tacka pripada trecem kvadrantu')


#Zadatak23
    
from math import sqrt
x=float(input('X koordinata: '))
y=float(input('Y koordinata: '))


if ( x<0 and y>0 and 6>sqrt(x**2+y**2)>4) or (4>x>0 and 4>y>0 and sqrt(x**2+y**2)<4) or (sqrt(x**2+y**2)<4 and y<x-4 and -4<y<0 and 4>x>0) or (6>sqrt(x**2+y**2)>4 and y<x-4 and 6>x>4 and y>0):
    print('Pripada')
else:
    print('Ne pripada')


#Zadatak24
    
string=input('String: ')

if len(string)>30:
    string=string[:30]+'...'

print(string)

#Zadatak25

tring=input('String: ')

string=string[1:-1]

print(string)


#Zadatak26

broj=input('Broj: ')

if broj[0:2] == '0b':
    print('Binarni broj')
elif broj [0:2]=='0o':
    print('Oktalni broj')
elif broj[0:2]=='0x':
    print('Heksadecimalni broj')
else:
    print('Dekadni broj')


#Zadatak27
    
string=input('String: ')

if string.count('a')>0 or string.count('e')>0 or string.count('i')>0 or string.count('o')>0 or string.count('u')>0:
    print('String sadrzi bar jedan samoglasnik.')
else:
    print('String ne sadrzi samoglasnik.')


#Zadatak28
    
string=input('String: ')
target=input('Target: ')

if string[len(string)-len(target):len(string)]==target:
    print('Da')
else:
    print('Ne')


#Zadatak29
    
string=input('String: ')

if string.count('0')+string.count('1')==len(string):
    print('String je binarni')
else:
    print('String nije binarni.')


#Zadatak30
    
n=int(input('Broj: '))

suma=0
proizvod=1
br_par=0
br_nep=0

for i in range(1,n+1):

    if i%2==0:
        br_par+=1
        suma+=i

    else:
        br_nep+=1
        proizvod*=i


print(suma,proizvod)
print(br_par,br_nep)


#Zadatak31

start=int(input('Start: '))
end=int(input('End: '))

suma=0

for i in range(start,end+1):
    if i%2==0 and not i%4==0:
        suma+=i**2

print(suma)


#Zadatak32

a=int(input('Pocetak: '))
b=int(input('Kraj: '))
djelilac=int(input('Djelilac: '))

br=0
suma=0

for i in range(a+1,b):
    if i%djelilac==0:
        br+=1
        suma+=i

print(suma,br)


#Zadatak33

broj=int(input('Broj:'))

suma=0

while broj>0:
    suma+=broj%10
    broj//=10

print(suma)


#Zadatak34

string=input('String: ')

proizvod=1

for i in string:
    if i.isdigit()==True:
        proizvod*=int(i)

print(proizvod)


#Zadatak35

string=input('String: ')

brojevi=''

for i in string:
    if i.isdigit()==True:
        brojevi+=i

brojevi=int(brojevi)
print(brojevi)

#Zadatak36

string=input('String: ')

s=''

for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        s+='1'
    else:
        s+='0'

print(s)


#Zadatak37

string=input('String: ')

zbir=0

for i in string:
    if i=='1':
        zbir+=1
    elif i=='*':
        zbir-=1

if zbir>0:
    print(f'Igrac je u plusu ({zbir})')
elif zbir<0:
    print(f'Igrac je u minusu ({zbir})')
else:
    print('Igrac je na nuli')


#Zadatak38
    
string=input('String: ')

s=''

for i in string:
    if i.isdigit()==True:
        if int(i)%2==0:
            s+='0'
        else:
            s+='1'

print(s)


#Zadatak39

broj=input("Broj: ")

stepen=len(broj)
broj=int(broj)
broj_pom=broj
rezultat=0

while broj_pom>0:
    rezultat+=(broj_pom%10)**stepen
    broj_pom//=10

if rezultat==broj:
    print('Da')
else:
    print('Ne')


#Zadatak40
    
brojevi=input("Brojevi: ")
brojevi=brojevi.split(' ')

suma=0

for i in brojevi:
    if (n:=int(i))<0 and n%2==0:
        suma+=abs(n)

print(suma)

#Zadatak41

brojevi=input("Brojevi: ")
maks=int(input('Broj: '))

lista=[int(i) for i in brojevi.split(' ')]
br=0
for i in lista:
    if i<maks:
        br+=1

print(br)


#Zadatak42

orig_cijene=input('Originalne cijene: ')
popust=input('Popust: ')

orig_cijene=[int(x) for x in orig_cijene.split(' ')]

nove_cijene=[(1-int(popust)/100)*x for x in orig_cijene ]

print(nove_cijene)


#Zadatak43

ocjene=input('Ocjene: ')

ocjene=[int(x) for x in ocjene.split(' ')]

tri=0
cetiri=0
pet=0

for i in ocjene:
    if i==3:
        tri+=1
    elif i==4:
        cetiri+=1
    else:
        pet+=1

print(f'Tri: {tri}')
print(f'Cetiri: {cetiri}')
print(f'Pet: {pet}')


#Zadatak44

posjeta = input('Posjeta: ')

posjeta = [int(i) for i in posjeta.split(' ')]
maks=max(posjeta)

print(maks)


#Zadatak45

plate = input('Plate: ')

plate=[int(i) for i in plate.split(' ')]

prosjecna=sum(plate)/len(plate)
br=0
for i in plate:
    if i>prosjecna:
        br+=1

print(br)


#Zadatak46

late = input('Plate: ')

plate=[int(i) for i in plate.split(' ')]
plate.sort()

print(plate[-2])


#Zadatak47

brojevi = input('Brojevi: ')

brojevi=[int(i) for i in brojevi.split(' ')]
minim=min(brojevi)
maks=max(brojevi)

print(f'{minim} i {maks}')


#Zadatak48

broj = int(input('Broj: '))
stepen=int(input('Stepen: '))

broj2=1

for i in range(1,stepen+1):
    broj2*=broj

print(broj2)


#Zadatak49

string = input('String: ')
broj = int(input('Broj: '))

if broj >= len(string):
    string+='...'
else:
    string=string[:broj]+'...'

print(string)


#Zadatak50

string = input('String: ')


string2=''

for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        string2+=i

print(string2)


#Zadatak51

sifra = input('Sifra (Maksimalno 100 karaktera): ')

vl_slova=0
ml_slova=0
cifre=0

for i in sifra:
    if i.isdigit()==True:
        cifre+=1
    elif i.isalpha()==True:
        if i.isupper()==True:
            vl_slova+=1
        else:
            ml_slova+=1

if cifre>0 and vl_slova>0 and ml_slova>0:
    print('YES')
else:
    print('NO')


#Zadatak52
    
a = input('a: ')
pre = input('pre: ')
suf = input('suf: ')
num=int(input('num: '))

string=''
string=num*pre+a+num*suf

print(string)


#Zadatak53

N=int(input('N: '))

suma=0
br=0

while suma<N:
    br+=1
    suma+=br

print(br)


#Zadatak54

string = input('String: ')
pozicija = int(input('Pozicija: '))

if pozicija == 0:
    if string[1] == '0':
        print('1')
    else:
        print('0')

elif pozicija == len(string)-1:
    if string[-2]=='0':
        print('1')
    else:
        print('0')

else:
    if string[pozicija-1]=='0' and string[pozicija+1]=='0':
        print('1')
    elif string[pozicija-1]=='1' and string[pozicija+1]=='0':
        print('1')
    else:
        print('0')


#Zadatak55
        
h = int(input('Broj molekula vodonika: '))
o = int(input('Broj molekula kiseonika: '))

print(min(h//2,o))


#Zadatak56
string=input('String: ')

brojevi=string.split('-')

negativni = [int(i) for i in brojevi if i.isdigit()]
br=0

for i in negativni:

    if i<10:
        br+=1

print(br)


#Zadatak57

broj = input('Broj: ')

stepen = len(broj)
broj_pom = int(broj)
rezultat = 0

while broj_pom > 0:
    rezultat += (broj_pom % 10) ** stepen
    broj_pom //= 10
    

if int(broj)==rezultat:
    print('Da')
else:
    print('Ne')


#Zadatak58
    
string=input('String: ')

string1=''.join([i for i in string if i.isdigit()==False])

print(string1)


#Zadatak59

s=input('String: ')
s1=''
for i in s:
    if int(i)%2==0:
        s1+='0'
    else:
        s1+='1'

print(s1)


#Zadatak60

start = int(input('Start: '))
end = int(input('Start: '))

rezultat=sum(i**2 for i in range(start,end+1) if i%3==0 and i%6!=0)

print(rezultat)


#Zadatak61

string= input('String: ')

string=string.split('. ')
slova=''
for i in string:
    slova+=i[0]

print(slova)


#Zadatak62

a=input('Brojevi: ')

a=a.split(' ')
br=0

for i in a:
    if i[0:2]=='0x':
        br+=1

print(br)


#Zadatak63

string=input('String: ')

string=string.split(' ')

najduza=''

for i in string:
    if len(i)>len(najduza):
        najduza=i

print(najduza)


#Zadatak64

broj=int(input('Broj: '))

maks=broj%10
minim=broj%10

broj//=10

while broj>0:
    if broj%10>maks:
        maks=broj%10
    elif broj%10<minim:
        minim=broj%10
    
    broj//=10

print(maks+minim)


#Zadatak65

d = float(input('Duzina terase: '))*100
n = int(input('Broj stubica: '))
s = float(input('Sirina stubica u cm: '))

d1 = d - n*s

rastojanje = d1/(n+1)

print(f'Rastojanje je {rastojanje:.2f}')


#Zadatak66

brojevi=input('Brojevi: ')

brojevi=[int(i) for i in brojevi.split(' ')]
dvocifreni=0
trocifreni=0

for i in brojevi:
    if i>=10 and i<=99:
        dvocifreni+=1
    elif i>=100 and i<=999:
        trocifreni+=1

print(f"Dvocifreni: {dvocifreni}, Trocifreni: {trocifreni}")


#Zadatak67

brojevi=input('Brojevi: ')
n=int(input('Broj: '))

ponavljanja=sum(1 for i in brojevi.split(' ') if int(i)==n)

print(ponavljanja)


#Zadatak68

plate=input('Plate: ')
x=int(input('X: '))

plate=[int(i) for i in plate.split(' ')]

srednja= sum(plate)/len(plate)

for i in range(len(plate)):
    if plate[i]>srednja:
        plate[i]+=x

print(srednja)
print(plate)


#Zadatak69

plate=input('Plate: ')

plate=[int(i) for i in plate.split(' ')]

srednja= sum(plate)/len(plate)
br=0

for i in range(len(plate)):

    if plate[i]>srednja:
        plate[i]*=0.9

    elif plate[i]<srednja:
        plate[i]*=1.1

    if plate[i]>srednja:
        br+=1

print(br)


#Zadatak70

lista=input('Lista: ')

rezultat=sum(int(i)**2 for i in lista.split(' ') if int(i)%3==0)

print(rezultat)


#Zadatak71

from math import sqrt
lista=input('Lista: ')

lista=[int(i) for i in lista.split(' ')]
br=0

for i in lista:
    if sqrt(i)%1==0:
        br+=1

print(br)


#Zadatak72

ocjene=input('Ocjene: ')

ocjene=[int(i) for i in ocjene.split(' ')]

prosjek=[i for i in ocjene if ocjene!=5]

prosjek=sum(prosjek)/len(prosjek)
print(prosjek)

br=0
br=sum(1 for i in ocjene if i > prosjek)

print(br)


#Zadatak73

inventar=['mac', ' sesir', 'rukavice']

pozicija=int(input('Pozicija: '))

if pozicija>=len(inventar):
    print('Pozicija izvan opsega')

else:
    print(f' Predmet na poziciji {pozicija} je {inventar[pozicija]}')


#Zadatak74
    
plate_e = input('Plate u eurima: ')

plate_d = [1.1*int(i) for i in plate_e.split(' ')]
prosjecna_vrijednost_d=sum(plate_d)/len(plate_d)

print(prosjecna_vrijednost_d)


#Zadatak75

pocetni_iznosi=input('Pocetni iznosi: ')
kamatna_stopa=int(input('Kamatna stopa: '))

pocetni_iznosi=[float(i) for i in pocetni_iznosi.split(' ')]
ukupni_gubitak=0

for i in pocetni_iznosi:
    ukupni_gubitak += i*kamatna_stopa/100

print(f'Ukupni gubitak banke: {ukupni_gubitak}')


#Zadatak76

lista=input('Lista: ')
element1=int(input('Element1: '))
element2=int(input('Element2: '))

lista=[int(i) for i in lista.split(' ')]

for i in range(len(lista)):
    if lista[i]==element1:
        lista[i]=element2

print(lista)


#Zadatak77

lista=input('Lista: ')

lista=[int(i) for i in lista.split(' ')]

print(lista==sorted(lista))


#Zadatak78

proizvodi={
    'prozivod1':100,
    'prozivod2':300,
    'prozivod3':900,
    'prozivod4':1000,
    'prozivod5':1100,
    'prozivod6':500
}

maks=max(proizvodi.values())
maks2=min(proizvodi.values())

for i in proizvodi.items():
    if i[1]>=maks2 and i[1]<maks:
        maks2=i[1]
        maks2_key=i[0]

print(maks2_key,maks2)


#Zadatak79

lista=input('Lista: ')

lista=[int(i) for i in lista.split(' ')]
br=0

for i in lista:
        if i>0 and -i in lista:
            br+=1

print(br)


#Zadatak80

lista=input('Lista: ')

lista=[float(i) for i in lista.split(' ')]

print(max(lista)-min(lista))


#Zadatak81

cijene=input('cijene: ')

cijene=[float(i) for i in cijene.split(' ')]

maks_rast=0
maks_pad=0

for i in range(len(cijene)-1):

    maks_pad = cijene[i+1] - cijene[i] if cijene[i+1] - cijene[i] < maks_pad else maks_pad
    maks_rast= cijene[i+1]- cijene[i] if cijene[i+1] - cijene[i] >maks_rast else maks_rast

print(maks_pad, maks_rast)


#Zadatak82

lista=input('Slobodna sjedista: ')
n=int(input('Broj osoba: '))

lista=[int(i) for i in lista.split(' ')]

najbolji_red=lista[0]

for i in lista[1:]:
    if i-n>najbolji_red-n:
        najbolji_red=i

print(f'Najbolji red ima {najbolji_red} slobodnih mjesta')


#Zadatak83

cijene=input('Cijene putovanja: ')
budzet=int(input('Budzet: '))

cijene=[int(i) for i in cijene.split(' ')]

odabrana_cijena=0

for i in cijene:
    if i>odabrana_cijena and i<budzet:
        odabrana_cijena=i

print(f'Cijena izabranog putovanja je {odabrana_cijena} i ostaje {budzet-odabrana_cijena} u budzetu')


#Zadatak84

stolovi=input('Kapaciteti stolova: ')
br_gostiju=int(input('Ocekivani broj gostiju: '))

stolovi=[int(i) for i in stolovi.split(' ')]
dodatni_stolovi=(br_gostiju-sum(stolovi))//4 + 1

print(f'Broj potrebnih stolova: {dodatni_stolovi}')


#Zadatak85

slobodna_mjesta=input('Broj slobodnih mjesta po redovima: ')
n=int(input('Broj posjetilaca: '))

slobodna_mjesta=[int(i) for i in slobodna_mjesta.split(' ')]
slobodna_mjesta.sort(reverse=True)

popunjeni_redovi=slobodna_mjesta.copy()

for i in range(len(slobodna_mjesta)):
    popunjeni_redovi_pom=[slobodna_mjesta[i]]
    
    if sum(popunjeni_redovi_pom)>=n and len(popunjeni_redovi_pom)<=len(popunjeni_redovi):
        popunjeni_redovi=popunjeni_redovi_pom.copy()

    for j in range(i+1,len(slobodna_mjesta)):
        popunjeni_redovi_pom.append(slobodna_mjesta[j])
        
        if sum([slobodna_mjesta[i],slobodna_mjesta[j]])>=n and len([slobodna_mjesta[i],slobodna_mjesta[j]])<=len(popunjeni_redovi):
            popunjeni_redovi=[slobodna_mjesta[i],slobodna_mjesta[j]]

        if sum(popunjeni_redovi_pom)>=n and len(popunjeni_redovi_pom)<=len(popunjeni_redovi):
            popunjeni_redovi=popunjeni_redovi_pom.copy()

        if len(popunjeni_redovi_pom)>len(popunjeni_redovi):
            break

print(popunjeni_redovi)


#Zadatak86

def absoulte_of_even_sum(x):
    rezultat=0
    for i in x:
        if i<0 and i%2==0:
            rezultat+=abs(i)

    return rezultat


brojevi=input('Lista: ')

brojevi=[int(i) for i in brojevi.split(' ')]
print(absoulte_of_even_sum(brojevi))


#Zadatak87

def presjek(a,b):

    x=[i for i in a if i in b]
    return x


a=[1,2,'a']
b=['a',2]

print(presjek(a,b))


#Zadatak88

def br_elemenata(lista,maks):

    br=sum(1 for i in lista if i < maks)
    return(br)

lista=input('Lista: ')
maks=int(input('Broj: '))
lista=[int(i) for i in lista.split(' ')]

print(br_elemenata(lista,maks))


#Zadatak89

def br_elemenata(a):
    br=0
    for i in a:
        if i>0 and -i in a:
            br+=1

    return br


a=input('Lista: ')
a=[int(i) for i in a.split(' ')]

print(br_elemenata(a))


#Zadatak90

def update_list(a,x):

    for i in range(len(a)):
        if a[i]%2 == 0:
            a[i] += x
    return a


a=input('Lista: ')
x=int(input('Broj: '))

a=[int(i) for i in a.split(' ')]

print(update_list(a,x))


#Zadatak91

def second_max(a):
    a.sort()
    return a[-2]


a=input('Lista: ')

a=[int(i) for i in a.split(' ')]

print(second_max(a))


#Zadatak92

def spisak_proizvoda(n):

    lista=[]
    for i in range(n):
        naziv_proizvoda=input('Naziv proizvoda: ')
        opis=input('Opis: ')
        cijena=float(input('Cijena proizvoda: '))
        broj_artikala=int(input('Broj artikala: '))
        
        proizvod={'naziv_proizvoda' : naziv_proizvoda,
                  'opis' : opis,
                  'cijena' : cijena,
                  'broja artikala': broj_artikala}
        
        lista.append(proizvod)
  
        
    return lista

def search_term(spisak_proizvoda, n):

    trazeni_proizvodi=[]
    for i in spisak_proizvoda:
        if i['naziv_proizvoda'][0]==n:
            trazeni_proizvodi.append(i)

    return trazeni_proizvodi



proizvodi=spisak_proizvoda(3)
print(proizvodi)
print(search_term(proizvodi,'p'))


#Zadatak93

def odabir(lista_igrica,x,y):

    odabrane=[i for i in lista_igrica if i['ocjena']>x and i['izdavac']==y]

    return(odabrane)


broj_igrica=int(input('Broj_igrica: '))
lista_igrica=[]
for i in range(broj_igrica):
    ime=input('Ime: ')
    izdavac=input('Izdavac: ')
    godina_izlaska=int(input('Godina izlaska: '))
    ocjena=float(input('Ocjena: '))

    igrica={'ime':ime,
            'izdavac':izdavac,
            'godina izlaska': godina_izlaska,
            'ocjena':ocjena}
    
    lista_igrica.append(igrica)

ocjena=float(input('Trazena ocjena: '))
izdavac=input('Trazeni izdavac: ')

print(odabir(lista_igrica,ocjena, izdavac))


#Zadatak94

def get_ewfbyr(string,slovo):
    string=string.split(' ')
    string1=[]
    for i in string:
        if len(i)%2==0 and slovo not in i:
            string1.append(i)

    return string1


string=input('String: ')
slovo=input('Slovo: ')

print(get_ewfbyr(string,slovo))


#Zadatak95

def longest_increasing(lista):

    podlista=[]
    for i in range(len(lista)-1):

        if lista[i]>0:
            podlista_pom=[lista[i]]
            j=i+1
            while lista[j]>0 and lista[j]>=lista[j-1] and j<len(lista):
                podlista_pom.append(lista[j])
                j+=1
            if len(podlista_pom)>len(podlista):
                podlista=podlista_pom
        
    return(podlista)


lista=input('Lista: ')

lista=[int(i) for i in lista.split(' ')]
print(longest_increasing(lista))


#Zadatak96

def split_string(string,n):

    i=0
    lista=[]

    while i<len(string):

        if i+n-1<=len(string)-1:
            lista.append(string[i:i+n])
        else:
            print(i)
            print(i+n)
            print(len(string))
            print(i+n-1-len(string)-1)
            lista.append(string[i:len(string)]+(i+n-1-(len(string)-1))*'*')
            
        i+=n
    return (lista)

string=input('String: ')
n=int(input('Broj: '))

print(split_string(string,n))


#Zadatak97

def spisak_proizvoda(n):

    lista=[]
    for i in range(n):
        naziv_proizvoda=input('Naziv proizvoda: ')
        opis=input('Opis: ')
        cijena=float(input('Cijena proizvoda: '))
        broj_artikala=int(input('Broj artikala: '))
        
        proizvod={'naziv_proizvoda' : naziv_proizvoda,
                  'opis' : opis,
                  'cijena' : cijena,
                  'broj artikala': broj_artikala}
        
        lista.append(proizvod)
  
        
    return lista


def kupovina(lista, naziv_proizvoda, raspolozivi_novac):

    for i in lista:
        if i['naziv_proizvoda']==naziv_proizvoda:

            if raspolozivi_novac//i['cijena']>0 and raspolozivi_novac//i['cijena'] <= i['broj artikala']:
                return(raspolozivi_novac//i['cijena'])
            
            elif raspolozivi_novac//i['cijena']==0:
                return('Kupac nema novca da kupi ni jedan artikal')
        
            elif raspolozivi_novac//i['cijena'] > i['broj artikala']:
                return(f'Korisnik ne moze kupiti vise od {i['broj artikala']} artikala')
        
            break
        
n=int(input('Broj proizvoda: '))
zeljeni_proizvod=input('Ime zeljenog proizvoda: ')
raspolozivi_novac=int(input('Raspolozivi_novac: '))


print(kupovina(spisak_proizvoda(n), zeljeni_proizvod, raspolozivi_novac))


#Zadatak98

zahtjev=input('Zahtjev: ')

zahtjev=zahtjev.split(',')
b=0
s=0

for i in zahtjev:

    i=i.split(' ')
    if i[3]=='B':
        b+=int(i[1])*float(i[2])
    else:
        s+=int(i[1])*float(i[2])

print(f'Buy: {b:.2f} Sell: {s:.2f}')


#Zadatak99

def split_string(string,n):
    lista=[]

    i=0

    while i<len(string):

        if i+n-1<len(string)-1:
            lista.append(string[i:i+n])

        else:
            lista.append(string[i:len(string)])

        i+=n

    return(lista)


string=input('String: ')
broj=int(input('Broj: '))

print(split_string(string,broj))


#Zadatak100

def password_validator(string, n, flagUpper=False, flagLower=False, flagDigit=False):

    if len(string)>=n and flagUpper==True and flagLower==True and flagDigit==True:
        return True
    else:
        return False
    

passwrd=input('Password: ')
n=int(input('Trazena duzina: '))

print(password_validator(passwrd,n, any(i.isupper() for i in passwrd), any(i.islower() for i in passwrd), any(i.isdigit() for i in passwrd)))


#Zadatak101

vrijeme=input('Vrijeme: ')

vrijeme=[int(i) for i in vrijeme.split(':')]

if vrijeme[1]== 0 and vrijeme[0]>=6:
    print(10)
elif vrijeme[0]<6:
    if 6*60-vrijeme[0]*60-vrijeme[1]-5 >=0:
        print(6*60-vrijeme[0]*60-vrijeme[1]-5)
    else:
        print(6*60-vrijeme[0]*60-vrijeme[1]-5+15)
else:
    
    if  15*(vrijeme[1]//15+1)-vrijeme[1]>=5 or vrijeme[1]%15==0:
        print(15*(vrijeme[1]//15+1)-5-vrijeme[1])
    else: 
        print(15*(vrijeme[1]//15+1+1)-5-vrijeme[1])


#Zadatak102

N=int(input('Broj ucenika: '))

lista=[0]*N

for i in range(N):
  
    for j in range(0+i,N,i+1):
    
        if lista[j]==1:
            lista[j]=0
        else:
            lista[j]=1

print(lista)
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


    

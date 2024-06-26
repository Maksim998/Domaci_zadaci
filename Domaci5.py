#Zadatak1

import pandas
from matplotlib import pyplot

def odredjivanje_korelacije(dataset_pom2):
    columns_names = dataset_pom2.columns.tolist()
    kor_poz=0
    kor_neg=0
    kor_poz_kolone=()
    kor_neg_kolone=()

    for i in range(len(columns_names)-1):

        if (n:=dataset_pom2[columns_names[i]].corr(dataset_pom2[columns_names[i+1]])) > kor_poz:
            kor_poz = n
            kor_poz_kolone = columns_names[i], columns_names[i+1],kor_poz
        
        elif (n:=dataset_pom2[columns_names[i]].corr(dataset_pom2[columns_names[i+1]])) < kor_neg:
            kor_neg = n
            kor_neg_kolone = columns_names[i], columns_names[i+1], kor_neg

    return kor_neg_kolone, kor_poz_kolone




dataset = pandas.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')
kolona = input('Zeljena kolona (Age, Height, Weight, FCVC, NCP): ')

print(dataset['Age'].corr(dataset['Height']))

maks = max(dataset[kolona])
minim = min(dataset[kolona])
print('Minimalna i maksimalna vrijednost tražene kolone: ',minim, ', ',maks)

srednja_vrijednost = sum(dataset[kolona]/len(dataset[kolona]))
print('Srednja vrijednost tražene kolone: ', srednja_vrijednost)

procentualna_razlika= (maks- srednja_vrijednost)/maks*100
print('Procentualna razlika: ', procentualna_razlika)

dataset_pom =dataset.copy()
dataset_pom[kolona] = dataset[kolona]/maks
dataset_pom.to_csv('ObesityDataSet_raw_and_data_sinthetic_normalizovano.csv', index= False)


dataset_pom2 = dataset[['Age', 'Height', 'Weight', 'FCVC','NCP']]
dataset_pom_devijacija = dataset_pom2.std()
print('Standardna devijacija kolona:\n', dataset_pom_devijacija)


print('Najveća negativna i pozitivna korlacija su između kolona: ', odredjivanje_korelacije(dataset_pom2) )


fig1,ax1 = pyplot.subplots()
ax1.hist(dataset['Age'], bins=6)
ax1.set_title('Raspodjela vrijednosti u koloni Age')
ax1.set_ylabel('Učestalost')
ax1.set_xlabel("Vrijednosti")

fig2,ax2 = pyplot.subplots()
ax2.hist(dataset['Height'], bins=6)
ax2.set_title('Raspodjela vrijednosti u koloni Height')
ax2.set_ylabel('Učestalost')
ax2.set_xlabel("Vrijednosti")

fig3,ax3 = pyplot.subplots()
ax3.hist(dataset['Weight'], bins=7)
ax3.set_title('Raspodjela vrijednosti u koloni Weight')
ax3.set_ylabel('Učestalost')
ax3.set_xlabel("Vrijednosti")

fig4,ax4 = pyplot.subplots()
ax4.hist(dataset['FCVC'], bins=8)
ax4.set_title('Raspodjela vrijednosti u koloni FCVC')
ax4.set_ylabel('Učestalost')
ax4.set_xlabel("Vrijednosti")

fig5,ax5 = pyplot.subplots()
ax5.hist(dataset['NCP'], bins=6)
ax5.set_title('Raspodjela vrijednosti u koloni NCP')
ax5.set_ylabel('Učestalost')
ax5.set_xlabel("Vrijednosti")

pyplot.show()


#Zadatak2

import requests
import bs4
import pandas
from datetime import datetime
import time

#Pretrazivanje kuca na prodaju u Kotoru
k=0
links = []


while True:

    #res = requests.get(f'https://www.realitica.com/?cur_page={k}&for=Prodaja&opa=Kotor&type%5B%5D=Home&since-day=p-anytime&qob=p-default&lng=hr')
    url = f'https://www.realitica.com/?cur_page={k}&for=Prodaja&opa=Kotor&cty%5B%5D=Dobrota&type%5B%5D=Home&since-day=p-anytime&qob=p-default&lng=hr'
   
    res = requests.get(url)
    k += 1
    
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    soup = soup.find_all('div', class_ = 'thumb_div')

    if len(soup)== 0:
        break

    for i in soup:
        links.append(i.find('a').get('href'))
    time.sleep(1)



vrsta = []
podrucje = []
lokacija = []
broj_spavacih_soba = []
broj_kupatila = []
cijena = []
stambena_povrsina = []
parking_mjesta = []
od_mora = []
novogradnja = []
klima = []
naslov = []
opis = []
web_stranica = []
oglasio = []
mobilni = []
id_oglasa = []
zadnja_promjena = []
slike = []



for i in links:
    #Kao dva primjera su data stan i kuca/ naknadno dodati ostale
    print(i)
    res = requests.get(i)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    listing_body = soup.find('div', id='listing_body')


    if (listing_body.find('strong', string='Vrsta').next_sibling.split(' ')[2]).lower()== 'kuću':
        vrsta.append('Kuća')
    elif (listing_body.find('strong', string='Vrsta').next_sibling.split(' ')[2]).lower() == 'stan':
        vrsta.append('Stan')

    podrucje.append(listing_body.find('strong', string='Područje').next_sibling.split(' ')[1])

    lokacija.append(listing_body.find('strong', string='Lokacija').next_sibling.split(' ')[1])

    try:
        broj_spavacih_soba.append(int(listing_body.find('strong', string='Spavaćih Soba').next_sibling.split(' ')[1]))
    except:
        broj_spavacih_soba.append('Nije navedeno')

    try:
        broj_kupatila.append(int(listing_body.find('strong', string='Kupatila').next_sibling.split(' ')[1]))
    except:
        broj_kupatila.append('Nije navedeno')

    try: 
        cijena.append(float(listing_body.find('strong', string = 'Cijena').next_sibling.split('€')[1].replace('.','')))
        print(cijena)
    except:
        cijena.append('Nije navedena')

    try:
        stambena_povrsina.append(f'{listing_body.find('strong', string = 'Stambena Površina').next_sibling.split(' ')[1]} m\u00B2')
    except:
        stambena_povrsina.append('Nije navedeno')


    try:
        parking_mjesta.append(int(listing_body.find('strong', string = 'Parking Mjesta').next_sibling.split(' ')[1]))
    except:
        parking_mjesta.append('Nije navedeno')

    try:
        od_mora.append(f'{listing_body.find('strong', string = 'Stambena Površin').next_sibling.split(' ')[1]} m')
    except:
        od_mora.append('Nije navedeno')

    novogradnja.append(True if listing_body.find('strong', string='Novogradnja') else False)

    klima.append(True if listing_body.find('strong', string='Klima Uređaj') else False)

    naslov.append(listing_body.find('h2').text)



    opis_tag = listing_body.find('strong', string = 'Opis')

    if opis_tag:
        next_element = opis_tag
        pom=[]
        while next_element:

            if isinstance(next_element.next_sibling,str):
                pom.append(next_element.next_sibling.strip())
            
            next_element = next_element.find_next_sibling()
        pom = ''.join([elem for elem in pom])
        pom = pom.lstrip(': ')
        opis.append(pom)
    else:
        opis.append('Nema opisa')    


    try:
        web_stranica.append(listing_body.find('strong', string = 'Više detalja na').next_sibling.next_sibling.get('href'))

    except:
        web_stranica.append('Nema web stranicu')

    try:
        oglasio.append(listing_body.find('strong', string = 'Oglasio').next_sibling.next_element.text)
    except:
        oglasio.append('Nije navedeno')
    try:
        mobilni.append(listing_body.find('strong', string = 'Mobitel').next_sibling.split(': ')[1])
    except:
        mobilni.append('Nije navedeno')

    id_oglasa.append(listing_body.find('strong', string = 'Oglas Broj').next_sibling.split(': ')[1])

    zadnja_promjena.append(str(datetime.strptime(listing_body.find('strong', string = 'Zadnja Promjena').next_sibling.split(': ')[1].strip(),'%d %b, %Y').date()))

    galerija = soup.find('div', id = 'rea_blueimp').find_all('a')
    slike_pom = []
    for i in galerija:
        slike_pom.append(i.get('href'))

    slike.append(slike_pom)


    time.sleep(1)


df = pandas.DataFrame({'Vrsta': vrsta, 'Podrucje': podrucje, 'Lokacija':lokacija, 'Broj spavacih soba': broj_spavacih_soba, 'Broj kupatila': broj_kupatila, 'Cijena':cijena, 'Stambena povrsina':stambena_povrsina, 'Parking mjesta':parking_mjesta,
                       'Udaljenost od mora': od_mora, 'Novogradnja': novogradnja, 'Klima uređaj': klima, 'Naslov oglasa': naslov, 'Opis': opis, 'Web stranica': web_stranica, 'Oglasio': oglasio,
                       'Mobilni telefon': mobilni, 'ID oglasa': id_oglasa, 'Posljednja promjena oglasa':zadnja_promjena, 'Slike':slike, 'Linkovi':links})

df.to_csv('Scraping_Realitica.csv', index= False)


#Zadatak3

import json
import pandas


def pretraga_clanaka(myfile,naslov):
    for i in myfile["data"]["articles"]:
        if i['title'] == naslov:
            return i
    return 'Ne postoji trazeni clanak'


def dodavanje_komentara(myfile, clanak, title, description, author = 'anonim'):
    
    if (n:=pretraga_clanaka(myfile, clanak)) == 'Ne postoji trazeni clanak':
       print ('Ne postoji trazeni clanak, komentar nije dodat')
    else:
        myfile['data']['articles'].index(n)
        n['comments'].append({'title': title, 'author':author, 'description':description})

        print ('Komentar uspjesno dodat')


def uklanjanje_clanka(myfile, komentar):

    for i in myfile['data']['articles']:
        for j in i['comments']:
            if j['title'] == komentar:
                myfile['data']['articles'].remove(i)
                print('Clanak uspjesno uklonjen')
                break
    print('Clanak nije uklonjen, navedeni komentar ne postoji')


def zadati_clanak_zadati_komentar(myfile, clanak, komentar):

    for i in myfile['data']['articles']:
        if i['title']== clanak:
            for j in i['comments']:
                if j['title'] == komentar:
                    return j
                
    return('Nije pronadjen trazeni clanak')


def return_komentari_zadati_autor(myfile, autor):
    komentari = []
    for i in myfile['data']['articles']:
        for j in i['comments']:
            if j['author'] == autor:
                komentari.append(j)

    if len(komentari) == 0:
        return 'Ne postoji ni jedan komentar sa ovim autorom'
    
    else:
        return komentari


def return_clanci_zadati_autor(myfile, autor):
    clanci = []
    for i in myfile['data']['articles']:
        if i['author'] == autor:
            clanci.append(i)

    if len(clanci) == 0:
        return('Ne postoji clanak sa ovim autorom')
    else:
        return clanci
    

def upisivanje_u_csv(clanci_po_autoru):
    clanci_po_autoru.sort(key= lambda x: len(x['comments']), reverse= True)
    df = pandas.DataFrame(clanci_po_autoru)
    df.to_csv('Clanci trazenog autora, sortirani.csv', index=False)

def upisivanje_u_json(clanci_po_autoru):
    clanci_po_autoru.sort(key= lambda x: x['views'], reverse= True)
    with open('json_fajl_sortirano_po_autorima.json', 'w') as file:
        json.dump(clanci_po_autoru, file, indent=True)


with open('Domaci5_json.json', 'r') as myfile:
    myfile = json.load(myfile)

naslov = input('Trazeni naslov: ')
print(pretraga_clanaka(myfile, naslov))

dodavanje_komentara(myfile, 'The World\'s Most Influential Cities', 'Naslov komentara','Proba')
uklanjanje_clanka(myfile, "Bravo!")

print(json.dumps(myfile, indent=True))


print(zadati_clanak_zadati_komentar(myfile, 'Apple is Listening 2', 'Nice'))
komentari_po_autoru = return_komentari_zadati_autor(myfile, 'anonim')

clanci_po_autoru = return_clanci_zadati_autor(myfile, 'Marco Arment')

upisivanje_u_csv(clanci_po_autoru)
upisivanje_u_json(clanci_po_autoru)
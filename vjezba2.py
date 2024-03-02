broj=input('Sestocifreni broj: ')

a=int(broj[0])*int(broj[2])+2+int(broj[-1])
b=int(broj[1])+int(broj[3])*int(broj[-2])

print(a==b)

import random
def switch(v): yield lambda *c: v in c

V={
  'a': "Xavier",
  'b': "Ivan",
  'c': "Vladimir",
  'd': "Alexei",
  'e': "Dimitri",

  't': "El objeto Tuberia",
  'u': "El objeto Cuchillo",
  'n': "El objeto Navaja",
  'r': "El objeto Armonica",
  'p': "El objeto Pica hielo",

  '1': "Nivel 1",
  '2': "Nivel 2",
  '3': "Nivel 3",
  '4': "Nivel 4",
  '5': "Nivel 5"
}
l1 = ['a','b','c','d','e']
l2 = ['t','u','n','r','p']
l3 = ['1','2','3','4','5']
storys=[]

Vr={}
y=4
for j in range(5):
    Sx={}
    x1=l1[random.randint(0,y)];
    x2=l2[random.randint(0,y)];
    x3=l3[random.randint(0,y)];

    l = V.get(x1)
    ll = V.get(x2)
    lll = V.get(x3)

    Sx.update({x1:l+" fue detectado en su celda"})
    Sx.update({x2:ll+" fue detectado en el area central"})
    Sx.update({x3:lll+ " el estatus electrico y/o segurdia: OK"})
    
    if y==4:
        Sx.update({x1:l+" NO fue detectado en su celda"})

        Vr.update({x1:l})
    if y==3:
        Sx.update({x2:ll+" NO fue detectado en el area central"})
    
        Vr.update({x2:ll})
    if y==2:
        Sx.update({x3:lll+ " el estatus electrico y/o segurdia: OFF"})

        Vr.update({x3:lll})

    l1.remove(x1)
    l2.remove(x2)
    l3.remove(x3)

    storys.append(Sx)
    y-=1
    
Vr_L=list(Vr.keys())

print("Un gulag en siberia tuvo un falla en su sistema de seguridad.")
print("Y debido a eso una celda se abrio por lo que un reo al intetar escapar mato un guardia,")
print("al no enctotrar salida regreseso a su repectiva celda.\n")
print("Por lo que debes descubir quien fue el asesino.\n")
print("A continuacion podras recuperar informacion del sistema de seguridad sobre lo sucedido.")
print("\nSolo podras acceder 5 veces a la informacion guardada, buena suerte.")

print("\n Selecione una seccion: \n 1.Reos \n 2.Armas \n 3.Lugares\n")

vez=0
while vez<5:
    print("\n Selecione una seccion: \n 1.Reos \n 2.Armas \n 3.Lugares\n")
    op=input()
    for case in switch(op):
        
        if case('1'):
            print("Selecione reo: \n 1.Xavier \n 2.Ivan \n 3.Vladimir \n 4.Alexei \n 5.Dimitri")
            op=input()
            for case in switch(op):
                if case('1'):
                    rr= next((index for (index, d) in enumerate(storys) if 'a' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))
                    vez+=1 
                    break
                if case('2'):
                    rr= next((index for (index, d) in enumerate(storys) if 'b' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('3'):
                    rr= next((index for (index, d) in enumerate(storys) if 'c' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('4'):
                    rr= next((index for (index, d) in enumerate(storys) if 'd' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('5'):
                    rr= next((index for (index, d) in enumerate(storys) if 'e' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break        
            break

        if case('2'):
            print("Selecione el arma: \n 1.Tuberia \n 2.Cuchillo \n 3.Navaja \n 4.Armonica \n 5.Pica hielo")
            op=input()
            for case in switch(op):
                if case('1'):
                    rr= next((index for (index, d) in enumerate(storys) if 't' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))
                    vez+=1 
                    break
                if case('2'):
                    rr= next((index for (index, d) in enumerate(storys) if 'u' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('3'):
                    rr= next((index for (index, d) in enumerate(storys) if 'n' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('4'):
                    rr= next((index for (index, d) in enumerate(storys) if 'r' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('5'):
                    rr= next((index for (index, d) in enumerate(storys) if 'p' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break        
            break

        if case('3'):
            print("Selecione el lugar: \n 1.Nivel 1 \n 2.Nivel 2 \n 3.Nivel 3 \n 4.Nivel 4 \n 5.Nivel 5")
            op=input()
            for case in switch(op):
                if case('1'):
                    rr= next((index for (index, d) in enumerate(storys) if '1' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))
                    vez+=1 
                    break
                if case('2'):
                    rr= next((index for (index, d) in enumerate(storys) if '2' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('3'):
                    rr= next((index for (index, d) in enumerate(storys) if '3' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('4'):
                    rr= next((index for (index, d) in enumerate(storys) if '4' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
                if case('5'):
                    rr= next((index for (index, d) in enumerate(storys) if '5' in d), None)
                    print('\n'.join("{}".format(k) for k in storys[rr].values()))    
                    vez+=1 
                    break
            break            
            
        
    else:
        print("\nDato incorrecto\n Selecione una seccion: \n 1.Reos \n 2.Armas \n 3.Lugares")
        op=input()



print("\nSelecione al culpable: \n 1.Xavier \n 2.Ivan \n 3.Vladimir \n 4.Alexei \n 5.Dimitri")
Vt=[]

o=input()
for case in switch(o):
    

    if case('1'):
        Vt.append('a')
        break

    if case('2'):
        Vt.append('b')
        break

    if case('3'):
        Vt.append('c')
        break

    if case('4'):
        Vt.append('d')
        break

    if case('5'):
        Vt.append('e')
        break
else:
    print("\nDato incorrecto \nSelecione reo: \n 1.Xavier \n 2.Ivan \n 3.Vladimir \n 4.Alexei \n 5.Dimitri")
    o=input()

print("Selecione el arma: \n 1.Tuberia \n 2.Cuchillo \n 3.Navaja \n 4.Armonica \n 5.Pica hielo")

o=input()
for case in switch(o):
    if case('1'):
        Vt.append('t')
        break

    if case('2'):
        Vt.append('u')
        break
    if case('3'):
        Vt.append('n')
        break

    if case('4'):
        Vt.append('r')
        break

    if case('5'):
        Vt.append('p')
        break
else:
    print("\nDato incorrecto \nSelecione el arma: \n 1.Tuberia \n 2.Cuchillo \n 3.Navaja \n 4.Armonica \n 5.Pica hielo")
    o=input()

print("\nSelecione el lugar: \n 1.Nivel 1 \n 2.Nivel 2 \n 3.Nivel 3 \n 4.Nivel 4 \n 5.Nivel 5")

o=input()
for case in switch(o):
    if case('1'):
        Vt.append('1')
        break
    
    if case('2'):
        Vt.append('2')
        break
    
    if case('3'):
        Vt.append('3')
        break
    
    if case('4'):
        Vt.append('4')
        break
    
    if case('5'):
        Vt.append('5')
        break
else:
    print("\nDato incorrecto \nSelecione el lugar: \n 1.Nivel 1 \n 2.Nivel 2 \n 3.Nivel 3 \n 4.Nivel 4 \n 5.Nivel 5")
    o=input()


m=2

for z in Vr_L:
    if m==2:
        if z==Vt[0]:
            print("\nCorrecto: "+Vr.get(z)+" era el asesino\n")
        else:
        	print("\nIncorrecto: "+Vr.get(z)+" era el asesino\n")
    
    if m==1:
        if z==Vt[1]:
            print("\nCorrecto: "+Vr.get(z)+" era el arma\n")
        else:
        	print("\nIncorrecto: "+Vr.get(z)+" era el arma\n")
    
    
    if m==0:
        if z==Vt[2]:
            print("\nCorrecto: era el nivel"+Vr.get(z))
        else:
        	print("\nIncorrecto: era el "+Vr.get(z))
    m-=1
 


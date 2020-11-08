file = open("sonad.txt", "r")
read = file.readlines()
import random
random.shuffle(read)
hea=0
kesk=0
halb=0
uuesti = []
while len(uuesti)+len(read):
    vast="tyhi"
    try:
        r = random.choice(read+uuesti)
        if r in read:
            read.remove(r)
        else:
            uuesti.remove(r)
        r = r.strip()
        [kys, vast] = r.split(":")
        print (kys)
        l = vast.split(";")
        v = []
        if len(l)==1:
            v.append(input("Vaste: "))
        elif len(l)==2:
            v.append(input("Nom: "))
            v.append(input("Gen: "))
        else:
            v.append(input("M: "))
            v.append(input("F: "))
            v.append(input("N: "))
        sv = -1
        if len(l[-1].split("-"))==2:
            s = input("Sugu: ")
            sv = l[-1].split("-")[1]
            l[-1] = l[-1].split("-")[0]
        oige=0
        vaar=0
        for i in range(len(v)):
            if v[i]==l[i]:
                oige+=1
            else:
                vaar+=1
        if oige==0:
            halb+=1
            uuesti.append(r)
            print("Vale, skoor %d/%d/%d, %d+%d veel"%(hea,kesk,halb,len(read),len(uuesti)))
        elif vaar==0:
            hea+=1
            print("Hea, skoor %d/%d/%d, %d+%d veel"%(hea,kesk,halb,len(read),len(uuesti)))
        else:
            kesk+=1
            uuesti.append(r)
            print("Peaaegu, skoor %d/%d/%d, %d+%d veel"%(hea,kesk,halb,len(read),len(uuesti)))
    except:
        print("Oopsie woopsie, viga failis")
    print("Peaks olema: "+vast)
    print()
import math
import sys

def feladat_1(n):
    osztok=[n]
    for i in range(1,int(n/2)+1):
        if n%i==0:
            osztok.append(i)
    if n<0 or n!=int(n):
        print("Nem megfelelő szám")
    elif len(osztok)==4:
        return True
    else:
        return False

def feladat_2(n):
    primek=[]
    k=2
    while k!=0:
        oszto_db=1
        for i in range(1,int(k/2)+1):
            if k%i==0:
                oszto_db=oszto_db+1
        if oszto_db==2:
            primek.append(k)
        if len(primek)==n:
            k=0
        else:
            k=k+1
            oszto_db=1
    return primek[-1]

def feladat_3(n):
    k=1
    while k!=0:
        i=2**k
        k=k+1
        if i>=n:
            return i

def feladat_4():
    li=[]
    for i in range(100,1000):
        kulonbozo=[]
        első_szjegy=i//100
        masodik_szjegy=(i%100)//10
        harmadik_szjegy=i%10
        kulonbozo.append(első_szjegy)
        if masodik_szjegy not in kulonbozo:
            kulonbozo.append(masodik_szjegy)
        if harmadik_szjegy not in kulonbozo:
            kulonbozo.append(harmadik_szjegy)
        if len(kulonbozo)==3:
            li.append(i)
    print(li)

def feladat_5(n):
    eredmeny=[]
    max_oszto=0
    for i in range(1,n+1):
        oszto_db=1
        for j in range(1,n+1):
            if i%j==0:
                oszto_db=oszto_db+1
        if oszto_db>max_oszto:
            eredmeny.append(i)
            max_oszto=oszto_db
    print(eredmeny)

def feladat_6(a,b):
    kozos=0
    a_szamjegyek=[]
    b_szamjegyek=[]
    while a > 0:
        szamjegy_a=a%10
        if szamjegy_a not in a_szamjegyek:
            a_szamjegyek.append(szamjegy_a)
        a=a//10
    while b>0:
        szamjegy_b = b % 10
        if szamjegy_b not in b_szamjegyek:
            b_szamjegyek.append(szamjegy_b)
        b = b // 10
    for i in a_szamjegyek:
        if i in b_szamjegyek:
            kozos=kozos+1
    if kozos>=2:
        return "Rokonok"
    else:
        return "Nem rokonok"

def feladat_7(a,b):
    kozos=0
    a_szamjegyek=[]
    b_szamjegyek=[]
    while a > 0:
        szamjegy_a=a%10
        if szamjegy_a not in a_szamjegyek:
            a_szamjegyek.append(szamjegy_a)
        a=a//10
    while b>0:
        szamjegy_b = b % 10
        if szamjegy_b not in b_szamjegyek:
            b_szamjegyek.append(szamjegy_b)
        b = b // 10
    for i in a_szamjegyek:
        if i in b_szamjegyek:
            kozos=kozos+1
    if kozos>=1:
        return "Barátok"
    else:
        return "Nem barátok"

def feladat_8(n):
    s=1
    db=1
    while s<n:
        s=s+1+db
        db=db+1
    return db

def feladat_9():
    m=1
    perc=0
    k=1
    while m<300:
        m=m+m*(1/(1+k))
        k=k+1
        perc=perc+1
    return perc

def feladat_10():
    try:
        fajl1=open("be.txt", mode="r")
        max_hossz=-math.inf
        for sor in fajl1:
            sor=sor.strip()
            hossz=len(sor)
            if sor[0].isupper() and hossz>max_hossz:
                max_hossz=hossz
        print(max_hossz)
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_11():
    try:
        fajl1=open("be.txt", mode="r")
        max_hossz=-math.inf
        abc="aábcdeéfghiíjklmnopqrstuúüűvwxyz"
        for sor in fajl1:
            sor=sor.strip()
            hossz=len(sor)
            if sor[-1] not in abc and hossz>max_hossz:
                max_hossz=hossz
        print(max_hossz)
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_12():
    try:
        fajl1=open("be.txt", mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajl1:
            db=int(sor[-1])
            egyforma=1
            for i in range(1,len(sor)-1):
                if sor[i]==sor[i+1]:
                    egyforma=egyforma+1
        if egyforma>=db:
            fajl2.write("True")
        else:
            fajl2.write("False")
        fajl1.close()
        fajl2.close()
    except Exception as e:
        print(e)

def feladat_13():
    try:
        fajl1=open("be.txt",mode="r")
        db=0
        hossz=0
        for sor in fajl1:
            for k in sor:
                hossz=hossz+1
        for i in range(hossz-1):
            for j in range(i+1,i+2):
                if abs(int(sor[i])-int(sor[j]))<=int(sor[-1]):
                    db=db+1
        print(db)
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_14():
    try:
        fajl1 = open("be.txt", mode="r", encoding="utf-8")
        fajl2 = open("ki.txt", mode="w", encoding="utf-8")
        for sor in fajl1:
            sor = sor.strip()
            max_hossz = 0
            border1 = []
            border2 = []
            k = 1
            for i in range(0, len(sor)):
                border1.append(sor[0:i])
            for j in range(k, len(sor) + 1):
                border2.append(sor[k:len(sor)])
                k = k + 1
            for k in range(0, len(border1)):
                for t in range(0, len(border2)):
                    if border1[k] == border2[t] and len(border1[k]) > max_hossz:
                        max_hossz = len(border1[k])
            fajl2.write(str(max_hossz))
            fajl2.write("\n")
        fajl1.close()
        fajl2.close()
    except Exception as e:
        print(e)
def feladat_15():
    try:
        fajl1=open("be.txt", mode="r")
        fajl2=open("ki.txt", mode="w")
        for sor in fajl1:
            if sor!="\n":
                sor=sor.strip()
                fajl2.write(sor)
                fajl2.write("\n")
            else:
                break
        fajl1.close()
        fajl2.close()
    except Exception as e:
        print(e)

def feladat_16():
    try:
        fajll=open("be.txt", mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajll:
            sor=sor.strip()
            nagy=True
            szavak=sor.split(" ")
            for szo in szavak:
                if szo[0].islower():
                    nagy=False
            if nagy:
                fajl2.write(sor)
                return
        fajl1.close()
        fajl2.close()
    except Exception as e:
        print(e)

def feladat_17():
    try:
        fajl1=open("be.txt",mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajl1:
            sor=sor.strip()
            szavak=sor.split(" ")
            for i in szavak:
                if i.islower():
                    fajl2.write(i)
                    return
        fajl.close()
        fajl2.close()
    except Exception as e:
        print(e)


def feladat_18():
    try:
        fajl1=open("be.txt", mode="r")
        csapat1=""
        csapat2=""
        gyozelmek1=0
        gyozelmek2=0
        gyoztesek=[]
        sor_szam=0
        for sor in fajl1:
            sor_szam+=1
            sor=sor.strip()
            lista=sor.split(" ")
            if sor_szam==1:
                csapat1=lista[0]
                csapat2=lista[2]
            eredmenyek=lista[-1].split(":")
            if int(eredmenyek[0])>int(eredmenyek[1]):
                gyoztesek.append(lista[0])
            else:
                gyoztesek.append(lista[2])
        for i in range(len(gyoztesek)):
            if gyoztesek[i]==csapat1:
                gyozelmek1+=1
            else:
                gyozelmek2+=1
        if gyozelmek1>gyozelmek2:
            print(csapat1)
        else:
            print(csapat2)
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_19():
    try:
        fajl1=open("be.txt", mode="r", encoding="utf-8")
        legtobb_szam=0
        legjobb_oldal=""
        for sor in fajl1:
            sor=sor.strip()
            sor=sor.split(" ")
            if int(sor[1])>legtobb_szam:
                legtobb_szam=int(sor[1])
                legjobb_oldal=sor[0]
        print(legjobb_oldal)
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_20():
    try:
        fajll=open("be1.txt",encoding="UTF-8",mode="r")
        fajl2=open("ki.txt",encoding="UTF-8",mode="w")
        max_varos=""
        max_lakos=math.inf
        for sor in fajl:
            sor=sor.strip()
            varos=sor[0]
            lakosok=sor[2]
            if lakosok>max_lakos:
                max_lakos=lakosok
                max_varos=varos
        fajl2.write(varos)
        fajl1.close()
        fajl2.close()
    except Exception as e:
        print(e)

def feladat_21():
    try:
        fajl1=open("be.txt", mode="r", encoding="utf-8")
        maxpont=0
        bajnok=""
        for sor in fajl1:
            sor=sor.strip()
            pontok=0
            lista=sor.split(";")
            for i in range(len(lista)):
                if i!=0:
                    pontok=pontok+int(lista[i])
            if pontok>maxpont:
                maxpont=pontok
                bajnok=lista[0]
        print(bajnok)
        fajl1.close()
    except Exception as e:
        print(e)
    fajl1.close()


def feladat_22():
    try:
        fajl1=open("be.txt", mode="r")
        fajl2=open("ki.txt", mode="w")
        leggyorsabb_nev=""
        leggyorsabb_ido=math.inf
        for sor in fajl1:
            sor=sor.strip()
            sor=sor.split(";")
            nev=sor[0]
            ido=float(sor[2])
            if ido<leggyorsabb_ido:
                leggyorsabb_ido=ido
                leggyorsabb_nev=nev
        fajl2.write(leggyorsabb_nev)
        fajl1.close()
        fajl2.close()
    except Exception as e:
        print(e)

def feladat_23():
    try:
        fajl1=open("be.txt", mode="r", encoding="utf-8")
        egyenes=True
        elozo_sor=0
        for sor in fajl1:
            if int(sor)>=int(elozo_sor):
                elozo_sor=sor
            else:
                egyenes=False
        if egyenes:
            print("YES")
        else:
            print("NO")
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_24():
    try:
        fajl1=open("be.txt", mode="r", encoding="utf-8")
        teki=0
        csiga=0
        sor_szama=0
        for sor in fajl1:
            sor_szama=sor_szama+1
            sor=sor.strip()
            sor=sor.split(" ")
            if sor_szama==2:
                for i in range(len(sor)):
                    teki=teki+int(sor[i])
            elif sor_szama==3:
                for j in range(len(sor)):
                    csiga=csiga+int(sor[j])
        if teki>csiga:
            print(teki*2)
            print("TURTLE")
        elif csiga>teki:
            print(csiga*2)
            print("SNAIL")
        else:
            print(csiga*2)
            print("DRAW")
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_25():
    try:
        fajl1=open("be.txt", mode="r", encoding="utf-8")
        sor_szam=0
        angol=[]
        magyar=[]
        for sor in fajl1:
            sor_szam=sor_szam+1
            if sor_szam!=1:
                sor=sor.strip()
                szo=sor.split(":")
                if szo[0] not in angol:
                    angol.append(szo[0])
                if szo[1] not in magyar:
                    magyar.append(szo[1])
        print(len(angol))
        print(len(magyar))
        fajl1.close()
    except Exception as e:
        print(e)

def feladat_26():
    try:
        fajl1 = open(sys.argv[1], mode="r", encoding="utf-8")
        fajl2 = open(sys.argv[2], mode="r", encoding="utf-8")
        fajl3 = open("ki.txt", mode="w", encoding="utf-8")
        sor_szam = 0
        sor_szam2 = 0
        sample1 = []
        sample2 = []
        for sor in fajl1:
            sor = sor.strip()
            sample1.append(sor)
            sor_szam = sor_szam + 1
        for sor2 in fajl2:
            sor2 = sor2.strip()
            sample2.append(sor2)
            sor_szam2 = sor_szam2 + 1
        sor_szam = str(sor_szam)
        sor_szam2 = str(sor_szam2)
        fajl3.write(sor_szam)
        fajl3.write(" ")
        fajl3.write(sor_szam2)
        fajl3.write("\n")
        for i in sample1:
            if i not in sample2:
                fajl3.write(i)
                fajl3.write("\n")
        fajl1.close()
        fajl2.close()
        fajl3.close()
    except Exception as e:
        print(e)

def feladat_27():
    try:
        fajl1=open(sys.argv[1],mode="r",encoding="utf-8")
        fajl2=open("ki.txt",mode="w",encoding="utf-8")
        min_szerzo=math.inf
        for sor in fajl1:
            sor=sor.strip()
            cim,szerzo=sor.split(":")
            szerzok=szerzo.split(",")
            if len(szerzok)<min_szerzo:
                min_szerzo=len(szerzok)
        fajl1.close()
        fajl2.close()
    except Exception as e:
        print(e)

def main():
    print(feladat_1(8))
    print(feladat_2(5))
    print(feladat_3(513))
    feladat_4()
    feladat_5(1000)
    print(feladat_6(17654,134))
    print(feladat_7(1442,1))
    print(feladat_8(51))
    print(feladat_9())
    feladat_10()
    feladat_11()
    feladat_12()
    feladat_13()
    feladat_14()
    feladat_15()
    feladat_16()
    feladat_17()
    feladat_18()
    feladat_19()
    feladat_20()
    feladat_21()
    feladat_22()
    feladat_23()
    feladat_24()
    feladat_25()
    feladat_26()
    feladat_27()
if __name__ == '__main__':
    main()
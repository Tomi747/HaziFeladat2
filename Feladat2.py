import math

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
    k=1
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
        fajl=open("be.txt", mode="r")
        max_hossz=-math.inf
        for sor in fajl:
            sor=sor.strip()
            hossz=len(sor)
            if sor[0].isupper() and hossz>max_hossz:
                max_hossz=hossz
        print(max_hossz)
    except Exception as e:
        print(e)

def feladat_11():
    try:
        fajl=open("be.txt", mode="r")
        max_hossz=-math.inf
        abc="aábcdeéfghiíjklmnopqrstuúüűvwxyz"
        for sor in fajl:
            sor=sor.strip()
            hossz=len(sor)
            if sor[-1] not in abc and hossz>max_hossz:
                max_hossz=hossz
        print(max_hossz)
    except Exception as e:
        print(e)

def feladat_12():
    try:
        fajl=open("be.txt", mode="r")
        fajl2=open("ki.txt",mode="w")
        for sor in fajl:
            db = int(sor[-1])
            egyforma=0
            for i in range(1,len(sor)-1):
                if sor[i]==sor[i+1]:
                    egyforma=egyforma+1
        if egyforma>=db:
            fajl2.write("True")
        else:
            fajl2.write("False")
    except Exception as e:
        return e

def feladat_13():
    try:
        fajl=open("be.txt",mode="r")
        db=0
        hossz=0
        for sor in fajl:
            for k in sor:
                hossz=hossz+1
        for i in range(hossz-1):
            for j in range(i+1,i+2):
                if abs(int(sor[i])-int(sor[j]))<=int(sor[-1]):
                    db=db+1
        print(db)
    except Exception as e:
        print(e)

def feladat_15():
    try:
        fajl1=open("be.txt", mode="r")
        fajl2=open("ki.txt", mode="w")
        for sor in fajl1:
            if sor!="\n":
                fajl2.write(sor)

    except Exception as e:
        return (e)
    fajl1.close()
    fajl2.close()

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
    feladat_15()
if __name__ == '__main__':
    main()
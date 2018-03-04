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
        for j in range(1,int(i/2)+1):
            if i%j==0:
                oszto_db=oszto_db+1
        if oszto_db>max_oszto:
            eredmeny.append(i)
            max_oszto=oszto_db
    print(eredmeny)


def main():
    print(feladat_1(8))
    print(feladat_2(5))
    print(feladat_3(513))
    feladat_4()
    feladat_5(1000)
if __name__ == '__main__':
    main()
f=open("med.txt","r+")
f.read()
med=["sinarest","cold",36],["crocin","fever",20],["dolox","painkiller",40],["strepsils","cough",45]
f.write(med)
ch=int(input("DO you want to enter disease or medicine:(1/2)"))
if ch==1:
    dis=input("cold/fever/painkiller/cough:")
    disease=dis.lower()
    for i in med:
        if disease==i[1]:
            print(med[i])
            

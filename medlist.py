med=[["sinarest","cold",20],["dolox","pk","30"],["strepsils","cough",40],["xyz","cold",50]]
def disease():
    dis=input("enter the disease")
    dis1=dis.lower()
    for i in med:
        if dis1==i[1]:
            #d1=med[i]
            print("Disease:",i[1],"Medicine:",i[0])
            #quantity(d1)
            quantity(i[1])
        else:
            print("tablet realted to this dis is not present")
def quantity(m):
    b=int(input("do u want to buy y/n:(1/2)"))
    if b==1:
        q=int(input("enter quantity"))
        for k in [med]:
            if m==k[1]:
                q1=int(k[2])
                if q<=q1:
                    if m==med[0]:
                        a=10*q
                        print(med[0],"tamt",a)
                    elif m==med[1]:
                        a=12*q
                        print(med[1],"tamt",a)
                    elif m==med[2]:
                        a=13*q
                        print(med[2],"tamt",a)
                    else:
                        a=13*q
                        print(med[3],"tamt",a)
                else:
                    print("no stock")
    else:
        print("thank u")


        
tab=int(input("enter the med/disease:(1/2)"))
if tab==1:
    t=input("enter the med")
    dis2=t.lower()
    for j in med:
        if dis2==j[0]:
            #d2=med[j]
            print("Medicine:", j[0],"Disease:",j[1])
            #print(med[j])
            quantity(j[2])
        else:
            print("tab is not there")
else:
    d=input("enter the disease")
    dis3=d.lower()
    for l in med:
        if dis3==l[1]:
            #d3=l[1]
            #print(med[l])
            print("Disease:",l[1],"Medi:",l[0])
            quantity(l[2])
        else:
            print("tab related to the disease is not present")
            d4=int(input("do u want the other tab y/n:(1/2)"))
            if d4==1:
                disease()
            else:
                print("thank u")
                
        
            
        
        

           

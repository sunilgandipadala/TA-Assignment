import random
from collections import defaultdict
Grocarylist=[]
productlist=[]
pricelist=[]
quantitylist=[]
budget=int(input("Enter your BUDJET : "))
print("1.Add item\n2.Exit")
choice=int(input("Enter your choice : "))
while(choice!=2):
    print("\n\n")
    if(choice<3 and choice>0):
        product=input("Enter product : ")
        quantity=input("Enter quantity :")
        price=int(input("Enter price : "))
        if price>budget:
            print("You don't have sufficient budget decrease your quantity")
        else:
            budget=budget-price
            productlist.append(product)
            pricelist.append(price)
            quantitylist.append(quantity)
        print("\n\nAmount left : ",budget,"\n\n")
        if(budget==0):
            print("Your budget is nill ,you can't buy any more........")
            break
    else:
        print("Enter valid choid\n\n")
    print("1.Add item\n2.Exit")
    choice=int(input("Enter your choice : "))
num=0    
flag=1
if(budget>0):
    i=random.randint(0,len(productlist)-1)
    while(len(pricelist)>num):
        num+=1
        if(pricelist[i]<budget):
            print("Amount left with you is: {0}, you can buy {1}".format(budget,productlist[i]))
            flag=0
            break
        else:
             i=random.randint(0,len(productlist)-1)
if(flag==1):               
    print("You have low money to again buy your cart products")
newlist=[]
for data in quantitylist:
    count=0
    for da in data:
        if(da.isdigit()or da=="."):
            count+=1
        else:
            break
    newlist.append(float(data[:count]))
quantitylist=newlist
for i in range(0,len(productlist)):
    for j in range(i+1,len(productlist)):
        if(productlist[i]==productlist[j]):
            quantitylist[j]=quantitylist[i]+quantitylist[j]
            pricelist[j]=pricelist[i]+pricelist[j]
            quantitylist.pop(i)
            productlist.pop(i)
            pricelist.pop(i)
            
priceandquantity=list(zip(quantitylist,pricelist))
Grocerylist=list(zip(productlist,priceandquantity))
bylet=defaultdict(list)
for data in Grocerylist:
    bylet[data[0]].append(data[1])
bylet=dict(bylet)
print("Grocery List is: ")
print ("{:<15} {:<10} {:<8}".format('Product name','Quantity','Price'))
for k, v in bylet.items():
    qunat=v
    print ("{:<15} {:<10} {:<8}".format(k,qunat[0][0],qunat[0][1]))

    

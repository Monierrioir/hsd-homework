'''10 ürün bulunan bir markette alışveriş tutarını ve para üstünü hesaplama'''

product1=input("productcost1:")
product2=input("productcos2: ")
product3=input("productcost3: ")
product4=input("productcost4: ")
product5=input("productcost5: ")
product6=input("productcost6: ")
product7=input("productcost7: ")
product8=input("productcost8: ")
product9=input("productcost9: ")
product10=input("productcost10: ")

cost=int(product1+product2+product3+product4+product5+product6+product7+product8+product9+product10)
money=int(input("money:"))

print(money-cost)


 

 


'''Üniversite notlarını alıp alınan nota göre har notu giren sistem'''

mark=int(input("mark: "))
if(mark>90):
    print("mark is:A" )
elif(mark>80):
        print("mark is:B")
elif(mark>60):
            print("mark is:C")
elif(mark<60):
    print("mark is:D")


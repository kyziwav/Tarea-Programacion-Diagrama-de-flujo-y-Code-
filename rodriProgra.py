saldo= 5 
contador = 0
while saldo > 0: 
    print ("Tienes:", saldo, "Bs")
    print ("1= papas= 1,50")
    print ("2= chocolate= 2,00")
    print ("3= refresco= 2,50")
    print ("4= finalizar compra")
    opción = int(input("selecciona una opción"))
    if opción == 1:
       costo = 1.50
       if saldo >= costo:
            saldo = saldo - costo
            contador +=1
            print ("compraste papas")
            print ("tu saldo actual es", saldo)
       else:
           print ("no tienes saldo vro")
    elif opción == 2:
         costo = 2.00
         if saldo >= costo:
             saldo = saldo - costo 
             contador +=1
             print ("compraste chocolate")
             print ("tu saldo actual es", saldo)
         else:
             print ("no tienes saldo vro")
    elif opción == 3:
         costo = 2.50
         if saldo >= costo:
             saldo = saldo - costo 
             contador +=1
             print ("compraste refresco")
             print ("tu saldo actual es", saldo)
         else:
            print (" no tienes saldo vro")
    elif opción == 4:
         print ("gracias por tu compra")
         break
    else: 
        print ("opción invalida")
        break
print ("compraste", contador, "productos") 
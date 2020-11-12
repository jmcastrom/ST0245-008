def invertir(pila):                 #Recibe una pila como parámetro
        pila2 = Pila()              #Crea una nueva
        pila.items.reverse()        #Invierte los elementos de la pila original
        pila2.items =  pila.items   #Asigna los elementos invertidos
        while len(pila.items)>0:
          pila.items.pop()          #Elimina los elementos de la pila 1, mientras esta no sea vacía
        return pila2

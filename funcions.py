#Exercici 1 Calculadora de preus
def calcular_preu(preu_peces, cost_mà_obra):
     total = preu_peces + cost_mà_obra
     return total

preu = calcular_preu(45, 30)
print ("Cost total:","preu", "€")
#Preguntes de l'exercici 
# 1. Quants paràmetres té la funció?
#    Dos: preu_peces i cost_ma_obra.
# 2. Quin valor retorna?
#    La suma dels dos paràmetres, és a dir, el cost total de la reparació. Amb calcular_preu(45, 30) retorna 75.
# 3. Què passaria si eliminéssim el return?
#    La funció faria el càlcul, però el resultat es perdria. Retornaria
#    None, així que la variable preu valdria None i el print mostraria
#    "Cost total: None €". 
#==================================
#Exercici 2 Funcions amb condicions
def aplicar_descompte(preu, tipus_client):
    # Acceptem el tipus de client en minúscules, majúscules o amb inicial
    # majúscula: el passem tot a minúscules amb .lower() abans de comparar-lo
    descompte = 0
    tipus = tipus_client.lower()

    if tipus == "particular":
        percentatge = 0
    elif tipus == "empresa":
        percentatge = 0.10
    elif tipus == "habitual":
        percentatge = 0.15
    else:
        # Tipus no vàlid: mostrem l'error i retornem el preu original
        print("Error: tipus de client no vàlid")
        return preu

    preu_final = preu - preu * percentatge / 100
    return preu_final
# Proves
    print(aplicar_descompte(100, "Particular"))  
    print(aplicar_descompte(100, "Empresa"))     
    print(aplicar_descompte(100, "Habitual"))    
    print(aplicar_descompte(100, "estudiant"))  
#============================================== 
#Exercici 3 Funcions que criden altres funcions
def calcular_iva(preu):
    # Retorna només l'import de l'IVA (21 %), no el preu amb IVA
    iva = preu * 21 / 100
    return iva


def calcular_factura(preu, tipus_client):
    # Reutilitzem les funcions anteriors en lloc de repetir codi
    preu_descomptat = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descomptat)
    total = preu_descomptat + iva
    return total


# Proves
print(calcular_iva(100))                  
print(calcular_factura(100, "Empresa"))   
#===========================================
#Exercici 4. Programa complet: servei tècnic
def mostrar_menu():
    print()
    print("===== SERVEI TÈCNIC INFORMÀTIC =====")
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")


def nova_reparacio():


    nom = input("Nom del client: ")

    peces = float(input("Preu de les peces: "))

    ma_obra = float(input("Cost de la mà d'obra: "))

    total = calcular_preu (peces, ma_obra)

    return total

def reparacions():
    # Aquestes dues variables s'inicialitzen Abans del bucle
    nombre_reparacions = 0
    facturacio_acumulada = 0.0

    opcio = ""
    while opcio != "4":
        mostrar_menu()
        opcio = input("Selecciona una opció: ").strip()

        if opcio == "1":
            total = nova_reparacio()
            nombre_reparacions += 1
            facturacio_acumulada += total
        elif opcio == "2":
            print("Nombre de reparacions realitzades:", nombre_reparacions)
        elif opcio == "3":
             print(f"Facturació acumulada: {facturacio_acumulada:.2f} €")
        elif opcio == "4":
            print("Fins aviat!")
        else:
            print("Opció no vàlida. Tria una opció del menú.")

if __name__=="__main__":
    reparacions()
    #==================================
    #Exercici 5 Reflexió Final
     #Respon aquestes preguntes com a comentaris al final del fitxer o en un document de text:
     #Quina diferència hi ha entre print() i return? 
     #Print: Imprimeix el contingut que hi ha dintre dels paréntesis ()pot ser una variable un valor o una nota.
     #Return: la seva funció es retornar el resultat de una variable, objecte o un valor.
     #Per què és millor dividir un programa en funcions?  
     #Perquè el codi queda més ordenat i llegible, es pot provar cada part per separat, s'eviten repeticions i és més fàcil de modificar. 
     #Què és un paràmetre?
     #Un paràmetre és una dada que la funció necessita per poder funcionar. Es posa entre parèntesis quan es defineix la funció.
     #Què és una variable local? és Una variable creada dins d'una funció desapareix quan la funció acaba.
     #Quins avantatges té reutilitzar una funció? els avantatges que té reutilitzar una funció és estalviar temps tornant a escriure diferents lines de codi 
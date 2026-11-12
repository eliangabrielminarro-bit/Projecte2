#Exercici 1 Calculadora de preus
def calcular_preu(preu_peces, cost_mà_obra):
     total = preu_peces + cost_mà_obra
     return total
preu = calcular_preu(45, 30)
print("Cost total:",preu, "€")
#==================================
#Exercici 2 Funcions amb condicions
def aplicar_descompte(preu, tipus_client):
    # Acceptem el tipus de client en minúscules, majúscules o amb inicial
    # majúscula: el passem tot a minúscules amb .lower() abans de comparar-lo
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


def main():
    # Aquestes dues variables s'inicialitzen ABANS del bucle
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


main()
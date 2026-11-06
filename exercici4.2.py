hi_ha_10 = False
nota = int(input("Introdueix una nota (-1 per acabar): "))
while nota != -1:
     if nota == 10:
          hi_ha_10 = True
     nota = int(input("Introdueix una nota (-1 per acabar): "))
if hi_ha_10:
     print("Hi ha hagut alguna nota que té un 10")
else:
      print("No hi ha cap 10")     
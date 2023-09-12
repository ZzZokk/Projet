if choix =='1':
    resultat = addition(nombre1, nombre2)
elif choix =='2':
    resultat = multiplication(nombre1, nombre2)
elif choix =='3':
    resultat = substraction(nombre1, nombre2)
elif choix =='4':
    resultat = division(nombre1, nombre2)
else:
    resultat = "choix invalide"

print("le resultat est : ", resultat)

#Eva Desbiens - 04/10/2024
import math

#nombre entier positif rentré par l'utilisateur
nbr = (input("Entrez un nombre positif (0 pour arrêter):"))

while nbr.isdigit():
    if int(nbr) > 0:
        #Variable qui détermine la chaine entiere de décomposition
        decomp = nbr + " = "
        #Décomposition en puissance de 10
        for position in range (len(nbr)-1):
            if int(nbr[position]) != 0:
             decomp= decomp + nbr[position]+"*10**"+str(len(nbr)-1-position)+" + "
             #Rien indiquer si le chiffre est 0
            else:
                decomp = decomp
        #Pour l'unité finale = 10**0 = 1 (pas besoin d'indiquer la puissance de 10)
        decomp = decomp + nbr[-1]
        print(decomp)

        #Variable de la somme des factoriels qui sera portée au changement
        somme = 0
        # Somme des factoriels de tous les chiffres composant le nombre
        for position in range(len(nbr)):
            chiffre = int(nbr[position])
            if chiffre != 0:
              somme = somme + math.factorial(chiffre)
            # On ne compte pas les 0
            else:
              somme = somme
        print("La somme des factoriels des chiffres de "+nbr+ " est: "+str(somme))

    #Sortie de la boucle, si la réponse est 0
    else:
        break
    #Recommencement de la boucle
    nbr = (input("Entrez un nombre positif (0 pour arrêter):"))

print("Au revoir")

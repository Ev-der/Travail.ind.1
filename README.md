# Travail.ind.1
Décomposition d'un Nombre en Somme de Puissances et Calcul de la Somme des Chiffres

Écrire un programme Python qui demande à l'utilisateur de saisir un nombre positif. Le programme doit :
Décomposer le nombre saisi en une somme de puissances de 10.
Calculer la somme des factoriels des chiffres de ce nombre.
Répéter l'opération tant que l'utilisateur ne saisit pas 0 (zéro).
Exemple 1 de fonctionnement :
Le programme doit afficher (Ce qui n’est pas en gras, c’est ce que l’utilisateur va saisir):
Entrez un nombre positif (0 pour arrêter) : 543
543 = 5*10**2 + 4*10**1 + 3
La somme des factoriels des chiffres de 543 est : 150

Explication :
Décomposition : 543=5×102+4×101+3
Somme des factoriels :
5!=120
4!=24
3!=6
Somme = 120 + 24 + 6 = 150
Remarque : Il est à noter que dans l’affichage, avant et après le + il y a un espace.
Exemple 2 de fonctionnement :
Entrez un nombre positif (0 pour arrêter) : 205
205 = 2*10**2 + 5
La somme des factoriels des chiffres de 205 est : 122


Explication :
Décomposition : 205=2×102+5
Somme des factoriels :
2!=2
5!=120
Somme = 2 + 120 = 122

Rappel : Le factoriel d'un nombre entier positif n, noté par n! est le produit de tous les entiers positifs inférieurs ou égaux à n:
n!=n*(n−1)*(n−2)*⋯*1
Quelques règles :
Le factoriel de 0 est toujours égal à 1 : 0!=1
Le factoriel est défini uniquement pour les entiers positifs. 
Exemples de Factoriels :
1!=1
2!=2*1=2
3!=3*2*1=6
4!=4*3*2*1=24
5!=5*4*3*2*1=120

Utilisation sous python : 
Il est possible d’utiliser la fonction prédéfinie de Math pour calculer le factoriel: math.factorial(n) (avec n est un nombre positif)

Remarque et barème :
- Votre programme doit utiliser des identificateurs significatifs
- il doit être bien indenté, sans ligne trop longue
- il doit être bien commenté. Les commentaires doivent indiquer :
votre nom et la date au début du code
une brève explication de l'utilité du code.
une brève explication des variables déclarée
une brève explication du fonctionnement du code (sa logique)

- l’exercice est noté sur 20
3 points pour les commentaires
14 points pour la logique et le bon déroulement du programme
3 points pour le respect de l’affichage.
Des points seront enlevés en cas de :
présence des bogues.
non-respect des consignes
non-consistance et mauvaise logique dans programme

Plagiat 
Sachez que le plagiat entraîne directement la note de 0 et mène à une note dans votre dossier. Tout partage de code ou copie de code qui n'est pas le vôtre, qu'il soit sous forme de texte, de photo ou tout autre format, est considéré comme du plagiat. L’utilisation de toute intelligence artificielle est considérée comme plagiat. Lors de la correction, je vais utiliser plusieurs méthodes pour détecter le plagiat. 
Remise 
Remettre sur Léa votre fichier. Il est de votre devoir de vérifier que vous avez fait correctement la remise.

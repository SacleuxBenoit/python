# exercice-06-listes.py

from hashlib import new
import random

# Remarque 6.1
# Dans le texte, quand il est écrit Xème position, cela correspond à l'index X-1

# exo 6.1
# Créez une liste nommée `my_list` contenant un nombre entier, un nombre à virgule flottante, une chaîne de caractères et un booléen

# réponse 6.1
my_list = [22, 1.14, "mardi", True]
# exo 6.2
# Affichez l'élément qui se trouve à la troisième position de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.2
print(my_list[2])

# exo 6.3
# Ajoutez une chaîne de caractères à la fin de la liste `my_list` (sans modfier le code d'initialisation) et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.3
my_list.append('leeeroy')
print(my_list)

# exo 6.4
# Supprimez l'élément qui se trouve en deuxièm position de la liste et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.4
del(my_list[1])
print(my_list)
# exo 6.5
# Remplacez l'élément qui se trouve en deuxièm position de la liste par un nombre entier et affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.5
my_list[1] = 11
print(my_list)

# exo 6.6
# Affichez la taille de la liste
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.6
last_index = len(my_list)
print(last_index)
# len(my_list) car on recherche la taille de la liste et non le dernier index sinon c'est len(my_list) - 1

# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7
my_list[1] = "lorem"
my_list[3] = "bar"
print(my_list)

# Remarque 6.2
# les exercices suivants nécessitent l'utilisation d'une boucle `for`

# exo 6.8
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42]
# réponse 6.8
sum = 0
for numbers in my_list:
    sum+=numbers
    
print(sum)

# exo 6.9
# Calculez la somme des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.9
sum = 0
for numbers in my_list:
    sum += numbers
    
print(sum)

# exo 6.10
# Calculez la moyenne des nombres de la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]
average = 0
# réponse 6.10
for numbers in my_list:
    average += numbers / 6
    
print(average)

# exo 6.11
# Trouvez l'index de la valeur `3.14` dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.11
index = my_list.index(3.14)
print(index)

# exo 6.12
# Comptez les nombres plus petits ou égaux à 10 dans la liste et affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]
# réponse 6.12

numberLessThanTen = 0
for lessThanTen in my_list:
    if lessThanTen <= 10:
        numberLessThanTen+= 1

print(numberLessThanTen) # Affiche 4

# exo 6.13
# Multipliez chacun des nombres dans la liste par 100, réaffactez le résultat à la place de la valeur originelle puis affichez le résultat
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.13
new_list= []
for number in my_list:
    number = number *100
    new_list.append(number)

print(new_list)

# exo 6.14
# Créez une deuxième liste ne contenant que les nombre entiers de la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14
new_list = []
for items in my_list:
    new_list.append(int(items))

print(new_list)

# exo 6.15
# Ici le but est d'intervertir les éléments de la liste deux à deux
# Liste initiale :
#
#   my_list = [2.71, 42, 123, 2, 3.14, 1.61]
#
# Résultat attendu :
#
#   my_list = [42, 2.71, 2, 123, 1.61, 3.14]
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.15
for items in my_list:
    i = 0
    j = 1
    
    storage1 = my_list[i]
    storage2 = my_list[j]
    
    storage1 = my_list[j]
    storage2 = my_list[i]
    i += 2
    print(my_list)
    
# exo 6.16
# Triez la liste en utilisant l'algorithme du tri bulle puis affichez la liste
my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.16
len_list = len(my_list)
for i in range(len_list):
    for j in range(0, len_list-i-1):
        if my_list[j] > my_list[j+1] :
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
            print(my_list)

# code 6.1
# Lire la valeur de la ligne `m` et de la colonne `n` d'un tableau en 2 dimensions
# print(matrix[m][n])
#
# Exemple avec la ligne 2 (index 1) et la colonne 3 (index 2)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
# Cette ligne affiche `6`
print(matrix[1][2])

# exo 6.17
# Affichez la valeur qui se trouve à la colonne 4, ligne 3
# Attention : il faut faire `- 1` pour obtenir les index correspondant
size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.17
print(matrix[3][2])

# code 6.2
# Pour afficher toutes les combinaisons possibles de deux nombres de 0 à n inclus vous pouvez utiliser deux boucles `for` imbriquées
#
# Exemple de toutes les combinaisons possibles de deux nombres de 0 à 2 inclus
for i in range(0, 3):
    for j in range(0, 3):
        print(i, j)

# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)

# réponse 6.18

# exercice-09-dictionnaires.py

# exo 9.1
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé alphanumérique et un nombre entier
# - une clé alphanumérique et un nombre à virgule flottante
# - une clé alphanumérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.1
my_dict = {
    'int':22,
    'float':3.14,
    'str':"Hello World",
    'bool':True
}
print(my_dict)
# exo 9.2
# Créez un dictionnaire nommé `my_dict` associant :
# - une clé booléenne et un nombre entier
# - une clé booléenne et un nombre à virgule flottante
# - une clé numérique et une chaîne de caractères
# - une clé alphanumérique et un booléen
# Puis affichez le résultat avec un simple `print()`

# réponse 9.2
my_dict = {
    False:3,
    True:3.14,
    42:'Hello World',
    'bool':False
}
print(my_dict)

# exo 9.3
# Ajoutez au dictionnaire un élément qui associe la clé alphanumérique `ipsum` à la valeur `2.71`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# réponse 9.3
my_dict['ipsum'] = 2.71
print(my_dict)

# exo 9.4
# Affichez la valeur associée à la clé 'lorem' dans le dictionnaire de 9.3

# réponse 9.4
print(my_dict['lorem'])

# exo 9.5
# Supprimez du dictionnaire la clé `foo`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# réponse 9.5
del my_dict['foo']
print(my_dict)

# exo 9.6
# Remplacez la valeur du dictionnaire associée à la clé `foo` par `123`
# Puis affichez le résultat avec un simple `print()`
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.6
my_dict['foo'] = 123
print(my_dict)

# exo 9.7
# En utilisant une boucle `for`, affichez les clés (et pas les valeurs) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}

# réponse 9.7
for key in my_dict:
    print(key)
    
# exo 9.8
# En utilisant une boucle `for` et sans utiliser la méthode `values()`, affichez les valeurs (et pas les clés) qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# réponse 9.8
for value in my_dict:
    print(my_dict[value])
    
# exo 9.9
# En utilisant une boucle `for` et sans utiliser la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.9
for item in my_dict:
    print(my_dict)
    
# exo 9.10
# En utilisant une boucle `for` et la méthode `items()`, affichez les clés et les valeurs qui se trouvent dans le dictionnaire
my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': 'lorem ipsum',
    'lorem': True
}
# Exemple de résultat attendu :
# key: foo, value: 42
# key: bar, value: 3.14
# key: baz, value: lorem ipsum
# etc...

# réponse 9.10
for key, item in my_dict.items():
    print(key, ":", item)
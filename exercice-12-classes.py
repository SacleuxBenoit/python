# exercice-12-classes.py

# exo 12.1
# Créez une classe nommée `User` qui possède les attributs suivants :
# - firstname: valeur par défaut ''
# - lastname: valeur par défaut ''
# - email: valeur par défaut ''
# - newsletter: valeur par défaut False
# et la méthode suivante :
# - __init__() : le constructeur
# Pas la peine de créer de getters et de setters

# réponse 12.1
class User:
    def __init__(self, firstname: str = "", lastname: str = "", email: str = "", newsletter: bool = False):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.newsletter = newsletter


# exo 12.2
# Créez 4 instances de la classe `User` et affectez les valeurs suivantes à ses attributs :
# - user1
#   - firstname: Joe
#   - lastname: Dalton
#   - email: joe.dalton@example.com
#   - newsletter: true
# - user2
#   - firstname: William
#   - lastname: Dalton
#   - email: william.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Jack
#   - lastname: Dalton
#   - email: jack.dalton@example.com
#   - newsletter: false
# - user3
#   - firstname: Avrel
#   - lastname: Dalton
#   - email: avrel.dalton@example.com
#   - newsletter: true

# réponse 12.2
user1 = User("Joe","Dalton","Joe.dalton@example.com",True)
user2 = User("William","Dalton","william.dalton@example.com",False)
user3 = User("Jack","Dalton","jack.dalton@example.com",False)
user4 = User("Avrel", "Dalton", "avrel.dalton@example.com",True)

# exo 12.3
# Ajoutez chacune des instances de la classe `User` à une liste nommée `users`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom complet et l'email de chaque utilisateur s'il est abonné à la newsletter (c-à-d si newsletter == True)

# réponse 12.3
users = [user1,user2,user3,user4]

for user in users:
    if(user.newsletter):
        print(user.firstname, user.lastname, user.email)
        
# exo 12.4
# Créez une classe nommée `ProductLorem` qui possède les attributs suivants :
# - _name: valeur par défaut ''
# - _price: valeur par défaut 0.0
# et les méthodes suivantes :
# - __init__() : le constructeur
# - get_name() : renvoit le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoit le prix du produit
# - set_price() : détermine le prix du produit

# réponse 12.4
class ProductLorem:
    def __init__(self, name = '', price = 0.0):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

# exo 12.5
# Créez 3 instances de la classe `ProductLorem` et affectez les valeurs suivantes à ses attributs en utilisant les setters :
# - product1
#   - name: Foo
#   - price: 31,41
# - product2
#   - name: Bar
#   - price: 27,18
# - product3
#   - name: Baz
#   - price: 16,18

# réponse 12.5

firstProduct = ProductLorem()
firstProduct.set_name("Lorem")
firstProduct.set_price(42)

print("name : ", firstProduct._name, "/ price : ", firstProduct._price)

secondProduct = ProductLorem()
secondProduct.set_name("foo")
secondProduct.set_price(72.99)

print("name : ", secondProduct._name, "/ price : ", secondProduct._price)

thirdProduct = ProductLorem()
thirdProduct.set_name("bar")
thirdProduct.set_price(123.99)

print("name : ", thirdProduct._name, "/ price : ", thirdProduct._price)
# exo 12.6
# Ajoutez chacune des instances de la classe `ProductLorem` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom et le prix de chaque produit
# Calculez la somme du prix des produits et affichez-en un arrondi à 2 chiffres après la virgule, après la boucle `for`

# réponse 12.6
products = [firstProduct, secondProduct, thirdProduct]

for product in products:
        print(product.get_name())
        print(product.get_price())


my_sum = 0
for product in products:
    my_sum += product.get_price()

my_sum = round(my_sum, 2)
print(my_sum)

# exo 12.7
# Créez une classe nommée `ProductIpsum` qui possède les attributs suivants :
# - _name: valeur str transmise par le constructeur
# - _price: valeur float par défaut 0.0
# - _tax: valeur float par défaut 0.0
# et les méthodes suivantes :
# - __init__(name, price, tax) : le constructeur
# - get_name() : renvoit le nom du produit
# - set_name() : détermine le nom du produit
# - get_price() : renvoit le prix du produit
# - set_price() : détermine le prix du produit
# - get_tax() : renvoit la taxe en pourcentage
# - set_tax() :  détermine la taxe en pourcentage (pour une taxe de 20 %, le paramètre doit être 20.0)
# - get_tax_fee() : cette méthode calcule le montant de la taxe et le renvoit ; par exmeple pour un produit de 100 € et une taxe de 20 %, le résultat est 20.0
# - get_tax_included_price() : cette méthode calcule le prix taxe incluse et le renvoit ; par exemple pour un produit de 100 € et une taxe de 20 %, le résultat est 120.0

# réponse 12.7
class ProductIpsum: 
    def __init__(self, name:str, price:float = 0.0, tax:float = 0.0):
        self._name = name
        self._price = price
        self._tax = tax

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_tax(self):
        return self._tax
    
    def set_tax(self, tax):
        self._tax = tax

    def get_tax_fee(self):
        return self.get_price() * self.get_tax() / 100

    def get_tax_included_price(self):
        return self.get_price() + self.get_tax_fee()
# exo 12.8
# Créez 3 instances de la classe `ProductIpsum` et affectez les valeurs suivantes à ses attributs en utilisant le constructeur :
# - product1
#   - name: Dolor
#   - price: 31,41
#   - tax: 20.0
# - product2
#   - name: Sit
#   - price: 27,18
#   - tax: 10.0
# - product3
#   - name: Amet
#   - price: 16,18
#   - tax: 5.5

# réponse 12.8

product1 = ProductIpsum("Dolor", 31.41, 20.0)
product2 = ProductIpsum("Sit", 27.18, 10.0)
product3 = ProductIpsum("Amet", 16.18, 5.5)

# exo 12.9
# Ajoutez chacune des instances de la classe `ProductIpsum` à une liste nommée `products`
# Utilisez une boucle `for` (type `foreach`) pour afficher le nom, le prix (sans la taxe), la taxe et le prix taxe incluse de chaque produit
# Calculez :
# - la somme du prix des produits sans les taxes
# - la somme du montant des taxes
# - la somme du prix des produits taxes incluses
# Et affichez-en des arrondis à 2 chiffres après la virgule, après la boucle `for`

# réponse 12.9

products = [product1, product2, product3]

for product in products:
    print(f'product name : {product.get_name()}, price without tax : {product.get_price()}€, current tax : {product.get_tax()}%, including taxes: {product.get_tax_included_price()}€')
    withoutTaxes = product1.get_price() + product2.get_price() + product3.get_price()
    summTotalTax = product1.get_tax_fee() + product2.get_tax_fee() + product3.get_tax_fee()
    withTaxes = product1.get_tax_included_price() + product2.get_tax_included_price() + product3.get_tax_included_price()

print(f'summ without taxes : {round(withoutTaxes,2)}€')
print(f'summ with taxes : {round(summTotalTax, 2)}€')
print(f'summ with taxes : {round(withTaxes, 2)}€')
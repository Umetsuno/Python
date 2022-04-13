
#Base
from numpy import append, concatenate


print("Hello World !")
livre = 20
print(livre)
livre = "ABCDEFG"
print(livre)

#Tableaux
liste_de_courses = ["Pomme", 2, "Poire", 1, "Banane", 7]
print(liste_de_courses)
print(liste_de_courses[0], liste_de_courses[1])
print(livre[-7])

bouquin = ['Le','Petit','Prince']
bouquin.append("Patapoulpinet")
print(bouquin)
bouquin.sort()
print(bouquin)

#Dictionnaires clés/valeurs
monDictionnaire = {
	"user_id": 1,
	"user_name": "John",
	"user_age": 25
}

tauxDeConversion = {}
tauxDeConversion["EUR"] = 1.14
tauxDeConversion["USD"] = 1.00
tauxDeConversion["GBP"] = 0.89
print(monDictionnaire)
print(tauxDeConversion)
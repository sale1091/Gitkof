prenom = "bernard"
print("avant", prenom)


def nom(nom, prenom, age):
    print("votre nom est : " + nom)
    print("votre Prenom est : " + prenom)
    print("votre age est :",age)

nom("lamah", "eugene", 22) 

print("apres", prenom)

class Utilisateur():
    nom = "lamah"
    prenom = "eugene"
    age = 22

info = Utilisateur()
philippe = Utilisateur()
print(info.nom, info.prenom, info.age)
print(philippe.nom, philippe.prenom, philippe.age)
class Affiche:
 def__init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
info = Affiche("lamah", "eugene", 24)
philippe = Affiche("mamy", "ousmane", 25) 
print(info.nom)
print(philippe.nom)       






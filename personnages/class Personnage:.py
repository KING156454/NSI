

###############################################################################
##Parametre

class Personnage:
    def __init__(self, pseudo, vie, force, agilite, inteligence, chance = 50 ,level = 0):
        self.pseudo = pseudo
        self.vie = vie
        self.level = level
        self.force = force
        self.agilite = agilite
        self.intelligence = inteligence
        self.chance = chance

    def est_en_vie(self):
        if self.vie == 0:
            return False
        return True
    
    def attack(self,ennemis):
        if ennemis.est_en_vie() == False:
            return print("ennemis est mort")
        if self.est_en_vie() == False:
            return print("tu est mort")
        
        ennemis.vie -= (self.force + self.intelligence)/10
        if ennemis.vie < 0 :
            ennemis.vie = 0
            self.level += 1



################################################################################
##Class

perso1 = Personnage("guerrier",100,100,20,20)
perso2 = Personnage("mage",100,20,20,100)

################################################################################
##Test
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
perso1.attack(perso2)
print(perso2.vie)
print(perso1.level)
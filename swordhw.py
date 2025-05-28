
#class
class Sword:    

#constructor
    def __init__(self, type, damage, weight):
        self.type = type #claymore, katana, rapier
        self.damage = damage #claymore = 125, katana = 100, rapier = 75
        self.weight = weight  #claymore = 5 , katana = 3 , rapier = 4 


    def get_type(self):
        #self.type = "buster"
        print(self.type)

    def get_damage(self):
        print(self.damage)

    def get_weight(self):
        print(self.weight)
        
    #setter
    def set_sword(self, type, damage, weight):
        self.type = type
        self.damage = damage
        self.weight = weight
        



    
class NPC:
    

	#constructor
    def __init__(self, name):
        self.name = name
        self.health = 100 #assume that is percent
        self.inventory = []
		
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} has died!")

    def attack(self, target, damage):
        print(f"{self.name} attacks {target.name}!")
        target.take_damage(damage)

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item.name}")

    def show_inventory(self):
        if self.inventory:
            print(f"{self.name}'s inventory:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print(f"{self.name}'s inventory is empty.")
            
	
            

#session 2. 
# Homework review
# I owe an example of getter and setting in a class

from npc import NPC

my_first_npc = NPC("bob")
my_second_npc=NPC("Goerge")
print("second npc started with: " + str(my_second_npc.health) + " health")
my_first_npc.attack(my_second_npc, 10)
print(my_second_npc.health)

my_first_npc.add_item("sword")
my_first_npc.attack(my_second_npc, 20)
print(my_second_npc.health)
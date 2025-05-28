# In this session I will push my files into a repo.
# You will clone that repo into a new empty folder
# Once you have a clone of my repo, you will add your sword file to the clone repo
# You will commit and push your changes.
# I will pull your changes
# I will then incorporate your sword class and push the changes so you have access to them

#imports
from npc import NPC #imported a NPC
from gold import Gold #imported a gold coin

goblin = NPC("Harold") #instantiated an instance of NPC
gold_coin = Gold(10) #Instantiated na instance of gold coin with an inital value of 10

goblin.add_item(gold_coin) #had the npc instance add the gold coin instance to his class

goblin.show_inventory() #had the npc instance who his inventory

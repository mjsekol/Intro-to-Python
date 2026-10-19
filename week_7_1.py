# Python Classes and Objects

#Start a class with "class" keyword followed by the class name and a colon. The class name should be in PascalCase.

class Player:
    # pass # The pass statement is used as a placeholder for future code. It does nothing when executed.
    # Constructor method is called when an object is created from the class and allows the class to initialize the attributes of the class.
    def __init__(self, name, health, lightsaber_skill):
        self.name = name
        self.health = health
        self.lightsaber_skill = lightsaber_skill
        self.inventory = []  # Initialize an empty inventory list for the player

    # Method to take damage and reduce the player's health
    def take_damage(self, damage):
        self.health -= damage  # Reduce the player's health by the damage amount
        if self.health < 0:
            self.health = 0  # Ensure health doesn't go below 0

    # Attack method to simulate an attack on another player
    def attack(self, other_player):
        if self.lightsaber_skill > other_player.lightsaber_skill:
            damage = self.lightsaber_skill - other_player.lightsaber_skill
            other_player.take_damage(damage)
            print(f"{self.name} attacks {other_player.name} and deals {damage} damage!")
        else:
            print(f"{self.name} attacks {other_player.name} but it's not very effective.")

    # Method to heal the player
    def heal(self, amount):
        self.health += amount  # Increase the player's health by the specified amount
        if self.health > 100:
            self.health = 100  # Ensure health doesn't exceed 100

    # Method to add an item to the player's inventory
    def add_to_inventory(self, item):
        self.inventory.append(item)  # Add the item to the player's inventory list
        print(f"{item} has been added to {self.name}'s inventory.")

keith = Player("Keith", 200, 200)  # Create an instance of the Player class with name, health, and lightsaber_skill
trenton = Player("Trenton", 100, 80)  # Create another instance of the Player class

print(f"{keith.name} has {keith.health} health and a lightsaber skill of {keith.lightsaber_skill}.")
print(f"{trenton.name} has {trenton.health} health and a lightsaber skill of {trenton.lightsaber_skill}.")
keith.attack(trenton)
keith.add_to_inventory("Health Pack")
keith.heal(20)
trenton.attack(keith)
trenton.add_to_inventory("Force Crystal")

# Status update after attacks and healing
print(f"{keith.name}'s health after the attack: {keith.health}")
print(f"{trenton.name}'s health after the attack: {trenton.health}")

# Inventory Status Update
print(f"{keith.name}'s inventory: {keith.inventory}")
print(f"{trenton.name}'s inventory: {trenton.inventory}")
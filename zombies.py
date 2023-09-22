import random

# Define the player and zombie attributes
player_health = 100
zombie_health = 50

# Define the available weapons
weapons = {
    "knife": 10,
    "pistol": 20,
    "shotgun": 30,
    "rifle": 40,
    # ... Add more weapons here
}

# Function to randomly select a weapon
def select_weapon():
    return random.choice(list(weapons.keys()))

# Function to calculate damage
def calculate_damage(weapon):
    return weapons.get(weapon, 0)

# Game loop
while True:
    # Print player and zombie health
    print(f"Player Health: {player_health}")
    print(f"Zombie Health: {zombie_health}")
    
    # Player's turn
    player_weapon = select_weapon()
    player_damage = calculate_damage(player_weapon)
    zombie_health -= player_damage
    print(f"You attacked the zombie with a {player_weapon} and dealt {player_damage} damage.")
    
    # Check if the zombie is dead
    if zombie_health <= 0:
        print("Congratulations! You killed the zombie!")w
        break
    
    # Zombie's turn
    zombie_weapon = select_weapon()
    zombie_damage = calculate_damage(zombie_weapon)
    player_health -= zombie_damage
    print(f"The zombie attacked you with a {zombie_weapon} and dealt {zombie_damage} damage.")
    
    # Check if the player is dead
    if player_health <= 0:
        print("Game Over! The zombie killed you.")
        break
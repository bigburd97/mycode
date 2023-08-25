#!/usr/bin/env python3

import time
import random
from art import *

def display_status(name, player_health, monster_health, freeze_potion, heals_remaining):
    """
    Function to display the player's status, monster's health, and inventory.
    """
    print("\n----- Status -----\n")
    print(f"Your Health: {player_health}")
    print(f"Monster Health: {monster_health}")
    print(f"Heals Remaining: {heals_remaining}")
    print(f"Freeze Potions: {freeze_potion}\n")
    print("------------------\n")

def battle(name, player_health, monster_health, freeze_potion, heals_remaining):
    """
    Function to simulate the battle between the player and a monster.
    """
    while player_health > 0 and monster_health > 0:
        display_status(name, player_health, monster_health, freeze_potion, heals_remaining)
        action = input("Do you want to 'attack', 'heal', or use 'freeze' potion? ").lower()

        if action == 'attack':
            if random.random() > 0.2:  # 20% chance to miss
                damage = random.randint(10, 20)
                monster_health -= damage
                print(f"You attack the monster for {damage} damage!")
            else:
                print("You missed your attack!")
        if action == 'heal':
            player_health += (5)

            # Monster's turn to attack
            if random.random() > 0.3:  # 30% chance for the monster's attack to miss
                monster_damage = random.randint(5, 25)
                player_health -= monster_damage
                print(f"The monster attacks {name} for {monster_damage} damage!")
            else:
                print("The monster's attack missed!")

        # start of game

def main():
    """
    Main function to play the Battle Arena game.
    """
    print("Welcome to the Battle Arena!")

    # Gather user information
    name = input("Enter your name: ")
    character = input("Enter your character type: ")

    print(f"\nWelcome {name}! I see you're a very powerful {character}.")
    print(f"{name}, you will be facing many monsters. Prepare yourself!")
    time.sleep(2)

    # Display ASCII art of a sword or weapon
    print("\n")
    tprint("Prepare\n to\nFIGHT", font="doom")  # Display "FIGHT" in ASCII art
    print("\n")

    # Initialize player's stats and items
    player_health = 50
    monster_health = 65
    freeze_potion = 1
    heals_remaining = 3

    battle(name, player_health, monster_health, freeze_potion, heals_remaining)

    if player_health > 0:
        tprint(f"WHAT!\n {name}\n you defeated\n the monster", font="doom")
    else:
        tprint("Death\nObviously", font="doom")

if __name__ == "__main__":
    main()


#!/usr/bin/env python3

import random

def main():
    """
    Main function to play the Battle Arena game.
    """
    print("Welcome to the Battle Arena!")
    
    # Gather user information
    name = input("Enter your name: ")
    character = input("Enter your character type: ")
    star_sign = input("Enter your star sign: ")

    print(f"\nWelcome, {name} the {character}, born under the sign of {star_sign}!")

    hero_life = 100
    round_num = 1

    while hero_life > 0:
        print(f"\nRound: {round_num}")
        monster = get_random_monster()  # Get a random monster for the round
        enemy_health = random.randint(10, 20) + round_num * random.randint(1, 10)
        
        print(f"A wild {monster} appears!")
        print(f"Hero total: {hero_life}\t\tEnemy health: {enemy_health}")

        hero_attack = int(input("Enter your attack strength (1-30): "))
        if hero_attack < 1:
            hero_attack = 1
        elif hero_attack > 30:
            hero_attack = 30

        print(f"Hero attack: {hero_attack}\n")

        if hero_attack >= enemy_health:
            print(f"You defeated the {monster}!")
            enemy_health = 0  # Defeat the enemy without taking damage
        else:
            print(f"The {monster} counterattacks!")
            hero_life -= max(0, enemy_health - hero_attack // 2)  # Deduct life based on enemy's remaining health

        if hero_life <= 0:
            print("DEATH!!!!")
            break

        round_num += 1

    if hero_life > 0:
        print(f"\nCongratulations! {name}, the {character}, defeated the enemies.")

def get_random_monster():
    """
    Returns a random monster name for each round.
    """
    monsters = ["Dragon", "Goblin", "Orc", "Zombie", "Spider"]
    return random.choice(monsters)

if __name__ == "__main__":
    main()


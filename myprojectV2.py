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
        enemy_health = random.randint(5, 10) +  random.randint(1, 10)
        
        # Prompt for user input on attack strength
        hero_attack = int(input("Enter your attack strength (1-30): "))
        if hero_attack < 1:
            hero_attack = 1
        elif hero_attack > 30:
            hero_attack = 30

        print(f"Hero total: {hero_life}\t\tEnemy health: {enemy_health}")
        print(f"Hero attack: {hero_attack}\n")

        if hero_attack >= enemy_health:
            print("Survived!")
            hero_life -= max(0, enemy_health - hero_attack // 2)  # Deduct life based on attack strength
        else:
            print("DEATH!!!!")
            break
        
        round_num += 1

    if hero_life <= 0:
        print(f"\nGame Over! {name}, the {character}, couldn't defeat the enemies.")

if __name__ == "__main__":
    main()


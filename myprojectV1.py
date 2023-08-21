#!/usr/bin/env python3

import random

def battle(player_power, monster_health):
    """
    Simulate a battle between the player and a monster.

    Args:
        player_power (int): The player's power level.
        monster_health (int): The monster's initial health.

    Returns:
        int: Updated player power after the battle.
    """
    print(f"A monster with {monster_health} health appears!")
    while monster_health > 0 and player_power > 0:
        action = input("Do you want to 'attack' or 'defend'? ").lower()
        if action == 'attack':
            damage = random.randint(10, 25)
            monster_health -= damage
            print(f"You attack the monster for {damage} damage!")
            if monster_health > 0:
                player_power -= random.randint(5, 15)
                print(f"The monster attacks back, your power is now {player_power}.")
        elif action == 'defend':
            player_power -= random.randint(5, 10)
            print(f"You defend and lose some power, your power is now {player_power}.")
        else:
            print("Invalid action. Choose 'attack' or 'defend'.")

    if monster_health <= 0:
        print("You defeated the monster!")
    else:
        print("You were defeated by the monster...")

    return player_power

def main():
    """
    Main function to run the game.
    """
    player_power = 100
    round_num = 1

    while player_power > 0 and round_num <= 5:
        monster_health = random.randint(1, 25 + round_num * 15)
        print(f"\nRound {round_num}")
        player_power = battle(player_power, monster_health)
        round_num += 1

    if player_power > 0:
        print("Congratulations! You won!")
    else:
        print("Game Over! Your power reached zero.")

if __name__ == "__main__":
    main()


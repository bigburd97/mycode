#!/usr/bin/env python3

import time
import random
from art import *

def main():
    """
    Main function to play the Battle Arena game.
    """
    print("Welcome to the Battle Arena!")
    
    # Gather user information
    name = input("Enter your name: ")
    character = input("Enter your character type: ")

    print(f"\n Welcome {name} I see your a very powerful {character}\n you will be facing many monsters!\n Prepare yourself!")
    time.sleep(2)

    # Display ASCII art of a sword or weapon
    print("\n")
    tprint("FIGHT", font="doom")  # Display "FIGHT" in ASCII art
    print("\n")

main()

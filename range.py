#!/usr/bin/env python3

import time #imports the time module 

def main():
    # Defining the number of beer bottles.
    x = int(input("How many bottles will we be drinking tonight sir? :"))

    while x > 0:  # As long as the number of bottles is above 0, the loop continues
        print(f"{x} bottles of beer on the wall!")
        print(f"{x} bottles of beer on the wall! You take one down, pass it around!")
        x -= 1  # Subtract 1 from x every loop
        print(f"{x} bottles of beer on the wall!\n")
        time.sleep(1) #sleep of 3 seonds 

main()


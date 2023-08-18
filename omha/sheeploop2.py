#!usr/bin/evn python3

#list from farm
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def main():
    for farm in farms:
        print("-", farm["name"])
    choice= input("pick a farm! \n :")
    
    for farm in farms:
        if farm["name"].lower() == choice.lower():
            print(
main() 

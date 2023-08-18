"""#!/usr/bin/env python3

with open("dracula.txt" , "r") as foo:
    for line in foo:
        if str.lower("vampire") in line:
            print(line) >> vampirelines.txt
    count= 0 
    for line in foo:
        if "vampire" in line.lower():
            count += 1
    print(count)"""

#!/usr/bin/env python3

with open("dracula.txt", "r") as foo:
    with open("vampirelines.txt", "w") as vampire_file:
        count = 0
        for line in foo:
            if "vampire" in line.lower():
                print(line, end="", file=vampire_file)
                count += 1

print(f"Total occurrences of 'vampire': {count}")


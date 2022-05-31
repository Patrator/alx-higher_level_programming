#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print(f'{number} "Is negative"')
elif number == 0:
    print(f"{number} 'is zero'")
elif number > 0:
    print(f"{number} 'Is positive'")

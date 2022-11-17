Python 3.11.0 (v3.11.0:deaf509e8f, Oct 24 2022, 14:43:23) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... import time
... 
... 
... print("Hi! Welcome to the number guessing game. I am going to pick a number between 1 and 100 and you are going to guess it.")
... time.sleep(3)
... 
... print("Picking a number...")
... time.sleep(2)
... 
... guess = int(input("What is your guess?: "))
... correct_number = random.randint(1,100)
... guess_count = 1
... 
... while guess != correct_number:
...   time.sleep(1)
...   if guess < correct_number:
...     guess = int(input("Wrong. You need to guess higher. What is your guess?: "))
...   if guess > correct_number:
...     guess = int(input("Wrong. You need to guess lower. What is your guess?: "))
...   guess_count += 1
...   

import random

def guess_the_number(x):
    print("=======================")
    print("¡Welcome to the game!")
    print("=======================")
    print("your goal is guessing the number generated by the computer")
    random_number = random.randint(1, x) # random number betwen 1 and x
    # at the beginning we don't want that prediction being equal to  random_number
    prediction = 0
    # we don't know the number of attempts of the user 
    while prediction != random_number:
        # User enters a number
        prediction = int(input(f"Guess a number betwen 1 and {x}: "))
        if prediction < random_number:
            print(f"your number {prediction} is lower")
        elif prediction > random_number:
            print(f"your number {prediction} is bigger")
    print(f"Contragutulations! You guess the number {random_number}")


guess_the_number(10)
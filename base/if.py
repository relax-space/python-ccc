# if – elif – else
age = int(input("Age of dog:"))
if age < 0:
    print("This can hardly be true!")
elif age == 1:
    print("about 14 human years")
elif age == 2:
    print("about 22 human years")
elif age > 2:
    human = 22 + (age - 2)*5
    print("Human years: ", human)

###
input('press Return>')

number = 8
guess = -1
print("Guess the number!")
while guess != number:
    guess = int(input("Is it... "))
    if guess == number:
        print("Hooray! You guessed it right!")
    elif guess > number:
        print("It's not so big.")
    elif guess < number:
        print("It's bigger...")

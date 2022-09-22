secret_word = "Done"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        if guess_count!=3 and guess!= secret_word:
         print(" Try again\n The Number of tries you have is : ",3-guess_count)
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")
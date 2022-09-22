def translate(phrase):
    translation = ""
    for letter in phrase.lower():
        if letter in "AEIOUaeiou":
            translation = translation + "V"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
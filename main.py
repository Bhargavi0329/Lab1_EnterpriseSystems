alphabet = input("Enter an alphabet: ")
alphabet = alphabet.lower()
if alphabet in ['a', 'e', 'i', 'o', 'u']:
    print(alphabet + " is a vowel")
else:
    print(alphabet + " is not a vowel")

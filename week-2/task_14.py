word = input("Enter a word: ")
# Convert the word to lowercase so uppercase/lowercase differences are ignored
word = word.lower()

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

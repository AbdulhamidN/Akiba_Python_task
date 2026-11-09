def analyze_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove basic punctuation
    punctuation = ".,!?;:'\"()"

    for p in punctuation:
        text = text.replace(p, "")

    # Split text into words
    words = text.split()

    # 1. Count words
    word_count = len(words)

    # 2. Count characters excluding spaces
    char_count = len(text.replace(" ", ""))

    # 3. Count vowels and consonants
    vowels = 0
    consonants = 0

    for ch in text:
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    # 4. Find the longest word
    longest_word = ""

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    # 5. Count how many times each word appears
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # 6. Identify repeated words
    repeated_words = []

    for word in frequency:
        if frequency[word] > 1:
            repeated_words.append(word)

    # 7. Find five most frequent words
    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    top_five = sorted_words[:5]

    # Display results
    print("Words:", word_count)
    print("Characters (excluding spaces):", char_count)
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Longest word:", longest_word)
    print("Word frequency:", frequency)
    print("Repeated words:", repeated_words)
    print("Top five frequent words:", top_five)


# Main program
text = input("Enter a paragraph: ")

analyze_text(text)
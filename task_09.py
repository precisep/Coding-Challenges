def word_vowels(word):
    VOWELS = ["a", "e", "i", "o", "u"]
    word = word.lower()
    vowel_list = []

    for char in word:
        if char in VOWELS:
            vowel_list.append(char)

    print("Vowels:", ", ".join(set(vowel_list)))


if __name__ == "__main__":
    word_vowels("Umuzi")

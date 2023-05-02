def word_vowels(word):
    vowels = ["a", "e", "i", "o", "u"]
    word = word.lower()
    vowel_list = []

    for char in word:
        if char in vowels:
            vowel_list.append(char)
        else:
            continue

    print("Vowels :", ", ".join(set(vowel_list)))

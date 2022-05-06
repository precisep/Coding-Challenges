def word_vowels(word):
	
	vowels = ['a','e','i','o','u']
	word = word.lower()
	vowel_list = []

	for i in word:
		if i in vowels:
			vowel_list.append(i)
		else:
			None

	return print("Vowels :", ', '.join(set(vowel_list)))

def common_characters(string_1, string_2):

	common_letters = [char_1 for char_1 in string_1.lower() for char_2 in string_2.lower() if char_1 == char_2 ]

	return  print("Common letters:",', '.join(set(common_letters)))

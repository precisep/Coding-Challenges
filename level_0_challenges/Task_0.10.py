def common_characters(string_1, string_2):

	common_letters = [x for x in string_1.lower() for y in string_2.lower() if x == y ]

	return  print("Common letters:",', '.join(set(common_letters)))

def hello(word):
	if type(word) == 'str':
		print('Please enter a string')
	else:
		print('Hello',f'{word}!')

hello('Precise')

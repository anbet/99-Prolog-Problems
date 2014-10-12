def break_words(stuff):
	"""This function will break words for us"""
	words= stuff.split(' ')
	return words

def sort_words(words):
	"""sorts words for us"""
	return  sorted(words)

def print_first_word(words):
	"""Prints the first word"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""prints the last word for us"""
	word = words.pop(-1)
	print word

def sort_sentence(sen):
	"""This takes up the complete sentence and then sorts it up"""
	word = break_words(sen)
	return sort_words(word)

def print_first_and_last_word(sen):
	"""Prints the first and last word of the sentence """
	words = sort_sentence(sen)
	print_first_word(words)
	print_last_word(words)

sen="""Hello fellows wats up how are you doing this night!"""
print_first_and_last_word(sen)

sorted_words= sort_sentence(sen)
print_last_word(sorted_words)
print sorted_words

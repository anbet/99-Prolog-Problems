
import random
from urllib import urlopen
import sys

WORD_URL ="http://learncodethehardway.org/words.txt"
WORD = []

PHRESES = {
"class %%%(%%%):":
	"Make a class named %%% that is-a %%%.",
"class %%%(object):\n\tdef __init__(self,***)":
	"class %%% has-a __init__ that takes self and *** parameters.",
"class %%%(object):\n\tdef ***(self,@@@)":
	"class %%% has-a function named *** that takes self and @@@ parameters.",
"*** = %%%()":
	"set *** to an instance of class %%%.",
"***.***(@@@)":
	"From *** get the *** function, and call it with parameters self, @@@.",
"***.*** ='***'" :
	"From *** get the *** attribute and set it to '***'."
}

# do they want to drill pharas first
PHRASE_FIRST =False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST =True

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORD.append(word.strip())

def converts(snippet, phrase):
	class_name = [w.captalize() for w in
			random.sample(WORDS, snippt.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results= []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random. randlist(1,3)
		param.name.append(','.join(random.sample(WORDS, param_count)))
		param_names.append(','.join(random.sample(WORDS, param_count)))
	
	for sentence in phrase:
		result = sentence[:]

#fake class names
	for word in class_name:
		result = result.replace("%%%", word, 1)

#fake other name
	for word in other_name:
		result = result.replace("***",word,1)

#fake parameter lists
	for word in param_names:
		result = result.replace("@@@",word,1)
	
	results.append(result)
	return results

try:
	while True:
		snippet = PHRESES.key()
		random.shuffle(snippet)

		for snippets in snippet:
			phrase = PHRASES[snippets]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question , answer =answer , question
			print question
			raw_input("> ")
			print "ANSWER: %s\n\n" %answer
except EOFError:
	print "\nBYE"


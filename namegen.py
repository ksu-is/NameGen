import requests
import random

word_site = "https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co"

response = requests.get(word_site)
WORDS = response.content.splitlines()

the_name=''
the_gender=''
suggestions=''
number=0

def gen():
	global the_gender
	while True:
		baby_gender=input("What is the baby's gender?(boy or girl)")
		if baby_gender.isalpha():
			the_gender+=baby_gender
			break
		else:
			print("Please enter either boy or girl!")
gen()

def suggest():
	global the_word
	global suggestions
	for word in WORDS:
		gen=random.choice(WORDS).capitalize()
		print(gen.decode('utf-8'))
		like_or=input("Do you like this name? (yes or no)")
		if like_or=="yes":
			the_word+=str(gen.decode('utf-8'))
			break
		elif like_or=="maybe":
			global number 
			suggestions+=str(gen.decode('utf-8'))+"\n"
			number+=1
		if number==5:
			print(suggestions,"\n")
			would_you=input("Which one of these names do you like?")
			if would_you in suggestions:
				the_word+=would_you
				break
			else: 
				print("Copy the name exactly as it is above!")
				
suggest()

print("Your baby ",the_gender,"'s","name is ",the_name)

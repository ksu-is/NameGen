import requests
import random

word_site = "https://svnweb.freebsd.org/csrg/share/dict/propernames?view=co"

response = requests.get(word_site)
WORDS = response.content.splitlines()


the_gender=''
the_name=''
suggestions=''
number=0




def gend():
   global the_gender
   while True:
      your_gen=input("Is the baby a boy or girl?")
      if your_gen.isalpha():
         the_gender+=your_gen
         break
      else:
         print("Please try to use letters from the alphabet!")
gend()


def suggest():
   global the_name
   global suggestions
   for word in WORDS:
      gen=random.choice(WORDS).capitalize()
      print(gen.decode('utf-8'))
      happy_or=input("Do you like the name? (yes or no or maybe)")
      if happy_or=="yes":
         the_name+=str(gen.decode('utf-8'))
         break
      elif happy_or=="maybe":
         global number 
         suggestions+=str(gen.decode('utf-8'))+"\n"
         number+=1
      if number==5:
         print(suggestions,"\n")
         would_you=input("Which one of the suggestions do you like?")
         if would_you in suggestions:
            the_name+=would_you
            break
         else:
            print("Type the word in the suggestions correctly!")
                
      
            
suggest()
print("Your baby",the_gender,"'s","name will be:",the_name)

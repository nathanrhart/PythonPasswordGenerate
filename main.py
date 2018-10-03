"""AUTHOR: NathanHart - github.com/nathanrhart
   NOUNLIST AUTHOR: http://www.desiquintans.com/nounlist"""

import random
import time

wordlist = []
print("Password Generator V0.9")

def loadnouns():
  global wordlist
  print("Reading Nouns list TXT")
  file = open("parsednouns.txt")
  wordlist = file.read().splitlines()
  print("Amount of words: " + str(len(wordlist) ) )

minletters = 5
maxletters = 8
wordsamount = 4
noiselevel = 1
original = ""

def menu():
  print("\nChoose parameters by typing the number, followed by setting (if required)")
  print("minletters - Choose minimum letters in a word amount [1-30] default:5")
  print("maxletters - Choose maximum letters in a word amount [1-30] default:8")
  print("wordsamount - Choose amount of words to use [1-30] default:4")
  print("noiselevel - Choose level of noise to apply [0-3] default:1")
  print("generate - Generate your password")
  print("bruteforce - keep generating until last password is found")
  print("help - used to explain commands(no argument to reprint this menu)")

def takeinput():
  userinput = (input("Action: ")).lower().split(" ")
  while len(userinput) < 2:#this makes sure the user always sends 4 arguments
    userinput.append("")#add the blank arguments
  while len(userinput) > 2:#if the user inputted more than 4 'args'
    userinput.pop()#removing any extras they may put
  return userinput

def generate():
  global minletters
  global maxletters
  global wordsamount
  global noiselevel
  global wordlist

  password = ""
  global original
  original = ""
  
  ####START OF GENERATION
  for i in range(0, int(wordsamount)):
    randomword = ""
    while len(randomword) < minletters or len(randomword) > maxletters:
      randomword = random.choice(wordlist)
    original += randomword
    if noiselevel > 1:
      randomword = randomword.title()
    password += randomword

  if noiselevel == 1:
    password = password.replace("e","3")
    password = password.replace("i","1")
    password = password.replace("o","0")
    password = password.replace("s","5")

  elif noiselevel == 2:
    password = password.replace("e","3")
    password = password.replace("i","1")
    password = password.replace("o","0")
    password = password.replace("s","5")
    password = password.replace("t","7")
    password = password.replace("a","4")
    password = password.replace("b","8")
    password = password.replace("E","3")
    password = password.replace("I","1")
    password = password.replace("O","0")
    password = password.replace("S","5")
    password = password.replace("T","7")
    password = password.replace("A","4")
    password = password.replace("B","8")
  elif noiselevel == 3:
    password = password.replace("e","£")
    password = password.replace("i","1")
    password = password.replace("o","0")
    password = password.replace("s","$")
    password = password.replace("t","7")
    password = password.replace("a","@")
    password = password.replace("b","8")
    password = password.replace("E","£")
    password = password.replace("I","1")
    password = password.replace("O","0")
    password = password.replace("S","$")
    password = password.replace("T","7")
    password = password.replace("A","@")
    password = password.replace("B","8")
  
  print("Your new password is: " + password)
  print("Before noise was: " + original)
  ####END OF GENERATION
  command(takeinput())

def bruteforce():
  print("Starting brute force attack!")
  global original
  password = ""
  count = 0
  start = time.time()
  
  while password != original:
    count += 1
    password = ""
    for i in range(0, int(wordsamount)):
      randomword = ""
      while len(randomword) < minletters or len(randomword) > maxletters:
        randomword = random.choice(wordlist)
      password += randomword
    if count % 10000000 == 0:
      end = time.time()
      print("Time Spent: " + str(end-start) )
      print("Running Pass: " + str(count))
  if password == original:
    end = time.time()
    print("Password found! Amount of tries: " + str(count) )
    print("Time Spent: " + str(end-start) )
    print("Password was: " + original)
    menu()
    command(takeinput())
    
def command(userinput):
  global minletters
  global maxletters
  global wordsamount
  global noiselevel
  
  if userinput[0] == "minletters":
    try:
      minletters = int(userinput[1])
      print("Minimum letters per word is now: " + str(minletters))
    except: print("Check your inputs!")

  if userinput[0] == "maxletters":
    try:
      maxletters = int(userinput[1])
      print("Maximum letters per word is now: " + str(maxletters))
    except: print("Check your inputs!")
    
  elif userinput[0] == "wordsamount":
    try:
      wordsamount = int(userinput[1])
      print("Amount of words used is now: " + str(wordsamount))
    except: print("Check your inputs!")
    
  elif userinput[0] == "noiselevel":
    try:
      noiselevel = int(userinput[1])
      print("Noise level is now: " + str(noiselevel))
    except: print("Check your inputs!")

  elif userinput[0] == "generate":
    generate()
    return

  elif userinput[0] == "bruteforce":
    bruteforce()
    return

  elif userinput[0] == "help":
    if userinput[1] == "":
      menu()
      command(takeinput())
    elif userinput[1] == "minletters":
      print("how many letters have to be in each word to get chosen from the noun list")
    elif userinput[1] == "wordsamount":
      print("how many words will be used to make the password (can sometimes be more due to nouns list)")
    elif userinput[1] == "noiselevel":
      print("How much noise will be used: Examples(may vary)")
      print("0 - thefiveboxingwizardsjumpquickly - converts nothing")
      print("1 - th3f1v3b0x1ngw1zard5jumpqu1ckly - converts some letters to numbers")
      print("2 - 7h3F1v380x1ngW1z4rdsJumpQu1cjly - converts letters to numbers and titles")
      print("3 - 7h3F1v380x1ngW1z4rd$JumpQu1ck1y - converts letters to numbers and symbols and titles")


  command(takeinput())

def start():
  loadnouns()
  menu()
  command(takeinput())

start()

'''
author = Richard Kadlec
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']


username_database = ["Bob", "Ann", "Mike", "Liz"]
password_database = ["123", "pass123", "password123", "pass123"]

print("Welcome to the text analyzer")

print("x" * 100)

username = input("Please enter username: ")
password = input("Please enter password: ")

if username in username_database and password in password_database:
    print("Login Successful!")
else:
    print("Login fail")
    quit()

print("x" * 100)

chosen_text = input("There are 3 texts available for analysis, choose one of them -> 1, 2 or 3: ")

if chosen_text in ('1', '2', '3'):
    print("Text chosen")

else:
    print("You didn't choose any of the available texts")
    quit()

print("x" * 100)

splitwords = (TEXTS[int(chosen_text) -1]).split()
numberwords = len(splitwords)
print(f"There are {numberwords} words in the selected text.")

titlecased = 0
lowercount = 0
suppercount = 0
numericcount = 0
sum: int = 0

for i in splitwords:
    if (i.istitle()):
        titlecased = titlecased + 1
    elif (i.islower()):
        count1 = lowercount + 1
    elif (i.isupper()):
        count2 = suppercount + 1
    elif (i.isnumeric()):
        numericcount = numericcount + 1
        if i.isnumeric():
            sum = (int(i)) + sum

print(f"There are {titlecased} titlecase words.")
print(f"There are {lowercount} lowecase words.")
print(f"There are {suppercount} uppercase words.")
print(f"There are {numericcount} numeric words.")
print(f"If we summed up all the numbers in this text we would get: {sum}.")

print("x" * 100)

stripwords = []
for word in splitwords:
    clear_words = len(word.strip("., "))
    stripwords.append(clear_words)

occurencecount = {}
for word in stripwords:
    if word not in occurencecount:
        occurencecount[word] = 1
    else:
        word in occurencecount
        occurencecount[word] += 1

for num,occur in occurencecount.items(): print(num, occur * '*', occur)
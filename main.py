#samples of print statements
#python string manipulation
#brief tutorial for myself and others--R.H.
print("""welcome to my brief string samples file.
 Stay, have a coffee, practice or
 review your most common python string functions
 and tricks""")
 #Using python 3.x


#basic print statement
print("Good Morning!")
#result should show Good Morning!

#changing capital letters into lower case letters
print("DOGS ARE SILLY ANIMALS".lower())
#result should be dogs are silly animals

#changing lower case letters into upper case letters
print("dogs are silly animals".upper())
#result should be DOGS ARE SILYY ANIMALS

#using "camel" case
#strings which have capitols as first letter of words within a string
#sevral ways to do this, simplest being concantination of the words, one example below
print("hogs"+"Sausage"+"Bacon"+"Lard")
#plus sign and no spaces important to achieve a camel case string
#this is just one way to achieve this, but this looks easiest of all
#result should be hogsSausageBaconLard

#concatination of strings
#use the + sign to make strings longer
#print statement only needed if you desire to have a output to screen
#can save the string as an object instead, but not covered here
print( "pizza" + "is" + "tasty" + "food")
#notice this does not allow for spaces
#adding spaces inside the quotes will separate words, but won't be #"concatination"
#result should be pizzaistastyfood
#printing multiple lines of strings
#Uses the /n for one way to do this
print(''"Count to three!\n" "One\n" "Two\n" "Three\n"'')
#an additional quote will be needed to enclose the whole line of #strings
#Quotes around the strings and the line of strings must be different #style, or it won't work
#result should be:
#Count to three!
#One
#Two
#Three

#string length
#this is the len() function
#remember spaces are counted too!
print(len("Joe eats sloppy joes"))
#return will be 20
print(len("Joeeatssloppyjoes"))
#return will be 17


#searching if a character in a string
txt = "If I were rich, I would buy an island"
print("r" in txt)

#the result will be True, or False
#this example should be True

#searching if a character is NOT in a string
txt = "If I were rich, I would buy an island"
print("Q" in txt)
#result should be True or False
#in this example, it will be False

#capitalizing just the first letter of a string
print("elvis".capitalize())
#result should be Elvis

#converting first character in each word to upper case
print("mary had a large dinosaur". title())
#result should be
#Mary Had A Large Dinosaur


#count the number of times a certain item is in a string
print("hippity " + "hop " + "bunny")
#to find number of times "h" appears
#this is ONE way to do it
txt = "hippity  hop  bunny"
x = txt.count("h")
print(x)
#Result should be 2, in this example

#looping a string
for x in "parachute":
    print(x)
    #result will be all the characters printed on their own line
    #indented print is important

#
#data = "They walk to school and The dog jumps over the wall"
#print(data.swapcase())

#greet = "  They walk to school and The dog jumps over the wall"
#print(greet.lstrip())

#data = "They walk to school and The dog jumps over the wall"
#print(data.find("walk"))

#out = (data.find("the"))
#print("position:",out)

#data = "They walk to school and The dog jumps over the wall"
#print(data.find("from"))
#print(data.index("from"))

#data = "They walk to school and The dog jumps over to the wall"
#print(data.count("school"))


#data = "They walk to school and The dog jumps over to the wall"
#print(data.replace("to","lish",1))

#data = "They walk to school and The dog jumps over to the wall"
#print(data.split())
#print("".join(data))

#output =(data.rsplit("to",1))
#print(output)
#print("----".join(output))

#words = "i", "love","python"
#print("-".join(words))


#data = "They walk to school and The dog jumps over to the wall"
#print(data.startswith("They"))
#print(data.endswith("walls"))

#data = "They walk to school and The dog jumps over to the wall"
#print(data.isalpha())


#data = "hello"
#print(data.isalpha())

#data = "They walk to school and The dog jumps over to the wall"
#print(data.isalnum())

#data = "python222"
#print(data.isalnum())

#data = "python222"
#print(data.isalnum())

#data = "python 111"
#print(data.isalnum())

#data = "123"
#print(data.isdigit())

#data = "hello"
#print(data.isspace())

#data = "hello   "
#print(data.isspace())

#data = " "
#print(data.isspace())

 
#data = "They walk to school and The dog jumps over to the wall"
#print(data.islower())

#data = " easy python"
# print(data.islower())


#data = "India"
#print(data.isupper())

#data = "INDIA"
#print(data.isupper())

#data = "mr. sonu"
#print(data.removeprefix("mr. "))

#data = "python.py"
#print(data.removesuffix(".py"))

#data = "They walk to school and The dog jumps over to the wall"
#output = (data.split())
#for word in set(output):
   #if output.count(word) >1:
    # print(word)


#data = "Lishmitha"
#for ch in set(data):
    #if data.count(ch) >1:
        #print(ch)


#data = "lishmitha"
#vowels = "aeiouAEIOU"
#for ch in set(data):
    #if ch in vowels:
        #print(ch)


data ="hello world"
vowels = "aeiouAEIOU"
for ch in set(data):
    if ch in vowels:
        print(ch)
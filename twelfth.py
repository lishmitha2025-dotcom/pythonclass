# data = "pythonclass"

# print(data[2:11:3])

# data1 = " python class programme"
# print(data1.upper())

# out =  "python class programme"
# print(out.lower())
# print(out.capitalize())
# print(out.title())

# message = "      Hello   python     "
# print(message.strip())

# message = "Learn Python Programming"
# # print(message.find("Learn"))
# print(message.find("Python"))
# print(message.find("Programming"))

# message = "Learn Python Programming"
# # print(message.find("Python"))
# # print(message.find("Java"))
# print(message.index("python"))

# message = "Python is easy. Python is powerful."
# # print(message.count("is"))

# message = "I like Java. Java is popular java java"

# # print(message.replace("Java","Python"))
# print(message.replace("Java","python",2))

# sentence = "Python is easy to learn"
# print(sentence.split())

# data = "python, sql,python,java"
# out = data.split()
# print(out)

# message = "Python is easy. Python is powerful."
# print(message.rsplit())
# print(message.split())

# word = "python", "java", "sql"
# print(",".join(word))

# data = "python is very easy to me"
# print(data.startswith("python"))
# print(data.endswith("me"))
# print(data.endswith("to"))


# data = "python"
# print(data.isalpha())

# data1 = "python1"
# print(data1.isalpha())
# data = "1245 python"
# print(data.isdigit())
# data1 = "122672829"
# print(data1.isdigit())


# data = "Python1222"
# print(data.isalpha())
# data1 = "python 1222"
# print(data1.isalpha())

# print("Python123".isalnum())
# data ="Python123"
# print(data.isalpha())

# print(" ".isspace())
# print("".isspace())

# name = "lishmith"
# location = "bangalore"

# output = f"my name is {name},im from {location}"
# print(output)


# a = 10
# b = 20
# print(f"total amount is {a + b}")

# salary = 2500000
# print(f" salary :{salary}")

# name = "Anita"
# course = "Python"

# message = "Student {} is learning {}".format(name, course)
# print(message)

# s = "PYTHON"
# s = s.replace("P", "J")
# print(s)


# name = "python"
# new_name = name.upper()
# print(new_name)

# a = "python"
# b = "java"
# c = "".join(["py","va"])
# print(c)


# a = "Python"
# c = "Python"
# d = "".join(["Py", "thon"])
# print(a == c, a is c)  
# print(d)

# marks = {"janu" : 80 , "manu" : 90}
# print(marks["manu"])
# print(marks["janu"])

# name = {"apple", "banana","apple"}
# print(name)

# data  = "hello student\nwelcome to pythnon class"
# print(data)

# data = "name\tage\tloaction"
# print(data)


# data = "it\'s a beautyfull day"
# print(data)
# data = "he said that \"python\" is easy"
# print(data)

# s = "PYTHON"
# s = s.replace("P", "J")
# print(s)

# countries = ["IND", "USA", "AUS", "SL", "JPN", "UAE"]
# print(countries[1])
# print(countries[-1])
# print(countries[-2:])
# print(countries[1::2])
# print(len(countries[1::2]))

# print(countries[5][1])
# print(countries[3][1:])
# print(countries[1][1:])


# data = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
# ]

# print(data[1])
# print(data[2:])
# print(data[:2])

# country = "INDIA"
# print(list(country))

# country =["India","sri land"]
# new = country[1] = "Bhuthan"
# print(new)

# fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
# print(fruits[2])
# print(fruits[-1])
# print(fruits[-2])
# print(fruits[-3])


# data = [1, 2, 3, 4, 5, 6, 7]
# print(data[1:])
# print(data[:6])
# print(data[:5])
# print(data[:4])
# print(data[3:])

# letters = ["A", "B", "C", "D"]
# print(letters[::-1])

# country = "INDIA"
# print(country[::-1])

# mark = [10 , 20, 40, 50]
# mark[0] = 100
# mark.append(99)
# print(mark)

# num = [ 20, 30, 40, 50]
# num[1] = 35
# num.append(90)
# print(num)

# num1 = [20, 30, 40]
# num1.append(100)
# print(num1)

# data = ["anu", "manu", "sonu"]
# data.append("janu")
# print(data)


# data = [ 50, 260, 70, 80]
# data.extend([90,100])
# print(data)


# data = [10, 20, 30, 40]
# data.append([60, 70])
# data.extend([100,200])
# print(data)

# data = [20, 40, 50, 60]
# data.insert(0,10)
# print(data)

# data = ["janu", "manju", "sonu"]
# data.remove("manju")
# print(data)

# data = ["jan","manju","soji"]
# print(data.pop(2))
# print(data)

# num = [10, 20, 30]
# del num [2]
# print(num)

# data = [20,30,40,60]
# del data[3]
# print(data)

# numbers = [10, 20, 30, 40, 50]
# del numbers[1::2]
# print(numbers)


# numbers = [10, 20, 30, 40, 50]
# numbers.clear()
# print(numbers)


# numbers = [10, 20, 10, 30, 10, 40]
# # print(numbers.count(10))

# print(numbers.index(30))

# numbers = [40, 10, 30, 20]
# numbers.sort()
# print(numbers)

# numbers = [40, 10, 30, 20]
# numbers.sort(reverse=True)
# print(numbers)

# numbers = [40, 10, 30, 20]
# out = sorted(numbers)
# print(sorted(out,reverse=True))


# data = [ 100, 80, 10, 90, 20, 50]
# # output = sorted(data)
# # print(sorted(output,reverse=True))

# print(sorted(data,reverse=True))

# names = ["Ravi", "Anu", "Kiran", "Manoj"]
# print(names.sort())

# numbers = [10, 20, 30, 40]
# out  =(numbers.reverse())
# print(out)


# numbers = [10, 20, 30, 40]
# output = reversed_number = numbers[::-1]
# print(output)

# num1 = [20, 30]
# num2 = [40, 50]
# combine = num1 + num2
# print(combine)


# num = [10, 20, 30, 20, 49]
# print(sum(num))
# print(min(num))
# print(max(num))
# print(sum(num)/len(num))
# num.sort()
# print(num)

# num = [10, 20, 30, 20, 49]
# num.sort()
# print(num)

# num = [10, 20, 30, 20, 49]

# # output = sorted(num)
# # print(output)

# result = sorted(num,reverse=True)
# print(result)

# num = [10, 20, 30, 20, 49]
# result = sorted(num)[-2]
# print(result)
# result1= sorted(num)[2]
# print(result1)
# result2= sorted(num)[:-2]
# print(result2)
# result3 = sorted(num)[2:]
# print(result3)

# names = ["Ravi", "Anu", "Kiran", "Anu", "Ravi"]
# uniq = list(set(names))
# print(uniq)

# numbers = [10, 20, 30, 40, 50, 60]
# rotation = numbers[1:] + numbers[:2]
# print(rotation)

# student = "Anu", 21, "Python"
# print(type(student))

# student = ("Rahul", 22, "Bengaluru")
# name, age, location = student
# print(name)
# print(age)
# print(location)

# languages = ("Python", "Java", "JavaScript", "SQL")

# print(languages[0])
# print(languages[1])
# print(languages[2])


# numbers = (10, 20, 30, 40, 50, 60)
# print(numbers[0::2])

# numbers = (10, 20, 30, 40)

# print(len(numbers))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# print(sorted(numbers))

# students = (
#     ("Rahul", 22),
#     ("Anu", 21),
#     ("Kiran", 23)
# )

# print(students[0])
# print(students[0][1])

# numbers = {10, 20, 20, 30, 30, 30}

# print(len(numbers))

# number = {10, 20}
# number.add(50)
# print(number)

# numbers = {10, 20}
# numbers.update([100, 90])
# print(numbers)

# # numbers = {10, 20}

# # numbers.update([30, 40])

# # print(numbers)


# numbers = {10, 20, 30}

# numbers.discard(50)

# print(numbers)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.union (b))
# print(a.intersection(b))
# print(a.difference(b))

# a = frozenset((10, 20, 30))
# b = frozenset({40, 50, 60})

# print(a)
# print(b)




# student = {
#     "name": "Anu",
#     "age": 21,
#     "course": "Python"
# }

# print(student["name"])
# print(student.get("name"))

# student.update({"age":30}) 
# print(student)



print(2//1)
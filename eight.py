# a = [10, 20, 30, 20, 40]

# a.sort()
# print(a)

# max = (max(a))
# print(max)

# data = (set(a))
# print(data)

# maxi = a.sort()
# print(a[-2])

# maxim = a.sort()
# print(a[-3])

# min = (min(a))
# print(min)


# data = frozenset(["anu","manu","sonu", "manu"])
# print(data)

# num = frozenset([1, 2, 3, 4, 3])
# print(num)

# south_state = frozenset(['KA','KE', 'AP', "TN"])
# north_state = frozenset(['AS','BI', 'CH', 'DL', 'GU'])

# output = south_state.union(north_state)
# print(output)

# data = {"name": "anu",
#         "age": 20,
#         "skills": ["excel", "sql"]
#         }

# # print(data["name"])
# # print(data["age"])
# # print(data["skills"])

# print(data.get("name"))
# print(data.get("city"))
# print(data["city"])

profle = {"name" : "janu",
          "age" : 20,
          "salary" : 20000,
          "name" : "mani",
          "age" : 25, 
          "salary" : 15000
       }

# print(profle.get("name"))
# print(profle.get("salary"))
# print(profle.get("age"))

# print(len(profle))

# print(list(profle.keys()))
# print(list(profle.values()))

# profle["salary"] = 50000

# print(profle.get("salary"))

# profle.update({"age" : 25 , "age" : 26 , "skill" : {"read" , "write"}})
# print(profle)

# profile = {"name" : "manju",
#            "age" : 24,
#            "location" : "tumkur",
#            "salary" : 60000
#            }
# print(profile)

# print(profile.get("age"))
# print(profle.get("name"))
# print(profile["salary"])
# profile["salary"] = 80000
# print(profile)
# profile.update({"age" : 24, "age" :25, "salary" : 80000 , "salary" : 1000000, "branch" : "indiranagar"})
# # print(profile)

# profile.update({"skills" : ["excel" , "sql", "python"]})
# # print(profile)

# profile.update({"heigh" : "6"})
# print(profile)

# profile.pop("heigh")
# print(profile)

# data = range (0, 11)
# print(list(data))
# even = range(2, 11, 2)
# print(list(even))
# odd = range (1, 11, 2)
# print(list(odd))

# greet = "anu" , "manu", "janu"
# print(type(greet))

# num = (1, 2, 3, 4, 5, 6, 3, 3, 3)
# print(num.count(3))

# print(num.index(3))

data = {"anu", "manu","janu"}
print(type(data))

num1 = {10, 20, 30, 40}
num2 = {50, 20, 60, 10}

ouput = num1.union(num2)
print(ouput)

out = num1.intersection(num2)
print(out)

put = num1.difference(num2)
print(put)
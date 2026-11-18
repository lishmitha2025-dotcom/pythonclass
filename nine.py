# a = "20", "30", "40"
# print(type(a))

# num = (10, 20, 30, 40, 20)
# print(num.count(20))
# print(num.index(40))

# data = "anu" ,"manu", "sonu","anu"
# print(data.index("manu"))
# print(data.count("anu"))

# data1 = {20, 30, 40, 50, 40, 60}
# data2 = {70, 80, 30, 20, 90, 90}


# print(data1.union(data2))
# print(data1.difference(data2))
# print(data1.intersection(data2))

# output = {10, 20, 30, 40}
# output.add(80)
# print(output)
# output.remove(20)
# print(output)
# output.pop()
# print(output)

# south_state = frozenset (['KA', "KE", "TE", "AP"])
# north_state = frozenset (["AS", "TN","BI","CH","DL","KA"])

# output = south_state.union(north_state)
# print(output)
# print(hash(output))

# south_state = {"AP","KA", "TE", "TN"}


# employee = { "name":"sonu",
#             "age": 25,
#             "salary" : 25000,
#             "location" : "bangalore"
#             }

# print(employee)
# print(employee.keys())
# print(employee.values())
# print(employee("team"))

# print(employee["age"])
# print(employee["location"])
# print(employee["name"])
# print(employee["salary"])

# print(employee.get("team"))
# print(employee.get("name"))
# print(employee.get("age"))
# print(employee.get("branch" ,"Key Not Found"))

# employee.update({"age" : 25, "age" : 28})
# print(employee)

# print(len(employee))
# print(employee)

# data = dict([["name", "sonu","manu"], ["age" ,26], ["skill", ["excel","sql"]]])
# print(data)

# out = dict([["fn", "sonu"]])
# print(out)

# employee["heigh"]=6
# print(employee)
# employee.pop("age")
# print(employee)
# employee.popitem()
# print(employee)

# employee = { "name":"manu",
#             "age": 28,
#             "salary" : 35000,
#             "location" : "mangalore"
#             }


# print(employee.setdefault("branch" , "jyothi"))

# print(employee.get("weight", 60))

# print(employee)

data = [
    {
        "id": 0,
        "title": "string",
        "price": 0.1,
        "description": "string",
        "category": "string",
        "image": "http://example.com"
    },
    {
        "id": 0,
        "title": "string",
        "price": 0.1,
        "description": "string",
        "category": "string",
        "image": "http://example.com"
    },
    {
        "id": 0,
        "title": "string",
        "price": 0.1,
        "description": "string",
        "category": "string",
        "image": "http://example.com"
    }
]

# print(data)
print(data[0].get("price") + data[1].get("price") + data[2].get("price"))



sum = 0

for data in datas:
    sum += data.get("price")

print(f"total is {sum}")

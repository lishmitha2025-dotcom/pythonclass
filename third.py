# data = "good morning!"

# data = []
# print(data)

# data = [1, 2, 3, 4, 5]
# print(data)

# data = ["AA", "BB", "CC"]
# print(data)

# data = list("123")
# print(data)

# data = [1,2,3]
# print(data)

# data = ["IND","USA","AUS","SL","JAP","MAL"]
# print(data[2:6])
# print(data[-1])

# country = ["IND","USA","AUS","SL","JAP","MAL",True]
# print(type(country))
# print(type(country[-2]))
# print(type(country[-1]))

country = ["IND","USA","AUS","SL","TRKY","MAL",True,500]
# data = (country[0])
# print(data)
# data = (country[0][2])
# print(data)
# data = (country[3][1])
# print(data)
# print(country[-1][0])

# country = ["IND","USA","AUS","SL","TRKY","MAL","True","500"]
# print(country[-1][1])
# print(country[-2][1])

# twos_tabale = [[2, 1, 2],
#                [2, 2, 4],
#                [2, 3, 6],
#                [2, 4, 8],
#                [2, 5, 10]]

# print(twos_tabale[2])
# print(twos_tabale[2][-1])
# print(twos_tabale[2][2])

# country = "IND"
# print(country[1])

# country = ["IND","  "]
# print(len(country))

# country = [["IND","UAS"]]
# print(len(country))

# countries = ["IND", "UAS"]
# print(len(countries))

# countries = ["IND","SL"]
# countries[0] = "USSR","MAL"
# print(countries)


# countries = ["IND","SL"]
# countries[1] = "USSR","MAL"
# print(countries)

# south = ["KA", "KE", "TE", 'AP', "TS"]
# north = ["AA", "BB", "CC", "DD"]
# print(south,north)

# south_states = ['KA', "KE", "TE", 'AP']
# north_states = ['AS', 'BI', 'CH', 'DL']

# states = [south_states, north_states]

# print(states)
# print(south_states)
# print(north_states)
# print(id(south_states))
# print(id(north_states))
# print(id(states))

# states[1] = ['MH', 'MP', 'MG']

# print(states)
# print(south_states)
# print(north_states)
# print(id(south_states))
# print(id(north_states))
# print(id(states))

data1 = ['A', 'B']
data2 = data1

# print(id(data1),data1)
# print(id(data2),data2)

# data2 = ['C', 'D']

# print(id(data1),data1)
# print(id(data2),data2)
# data2[0] = 'F'

# print(id(data1),data1)
# print(id(data2),data2)


tiffin_box = ['apple']
bag =[tiffin_box]
print(tiffin_box,bag)
print("tiffin_box",id(tiffin_box))
print("bag",id(bag))

tiffin_box = ['mango']
print(tiffin_box)
print(bag)
print("tiffin_box",id(tiffin_box))
print("bag",id(bag[0]))

bag = [tiffin_box]
print(bag)
print(id(bag[0]))

tiffin_box = ['apple']
bag = [tiffin_box]
print(tiffin_box)
print(bag)
print("tiffin_box",id(tiffin_box))
print("bag",id(bag[0]))
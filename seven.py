
# odd = range(1, 11)
# print(list(odd))

# odd_number = range(2, 11, 2)
# print(list(odd_number))

even_number = range(1, 11, 2)
print(list(even_number))

# reverse_1 = range(10, 0, -1)

# print(list(reverse_1))




# state = ["KA", "KE", "TE", "AP","KA", "KA","TE"]

# state = set(state)

# print(state)


# south_state = ['KA','KE', 'AP', "TN"]
# north_state = ['AS','BI', 'CH', 'DL', 'GU']

# state = south_state + north_state
# print(state)

# south_state = set(['KA','KE', 'AP', "TN"])
# north_state = set(['AS','BI', 'CH', 'DL', 'GU'])

# state = south_state.union(north_state)
# print(state)
# print(south_state)
# print(north_state)


south_state = set(['KA','KE', 'AP', "TN"])
north_state = set(['AS','AP', 'CH', 'DL', 'GU'])


state = south_state.intersection(north_state)

# print(state)
# print(south_state)
# print(north_state)

# state = south_state.intersection_update(north_state)

# print(state)
# print(south_state)
# print(north_state)

# state = south_state.difference(north_state)

# print(state)
# print(south_state)
# print(north_state)

# south_state = set(['KA','KE', 'AP', "TN"])
# south_state.remove('AP')
# print(south_state)
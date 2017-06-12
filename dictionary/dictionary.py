temp_key = 'hello'
zombie0 = {
    temp_key: 10,
    'power': 6,
    'hunger':5,
    'name': 'Will'
}

print(zombie0['power'])
# print(zombie0['speed'])


zombie0['weapon'] = 'axe'
zombie0['position_x'] = 23
print(zombie0)

# You can delete with delete

zombie0['huh'] = 'pointless'
del zombie0['huh']
print(zombie0)



#for loops through dict start with property placeholder followed by key-value

# for key, value in zombie0.items():
#     print('the key is ' + key + ' with a value of:' + str(value))
#     print(zombie0[key])
#
# print(zombie0.__contains__('name'))
# print(zombie0p[key])

# Eliminate value a just get the value from the dic[key]

# for key in zombie0:
#     print(zombie0[key])

# you can sort the dictionary in natural order
for key in sorted(zombie0):
    print(key + ": " + str(zombie0[key]))

# Like js, you can pout your dicitonaries in lists (or tuples)

zombies = [] # zombies is an empty list
zombies.append({
    'speed':10,
    'power':6,
    'hunger':5,
    'name': 'Joe'
})

zombies.append({
    'speed': 5,
    'power': 16,
    'hunger': 9,
    'name': 'Hank'
})
print(zombies)

for zombie in zombies:
    print(zombie['name'])

# Just like in JS you can assign a list to a dictionary
zombies[0]['victims'] = ['Jane', 'Zane', 'Bill']
print(zombies)
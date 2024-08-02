# 2
my_dict = {'Andrey': 38, 'Tanya': 22}
print(my_dict)

print(my_dict['Andrey'])

my_dict['Petya'] = 35
print(my_dict['Petya'])

my_dict.update({'Juliya': 25, 'Diana': 24})

removed_value = my_dict.pop('Petya')
print(removed_value)

print(my_dict)

# 3
my_set = {1, 3.0, 2, 'a', 'a', 2, 'b', 3.0, True}
print(my_set)

my_set.update([7, 8])

my_set.discard(2)

print(my_set)

# 2
immutable_var = 1, 2, 3, 'a', 'b', 'c', True
print(immutable_var)

# 3
# immutable_var[0] = 5
# print(immutable_var)
# 'tuple' object does not support item assignment
print(type(immutable_var))

# 4
mutable_list = [1, 2, 3]
mutable_list[0] = 5
print(mutable_list)

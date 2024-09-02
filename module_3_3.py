def print_params(a=1, b='string', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params([1, 2, 3])
print_params(c=5, b=7, a=[1, 2, 3])
print_params(5, 7, [1, 2, 3])

values_list = [1, 'a', True]
values_dict = {'a': 8, 'b': 'string', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [999, True]
print_params(*values_list_2, 777)

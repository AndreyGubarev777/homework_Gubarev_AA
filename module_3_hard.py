data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_structure):
    calculate = 0

    if isinstance(data_structure, list):
        for i in data_structure:
            calculate += calculate_structure_sum(i)

    elif isinstance(data_structure, tuple):
        for j in data_structure:
            calculate += calculate_structure_sum(j)

    elif isinstance(data_structure, set):
        for k in data_structure:
            calculate += calculate_structure_sum(k)

    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            calculate += calculate_structure_sum(key)
            calculate += calculate_structure_sum(value)

    elif isinstance(data_structure, (int, float)):
        calculate += data_structure

    elif isinstance(data_structure, str):
        calculate += len(data_structure)

    return calculate


result = calculate_structure_sum(data_structure)
print(result)

calls = 0

def count_calls(call):
    global calls
    calls += call
    return calls


def string_info(string):
    variable = []
    variable.append(len(string))
    variable.append(string.upper())
    variable.append(string.lower())
    count_calls(1)
    return variable


def is_contains(string_info, is_contains):
    string_info.lower()
    new_is_contains = []
    count_calls(1)
    for i in is_contains:
        new_is_contains.append(i.lower())
    return (string_info.lower() in new_is_contains)


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
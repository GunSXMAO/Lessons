calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    string_len = len(str((string)))
    string_up = string.upper()
    string_lower = string.lower()
    tuple_string = (string_len, string_up, string_lower)
    count_calls()
    print(tuple_string)

def is_contains(string, list_to_search):
    string_lower = string.lower()
    list_to_search_new = []
    count_calls()
    for i in list_to_search:
        low = i.lower()
        list_to_search_new.append(low)
    if string_lower in list_to_search_new:
        return print(True)
    else:
        return print(False)



string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN']) # Urban ~ urBAN
is_contains('cycle', ['recycling', 'cyclic']) # No matches
print(calls)

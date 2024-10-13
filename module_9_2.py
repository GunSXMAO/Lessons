first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
combined_strings = first_strings + second_strings

first_result = [len(x) for x in first_strings if len(x)>= 5]
second_result = [(i, y) for i in first_strings for y in second_strings if len(i) == len(y)]
third_result = {x: len(x) for x in combined_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)

dic_num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
           'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
           'eighteen': 18, 'nineteen': 19, 'twenty': 20}
# data_input = 'five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
data_input = list(set(input('Input your string:\n').split()))

data_input.insert(0, [0, 0, 0, 0])

print('Sum and product of numbers:')
for i in dic_num:
    if i in data_input[1:]:
        data_input.append(dic_num[data_input.pop(data_input.index(i))])      # Extract the text and add a number.

        data_input[0][1], data_input[0][2] = data_input[0][2], dic_num[i]    # Numbers that we will perform operations on.

        if type(data_input[-1]) == int and type(data_input[-2]) == int:
            if data_input[0][3] == 0:
                print(data_input[0][1] * data_input[0][2], end=' ')          # Output the results of operations.
                data_input[0][3] = 1
            else:
                print(data_input[0][1] + data_input[0][2], end=' ')          # Output the results of operations.
                data_input[0][3] = 0

        if dic_num[i] % 2 != 0:
            data_input[0][0] += dic_num[i]                                   # Sum of odd numbers.
print()
print('Ordered list:', data_input[1:], sep='\n')
print('Sum of odd numbers:', data_input[0][0], sep='\n')



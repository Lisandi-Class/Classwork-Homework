'''Print the location of every letter ‘o’ in the following string
phrase = ‘How much wood could a woodchuck chuck if a woodchuck could chuck wood’
Perform the exercise both as a regular iteration and as a list comprehension
Make the code flexible to find any character
Exercise 1b
Count the number of times each letter encountered appears in the phrase
I will work it into populi tomorrow with the instructors but this should give you a nice challenge '''


from pprint import pprint

phrase = 'How much wood could a woodchuck chuck if a woodchuck could chuck wood'
indicies_of_o = []

for index in range(len(phrase)):
    if 'o' == phrase[index]:
        indicies_of_o.append(index)
        
def which_index(astring,target):
    return [f'{target} at {index}' for index in range(len(phrase)) if target == astring[index] ]

pprint(which_index(phrase, 'o'))
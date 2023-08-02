# calling methods 
# append and remove 

acronyms = ['LOL', 'IDK', 'SMH']

# add new acronym to end of list 
acronyms.append('BFN')
print(acronyms)

# remove BFN from list 
acronyms.remove('BFN')
print(acronyms)

# add it back 
acronyms.append('BFN')
print(acronyms)
# this could also be done by specificying index with del keyword
del acronyms[3]
print(acronyms)

# check if exists in list 
if 1 in [1, 2, 3, 4, 5]:
    print('true')

word = "BFN"

if word in acronyms: 
    print(word + ' is in the list')
else:
    print(word + ' is not in the list')

# printing a list on new line
# syntax of a for loop
for acronym in acronyms:
    print(acronym)

# key value pairs 
acronyms = {'LOL' : 'laugh out loud',
            'IDK' : "I don't know", 
            'TBH' : 'to be honest'}

# acronyms['TBH'] = 'honestly'

# print(acronyms['TBH']) # honestly 

del acronyms['LOL'] 
print(acronyms) 

definition = acronyms.get('BTW')
print(acronyms) 

# none represents the absence of a value 
# instead of an error 

if definition:
    print(definition)
else:
    print("Key does not exist")

sentence = 'IDK' + ' what happened ' + 'TBH'
translation = acronyms.get('IDK') + ' what happened ' + acronyms.get('TBH')

print('sentence:', sentence)
print('translation:', translation)






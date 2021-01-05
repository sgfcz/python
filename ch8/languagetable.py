table = {'Python':'Guido van Rossum',
          'Perl':  'Larry Wall',
          'Tcl':   'John Ousterhout'}
language = 'Python'
creator = table[language]

print(creator)

for lang in table:
    print(lang, '\t', table[lang])
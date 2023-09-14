dictionary = {"a": 0, "b": 1, "c": 1, "d": 2, "e": 3}

""" Geef aan wat volgende code print"""
" Vul aan: {'a': 0, 'b': 1, 'c': 1, 'd': 2, 'e': 3}"
print(dictionary)

" Vul aan: a"
for x in dictionary:
    print(x)

" Vul aan: b"
print( list(dictionary.keys()))

" Vul aan: c"
print( dictionary.get("e", 4))

" Vul aan: d"
print( list(dictionary.values()))

" Vul aan: e"
print( dictionary.get("q", 4))

" Vul aan: ['a', 'b', 'c', 'd', 'e']"
for x, y in dictionary.items():
    print(y, x)

" Vul aan: 3"
for x in dictionary.values():
    print(x)

" Vul aan: 1"
print( dictionary.pop("c"))

"Vul aan: [('a', 0), ('b', 1), ('d', 2), ('e', 3)]"
print( list(dictionary.items()) )

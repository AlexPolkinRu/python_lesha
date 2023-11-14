dict1 = {'cd': 'sass', 'mum': 'utys', 'man': 'hjht' }
a = input('введите слово или фразу\n')
words = a.lower().split()
# print(words)
list1 = []
for word in words:
    if word in dict1:
        list1.append(dict1[word])
    else:
        list1.append(word)
print(" ".join(list1))
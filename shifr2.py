alfabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
perevedi = input('пожалуйста напишите сообщение для разшифровки\n').lower()
key = int(input('подалуйста введите ключ от 1-25\n'))
shifrovka = ""
for bukva in perevedi:
    if bukva in alfabet:
        position = alfabet.find(bukva)
        newposition = position - key
        shifrovka = shifrovka + alfabet[newposition]
    else:
        shifrovka = shifrovka + bukva
print(shifrovka)
#o nuvk tu ktkse yvoky gxk xkgjotm znoy huuq,ux znke`rr ixgiq uax iujk...
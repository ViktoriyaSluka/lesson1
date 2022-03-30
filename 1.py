import hashlib




hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())



def bucket(fruit):
    if (fruit == 'яблоко'): return 0
    if (fruit == 'слива'): return 1
    if (fruit == 'груша'): return 2


spisk = [11, 20, 8]


slovar = {
    'яблоко': 11,
    'слива': 20,
    'груша': 8
}


#put = input()


#print(slovar[put])


#print(spisk[bucket(put)])

#яблоко - 33 - 90

#груша - 4

#слива - 19


b = 'яблоко'

print(hash(b))


a = (1,2,2,2,2,2,2,2)
b = (1,2,2,2,2,2,2,2)




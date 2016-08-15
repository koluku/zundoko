# -*- coding: utf-8 -*-

import random

zun = 'ズン'
doko = 'ドコ'
zundoko =['ズン','ドコ']
kiyoshi = 'キ・ヨ・シ！'

set = []
mutch = ['ズン','ズン','ズン','ズン','ドコ']
while set != mutch:
    if len(set) == 5:
        del set[0]
    set.append(random.choice(zundoko))
    print(set[-1])
print(kiyoshi)

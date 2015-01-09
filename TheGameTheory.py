__author__ = 'ReadTheManual'

import random

"Always Cooperate: cooperate on every move"
a = 0
acounter = 0

"Always Defect: defect on every move"
b = 1
bcounter = 0

"Random Player: makes a random move"
ccounter = 0

"Tit for Tat: cooperates on the first move, then copies the opponent’s last move"
d = 0
dy = 0
dn = 1
dcounter = 0

"Grim Trigger: cooperates, until the opponent defects, and thereafter always defects"
e = 0
ey = 0
en = 1
ecounter = 0

counter = 0
while counter < 1000:
    if (a > b):
        acounter += 15
    elif (b > a):
        bcounter += 15
    elif (b == 0):
        acounter += 11
        bcounter += 11
    else:
        acounter += 5
        bcounter += 5
    counter += 1

counter = 0
while counter < 1000:
    c = random.randint(0,1)
    if (a > c):
        acounter += 15
    elif (c > a):
        ccounter += 15
    elif (c == 0):
        acounter += 11
        ccounter += 11
    else:
        acounter += 5
        ccounter += 5
    counter += 1

counter = 0
while counter < 1000:
    c = random.randint(0,1)
    if (b > c):
        bcounter += 15
    elif (c > b):
        ccounter += 15
    elif (c == 0):
        bcounter += 11
        ccounter += 11
    else:
        bcounter += 5
        ccounter += 5
    counter += 1

counter = 0
while counter < 1000:
    if (a > d):
        acounter += 15
        d = dn
    elif (d > a):
        dcounter += 15
        d = dy
    elif (d == 0):
        acounter += 11
        dcounter += 11
        d = dy
    else:
        acounter += 5
        dcounter += 5
        d = dn
    counter += 1
d = dy

counter = 0
while counter < 1000:
    if (d > b):
        dcounter += 15
        d = dy
    elif (b > d):
        bcounter += 15
        d = dn
    elif (b == 0):
        dcounter += 11
        bcounter += 11
        d = dy
    else:
        dcounter += 5
        bcounter += 5
        d = dn
    counter += 1
d = dy

counter = 0
while counter < 1000:
    c = random.randint(0,1)
    if (d > c):
        dcounter += 15
        d = dy
    elif (c > d):
        ccounter += 15
        d = dn
    elif (c == 0):
        dcounter += 11
        ccounter += 11
        d = dy
    else:
        dcounter += 5
        ccounter += 5
        d = dn
    counter += 1
d = dy

counter = 0
while counter < 1000:
    if (a > e):
        acounter += 15
        e = en
    elif (e > a):
        ecounter += 15
    elif (e == 0):
        acounter += 11
        ecounter += 11
    else:
        acounter += 5
        ecounter += 5
        e = en
    counter += 1
e = ey

counter = 0
while counter < 1000:
    if (b > e):
        bcounter += 15
        e = en
    elif (e > b):
        ecounter += 15
    elif (e == 0):
        bcounter += 11
        ecounter += 11
    else:
        bcounter += 5
        ecounter += 5
        e = en
    counter += 1
e = ey

counter = 0
while counter < 1000:
    c = random.randint(0,1)
    if (c > e):
        ccounter += 15
        e = en
    elif (e > c):
        ecounter += 15
    elif (e == 0):
        ccounter += 11
        ecounter += 11
    else:
        ccounter += 5
        ecounter += 5
        e = en
    counter += 1
e = ey

counter = 0
while counter < 1000:
    if (d > e):
        dcounter += 15
        e = en
    elif (e > d):
        ecounter += 15
    elif (e == 0):
        dcounter += 11
        ecounter += 11
    else:
        dcounter += 5
        ecounter += 5
        e = en
    counter += 1
e = ey

print ("Always Cooperate =",acounter)
print ("Always Defect =",bcounter)
print ("Random Player =",ccounter)
print ("Tit for Tat =",dcounter)
print ("Grim Trigger =",ecounter)
input()

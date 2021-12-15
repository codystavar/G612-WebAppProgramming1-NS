
# import flask #se importa un cod extern pentru API
# from flask import Flask #acelasi mod


# if(): fara brackets, se da tab sau 4 space sau enter

#declare variabila
variabila1 = 10
variabila2 = 23.04
variabila3 = 'string'
variabila4 = "alt string"
variabila5 = [1,2,3,4,5,6]
variabila6 = (1,2,3,4)

variabila7 = {
'a' : 'a',
'b' : '32432',
'c' : 20,
'd' : {
    'e' : [2,45]
   },
   'f': [],   # v
   (1,2): 'a' #tupple
}
variabila7['c'] = [1,2,3,4,5,6]
variabila7['g'] = 'qwrqwrqwrwq'
pprint(variabila7)
 
variabila8 = """"acesta este
un string pe mai multe randuri"""
#un tip imuatibil se creeaza o zona diferita de memorie si se creaza un nou obiect de acel tip care se baga aceasi valoare
#un tip mutabil nu se recreaza prin acest assignment sau prin modificarea valorilor, nu se creaza o noua zona de memorie care sa se tina acea informatie; cand vorbim de o colectie
#o zona intiala iar apoi daca modificam sau scoatem un element, noi nu recream lista

#conditia if
if variabila1 > 20: # sau if (variabila > 20 and variabila2 < 0) or not variabila2 == 20:
    print(variabila1)
elif variabila1<10:
        print('bb')
else:
    print('else')


#for

for el in variabila71:
    for el2 in variabila5:
        print (el, el2)

#while
a = 10
while a > 0:
    print(a)
    a = a - 1

import re


print("""
    **         Welcome MadLib Player!        **
    **       Get ready to have some fun      **
    **         Type during the prompt        **
           """)
   

def read_template(a):
    with open(a)as text:
        readtemp = text.read()
        return readtemp
# input file path  output returns file path

def parse_template(string):
    parser = tuple(re.findall(r"\{([A-Za-z0-9 '_]+)\}", string))
    parser1 = string.replace(parser[0], "")
    parser1 = parser1.replace(parser[2], "")
    return(parser1, parser)

def merge(x, y):
    str1 = x.format(y[0], y[1], y[2])
    print(str1)
    return str1

 

adject = input('enter in adjective ')
adject1 = input('another adjective ')
name = input('name? ')
verb = input('a verb ')
adject2 = input('more adjective please ')
adject3 = input('more please! ')
noun1 = input('plural noun ')
anim1 = input('favorite large animal ')
anim2 = input('favorite small animal ')
girl = input('a girl\'s name ')
adject4 = input('my apologies, last adjective please! ')
noun2 = input('plural noun ')
adject5 = input('adjective last one I swear! ')
noun3 = input('plural noun ')
num50 = input('number 1 - 50 ')
num = input('any number ')
noun4 = input('plural noun ')
num2 = input('any number ')
noun5 = input('plural noun ')

with open('./assets/madlib.txt', 'r') as madlib:
    insert = madlib.read() 

    # updated = updated[22:]
    insert = insert.replace('{Adjective}', adject, 1)
    insert = insert.replace('{Adjective}', adject1, 1)
    insert = insert.replace('{Name}', name)
    insert = insert.replace('{Verb}', verb)
    insert = insert.replace('{Adjective}', adject2, 1)
    insert = insert.replace('{Adjective}', adject3, 1)
    insert = insert.replace('{Noun}', noun1, 1)
    insert = insert.replace('{Animal}', anim1)
    insert = insert.replace('{Animal}', anim2)
    insert = insert.replace("{Girl Name}", girl)
    insert = insert.replace('{Adjective}', adject4, 1)
    insert = insert.replace('{Noun}', noun2, 1)
    insert = insert.replace('{Adjective}', adject5, 1)
    insert = insert.replace('{Noun}', noun3, 1)
    insert = insert.replace('{1-50}', num50)
    insert = insert.replace("{Names}", f"{name}'s")
    insert = insert.replace('{Number}', num, 1)
    insert = insert.replace('{Noun}', noun4, 1)
    insert = insert.replace('{Number}', num2, 1)
    insert = insert.replace('{Noun}', noun5, 1)
 
    print(insert)
     
with open('./assets/madlib.txt', 'wt') as madlib:
    madlib.write(insert)


    


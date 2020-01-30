
#Escape Characters: \" - Quotes inside of strings.  \n - new line.  \t - tab
mySentence = "\"loves\" the color"

color_list = ['red','blue','green','pink','teal','black','purple','gray','yellow']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst
#Function END

fname = input("Please enter your first name: ")

lst = color_function(fname)

for i in lst:
    print(i)

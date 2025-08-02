name = 'John'

# print(type(name))

s1 = 'sfsd'
s2 = "sdfsd"
s3 = """ sdgdfg
gdfgd
dfgd
dfgdfg
dfgddgh """

# print("Книга 'Кобзар' написана Шевченком")


street = 'South'

# print(len(street))

# print(street[5])

text = 'Hello, world!'

# slices [start : end + 1: step]

print(text[:8])
print(text[3:])
print(text[:])
print(text[::3])


# upper() - пишет все с большой букви
txt = 'loRem ipSUM'

print(txt.upper())

# lower()
print(txt.lower())

# title()
print(txt.title())

name = 'Jack'
age = 26

comb_text = 'Hello {0}. You are {1}'.format(name, age)
print(comb_text)

import turtle

t = turtle.Turtle()

wn = turtle.Screen()

wn.setup(width=800, height=800)
t.hideturtle()

# t.write('Hello world', font=('Arial', 24, "normal"))

# t.up()
# t.goto(-300, 200)
# t.down()

# user_text = wn.textinput("Введение", 'Enter some text')
# t.color(user_text)
# t.write(user_text, font=('Tahoma', 36, 'bold'))
t.write('phrase1', font=('Tahoma', 36, 'bold'))
t.up()
t.goto(0, -50)
t.down()
t.write('phrase2', font=('Tahoma', 36, 'bold'))
t.up()
t.goto(0, -100)
t.down()
t.write('phrase3', font=('Tahoma', 36, 'bold'))
wn.mainloop()

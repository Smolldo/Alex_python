lst1 = [1,2,3,4,5,6,7]

lst2 = ['a', 'b', 'c']

lst3 = [1,2,3, 3.45, 'dsfsdfs', True, [1,2,3,4]]

l = []
l1 = list()

print(lst1[0:5:2])

# append() - добавляет елемент в конец списка
lst1 = [1,2,3,4]
lst1.append(8)
print(lst1)

# insert() - 
names = ["Alice", "Bob", "Diane"]
names.insert(1, 'Jack')
print(names)

# remove()
lst1 = [1,2,3,4,5,5,6,7,8,8]
# lst1.remove(5)
# print(lst1)

# del lst1[0:4]
del lst1
# print(lst1)


# tuple() - кортеж
tpl1 = ()
tpl2 = tuple()

tpl = (1,2,3,4,5,5,5,5,5,6)
# print(tpl.count(5))

# print(tpl.index(5))


tpl3 = (1,2,3,4, [1,2,3,4])
tpl3[4].append(7)
print(tpl3)





num1 = int(input('Enter 1 num:'))
num2 = int(input('Enter 2 num:'))
print('actions. 1: +, 2: -, 3: *, 4: /')
action = input('Enter: action')

if action == '1':
    print(num1 + num2)

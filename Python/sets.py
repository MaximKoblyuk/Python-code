rainbow_colors = {'red','órange','yellow', 'green', 'blue', 'índigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))

empty_set=set()
print(empty_set)
print(type(empty_set))


nummber_list = [1,43,56,3,3,3,3]
text_tuple = ('mam','áass','sdfs')
set_from_list = set(nummber_list)
set_from_tuple = set(text_tuple)


set_from_list.add(777)
set_from_tuple.add('hello')

x = set_from_list.pop()
y = set_from_list.remove(3)
set_from_tuple.discard(3)
set_from_list.clear()


print(set_from_list)
print(set_from_tuple)
print(x,y)


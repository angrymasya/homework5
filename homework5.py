immutable_var = (1,2,3,'summer',True)
print (immutable_var)
immutable_var[0] = 7
print (immutable_var) #ошибка, так как кортеж не поддерживает изменение элементов

immutable_var = ([1,2,3],'summer',True)
print (immutable_var)
immutable_var[0][0] = 7
print(immutable_var) #однако, если в кортеже есть список,в самом списке, можно заменить элемент

mutable_list = [1,2,3,'world','ears',False]
print(mutable_list)
mutable_list[3] = 'lamp'
print(mutable_list)
mutable_list[1] = 6
print(mutable_list)
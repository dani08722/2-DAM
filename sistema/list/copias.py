original_list=[4,3,7,1]

#Lo que hace es apuntar la misma dirección de memoria y si cambio original_list se cambia copy_list
copy_list= original_list

original_list[0]=15

print("original_list: ",original_list)
print("copy_list: ",copy_list)

#Correcto

original_listv2=[4,3,7,1]

#Copia directamente el contenido de la lista
copy_listv2= original_listv2.copy()

original_listv2[0]=15

print("original_listv2: ",original_listv2)
print("copy_listv2: ",copy_listv2)

#Otro correcto

original_listv3=[4,3,7,1]

#Copia directamente el contenido de la lista
copy_listv3= original_listv3[:]

original_listv3[0]=15

print("original_listv3: ",original_listv3)
print("copy_listv3: ",copy_listv3)
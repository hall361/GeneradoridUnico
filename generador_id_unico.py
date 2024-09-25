#Generador ID Unico

from random import randint #se importa de una libreria

''' 
Propuesta

* Solicitar nombre, apellido y año de nacimiento de una persona; con los valores proporsionados, el programa debe hacer lo siguinete:

1. Con el valor de nombre extraer las dos primeras letras.
2. Con el valor de apellido extraer las dos primeras letras.
3. Con el valor del año extraer los dos ultimos digitos.
4. seguido de esto generar un valor aleatorio de 4 digitos.
5. unir todo en una sola cadena e imprimir acompañado de felicidades!.

Solución

'''



print('*** Sistemas de Generador ID Unico ***')

nombre = input('Cual es tu Nombre?: ')
nombre_2 = nombre[0:2].upper()
#print(nombre_2)

apellido = input('Cual es tu apellido?: ')
apellido_2 = apellido[0:2].upper()


anio = input('Cual es tu año de nacimiento (YYYY)?: ')
anio_2 =anio[2:4]
#print(anio_2)

# Generar valor de cuatro digitos aleatorio

aleatorio = randint(0,9999)
print(aleatorio)

#Generar ID unico

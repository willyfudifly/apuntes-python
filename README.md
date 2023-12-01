# apuntes-python
Mis apuntes de python

## Print

La función `print()` se encarga de imprimir por pantalla.

Por ejemplo:

```Python
print("hola que tal")
```
Podemos concatenar cadenas de caracteres.
```Python
print("hola","que tal")
print("Hola"+"Willy")
```
## Input

La función `input()` nos permite introducir información a través del teclado.

Podemos utilizarlo sin indicar nada entre paréntesis:

```Python
print("Introduce tu nombre")
input()
```
Si escribimos dentro de los paréntesis, podemos mostrar información antes de escribir:
```Python
input("Introduce tu nombre")
```
## Variables
Las variables nos permiten guardar en ellas información. Hay muchos tipos de variables:

- **Enteros**: 5
- **Cadenas de texto**: "Willy"
- **Booleanos**: True, False

Las vaiables tienen un nombre que las identifica. Por ejemplo:

```Python
Edad = 20
Nombre = "Willy"
vivo = True
```
Para imprimir una variable indicamos su nombre sin comillas:
```Python
nombre = "Willy"
print(nombre)
```
El signo igual asigna un valor a la variable.

Un ejemplo completo:

```Python
nombre = input("dime tu nombre")
print(nombre)
```
Si queremos convertir el resultado de un input en un número utilizamos la función `int()`. Por ejemplo:

```Python
edad = int(input("dime tu edad"))
print(edad+5)
```
## Condicionales
Para decidir ejecutar o no un bloque de código en función de si se cumple o no una condición utilizamos `if`.
```Python
edad = 18
if edad>=18
    print("mayor de edad")
```
También podemos usar `else` para cuando la condición no se cumpla.
```Python
edad = 18
if edad>=18
    print("mayor de edad")
else:
    print("eres menor de edad")
```
## Bucles
Los bucles nos permiten repetir un bloque de código más de una vez-

Un ejemplo es el bucle `for`.

```Python
for numero in (0,5):
    print(numero)
```
También podemos recorrer una lista:
```Python
alumnos= ["Pepe","Manolo","Juan"]
for alumno in alumnos:
    print(alumno)
```
## Funciones

Las funciones nos permiten guardar un bloque de cófigo con un nombre para llamarlas cuando queramos. Las funciones terminan en paréntesis:
`sumar()`,`jugar()`,etc.

Ejemplo:

```Python
def calcular():
```
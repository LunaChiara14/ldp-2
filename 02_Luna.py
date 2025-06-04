### Operadores Aritméticos ###

# Operaciones con enteros
print(2 + 8)
print(2 - 8)
print(2 * 8)
print(2 / 8)
print(28 % 14)
print(28 // 2)
print(2 ** 8)
print(2 ** 8 + 1 - 4 / 2 // 8)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Todo bien?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 2)
print("Hola " * (2 ** 1))

my_float = 2.8 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(2 > 8)
print(2 < 8)
print(2 >= 8)
print(8 <= 8)
print(2 == 8)
print(2 != 8)

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole 
print(2 > 8 and "Hola" > "Python")
print(2 > 8 or "Hola" > "Python")
print(2 < 8 and "Hola" < "Python")
print(2 < 8 or "Hola" > "Python")
print(2 < 8 or ("Hola" > "Python" and 8 == 8))
print(not (2 > 8))

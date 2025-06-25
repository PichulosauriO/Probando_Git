def contar_vocales(palabra):
    palabra = palabra.lower()
    contador = 0
    for i in palabra:
        if i in "aeiou":
            contador += 1
    return contador

palabra_usuario = input("ingrese su palabra : ")

print(f"La cantidad de vocales que tiene tu palabra es {contar_vocales(palabra_usuario)}")
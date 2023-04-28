
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def ingresar_palabra():
    palabra = input("ingresar palabra: ")
    significado = input("ingresar significado: ")
    r.set(palabra, significado)

def buscar_palabra():
    palabra = input("ingrese palabra para buscar significado: ")
    significado = r.get(palabra)
    if significado:
        print(significado.decode("utf-8"))
    else:
        print("esta palabra no existe  ")

def eliminar_palabra():
    palabra = input("eliminar palabra: ")
    r.delete(palabra)

def lista_palabra():
    palabras = r.keys("*")
    for palabra in palabras:
        print(palabra.decode("utf-8"))

def editar_palabra():
    palabra = input("palabra a editar: ")
    significado = input("nuevo significado: ")
    r.set(palabra, significado)

while True:
    print("\n......MENU.......\n")
    print("1. ingresar palabra")
    print("2. buscar palabra")
    print("3. eliminar palabra")
    print("4. lista de palabras")
    print("5. editar palabra")
    print("6. salir")
    choice = int(input("ingrese opcion: "))
    if choice == 1:
        ingresar_palabra()
    elif choice == 2:
        buscar_palabra()
    elif choice == 3:
        eliminar_palabra()
    elif choice == 4:
        lista_palabra()
    elif choice == 5:
        editar_palabra()
    elif choice == 6:
        break
    else:
        print("opcion no existe")
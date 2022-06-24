print("== Bienvenido a la calculadora! ==")

option = "Y"

while option == "Y" or option == "y":
    num1 = int(input("\nIngresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))

    print("Operaciones: ")
    print("[+] Suma")
    print("[-] Resta")
    print("[*] Multiplicacion")
    print("[/] Division")

    option = input("Ingresa la opción: ")

    if option == "+":
        result = num1 + num2
        print(num1, option, num2, "=", result)
    elif option == "-":
        result = num1 - num2
        print(num1, option, num2, "=", result)
    elif option == "*":
        result = num1 * num2
        print(num1, option, num2, "=", result)
    elif option == "/":
        result = num1 / num2
        print(num1, option, num2, "=", result)
    else:
        print("La opcion ingresada no es valida, ingrese de nuevo")

    option = "x"
    while option != "Y" and option != "y" and option != "N" and option != "n":
        option = input("¿Quieres realizar otra operacion? [Y/N]: ")

print("Fin del programa, buen día!")
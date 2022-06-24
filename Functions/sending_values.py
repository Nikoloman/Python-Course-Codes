def sum(a, b):
    return a + b

result = sum(5, 10)
print(result)

#----------------------
def par_o_impar(num):
    if num % 2 == 0:
        return "PAR"
    else:
        return "IMPAR"

numero = int(input("Write a number: "))
print(par_o_impar(numero))

#----------------------
def recortar(numero, minimo, maximo):
    if minimo < numero:
        return minimo
    if maximo > numero:
        return maximo
    else:
        return numero
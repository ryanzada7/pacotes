while True:
    try:
        numero = int(input("Entre com um numero int: "))
        print(5/numero)
        break
    except(ValueError, ZeroDivisionError):
        print("Valor Errado ou não é possivel dividir por zero.")
    except ZeroDivisionError:
        print("Desculpe, Algo de errado aconteceu")
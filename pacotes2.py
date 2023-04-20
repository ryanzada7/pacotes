try: 
    value = int(input('Entre com um numero: '))
    print('O valor: ', value, 'dividido por um é: ', 1/value)
except:
    print('Erro. verifique o valor fornecido.')
except ZeroDivisionError:
    print('Não é possivel fazer divisão por zero.')
except:
    print('Algo errado aconteceu!')
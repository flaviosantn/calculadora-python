#importamos time para depois usar o "time.sleep"
import time 

#criamos a função que irá fazer a multiplicação de dois valores
def multiplicacao():
    numero1 = float(input("Digite o número 1: "))
    numero2 = float(input("Digite o número 2: "))
    calc = numero1 * numero2
    print(f"O resultado da sua multiplicação é: {calc}")

#criamos a função que irá fazer a soma de quantos valores quisermos, finalizando caso '.' é inserido
def soma():
    resultado = 0

    while True:

        valor = input("Digite um número ('.' para parar): ")

        if valor == ".":
            break

        resultado += float(valor)

    print(f"O resultado da sua soma é: {resultado}")

#criamos a estrutura e fazemos com que o programa repita até '0' ser inserido
while True:

    print("\n==== CALCULADORA ====")
    print("Opção 1: Soma ")
    print("Opção 2: Multiplicação ")
    print("Opção 0: Sair ")

    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        soma()

    elif opcao == "2":
        multiplicacao()

    elif opcao == "0":
        print("Encerrando a operação...")
        time.sleep(2)
        break

    else:
        print("Opção inválida")   
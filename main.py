from exercicio1 import CalcularSalario
from exercicio2 import SequenciaNumerica
from exercicio3 import Fibonacci

def main():

    print("====================Selecione um dos exercicios ABAIXO: ========================\n")
    print("Exercicio1 (Salario) ======= 1")
    print("Exercicio2 (Sequencia Numerica) ======= 2")
    print("Exercicio3 (Fibonacci)  ======= 3\n")
    print("============================================\n")

    usuario = int(input("Selecione o exercicio que deseja:"))

    match usuario:
        case 1:

            valorHora = int(input("Digite o valor da hora de trabalho: "))
            horasTrabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
            filhos = int(input("Digite a quantidade de filhos: "))

            inputUser1 = CalcularSalario(valorHora, horasTrabalhadas, filhos)

            print(f"Salário Bruto: {inputUser1.calcularSalarioBruto()}")
            print(f"Salário Família: {inputUser1.calcularSalarioFamilia()}")
            print(f"Salário Líquido: {inputUser1.calcularSalarioLiquido()}\n")

        case 2:
            tamanhoLista = int(input("Tamanho da lista: "))

            numeros = []

            for i in range(tamanhoLista):
                numeros.append(int(input(f"Digite o {i + 1}º número: ")))

            inputUser2 = SequenciaNumerica(tamanhoLista,numeros)

            print(f"Sequencia: {inputUser2.sequencia()}")
            print(f"Sequencia crescente: {inputUser2.sequenciaCrescente()}")

        case 3:
            n = int(input("Digite o valorr de N: "))
            inputUser3 = Fibonacci(n)
            print(f"Primeiros numeros da sequencia: {inputUser3.sequenciaFibonacci()} ")

            if inputUser3.pertenceFibonacci():
                print("pertence à sequência de Fibonacci.")
            else:
                print("NÃO pertence à sequência de Fibonacci.")


        case _:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
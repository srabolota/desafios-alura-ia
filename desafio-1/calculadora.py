# ==============================================================
# CALCULADORA BÁSICA EM PYTHON - VERSÃO SIMPLES & DIRETA
# Ideal para quem está dando os primeiros passos na programação!
# ==============================================================

# 1. RECEBENDO OS DADOS DO USUÁRIO
# Usamos input() para ler o texto e float() para converter em número decimal
num1 = float(input("Digite o primeiro número: "))

# input() lê o símbolo da operação que o usuário deseja (+, -, *, /)
operacao = input("Digite a operação matemática (+, -, *, /): ")

# Lendo o segundo número
num2 = float(input("Digite o segundo número: "))

# 2. ESTRUTURA CONDICIONAL (LÓGICA DE DECISÃO)
# O Python avalia qual operação foi escolhida e calcula o resultado
if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado da soma: {num1} + {num2} = {resultado}")

elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado da subtração: {num1} - {num2} = {resultado}")

elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado da multiplicação: {num1} * {num2} = {resultado}")

elif operacao == "/":
    # Regra matemática: Não podemos dividir nenhum número por zero!
    if num2 == 0:
        print("Erro matemático: Não é possível dividir por zero!")
    else:
        resultado = num1 / num2
        print(f"Resultado da divisão: {num1} / {num2} = {resultado}")

else:
    # Caso o usuário digite um símbolo inválido (ex: %, x, abc)
    print("Operação inválida! Por favor, escolha +, -, * ou /.")

input("Pressione Enter para sair...")

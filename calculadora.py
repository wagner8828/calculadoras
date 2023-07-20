
print("Bem-vindo à Calculadora do Waguin!\n")

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão\n")

try:
    operacao = int(input("Digite o número da operação desejada: "))
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == 1:
        resultado = num1 + num2
        sinal = "+"
    elif operacao == 2:
        resultado = num1 - num2
        sinal = "-"
    elif operacao == 3:
        resultado = num1 * num2
        sinal = "*"
    elif operacao == 4:
        if num2 == 0:
            raise ValueError("Erro: Divisão por zero não é permitida.")
        resultado = num1 / num2
        sinal = "/"
    else:
        raise ValueError("Operação inválida.")

    print(f"\nResultado: {num1} {sinal} {num2} = {resultado}")

except ValueError as ve:
    print(ve)
except Exception as e:
    print(f"Erro inesperado: {e}")
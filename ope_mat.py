valor1 = int(input("Entre com o primeiro número: "))
valor2 = int(input("Entre com o segundo número: "))
oper = input("Entre com o operador (+, -, *, /): ")

if oper == "+":
    print("Resultado: ", valor1 + valor2)
elif oper == "-":
    print("Resultado: ", abs(valor1 - valor2))
elif oper == "*":
    print("Resultado: ", valor1 * valor2)
elif oper == "/":
    if valor2 != 0:  # Evita divisão por zero
        print("Resultado: ", valor1 / valor2)
    else:
        print("Erro: divisão por zero não permitida")
else:
    print("Operação inválida")

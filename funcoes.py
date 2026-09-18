#Função que recebe o nome e o salario e retorna uma lista com essas informações.
def cadastrar_funcionarios():
    funcionarios = []
    salario = 0

    print("--- Cadastro de Funcionários ---")
    while True:
        nome = input("Digite o nome do funcionário (ou 'fim' para encerrar): ")

        if nome.lower() == "fim":
            break

        while True:
            try:
                salario = float(input(f"Digite o salário de {nome}: R$ "))
                if salario > 0:
                    funcionarios.append((nome, salario))
                    print("-" * 30)
                    break
                else:
                    print("Entrada inválida. O salário deve ser maior que zero.")
            except ValueError:
                print("Entrada inválida. O salário deve ser um valor numérico.")

    return funcionarios


#Função que recebe uma lista com nome e salario e retorna uma nova lista com os salarios reajustados e o total de aumento.
def reajuste_salarial(lista_funcionarios):
    funcionarios_atualizado = []
    total_antigo = 0
    total_novo = 0

    for nome, salario in lista_funcionarios:
        total_antigo += salario

        if salario <= 2000.00:
            novo_salario = salario * 1.2
        elif salario <5000.00:
            novo_salario = salario * 1.15
        else:
            novo_salario = salario * 1.05

        total_novo += novo_salario
        funcionarios_atualizado.append((nome, novo_salario))

    total_aumento = total_novo - total_antigo
    return funcionarios_atualizado, total_aumento

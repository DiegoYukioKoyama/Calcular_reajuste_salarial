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

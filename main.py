import funcoes

# Cria a lista de funcionários.
lista_funcionarios = funcoes.cadastrar_funcionarios()

# Reajusta a lista de funcionários com os novos salários.
lista_funcionarios_atualizado, total_aumento = funcoes.reajuste_salarial(lista_funcionarios)

# Exibir os resultados.
print("\n" + "="*40)
print(f"Total geral de aumento: R${total_aumento:.2f}")
print("\nO seguintes funcionários recebem menos de R$2000.00 depois do aumento salárial:")
for nome, novo_salario in lista_funcionarios_atualizado:
    if novo_salario < 2000:
        print(f"- {nome}: R${novo_salario:.2f}")
print("=" * 40)

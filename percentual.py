#Exercício para calcular o percentual de cada estado.

#Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

# Dados de faturamento por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o total de faturamento somando todos os valores
total_faturamento = sum(faturamento.values())

# Calcula o percentual de faturamento para cada estado
percentuais = {}
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100
    percentuais[estado] = percentual

# Exibe o percentual de cada estado
for estado, percentual in percentuais.items():
    print(f"Percentual de {estado}: {percentual:.2f}%")

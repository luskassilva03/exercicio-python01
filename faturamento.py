import json

# Dados JSON com o faturamento diário
mes_setembro = '''
{
    "faturamento_diario": {
        "1": 0,
        "2": 2150.75,
        "3": 1850.50,
        "4": 2300.00,
        "5": 2400.25,
        "6": 2600.75,
        "7": 0,
        "8": 0,
        "9": 2500.00,
        "10": 2700.50,
        "11": 2300.00,
        "12": 2550.75,
        "13": 2750.00,
        "14": 0,
        "15": 0,
        "16": 2900.50,
        "17": 2600.00,
        "18": 2800.75,
        "19": 2700.00,
        "20": 0,
        "21": 0,
        "22": 0,
        "23": 2400.50,
        "24": 2500.75,
        "25": 2750.00,
        "26": 2600.50,
        "27": 3200.75,
        "28": 0,
        "29": 0,
        "30": 2900.00
    }
}
'''

# Carregar o JSON
dados = json.loads(mes_setembro)
faturamento = list(dados["faturamento_diario"].values())

# Filtrar valores maiores que 0
faturamento_validos = [valor for valor in faturamento if valor > 0]

# Calcular menor e maior faturamento
menor = min(faturamento_validos)
maior = max(faturamento_validos)

# Calcular a média
media = sum(faturamento_validos) / len(faturamento_validos)

# Contar dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento_validos if valor > media)

# Imprimir resultados
print("Menor valor de faturamento: R$", round(menor, 2))
print("Maior valor de faturamento: R$", round(maior, 2))
print("Número de dias com faturamento acima da média:", dias_acima_media)

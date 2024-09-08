#Exercício para saber qual o valor da variável soma.

# Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print("A soma dos números de 1 a 13 é:", SOMA)
